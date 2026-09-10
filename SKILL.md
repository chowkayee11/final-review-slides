---
name: final-review-slides
description: Create Chinese-, English-, or bilingual final-exam review packs and source-grounded mock exams from PDF/PPTX lecture decks, including mixed-language slides, Revision/Review decks, syllabi, assignments, quizzes, and past exams. Use for 期末复习, 课件总结, 考点整理, 模拟题, final review notes, formula/concept sheets, misconception guides, or source-cited exam preparation materials. Preserve lecture and slide order, inspect visual evidence, retain LaTeX sources, and apply strict coverage, depth, assessment, and rendering gates.
---

# Final Review Slides

Build a source-traceable exam pack without reordering or silently omitting course material. Use the `pdf` and `presentations` skills for format-specific intake and rendering; follow their render-and-verify requirements.

## Required deliverables

Unless the user explicitly changes the outputs, create:

- `final-review.tex` and `final-review.pdf`: complete lecture-by-lecture review in source order.
- `quick-reference.tex` and `quick-reference.pdf`: formulas, symbols, conditions, concepts, and fast lookup tables.
- `mistakes-and-distinctions.tex` and `mistakes-and-distinctions.pdf`: misconceptions, confusable concepts, invalid shortcuts, and diagnostic comparisons.
- `coverage-report.md`: source inventory, ordering basis, page/slide coverage, visual-check status, exclusions, uncertainties, and quality-gate verdicts.
- `course-map.json` and `course-map.mmd`, plus a rendered course map used in `final-review.pdf`.

When Revision/Review, assignments, quizzes, midterms, past exams, or an explicit mock-exam request supplies enough assessment evidence, also create:

- `mock-exam.tex` and `mock-exam.pdf`: new questions or source-grounded variants without answers.
- `mock-exam-solutions.tex` and `mock-exam-solutions.pdf`: model solutions, marking points, common errors, difficulty, assessed concepts, and citations.
- `mock-exam-blueprint.md`: scope, evidence basis, topic/type/difficulty/mark allocation, and validation results.

Keep generated files and intermediates in one dedicated output directory. Preserve `.tex` sources. Do not claim completion unless all required files exist, all PDFs compile successfully, and rendered PDFs pass visual inspection.

## Intake contract

Accept one or more `.pdf` or `.pptx` lecture decks. Also ingest, when supplied:

- Revision/Review/Final Review decks
- syllabus or course outline
- assignments and homework
- quizzes and midterms
- past exams and answer keys

Accept `language: auto | zh | en | bilingual`. Do not block when the user omits it: default `auto` to Chinese explanations while retaining English definitions, technical terms, proper names, abbreviations, variables, and exam-relevant original wording. If the user requests “follow the source”, use the detected dominant language. Record the resolved mode in `coverage-report.md`.

Accept `depth: concise | comprehensive | deep`; default to `comprehensive`. `final-review` is a teaching document, not a compressed outline. The depth option does not authorize omissions.

Read [bilingual-writing.md](references/bilingual-writing.md) when deciding terminology. Read [source-and-priority.md](references/source-and-priority.md) before assigning exam importance. Read [output-schemas.md](references/output-schemas.md) before drafting. Read [quality-gates.md](references/quality-gates.md) before verification.

## Workflow

### 1. Inventory and classify

Create a source inventory before summarizing. For every file record its path, type, apparent role, lecture identifier, title, page/slide count, language, and ordering evidence.

Classify files as lecture, review, syllabus, assignment, quiz/exam, answer key, or unknown. Search case-insensitively for `revision`, `review`, `final review`, `recap`, `summary`, `复习`, `总复习`, `考试重点`, and equivalent content signals. Confirm candidates from their contents rather than filenames alone.

Resolve lecture order using, in priority order: explicit syllabus schedule, lecture numbering inside the deck, dates, internal prerequisite statements, then filenames. Report missing, duplicate, or ambiguous items. Never silently guess an uncertain order.

### 2. Establish assessment evidence

Read the syllabus and review materials before deep chapter drafting. Extract explicit scope, exclusions, weights, formats, named topics, instructor warnings, and emphasized formulas. Then inspect assignments, quizzes, and past exams for recurring assessed skills.

Separate evidence labels:

- `Explicit`: directly stated by the instructor or assessment material.
- `Observed`: recurring in assignments, quizzes, or past exams.
- `Inferred`: predicted from repetition, examples, summaries, or dependencies.

Never present an inferred exam point as instructor-confirmed. If sources conflict, report the conflict with citations instead of choosing silently.

### 3. Build a global map

Read all decks broadly before writing chapter summaries. Identify major themes, subtopics, prerequisites, formula-heavy regions, examples, and assessment links.

Create one canonical `course-map.json`, then derive `course-map.mmd` as a Mermaid mind map showing course → major themes → subtopics → lecture identifiers. The map may show conceptual dependencies, but the written review must retain original lecture order.

