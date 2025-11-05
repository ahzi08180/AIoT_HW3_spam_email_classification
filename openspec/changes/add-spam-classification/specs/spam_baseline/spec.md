## ADDED Requirements

### Requirement: Baseline spam classification pipeline
The system SHALL provide a reproducible baseline training pipeline that ingests the provided dataset, preprocesses text, trains a Logistic Regression model, evaluates performance (accuracy, precision, recall, F1), and serializes the trained model for later inference.

#### Scenario: Download and ingest dataset
- **WHEN** the user runs the data loader with the provided URL
- **THEN** the dataset is downloaded, cleaned, and written to `data/processed.csv` and a short summary (rows, columns, label distribution) is printed

#### Scenario: Train baseline model
- **WHEN** the user runs `python -m src.train --data data/processed.csv --out models/baseline.pkl`
- **THEN** the training completes, a serialized model is written to `models/baseline.pkl`, and an evaluation JSON is produced containing accuracy, precision, recall, and F1

#### Scenario: Evaluate and report
- **WHEN** the evaluation step runs
- **THEN** metrics are computed on a held-out test set and written to `models/baseline_evaluation.json` and printed to stdout
