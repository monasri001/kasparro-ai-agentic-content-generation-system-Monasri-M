# 🧠 Kasparro AI Agentic Content Generation System

*A production-ready multi-agent workflow that transforms minimal product data into complete structured content.*

![Python](https://img.shields.io/badge/Python-3.11+-blue)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Build-Stable-brightgreen.svg)
![Tests](https://img.shields.io/badge/Tests-Passing-success.svg)

---

## 🚀 Overview

This project is a **fully engineered, rule-based multi-agent system** built for the **Kasparro Applied AI Engineer Challenge**.
It converts a small product dataset (8 fields) into **three structured JSON pages**:

* **FAQ Page** — 15+ categorized questions
* **Product Page** — specifications, usage, safety, pricing
* **Comparison Page** — real product vs. a fictional alternative

The system performs **zero external API or LLM calls**.
Everything is built using **deterministic engineering**, not generative AI.

---

## ✨ Key Features

### 🧩 Multi-Agent Architecture

Each agent performs exactly **one responsibility**:

* `ParserAgent` — Validate & structure raw product data
* `QuestionGeneratorAgent` — Generate categorized FAQ questions
* `ContentBlockManager` — Apply 5 reusable logic blocks
* `Template Agents` — Produce final JSON content pages
* `DAGOrchestrator` — Ensures correct execution order

---

### 🔗 DAG-Based Workflow

```
parser → question_generator → content_blocks → faq_template → product_template → comparison_template
```

---

### 🧱 Reusable Content Logic Blocks

Five powerful, modular content processors:

1. Benefits transformation
2. Usage step extraction
3. Ingredient analysis
4. Safety formatting
5. Price/value analysis

---

### 📄 Structured JSON Output

Each generated page follows a **strict, production-ready schema**.

---

### 🧪 Full Test Coverage

Includes:

* Unit tests
* Integration tests
* Full workflow tests

---

## 📂 Project Structure

```
kasparro-ai-agentic-content-generation-system/
│
├── src/
│   ├── agents/                 # All agents (Parser, QGen, Template Agents)
│   ├── models/                 # Pydantic data models
│   ├── logic_blocks/           # Five reusable content logic blocks
│   ├── templates/              # FAQ, Product, Comparison templates
│   ├── orchestration/          # DAG engine for workflow execution
│   └── utils/                  # JSON helpers and utilities
│
├── docs/
│   └── projectdocumentation.md # Full technical documentation
│
├── output/                     # Generated JSON pages
├── tests/                      # Unit + integration + E2E tests
├── main.py                     # Entry point
├── requirements.txt
└── README.md
```

---

## 🛠️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/kasparro-ai-agentic-content-generation-system.git
cd kasparro-ai-agentic-content-generation-system
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate     # Mac/Linux
venv\Scripts\activate        # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Run the System

```bash
python main.py
```

After execution, you will find these files in the `/output` folder:

| Output File            | Description                             |
| ---------------------- | --------------------------------------- |
| `faq.json`             | FAQ page with 15+ categorized questions |
| `product_page.json`    | Full product specifications             |
| `comparison_page.json` | Fictional comparison analysis           |
| `workflow_report.json` | Execution metadata                      |

---

## 🧪 Run Tests

Run all tests:

```bash
pytest tests/
```

Run tests by module:

```bash
python tests/test_parser.py
python tests/test_questions.py
python tests/test_blocks.py
python tests/test_templates.py
python tests/test_full_workflow.py
```

---

## 🧠 Architecture Overview

### Multi-Agent Pipeline

```
Raw Product Data
        ↓
[ParserAgent]
        ↓
Structured ProductData Model
        ↓
-------------------------------
| QuestionGeneratorAgent      |
| ContentBlockManager         |
-------------------------------
        ↓
Template Engine
        ↓
FAQ / Product / Comparison JSON
```

---

### Content Logic Blocks

| Block Name                | Purpose                                                   |
| ------------------------- | --------------------------------------------------------- |
| `BenefitsGeneratorBlock`  | Rewrite raw benefits into structured marketing statements |
| `UsageExtractorBlock`     | Convert usage instructions into stepwise format           |
| `IngredientAnalyzerBlock` | Provide structured ingredient information                 |
| `SafetyWarningBlock`      | Format safety guidelines                                  |
| `PriceFormatterBlock`     | Convert string price into structured value analysis       |

---

### Templates

| Template             | Output                          |
| -------------------- | ------------------------------- |
| `FAQTemplate`        | 5 categories, 15+ questions     |
| `ProductTemplate`    | Detailed product representation |
| `ComparisonTemplate` | A vs. fictional Product B       |

---

## 🔧 Extending the System

### ➕ Add a New Agent

```python
class NewAgent:
    def process(self, data):
        return transformed
```

Register it:

```python
orchestrator.add_node(
    "new_agent",
    NewAgent(),
    dependencies=["parser"]
)
```

---

### ➕ Add a New Block

```python
class NewBlock(ContentLogicBlock):
    @property
    def name(self): return "new-block"

    def apply(self, product):
        return {"result": "..."}
```

---

### ➕ Add a New Template

```python
class NewTemplate(Template):
    @property
    def name(self): return "new_template"

    def render(self, context):
        return {"content": ...}
```

---

## 📈 Evaluation Requirements Met

| Requirement                      | Status |
| -------------------------------- | ------ |
| Multi-agent modular architecture | ✅      |
| Clean DAG execution              | ✅      |
| 15+ categorized questions        | ✅      |
| Three page templates             | ✅      |
| Reusable content blocks          | ✅      |
| JSON schema correctness          | ✅      |
| Zero LLM/external API usage      | ✅      |

---

## 📘 Documentation

Full technical documentation:
📄 `docs/projectdocumentation.md`

Includes:

* System design diagrams
* Detailed agent descriptions
* JSON schemas
* Extensibility guide
* Testing strategy

---

## 🤝 Contributing

```bash
git checkout -b feature/my-feature
git commit -m "Add my feature"
git push origin feature/my-feature
```

Open a Pull Request 🚀

---

## 📄 License

This project is licensed under the **MIT License**.

---

## ❤️ Acknowledgments

* Kasparro for an exceptional engineering assignment
* Pydantic for reliable validation
* Python open-source community

---

