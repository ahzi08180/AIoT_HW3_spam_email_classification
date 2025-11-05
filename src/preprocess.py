"""Simple preprocessing and data loading utilities for the project.

This file provides a small, robust loader that accepts either a local CSV
path or an HTTP(S) URL and returns a pandas DataFrame with columns
['label','text'].
"""
from typing import Tuple
import io
import os

import pandas as pd


def load_dataset(path_or_url: str) -> pd.DataFrame:
    """Load dataset from a local path or URL.

    Expected CSV format (no header): label,text
    Returns DataFrame with columns ['label','text'] where label is 'spam' or 'ham'.
    """
    if path_or_url.startswith("http://") or path_or_url.startswith("https://"):
        df = pd.read_csv(path_or_url, header=None, names=["label", "text"])
    else:
        df = pd.read_csv(path_or_url, header=None, names=["label", "text"])

    # Basic cleaning
    df = df.dropna()
    df["text"] = df["text"].astype(str)
    df["label"] = df["label"].astype(str).str.strip().str.lower()

    # Normalize label values (if labels are 0/1, map to ham/spam)
    if set(df["label"].unique()).issubset({0, 1}):
        df["label"] = df["label"].map({0: "ham", 1: "spam"})

    return df[["label", "text"]]


def train_test_split(df: pd.DataFrame, test_size: float = 0.2, random_state: int = 42) -> Tuple[pd.Series, pd.Series, pd.Series, pd.Series]:
    from sklearn.model_selection import train_test_split as sk_split

    X = df["text"]
    y = df["label"].map({"ham": 0, "spam": 1})
    return sk_split(X, y, test_size=test_size, random_state=random_state, stratify=y)