Use a privacy-safe rendering ladder: (1) use a trusted local Mermaid renderer when its browser runtime is permitted; (2) otherwise derive a PDF-native LaTeX hierarchy/tree from the same JSON and embed it, while preserving `.mmd`; (3) use a remote renderer only with explicit user consent because it transmits course structure. Never bypass the sandbox. Mermaid image rendering is conditional; an embedded map consistent with the canonical JSON is mandatory.

### 4. Build the coverage ledger

Create one ledger row for every source page or PPTX slide. At minimum record:

`source_id`, `lecture_id`, `page_or_slide`, `topic`, `concept_id`, `importance`, `disposition`, `summary_location`, `explanation_depth`, `visual_check`, `citation`, `notes`.

Allowed dispositions are `covered`, `duplicate`, `administrative`, `blank`, and `uncertain`. Every row must have a disposition. `duplicate`, `administrative`, and `blank` require a short reason; `uncertain` blocks completion until resolved or explicitly accepted by the user.

Use `scripts/validate_coverage.py` to validate the machine-readable CSV ledger before finalization.

### 5. Summarize in strict source order

Write `final-review` by lecture order, then by page/slide order within each lecture. Do not reorganize the main chapters for thematic elegance. Handle cross-links with “see Lecture X” references rather than moving content.

For each chapter include, where supported:

- learning focus and assessment relevance
- definitions and core concepts
- formulas with symbol meanings, assumptions, and conditions
- methods or derivations in their presented order
- representative worked-example patterns
- links to assignments, quizzes, or past exams
- likely traps and distinctions
- tight page/slide citations

For every substantive core concept, explain rather than merely name it: definition or preserved original wording; intuition and purpose; mechanism, derivation, or steps; assumptions and boundary conditions; a representative example or exam application; failure/attack mode where relevant; distinctions from nearby concepts; and tight citations. Formula entries must define variables and conditions and include an application. Algorithms and protocols must preserve their sequence or message flow. Charts and tables must explain axes/headers, encodings, trend or relationship, and the supported conclusion.

Every explicit Revision topic needs a complete explanation. A ledger row is not “covered” merely because its title or keywords appear. Use the selected depth consistently and record it in the ledger.

Compress duplicates but retain citations to every occurrence. Never drop later lectures because of context limits; segment the work and merge only after every ledger range has been processed.

### 6. Inspect visual evidence

Render and inspect source pages/slides when they contain formulas, derivations, tables, charts, diagrams, spatial annotations, low extracted-text density, OCR anomalies, or layout-dependent meaning.

Verify subscripts, superscripts, operators, matrices, arrows, axes, legends, table row/column relations, color semantics, and animation-like incremental slides. Mark each inspected item in the ledger. Do not reconstruct unreadable mathematics or diagrams from guesswork.

### 7. Derive the companion documents

Generate `quick-reference` and `mistakes-and-distinctions` from the verified chapter notes and source evidence, not from memory alone. These documents may reorganize content for lookup, but every entry must retain lecture/page citations.

Do not omit non-formula courses from `quick-reference`; use definitions, frameworks, cases, dates, vocabulary, or comparison tables as appropriate.

### 8. Generate a source-grounded mock exam when applicable

Read [mock-exam.md](references/mock-exam.md). Build the blueprint before drafting questions. Use evidence in this order for assessment shape: explicit Revision/syllabus rules, past exams, quizzes/assignments, then lecture examples. Preserve stated format and marks; disclose missing information rather than inventing instructor policy.

Create new questions or meaningful variants by default. Keep answers separate. Cite sources in the solution document, not the question paper. Validate answerability, uniqueness of single-choice answers, numerical/protocol correctness, mark totals, topic balance, difficulty balance, and absence of unsupported content.

### 9. Verify and build

Run all gates in [quality-gates.md](references/quality-gates.md). A verifier must compare drafts against source pages and the coverage ledger, not merely review the prose.

Compile each `.tex` with XeLaTeX or another engine proven to preserve the selected language and mathematics. Render every generated PDF to images and inspect for missing glyphs, overflow, clipping, overlap, broken formulas, unreadable tables, and course-map placement. Fix and re-run checks until all blocking gates pass.

## Citation format

Use stable citations such as `[Lecture 04, p.17]`, `[Lecture 04, slides 17–19]`, `[Revision, p.8]`, or `[Quiz 2, Q3]`. Prefer exact pages; use tight ranges only for genuinely continuous material. Cite all sources when synthesizing across documents.

## Completion rules

Do not claim “no omissions” as an unsupported absolute. Report verified coverage numerically and disclose exclusions and uncertainties. Completion requires:

- every source inventoried and ordered or explicitly unresolved
- every page/slide represented in the coverage ledger
- zero uncovered or uncertain ledger rows
- all explicit review topics represented
- all required visual pages checked
- all citations sampled and validated
- the three core `.tex` files and three successfully compiled, visually checked PDFs
- mock-exam artifacts when assessment evidence or the user request triggers them
- canonical map JSON, Mermaid source, and a successfully embedded Mermaid or PDF-native fallback map
- a complete `coverage-report.md` with PASS/FAIL results
