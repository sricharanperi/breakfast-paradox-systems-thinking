#!/usr/bin/env python3
"""Markdown -> styled HTML -> PDF via Chrome headless print-to-pdf.
Replaces the pandoc+tectonic LaTeX pipeline for PDF output specifically
(docx is still built separately via plain pandoc). Usage:
    python3 build_pdf.py <source.md> <out.pdf> [--html-out <path>]
"""
import sys, re, subprocess, os, tempfile

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

def main():
    src = sys.argv[1]
    out_pdf = sys.argv[2]
    doc_dir = os.path.dirname(os.path.abspath(src))
    css_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "report-style.css")

    with open(src, "r") as f:
        text = f.read()

    title, subtitle = "", ""
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if m:
        fm = m.group(1)
        tm = re.search(r'^title:\s*"?(.*?)"?\s*$', fm, re.M)
        sm = re.search(r'^subtitle:\s*"?(.*?)"?\s*$', fm, re.M)
        if tm: title = tm.group(1)
        if sm: subtitle = sm.group(1)
        text = text[m.end():]

    result = subprocess.run(
        ["pandoc", "-f", "gfm", "-t", "html5", f"--resource-path={doc_dir}"],
        input=text, capture_output=True, text=True, check=True
    )
    body_html = result.stdout

    with open(css_path) as f:
        css = f.read()

    title_block = ""
    if title:
        title_block += f'<h1 class="title">{title}</h1>\n'
    if subtitle:
        title_block += f'<p class="subtitle">{subtitle}</p>\n'

    full_html = f"""<!doctype html>
<html><head><meta charset="utf-8">
<base href="file://{doc_dir}/">
<title>{title}</title>
<style>{css}</style>
</head><body>
{title_block}
{body_html}
</body></html>"""

    tmp_html = tempfile.NamedTemporaryFile(mode="w", suffix=".html", delete=False)
    tmp_html.write(full_html)
    tmp_html.close()

    html_out = None
    for i, a in enumerate(sys.argv):
        if a == "--html-out" and i + 1 < len(sys.argv):
            html_out = sys.argv[i + 1]
    if html_out:
        with open(html_out, "w") as f:
            f.write(full_html)

    subprocess.run([
        CHROME, "--headless", "--disable-gpu",
        f"--print-to-pdf={os.path.abspath(out_pdf)}",
        "--no-pdf-header-footer",
        f"file://{tmp_html.name}"
    ], capture_output=True)

    os.unlink(tmp_html.name)
    size = os.path.getsize(out_pdf)
    print(f"rendered {out_pdf} ({size} bytes)")

if __name__ == "__main__":
    main()
