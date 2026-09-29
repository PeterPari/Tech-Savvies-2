#!/usr/bin/env python3
"""Build public/admin/index.html, the owner's prompt checklist, from fix-prompts/ and fix-plan.md.

Run after editing a prompt or the plan:   python3 tools/build_admin.py
Fail if the page is out of date (for CI): python3 tools/build_admin.py --check

Order and phases come from the "Execution order" table in fix-plan.md, deliverables from its
"Prompt index" table, and model/effort from the "Parameters" list under each prompt.
Standard library only.
"""

import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROMPTS_DIR = ROOT / "fix-prompts"
PLAN = ROOT / "fix-plan.md"
OUT = ROOT / "public" / "admin" / "index.html"

MODEL_LABELS = {"haiku": "Haiku", "sonnet": "Sonnet", "opus": "Opus"}
EFFORT_LABELS = {"low": "Low", "medium": "Medium", "high": "High"}


def fail(message):
    sys.exit(f"build_admin: {message}")


def read_prompts():
    prompts = {}
    for path in sorted(PROMPTS_DIR.glob("[0-9][0-9]-*.md")):
        text = path.read_text(encoding="utf-8")
        num = path.name[:2]
        title = re.search(r"^# Prompt \d\d: (.+)$", text, re.M)
        block = re.search(r"^````text\n(.*?)\n^````$", text, re.M | re.S)
        model = re.search(r"^- Model: (\w+)", text, re.M)
        effort = re.search(r"^- Reasoning effort: (\w+)", text, re.M)
        if not (title and block and model and effort):
            fail(f"{path.name}: missing title, prompt block, Model or Reasoning effort")
        if model.group(1) not in MODEL_LABELS or effort.group(1) not in EFFORT_LABELS:
            fail(f"{path.name}: unknown model or effort")
        prompts[num] = {
            "title": title.group(1),
            "text": block.group(1),
            "model": model.group(1),
            "effort": effort.group(1),
            "file": path.name,
        }
    return prompts


def read_plan():
    plan = PLAN.read_text(encoding="utf-8")
    steps = []  # (prompt number, phase label, is final pass)
    for line in plan.splitlines():
        row = re.match(r"^\| (\d)\. ([^|]+?) \| (.+?) \|", line)
        if row:
            phase = f"{row.group(1)} · {row.group(2)}"
            final = "final pass" in row.group(3)
            for num in re.findall(r"\*\*(\d\d)\*\*", row.group(3)):
                steps.append((num, phase, final))
    deliverables = dict(re.findall(r"^\| (\d\d) \| \[`fix-prompts/[^|]+\| (.+?) \|$", plan, re.M))
    return steps, deliverables


def inline_code(text):
    return re.sub(r"`([^`]+)`", r"<code>\1</code>", html.escape(text, quote=False))


def row_html(step, num, phase, final, prompt, deliverable):
    key = f"{num}-final" if final else num
    title = "Local laws: final pass" if final else prompt["title"]
    text = prompt["text"] + ("\n\nfinal pass" if final else "")
    if final:
        deliverable = "Checks every live page against <code>docs/legal-compliance.md</code>"
    model = MODEL_LABELS[prompt["model"]]
    effort = EFFORT_LABELS[prompt["effort"]]
    return f"""          <tr class="prompt-row" role="row" data-row="{key}">
            <td class="col-done" role="cell">
              <input class="done-box" type="checkbox" id="done-{key}" data-done="{key}">
              <label class="visually-hidden" for="done-{key}">Mark step {step} done</label>
            </td>
            <td class="col-step" role="cell" data-label="Step">{step}</td>
            <td class="col-prompt" role="cell">
              <p class="prompt-title"><span class="prompt-num">{num}</span> {html.escape(title)}</p>
              <p class="prompt-deliverable">{deliverable}</p>
              <details class="prompt-details">
                <summary>View prompt</summary>
                <pre class="prompt-text" id="prompt-{key}" tabindex="0" aria-label="Prompt {num} text">{html.escape(text)}</pre>
              </details>
            </td>
            <td class="col-phase" role="cell" data-label="Phase">{html.escape(phase)}</td>
            <td class="col-model" role="cell" data-label="Model"><span class="badge badge--{prompt["model"]}">{model}</span></td>
            <td class="col-effort" role="cell" data-label="Effort"><span class="effort effort--{prompt["effort"]}">{effort}</span></td>
            <td class="col-copy" role="cell">
              <button class="btn btn--sm copy-btn" type="button" data-copy="prompt-{key}" hidden><span data-copy-label>Copy</span><span class="visually-hidden"> step {step} prompt</span></button>
            </td>
          </tr>"""


