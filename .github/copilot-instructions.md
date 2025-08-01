# Copilot Instructions for ANI Workspace

## Project Overview
This workspace is a LaTeX-based document project focused on Star Trek's warp propulsion concepts. The main file is `aaaa.tex`, which compiles to PDF using standard LaTeX workflows. There are no code components, tests, or custom build scripts—just LaTeX source and build artifacts.

## Key Files and Structure
- `aaaa.tex`: Main LaTeX source. All content and formatting logic reside here.
- `build/`: Contains LaTeX build artifacts (e.g., `.aux`, `.log`, `.pdf`). Do not edit these files directly.
- No README or agent-specific rules files are present.

## Developer Workflow
- **Editing**: Make all content changes in `aaaa.tex`.
- **Building**: Use a LaTeX editor or run `pdflatex aaaa.tex` to generate `build/aaaa.pdf`. No custom build scripts or Makefiles are present.
- **Output**: The final document is `build/aaaa.pdf`.

## Conventions and Patterns
- Use standard LaTeX packages (`inputenc`, `graphicx`, `color`, `soul`).
- Spanish language support is available but commented out (`babel`).
- Document structure follows typical LaTeX article conventions: title, sections, equations, and formatted tables.
- Inline formatting uses LaTeX commands (e.g., `\ul{...}` for underlining, `\hl{...}` for highlighting).
- Mathematical notation is included using the `equation` environment.

## Integration Points
- No external scripts, APIs, or code integrations.
- No automated testing or CI/CD pipelines.

## Examples
- To add a new section, use LaTeX sectioning commands (e.g., `\section{}` or custom formatting as in the current file).
- To update equations, use the `equation` environment as shown for warp speed calculation.

## AI Agent Guidance
- Focus all edits on `aaaa.tex` unless adding new LaTeX sources.
- Do not modify files in `build/`.
- Follow existing formatting and language conventions.
- If adding new packages, ensure compatibility with standard LaTeX distributions.

---
If any workflow or convention is unclear, please request clarification or examples from the user.
