"""Simple CLI to load a saved model and infer a single message or a CSV of messages.

Usage examples:
    python -m src.infer --model models/baseline.joblib --text "Free money"
    python -m src.infer --model models/baseline.joblib --input-file data/sample.csv --output-file out.csv
"""
import argparse
import csv
import json
from pathlib import Path

try:
    import joblib
except Exception:
    joblib = None
import pickle


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--model", required=True, help="Path to saved model (joblib)")
    grp = p.add_mutually_exclusive_group(required=True)
    grp.add_argument("--text", help="Single text message to classify")
    grp.add_argument("--input-file", help="CSV file with messages (first column is text)")
    p.add_argument("--output-file", help="Output CSV for batch predictions")
    return p.parse_args()


def predict_text(model_bundle, text: str):
    vect = model_bundle["vectorizer"]
    model = model_bundle["model"]
    X = vect.transform([text])
    prob = float(model.predict_proba(X)[:, 1])
    label = "spam" if prob >= 0.5 else "ham"
    return {"label": label, "score": prob}


def main():
    args = parse_args()
    if joblib is not None:
        try:
            bundle = joblib.load(args.model)
        except Exception:
            # if joblib fails to load, try pickle
            with open(args.model, "rb") as f:
                bundle = pickle.load(f)
    else:
        with open(args.model, "rb") as f:
            bundle = pickle.load(f)

    if args.text:
        out = predict_text(bundle, args.text)
        print(json.dumps(out))
        return

    # Batch mode
    input_path = Path(args.input_file)
    output_path = Path(args.output_file) if args.output_file else None

    rows = []
    with input_path.open("r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for r in reader:
            if not r:
                continue
            text = r[0]
            rows.append((text, predict_text(bundle, text)))

    if output_path:
        with output_path.open("w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["text", "label", "score"])
            for text, pred in rows:
                writer.writerow([text, pred["label"], pred["score"]])
    else:
        for text, pred in rows:
            print(json.dumps({"text": text, **pred}))


if __name__ == "__main__":
    main()
