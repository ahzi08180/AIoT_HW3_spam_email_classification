## ADDED Requirements

### Requirement: Spam inference interfaces
The system SHALL provide programmatic inference interfaces (CLI and REST API) that accept a text message and return a spam/ham label plus an associated confidence score.

#### Scenario: CLI classify single message
- **WHEN** a user runs the CLI with `--model <path>` and `--text "<message>"`
- **THEN** the CLI prints a JSON object containing `label` ("spam"|"ham") and `score` (float 0.0-1.0) and exits with code 0

#### Scenario: CLI classify file of messages
- **WHEN** a user runs the CLI with `--model <path>` and `--input-file <csv>`
- **THEN** the CLI writes predictions to stdout or an output CSV with `text,label,score` columns

#### Scenario: API predict single message
- **WHEN** a client `POST /predict` with JSON `{ "text": "<message>" }`
- **THEN** the service responds with `200` and JSON `{ "label": "spam|ham", "score": <0..1> }`
