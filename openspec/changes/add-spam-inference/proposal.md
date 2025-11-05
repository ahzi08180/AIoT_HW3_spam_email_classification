# Change: Add spam inference CLI and REST API

## Why
Users and graders need an easy, reproducible way to classify new email messages using the trained model. Currently the repository contains training artifacts and notebooks but lacks a simple inference interface for programmatic use and integration tests.

## What changes
- Add a small CLI `spam-infer` for local inference using a saved model artifact.
- Add a lightweight REST API (`/predict`) implemented with FastAPI (optional feature flag) for sending messages and receiving spam/ham predictions.
- Add end-to-end tests that exercise CLI and API flows using a tiny test model.
- Add documentation and examples in `README.md` and `openspec/changes/add-spam-inference/tasks.md`.

**BREAKING**: None expected. This is additive.

## Impact
- Affected specs: `specs/spam/spec.md` (added delta under changes)
- Affected code: `src/infer.py` (new CLI entrypoint), `src/api.py` (new FastAPI server), `tests/test_infer.py`, CI workflow (optional step to run API smoke tests)

## Rollout plan
1. Merge the change proposal after review/approval.
2. Implement CLI and unit tests in a feature branch and open a PR.
3. Run `openspec validate add-spam-inference --strict` and fix any spec formatting issues.
4. Add a small GitHub Actions job to run CLI tests (optional).

## Acceptance criteria
- `python -m src.infer --model models/local.pkl --text "Free money"` returns a deterministic label and probability.
- `POST /predict` with JSON `{ "text": "Free money" }` returns `{ "label": "spam", "score": 0.98 }` (schema validated in tests).
- Tests covering CLI and API pass in CI.

## Alternatives considered
- Only add a CLI (no API) — easier, but reduced integration testing utility. We choose CLI + optional API to maximize utility with small extra cost.

## Open questions
- Do you want the API to be included in CI (run with Uvicorn during tests) or only run locally?
- Preferred CLI interface: short flags (`--model`) or subcommands (`spam infer`)? Current proposal uses simple flags.

---
Placeholders: implementation tasks are listed in `tasks.md`.
