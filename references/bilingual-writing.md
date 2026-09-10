# Bilingual writing rules

## Resolution

Honor an explicit `zh`, `en`, or `bilingual` choice. For omitted or `auto`, use Chinese explanations while preserving English definitions, terms, proper names, abbreviations, variables, and exam-relevant original wording. If the user explicitly requests source-language output, detect and follow the dominant source language. Never block intake solely to ask for language. Record the resolved mode and keep it consistent across every deliverable.

## Chinese output

- Explain in Chinese and preserve important English terms at first use: `梯度下降（gradient descent）`.
- Preserve standard abbreviations, theorem names, algorithm names, variables, and exam-relevant English wording.
- Build a single terminology table and reuse exactly the same translation across lectures.

## English output

- Write natural academic English.
- Preserve useful Chinese source terminology in parentheses when mistranslation would lose meaning.
- Do not translate variable names or rewrite formal definitions without marking a paraphrase.

## Bilingual output

- Avoid duplicating every paragraph in two languages by default.
- Use the selected primary language for explanations and the secondary language for terms, concise definitions, and exam wording.
- Use parallel full translations only when the user explicitly requests them.

## Fidelity

- Quote only when exact wording matters; otherwise paraphrase and cite.
- Keep mathematical notation identical to the verified source.
- Mark uncertain OCR or translation instead of silently normalizing it.
