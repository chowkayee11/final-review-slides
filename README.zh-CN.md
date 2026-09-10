# final-review-slides

[English](README.md)

`final-review-slides` 是一个用于期末复习的 Codex Skill，可将 PDF 和 PowerPoint 课程讲义整理为带来源引用的完整复习资料，并根据 Revision、Quiz、作业及往年题生成模拟试卷。它支持中文、英文和中英混合课程，同时保留原始授课顺序、专业术语、公式以及可追溯的页码或幻灯片引用。

## 主要功能

- 支持一个或多个 `.pdf`、`.pptx` 讲义。
- 可读取 Revision/Review 课件、syllabus、作业、Quiz、期中考试、往年题、答案和课程大纲。
- 用户没有指定语言时自动选择输出语言，不会中断任务询问。
- 默认用中文解释，同时保留重要英文定义、专业术语、专有名词、缩写、公式变量及考试可能使用的英文原文。
- 支持 `auto`、`zh`、`en`、`bilingual` 四种语言模式。
- 支持 `concise`、`comprehensive`、`deep` 三种讲解深度，默认为 `comprehensive`。
- 逐章总结前先建立全局课程结构图。
- `final-review` 严格按照讲义和幻灯片的原始顺序编写。
- 为知识点添加 `[Lecture 04, p.17]`、`[Quiz 2, Q3]` 等紧密来源引用。
- 公式、推导、图表、表格、示意图和依赖版面关系的内容必须经过视觉检查。
- 当存在足够的考核资料或用户明确要求时，生成模拟试卷和独立答案册。
- 对覆盖率、讲解深度、顺序、引用、公式、视觉证据、渲染和考试依据设置阻塞式质量门槛。

## 输入资料

必需资料：

- 一个或多个 `.pdf` 或 `.pptx` 格式的课程讲义。

可选资料：

- Revision、Review、Final Review、recap 或 summary 课件
- syllabus 或课程大纲
- 作业和 Homework
- Quiz 和期中考试
- 往年题及答案

## 默认交付物

核心交付物包括：

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

触发模拟题功能时，还会生成：

```text
mock-exam.tex
mock-exam.pdf
mock-exam-solutions.tex
mock-exam-solutions.pdf
mock-exam-blueprint.md
```

所有 LaTeX 源文件都会保留，方便用户后续修改排版、内容或页面布局。

## 安装

将仓库克隆到个人 Codex Skills 目录：

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/chowkayee11/final-review-slides.git \
  ~/.codex/skills/final-review-slides
```

重新启动 Codex 或新建一个任务，使 Skill 被重新发现。

## 使用方法

在请求中写出 Skill 名称并提供课程资料路径：

```text
使用 $final-review-slides 读取 /path/to/course/lectures 中的全部讲义，
生成 comprehensive 深度的期末复习资料。
```

也可以指定语言、深度和模拟题要求：

```text
使用 $final-review-slides，language=bilingual，depth=deep。
读取 Revision、Quiz 和往年题，并生成一套模拟试卷及独立答案册。
```

如果不指定语言，可以直接说：

```text
使用 $final-review-slides 读取这个目录中的所有讲义，
生成完整复习资料、速查表、易错点辨析和模拟题。
```

## 语言规则

| 模式 | 行为 |
|---|---|
| `auto` | 默认使用中文解释并保留重要英文原文；只有用户明确要求“跟随课件语言”时才采用课件主语言。 |
| `zh` | 以中文为主，按需要保留英文专业术语和考试表述。 |
| `en` | 使用自然的学术英语；必要时保留原资料中的中文术语。 |
| `bilingual` | 使用一种主要语言进行讲解，另一种语言用于术语、简洁定义和考试原文。 |

公式变量、标准缩写、定理名称、算法名称和正式数学记号不会被翻译或改写。

## 讲解深度

| 等级 | 适用场景 |
|---|---|
| `concise` | 用于快速复习，讲解较紧凑，但仍必须覆盖全部来源。 |
| `comprehensive` | 默认模式；包含定义、直觉、机制、条件、例子、辨析和来源引用。 |
| `deep` | 提供更详细的推导、协议流程、应用计算和边界情况分析。 |

只写出标题、关键词或一句摘要不算完成讲解。Revision 明确点名的主题和高重要度知识点必须获得完整解释。

每个核心知识点会尽量包含：

- 定义或需要保留的原文表述
- 直觉和用途
- 工作机制、推导或步骤
- 前提条件和适用边界
- 典型例子或考试应用
- 失效条件、攻击方式或常见错误
- 与相近概念的辨析
- 紧密来源引用

## 模拟题生成

Skill 会先建立 `mock-exam-blueprint.md`，再编写题目。命题形式和重点按照以下证据优先级确定：

1. Revision/Review 和 syllabus 中的明确说明
2. 往年题
3. Quiz 和作业
4. Lecture 中的例题

默认生成新题或有实质变化的变式题，不直接复制原题。试卷正文不会包含答案或可能泄露答案的来源提示。独立答案册会为每道题提供标准答案、解题过程、评分点、常见错误、难度、所考知识点和来源引用。

质量检查包括：题目是否能由课程资料作答、重点和难度分布、总分计算、单选题答案唯一性、公式与协议过程是否正确，以及是否包含课程资料无法支持的内容。

## 课程结构图与 Mermaid

`course-map.json` 是唯一的课程结构数据源，`course-map.mmd` 由它生成。Skill 使用注重隐私的分层渲染方案：

1. 安全环境允许可信浏览器运行时，在本地渲染 Mermaid。
2. 本地浏览器被限制时，从同一份 JSON 生成 LaTeX 原生层级图并嵌入 `final-review.pdf`。
3. 只有用户明确同意时才使用远程 Mermaid 渲染服务，因为远程渲染会把课程结构发送给第三方。

Mermaid 源文件始终保留。Skill 不会尝试绕过安全沙箱。

## 质量门槛

完成任务前必须按适用情况满足以下要求：

- 所有输入文件均已登记和分类；
- 讲义顺序具有明确依据；
- 每个页面或幻灯片都有有效的覆盖状态；
- 主复习讲义严格遵循 Lecture 和页内顺序；
- Revision 明确列出的每个重点都对应一段完整讲解；
- 公式和依赖视觉信息的内容已经与渲染后的原页面核对；
- 抽查的引用能够指向直接支持相应结论的页面；
- 速查表和易错点内容均可追溯到课程资料；
- 所有必需的 LaTeX 文件成功编译；
- 所有生成的 PDF 通过视觉检查；
- 模拟题和答案通过专门的考试质量验证。

Skill 会用数字报告已验证的覆盖情况，并披露排除内容和未解决的不确定性，而不是在没有证据时声称“绝无遗漏”。

## 仓库结构

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

## 已知限制

- 输出质量取决于源文件的清晰度和完整性。
- 纯图片或低清晰度扫描件可能需要 OCR 和额外的视觉核验。
- PowerPoint 动画形成的渐进式内容可能需要逐页重建。
- Skill 不会把模型推测的考试重点表述为教师明确确认的内容。
- 未经用户明确授权，不使用远程 Mermaid 渲染服务。

## 参与贡献

欢迎提交 Issue 和 Pull Request。对流程或输出要求的修改应继续保留来源可追溯性、严格授课顺序、视觉核验和阻塞式质量门槛。

