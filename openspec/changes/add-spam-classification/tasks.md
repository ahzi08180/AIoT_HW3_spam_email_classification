## Phase 1 — Baseline (Logistic Regression)

### 1. Data
- [ ] 1.1 Add a data loader that accepts a local file path or URL and writes a cleaned CSV to `data/processed.csv`.
- [ ] 1.2 Add a small sample downloader script for CI testing that creates `data/sample.csv`.

### 2. Preprocessing
- [ ] 2.1 Implement `src/preprocess.py` to tokenize/clean text, handle missing values, and produce train/test splits.

### 3. Training
- [ ] 3.1 Implement `src/train.py` to train a Logistic Regression model (scikit-learn) and save the model (joblib/pickle) to `models/`.
- [ ] 3.2 Save a small evaluation report (JSON) alongside the model.

### 4. Inference
- [ ] 4.1 Implement `src/infer.py` CLI that loads the saved model and predicts on a single string or CSV file.

### 5. Tests and CI
- [ ] 5.1 Add `tests/test_preprocess.py` and `tests/test_train_integration.py` that run on `data/sample.csv`.
- [ ] 5.2 Update CI to run the integration test (optional: skip heavy runs).

### 6. Docs
- [ ] 6.1 Update `README.md` with Phase 1 instructions and examples.

## Phase 2 and later
- [ ] Phase 2: (placeholder)
- [ ] Phase 3: (placeholder)
