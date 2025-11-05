## 1. Implementation
- [ ] 1.1 Create `src/infer.py` with a CLI entrypoint that loads a model and classifies a single string or file
- [ ] 1.2 Add `src/api.py` implementing a minimal FastAPI app with `/predict` that returns `{label, score}`
- [ ] 1.3 Add unit tests: `tests/test_infer_cli.py`, `tests/test_api.py` using a tiny synthetic model
- [ ] 1.4 Add integration test that runs the CLI end-to-end on a small sample
- [ ] 1.5 Update `README.md` with usage examples for CLI and API

## 2. Validation
- [ ] 2.1 Run `pytest` and ensure tests pass
- [ ] 2.2 Run `openspec validate add-spam-inference --strict` and fix any spec formatting

## 3. Optional
- [ ] 3.1 Add a GitHub Actions workflow step to run the CLI smoke test
- [ ] 3.2 Add a small Dockerfile for the API (if you want containerized testing)
