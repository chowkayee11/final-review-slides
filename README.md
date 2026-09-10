# final-review-slides

[简体中文](README.zh-CN.md)

`final-review-slides` is a Codex skill for turning PDF and PowerPoint lecture materials into source-cited final-exam review packs and mock exams. It supports English, Chinese, and mixed-language courses while preserving lecture order, technical terminology, formulas, and traceable page or slide references.

## Features

- Accepts one or more `.pdf` and `.pptx` lecture decks.
- Reads optional Revision/Review decks, syllabi, assignments, quizzes, midterms, past exams, answer keys, and course outlines.
- Automatically resolves the output language when the user does not specify one.
- Uses Chinese explanations by default while retaining important English definitions, technical terms, proper nouns, abbreviations, formula variables, and exam-relevant original wording.
- Supports `auto`, `zh`, `en`, and `bilingual` language modes.
- Supports `concise`, `comprehensive`, and `deep` explanation depths; `comprehensive` is the default.
- Builds a global course map before writing lecture-by-lecture summaries.
- Preserves the original lecture and slide sequence in the main review.
- Adds tight citations such as `[Lecture 04, p.17]` and `[Quiz 2, Q3]`.
- Requires visual inspection for formulas, derivations, charts, tables, diagrams, and layout-dependent content.
- Generates source-grounded mock exams with separate solutions when assessment evidence is available or the user requests one.
- Applies blocking quality gates for coverage, depth, ordering, citations, formulas, visual evidence, rendering, and assessment fidelity.

## Inputs

Required:

- One or more lecture decks in `.pdf` or `.pptx` format.

Optional:

- Revision, Review, Final Review, recap, or summary decks
- syllabus or course outline
- assignments and homework
- quizzes and midterms
- past exams and answer keys

## Default outputs

The skill generates the following core artifacts:

```text
final-review.tex
final-review.pdf
quick-reference.tex
quick-reference.pdf
mistakes-and-distinctions.tex
mistakes-and-distinctions.pdf
coverage-report.md
course-map.json
course-map.mmd
```

When mock-exam generation is triggered, it also produces:

```text
mock-exam.tex
mock-exam.pdf
mock-exam-solutions.tex
mock-exam-solutions.pdf
mock-exam-blueprint.md
```

The generated LaTeX sources are retained so users can revise typography, content, or page layout later.

## Installation

Clone the repository into your personal Codex skills directory:

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/chowkayee11/final-review-slides.git \
  ~/.codex/skills/final-review-slides
```

Restart Codex or begin a new task so the skill can be discovered.

## Usage

Invoke the skill by name and provide the course-material path:

```text
Use $final-review-slides to read all lecture materials in
/path/to/course/lectures and generate a comprehensive final-review pack.
```

Specify language and depth when needed:

```text
Use $final-review-slides with language=bilingual and depth=deep.
Include the Revision deck, quizzes, and past exams, and generate a mock exam
with a separate solution booklet.
```

A Chinese request works as well:

```text
使用 $final-review-slides 读取这个目录中的全部讲义。
采用中文讲解并保留重要英文术语，生成完整复习资料和一套模拟题。
```

## Language behavior

| Mode | Behavior |
|---|---|
| `auto` | Chinese explanations with important English source wording retained; follows the source language only when explicitly requested. |
| `zh` | Chinese primary text with English technical terminology preserved where useful. |
| `en` | Natural academic English with source-language terminology retained when necessary. |
| `bilingual` | A selected primary language for explanations and a secondary language for terminology, concise definitions, and exam wording. |

The skill does not translate variables, standard abbreviations, theorem names, algorithm names, or formal notation.

## Explanation depth

| Level | Intended use |
|---|---|
| `concise` | Faster review with compact explanations; source coverage is still mandatory. |
| `comprehensive` | Default teaching-oriented review with definitions, intuition, mechanisms, conditions, examples, distinctions, and citations. |
| `deep` | More detailed derivations, protocol traces, worked applications, and boundary-case analysis. |

Mentioning a topic title or keyword does not count as explaining it. Explicit Revision topics and high-importance concepts must receive complete explanations.

## Mock-exam generation

The skill builds an exam blueprint before writing questions. Evidence is prioritized as follows:

1. Explicit Revision/Review and syllabus statements
2. Past exams
3. Quizzes and assignments
4. Lecture examples

Questions are newly written or meaningfully varied by default. The question paper does not contain answers or revealing citations. The separate solution booklet includes model answers, working or reasoning, marking points, common errors, difficulty, assessed concepts, and source citations.

The validator checks answerability, topic and difficulty balance, total marks, single-choice answer uniqueness, formula and protocol correctness, and unsupported content.

## Course-map rendering

`course-map.json` is the canonical course structure. The skill derives `course-map.mmd` from it and uses a privacy-safe rendering ladder:

1. Render Mermaid locally when a trusted browser runtime is permitted.
2. If local browser execution is blocked, generate a PDF-native LaTeX hierarchy from the same JSON and embed it in `final-review.pdf`.
3. Use a remote Mermaid renderer only with explicit user consent, because remote rendering transmits the course structure to a third party.

The Mermaid source is always preserved. The skill never attempts to bypass the execution sandbox.

## Quality gates

Completion requires, as applicable:

- every supplied source is inventoried and classified;
- lecture ordering is supported by evidence;
- every page or slide has a valid coverage disposition;
- the main review follows lecture and intra-lecture order;
- every explicit Revision topic maps to a complete explanation;
- formulas and visually dependent content are verified against rendered source pages;
- sampled citations resolve to directly supporting pages;
- derived reference sheets remain traceable to source evidence;
- all required LaTeX documents compile successfully;
- every generated PDF passes visual inspection;
- mock-exam questions and solutions pass assessment-specific validation.

The skill reports verified coverage numerically and discloses exclusions or unresolved uncertainty instead of claiming unsupported perfection.

## Repository structure

```text
final-review-slides/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── assets/
│   └── review-template.tex
├── references/
│   ├── bilingual-writing.md
│   ├── mock-exam.md
│   ├── output-schemas.md
│   ├── quality-gates.md
│   └── source-and-priority.md
└── scripts/
    └── validate_coverage.py
```

## Limitations

- Output quality depends on source readability and completeness.
- Image-only or low-quality scans may require OCR and additional visual verification.
- Animation sequences in PowerPoint may need slide-by-slide reconstruction.
- The skill does not treat inferred exam priorities as instructor-confirmed facts.
- Remote Mermaid rendering is disabled unless the user explicitly authorizes it.

## Contributing

Issues and pull requests are welcome. Changes to workflow or output requirements should preserve source traceability, strict lecture order, visual verification, and blocking quality gates.

