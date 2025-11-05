"""Train a Logistic Regression baseline and save model + evaluation.

Usage:
    python -m src.train --data <path_or_url> --out models/baseline.joblib
"""
import argparse
import json
import os
from pathlib import Path

try:
    import joblib
except Exception:
    joblib = None
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

from .preprocess import load_dataset, train_test_split


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--data", required=True, help="Path or URL to CSV dataset")
    p.add_argument("--out", required=True, help="Output model path (joblib)")
    p.add_argument("--test-size", type=float, default=0.2)
    return p.parse_args()


def train(data_path: str, out_path: str, test_size: float = 0.2):
    df = load_dataset(data_path)
    X_train, X_test, y_train, y_test = train_test_split(df, test_size=test_size)

    vect = TfidfVectorizer(stop_words="english", max_features=5000)
    X_train_t = vect.fit_transform(X_train)
    X_test_t = vect.transform(X_test)

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train_t, y_train)

    preds = model.predict(X_test_t)
    probs = model.predict_proba(X_test_t)[:, 1]

    metrics = {
        "accuracy": float(accuracy_score(y_test, preds)),
        "precision": float(precision_score(y_test, preds, zero_division=0)),
        "recall": float(recall_score(y_test, preds, zero_division=0)),
        "f1": float(f1_score(y_test, preds, zero_division=0)),
    }

    # Ensure output dir
    out_dir = Path(out_path).parent
    out_dir.mkdir(parents=True, exist_ok=True)

    # Save artifacts: vectorizer + model
    # Save artifacts: vectorizer + model. Use joblib when available.
    try:
        joblib.dump({"vectorizer": vect, "model": model}, out_path)
    except Exception:
        # Fallback to pickle if joblib is not installed or fails
        import pickle

        with open(out_path, "wb") as f:
            pickle.dump({"vectorizer": vect, "model": model}, f)

    eval_path = str(Path(out_path).with_name(Path(out_path).stem + "_evaluation.json"))
    with open(eval_path, "w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=2)

    print("Training complete. Model saved to:", out_path)
    print("Evaluation:")
    print(json.dumps(metrics, indent=2))


if __name__ == "__main__":
    args = parse_args()
    train(args.data, args.out, test_size=args.test_size)
