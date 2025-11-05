# Project Context

## Project name
hw3_spam_email (Spam Email Classification — course homework)

## Purpose
This repository contains the artifacts and code for a small spam email classification assignment. The goals are:
- Ingest and preprocess an email dataset (CSV / text files)
- Train and evaluate one or more machine learning models to detect spam
- Provide reproducible training and evaluation (notebooks + scripts)
- Offer a small inference interface (CLI and/or lightweight REST API) to classify new messages

Assumptions: this is a student/homework project focused on local, offline ML experiments and reproducibility. If your project is actually a production service, tell me and I will adjust conventions.

## Tech stack (primary)
- Python 3.9+ (recommended 3.10)
- Data: pandas, numpy
- ML: scikit-learn (or optionally XGBoost/lightgbm if needed)
- Notebooks: Jupyter / JupyterLab
- CLI / API: small CLI (argparse / click) and optional FastAPI for REST
- Packaging / tooling: pip / virtualenv; `requirements.txt` or `pyproject.toml` if you prefer Poetry
- (Dev) linters/formatters: black, isort, flake8
- (Ops) openspec CLI (installed globally via npm)

If your project uses Node/TypeScript instead of Python, tell me and I will adapt the stack.

## Recommended repository layout
```
.
├── data/                  # raw and processed datasets (do NOT commit large raw data)
├── notebooks/             # exploratory notebooks (.ipynb)
├── src/                   # package source: preprocessing, models, utils
│   └── hw3_spam_email
│       ├── preprocess.py
│       ├── train.py
│       └── infer.py
├── models/                # trained model artifacts (ignore large files in git)
├── tests/                 # pytest test suite
├── requirements.txt       # runtime/development dependencies
├── README.md
└── openspec/              # OpenSpec files and proposals
	├── project.md
	└── ...
```

## Project conventions

### Code style
- Use `black` for formatting (line-length 88 by default) and `isort` for imports.
- Use typing where practical for public functions.
- Keep modules small and single-purpose.

### Naming
- Python packages: `snake_case` for modules and functions; `PascalCase` for classes.
- CLI commands: verb-led, e.g. `spam-train`, `spam-infer`.

### Architecture patterns
- Small, single-process scripts and notebooks for experiments.
- Keep preprocessing and model code in `src/` so it can be imported by notebooks and scripts.

### Testing strategy
- Unit tests with `pytest` for preprocessing, metrics computation, and small model components.
- A lightweight integration test that runs training on a tiny synthetic dataset to ensure end-to-end flow.
- CI should run `pytest` and a lint step (optional).

### Git workflow
- Main branch: `main` (or `master`) — always keep green for submissions.
- Feature branches: `feature/<short-description>` or `fix/<issue>`.
- Commit messages: short imperative summary; optionally use Conventional Commits for automation.

## Domain context
- Dataset: typical spam/ham classification; messages (text), label (spam/ham), optional metadata (sender, timestamp).
- Typical failure modes: class imbalance, noisy tokens, multi-lingual content.

## Important constraints
- Keep data local; do not commit PII or large raw datasets to Git.
- Model artifacts should be stored under `models/` and large files listed in `.gitignore`.

## External dependencies
- No required external cloud services for the homework default. If you plan to expose a public API or use cloud storage (S3/Azure), document credentials and security requirements before adding them.

## How to run locally (recommended quickstart)
1. Create a virtual environment and install dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2. Run tests:

```powershell
pytest -q
```

3. Run a quick training (small sample):

```powershell
python src/train.py --data data/sample.csv --out models/local.pkl
```

4. Run inference (CLI):

```powershell
python src/infer.py --model models/local.pkl --text "Free money"
```

If you want me to convert this into `pyproject.toml`/Poetry or add CI (GitHub Actions), I can scaffold that next.

## Contact points for the AI assistant
- Refer to `openspec/project.md` when creating proposals.
- Ask 1–2 clarifying questions if a request is ambiguous. Make reasonable assumptions otherwise and note them.

---
Generated/edited by the assistant to capture the current project context. If any of these assumptions are wrong, tell me which parts to change.
