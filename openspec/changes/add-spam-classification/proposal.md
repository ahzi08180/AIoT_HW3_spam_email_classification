# Change: Add spam email classification baseline (logistic regression)

## Why
This project is a homework assignment to build a reproducible spam email classification pipeline. We need a clear baseline ML implementation (train/evaluate/save) that instructors and collaborators can run locally and extend in later phases.

## What changes
- Phase 1 (baseline): implement a reproducible training pipeline using Logistic Regression. Use the dataset at:

```
https://raw.githubusercontent.com/PacktPublishing/Hands-On-Artificial-Intelligence-for-Cybersecurity/refs/heads/master/Chapter03/datasets/sms_spam_no_header.csv
```

- Provide preprocessing, a training script/notebook, model serialization, basic evaluation (accuracy, precision, recall, F1), and usage examples.
- Add unit tests and a small integration test that trains and evaluates on a tiny sampled subset to ensure the pipeline runs in CI.

Phase 2 and later phases are planned but intentionally left empty now; they will be filled once Phase 1 is complete and we have results to guide further work.

## Scope
- Implement Phase 1: data ingestion, preprocessing, baseline model (Logistic Regression), evaluation, and saving model artifact.
- Optional: compare to an SVM baseline as an experiment (not required for Phase 1).

## Impact
- Affected code: `src/preprocess.py`, `src/train.py`, `src/evaluate.py`, `src/infer.py` (CLI), `notebooks/` for exploration, `models/` for artifacts, `tests/` for unit/integration tests.
- Affected specs: add a spec describing the baseline training capability and data ingestion.

## Acceptance criteria
- Training script `python -m src.train --data <path_or_url> --out models/baseline.pkl` completes successfully on the provided dataset (or a local sample) and produces a saved model file.
- Evaluation report (stdout or file) includes accuracy, precision, recall, and F1 macro/micro as appropriate.
- A minimal test exists that runs the training pipeline on a tiny synthetic or sampled dataset and asserts the pipeline completes and outputs a model file.

## Rollout plan
1. Create change proposal (this file).
2. Implement Phase 1 tasks in a feature branch and open a PR.
3. Run tests and `openspec validate add-spam-classification --strict`.
4. After review & merge, archive the change and update canonical specs if desired.

## Open questions / Clarifications
- You said the project will use Logistic Regression; you also mentioned SVM — should Phase 1 be strictly Logistic Regression (preferred), or do you want SVM as the baseline instead? If you prefer SVM, I will update the tasks to use SVM for Phase 1.
- Do you want the training script to download the dataset automatically from the provided URL when a URL is supplied, or should we require the user to download it manually into `data/`? Default: the script accepts either a local path or an HTTP(S) URL and will download when given a URL.

---
Phases (placeholder):

- Phase 1: baseline — Logistic Regression implementation (current scope)
- Phase 2: 
- Phase 3: 
