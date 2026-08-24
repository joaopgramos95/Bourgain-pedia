---
name: latex-source-audit
description: Audit LaTeX source before compilation and handoff, especially after creating or editing .tex manuscripts. Use for LaTeX writing, mathematical-paper editing, or compilation tasks to catch missing-backslash artifacts such as bare `qquad`, unresolved references, compilation failures, and layout warnings.
---

# LaTeX Source Audit

Run a deterministic source and build audit whenever editing or producing a `.tex` file.

## Workflow

1. Run `scripts/audit_latex_source.py FILE.tex` before compilation. Treat every finding as an error.
2. Compile with `pdflatex -interaction=nonstopmode -halt-on-error FILE.tex` at least twice. Use a third pass when labels or the table of contents changed.
3. Search the final log for `undefined`, `Warning`, `Overfull`, `Underfull`, `Fatal`, and `Error`. Resolve substantive findings. Inspect persistent layout warnings instead of silently ignoring them.
4. Run `scripts/audit_latex_source.py FILE.tex` again after the final edit.
5. If practical, render representative PDF pages and inspect them visually, especially pages containing newly edited displays.

Never mark a LaTeX task complete merely because a PDF was emitted. A bare `qquad` is text, not spacing: write `\qquad`. The bundled scanner rejects this recurring missing-backslash error.

## Command

```sh
python3 /path/to/latex-source-audit/scripts/audit_latex_source.py manuscript.tex
```

Exit status is nonzero if a malformed command is found.
