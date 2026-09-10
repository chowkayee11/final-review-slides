# Output schemas

## final-review

1. Course and source scope
2. Assessment evidence and Revision/Review priorities
3. Course map derived from `course-map.json` (Mermaid rendering or PDF-native fallback)
4. Chapters in strict lecture order
5. Per-chapter recap and source references
6. Cross-lecture dependency index

Each chapter follows the source sequence. For substantive concepts use supported fields: definition/original wording, intuition, purpose, mechanism or derivation, assumptions, boundary conditions, example/application, failure or attack mode, distinctions, assessment links, and citations. End with a recap. `comprehensive` is the default depth; headings or one-line mentions do not count as explanation.

## mock-exam

The question paper contains instructions, time/marks only when evidenced or clearly labeled as simulated, questions, and no solutions or source citations that reveal answers. The separate solution paper contains for each question: model answer, working/reasoning, marking points, common errors, difficulty, assessed concept IDs, and tight source citations.

`mock-exam-blueprint.md` records evidence, assumptions, topic/type/difficulty/marks matrix, coverage, answerability checks, single-choice uniqueness checks, total-mark arithmetic, and final verdict.

## quick-reference

Use compact tables organized for lookup. Suggested columns:

`item | definition/formula | symbols | assumptions/conditions | when to use | common trap | source`

For non-mathematical courses replace formulas with frameworks, cases, vocabulary, dates, arguments, or comparison criteria.

## mistakes-and-distinctions

Suggested sections:

- easily confused concept pairs
- invalid shortcuts and boundary conditions
- notation and terminology traps
- diagram/table interpretation errors
- recurring mistakes evidenced by assignments or assessments

Suggested columns:

`confusion | incorrect belief | correct distinction | diagnostic cue | counterexample | source`

## coverage-report

Include:

- source inventory and resolved order
- missing/duplicate/ambiguous source findings
- Revision/Review topics and where covered
- page/slide ledger summary by file and lecture
- visual-inspection counts and findings
- exclusions with reasons
- unresolved uncertainties
- citation spot-check results
- build and visual-QA results for each PDF
- resolved language and depth modes
- mock-exam blueprint and validation results when applicable
- map renderer used and fallback reason when applicable
- final gate table with PASS/FAIL and evidence
