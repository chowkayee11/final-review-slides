# Quality gates

All blocking gates must pass.

| Gate | Blocking test |
|---|---|
| Inventory | Every supplied file is classified; ambiguous roles are disclosed. |
| Ordering | Lecture order has evidence; missing and duplicate identifiers are reported. |
| Page coverage | Every page/slide has exactly one valid disposition; none remain uncovered or uncertain. |
| Sequence | Main review follows lecture and intra-lecture source order. |
| Review alignment | Every explicit Revision/Review point maps to a final-review location. |
| Explanation depth | Every A/B or explicit Revision concept has definition, explanation/mechanism, conditions, example/application, distinctions or failure modes where applicable, and citations; headings alone do not pass. |
| Assessment fidelity | Exam priorities use Explicit/Observed/Inferred labels with sources. |
| Visual evidence | Every page requiring visual inspection is marked checked with findings. |
| Formula fidelity | Sampled formulas match symbols, operators, assumptions, and conditions. |
| Citation fidelity | Sample citations resolve to pages that directly support their claims. |
| Terminology | Core terms are consistent and comply with the selected language mode. |
| Derived documents | Every quick-reference and misconception entry is traceable to verified source evidence. |
| Course map | Canonical JSON and Mermaid source exist; a consistent Mermaid rendering or PDF-native fallback is embedded. |
| Mock exam | When triggered, every question is supported and answerable; keys, calculations/protocols, mark totals, balance, separation of answers, and citations in solutions pass. |
| Build | All required LaTeX sources compile without fatal errors. |
| Visual QA | Rendered PDFs have no missing glyphs, clipping, overlap, broken math, or unusable layout. |

Record counts, samples, commands, and artifact paths in `coverage-report.md`. Do not mark a gate PASS solely because the draft looks plausible.
