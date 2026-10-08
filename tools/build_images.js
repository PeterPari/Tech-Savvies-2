#!/usr/bin/env node
// Rebuilds the raster brand images from the SVG logo and icon in public/assets/img/:
// logo.png, og-image.png, icon-192.png, icon-512.png, favicon-64.png, apple-touch-icon.png and
// favicon.ico. Run from the repo root after changing logo.svg or icon.svg:
//
//   NODE_PATH="$(npm root -g)" node tools/build_images.js
//
// Needs Playwright with Chromium, installed globally (not a repo dependency). Not run in CI.
// The PNGs stay because share cards, Apple touch icons, manifest icons and old browsers don't take SVG,
// and the legacy redirects in netlify.toml point at them.
"use strict";

const fs = require("fs");
const path = require("path");
const { chromium } = require("playwright");

const PUBLIC = path.join(__dirname, "..", "public");
const IMG = path.join(PUBLIC, "assets", "img");
const FONTS = path.join(PUBLIC, "assets", "fonts");

// Colors from the :root tokens in public/assets/css/styles.css
const BG = "#0f1419";
const HEADING = "#ffffff";
const MUTED = "#94a3b8";
const ACCENT = "#10b981";
const LINE = "rgba(255, 255, 255, 0.1)";

// Bounding box of the TS mark in icon.svg's user units
const MARK = { x: 1.5, y: 1.55, w: 152.68, h: 128.97 };

const read = (name) => fs.readFileSync(path.join(IMG, name), "utf8");
const svgInner = (svg) => svg.replace(/^[\s\S]*?<svg\b[^>]*>/, "").replace(/<\/svg>\s*$/, "");
const fontUrl = (name) => "data:font/woff2;base64," + fs.readFileSync(path.join(FONTS, name)).toString("base64");

// The TS mark centered on a square tile, `fill` of the tile's width; no background when `bg` is null
function tileHtml(markup, size, fill, bg) {
  const side = MARK.w / fill;
  const x = MARK.x + MARK.w / 2 - side / 2;
  const y = MARK.y + MARK.h / 2 - side / 2;
  return `<!doctype html><style>html,body{margin:0;background:${bg || "transparent"}}svg{display:block}</style>` +
    `<svg xmlns="http://www.w3.org/2000/svg" viewBox="${x} ${y} ${side} ${side}" width="${size}" height="${size}">${markup}</svg>`;
}

function logoHtml(logo) {
  return `<!doctype html><style>html,body{margin:0;background:transparent}svg{display:block}</style>${logo}`;
}

function ogHtml(logo) {
  return `<!doctype html>
<style>
  @font-face { font-family: "Plus Jakarta Sans"; src: url(${fontUrl("plus-jakarta-sans-latin-wght-normal.woff2")}) format("woff2"); font-weight: 200 800; }
  @font-face { font-family: "JetBrains Mono"; src: url(${fontUrl("jetbrains-mono-latin-500-normal.woff2")}) format("woff2"); font-weight: 500; }
  html, body { margin: 0; width: 1200px; height: 630px; overflow: hidden; background: ${BG}; }
  .logo { position: absolute; left: 79px; top: 71px; width: 255px; height: 76px; }
  .logo svg { display: block; width: 100%; height: 100%; }
  h1 { position: absolute; left: 80px; top: 233px; margin: 0; font: 800 92px/1.06 "Plus Jakarta Sans"; letter-spacing: -0.03em; color: ${HEADING}; }
  h1 > span { display: block; }
  .accent { color: ${ACCENT}; }
  .kern-dot { margin-left: -0.1em; }
  .rule { position: absolute; left: 80px; right: 80px; top: 513px; height: 1px; background: ${LINE}; }
  .foot { position: absolute; left: 80px; right: 80px; top: 539px; display: flex; justify-content: space-between; font: 500 20px/1.4 "JetBrains Mono"; letter-spacing: 0.235em; text-transform: uppercase; }
  .foot :first-child { color: ${ACCENT}; }
  .foot :last-child { color: ${MUTED}; letter-spacing: 0.175em; }
</style>
<div class="logo">${logo}</div>
<h1><span>Websites done fast<span class="kern-dot">.</span></span><span class="accent">Websites done right<span class="kern-dot">.</span></span></h1>
<div class="rule"></div>
<div class="foot"><span>tech-savvies.com</span><span>Websites · Google · Social</span></div>`;
}

// favicon.ico holding the given PNGs (PNG entries need Windows Vista or later, like the old file)
function ico(pngs) {
  const head = Buffer.alloc(6 + 16 * pngs.length);
  head.writeUInt16LE(0, 0);
  head.writeUInt16LE(1, 2);
  head.writeUInt16LE(pngs.length, 4);
  let offset = head.length;
  pngs.forEach(({ size, data }, i) => {
    const e = 6 + 16 * i;
    head.writeUInt8(size >= 256 ? 0 : size, e);
    head.writeUInt8(size >= 256 ? 0 : size, e + 1);
    head.writeUInt8(0, e + 2);
    head.writeUInt8(0, e + 3);
    head.writeUInt16LE(1, e + 4);
    head.writeUInt16LE(32, e + 6);
    head.writeUInt32LE(data.length, e + 8);
    head.writeUInt32LE(offset, e + 12);
    offset += data.length;
  });
  return Buffer.concat([head, ...pngs.map((p) => p.data)]);
}

async function main() {
  const logo = read("logo.svg").replace(/<\?xml[^>]*>\s*/, "");
  const mark = svgInner(read("icon.svg"));
  const browser = await chromium.launch();
  const page = await browser.newPage({ deviceScaleFactor: 1 });

  async function shot(html, width, height, transparent) {
    await page.setViewportSize({ width, height });
    await page.setContent(html);
    await page.evaluate(() => document.fonts.ready);
    return page.screenshot({ clip: { x: 0, y: 0, width, height }, omitBackground: transparent });
  }

  const out = {
    "assets/img/logo.png": await shot(logoHtml(logo), 443, 132, true),
    "assets/img/og-image.png": await shot(ogHtml(logo), 1200, 630, false),
    "assets/img/icon-512.png": await shot(tileHtml(mark, 512, 0.6, BG), 512, 512, false),
    "assets/img/icon-192.png": await shot(tileHtml(mark, 192, 0.6, BG), 192, 192, false),
    "apple-touch-icon.png": await shot(tileHtml(mark, 180, 0.75, BG), 180, 180, false),
    "assets/img/favicon-64.png": await shot(tileHtml(mark, 64, 1, null), 64, 64, true),
  };
  const icoSizes = [16, 32, 48];
  const icoPngs = [];
  for (const size of icoSizes) {
    icoPngs.push({ size, data: await shot(tileHtml(mark, size, 1, null), size, size, true) });
  }
  out["favicon.ico"] = ico(icoPngs);
  await browser.close();

  for (const [rel, data] of Object.entries(out)) {
    fs.writeFileSync(path.join(PUBLIC, rel), data);
    console.log("wrote public/%s (%d bytes)", rel, data.length);
  }
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