def build():
    prompts = read_prompts()
    steps, deliverables = read_plan()
    planned = {num for num, _, _ in steps}
    if planned != set(prompts):
        fail(f"execution order and prompt files differ: {sorted(planned ^ set(prompts))}")
    rows = []
    for index, (num, phase, final) in enumerate(steps, start=1):
        deliverable = inline_code(deliverables.get(num, ""))
        rows.append(row_html(index, num, phase, final, prompts[num], deliverable))
    return TEMPLATE.format(total=len(steps), rows="\n".join(rows))


TEMPLATE = """<!doctype html>
<!-- Generated by tools/build_admin.py from fix-prompts/ and fix-plan.md. Edit those, then rebuild. -->
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Prompt checklist | Tech-Savvies</title>
    <meta name="description" content="Internal checklist of the compliance fix prompts, with the model and effort for each.">
    <meta name="robots" content="noindex, nofollow">
    <meta name="theme-color" content="#0f1419">
    <link rel="icon" href="/favicon.ico" sizes="32x32">
    <link rel="icon" href="/assets/img/favicon-64.png" type="image/png" sizes="64x64">
    <link rel="preload" href="/assets/fonts/plus-jakarta-sans-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
    <link rel="preload" href="/assets/fonts/jetbrains-mono-latin-500-normal.woff2" as="font" type="font/woff2" crossorigin>
    <link rel="stylesheet" href="/assets/css/styles.css">
    <link rel="stylesheet" href="/admin/admin.css">
    <script src="/admin/admin.js" defer></script>
  </head>
  <body>
    <a class="skip-link" href="#main">Skip to content</a>

    <header class="site-header">
      <div class="container header-inner">
        <a class="brand" href="/">
          <img src="/assets/img/logo.png" width="161" height="48" alt="Tech-Savvies NYC home">
        </a>
        <p class="admin-tag">Internal · not linked from the site</p>
      </div>
    </header>

    <main id="main">
      <section class="section section--first">
        <div class="container container--wide">
          <h1 class="display-md">Prompt checklist</h1>
          <p class="lead admin-intro">Run the prompts in step order, one new Claude Code session each. Set the model and effort shown before pasting. Checkmarks are saved in this browser only.</p>

          <div class="admin-toolbar">
            <p class="admin-progress" aria-live="polite"><span data-done-count>0</span> of {total} done</p>
            <button class="admin-reset" type="button" data-reset hidden>Clear all checkmarks</button>
          </div>

          <table class="prompt-table" role="table">
            <caption class="visually-hidden">Compliance fix prompts in run order</caption>
            <thead role="rowgroup">
              <tr role="row">
                <th scope="col" role="columnheader" class="col-done">Done</th>
                <th scope="col" role="columnheader" class="col-step">Step</th>
                <th scope="col" role="columnheader" class="col-prompt">Prompt</th>
                <th scope="col" role="columnheader" class="col-phase">Phase</th>
                <th scope="col" role="columnheader" class="col-model">Model</th>
                <th scope="col" role="columnheader" class="col-effort">Effort</th>
                <th scope="col" role="columnheader" class="col-copy">Copy</th>
              </tr>
            </thead>
            <tbody role="rowgroup">
{rows}
            </tbody>
          </table>

          <p class="visually-hidden" aria-live="polite" data-copy-status></p>
        </div>
      </section>
    </main>
  </body>
</html>
"""


def main():
    page = build()
    if "--check" in sys.argv[1:]:
        if not OUT.exists() or OUT.read_text(encoding="utf-8") != page:
            fail("public/admin/index.html is out of date; run python3 tools/build_admin.py")
        return
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(page, encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
