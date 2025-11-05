import json
import tempfile
from pathlib import Path

from src import train


def test_train_on_small_sample(tmp_path):
    sample = tmp_path / "sample.csv"
    # two rows: label,text (no header)
    sample.write_text("spam,Free money now!\nham,Hello friend\n")

    out_model = tmp_path / "model.joblib"

    # Should run without raising and write model file
    train.train(str(sample), str(out_model), test_size=0.5)

    assert out_model.exists()
    # evaluation JSON should exist
    eval_path = out_model.with_name(out_model.stem + "_evaluation.json")
    assert eval_path.exists()
    data = json.loads(eval_path.read_text())
    assert "accuracy" in data
