"""Streamlit demo for the spam classification baseline.

Usage:
    pip install -r requirements.txt
    streamlit run streamlit_app.py

The app will try to load `models/baseline.joblib` by default. You can upload a joblib model bundle (vectorizer+model) as well.
"""
from pathlib import Path
import json

import joblib
import streamlit as st


@st.cache_data
def load_model(path: str):
    try:
        bundle = joblib.load(path)
        return bundle
    except Exception as e:
        st.error(f"Failed to load model: {e}")
        return None


def predict(bundle, text: str):
    vect = bundle["vectorizer"]
    model = bundle["model"]
    X = vect.transform([text])
    prob = float(model.predict_proba(X)[:, 1])
    label = "spam" if prob >= 0.5 else "ham"
    return label, prob


def main():
    st.title("Spam Classification Demo")
    st.write("Simple demo for the hw3_spam_email Logistic Regression baseline.")

    # Construct an absolute path to the model file
    current_dir = Path(__file__).parent
    default_model_path = current_dir / "models" / "baseline.joblib"
    st.sidebar.header("Model")
    use_default = st.sidebar.checkbox("Use default model (models/baseline.joblib)", value=True)
    uploaded_model = st.sidebar.file_uploader("Or upload joblib model bundle", type=["joblib", "pkl"])

    model_bundle = None
    if use_default:
        if Path(default_model_path).exists():
            model_bundle = load_model(default_model_path)
        else:
            st.sidebar.warning(f"Default model not found at {default_model_path}. You can upload one.")

    if uploaded_model is not None:
        # Save uploaded file to a temporary path and load
        tmp_path = Path(".streamlit_uploaded_model.joblib")
        with tmp_path.open("wb") as f:
            f.write(uploaded_model.getbuffer())
        model_bundle = load_model(str(tmp_path))

    st.sidebar.markdown("---")
    st.sidebar.markdown("Model bundle should include `vectorizer` and `model` keys (joblib dump).")

    st.header("Classify a message")

    if "text" not in st.session_state:
        st.session_state.text = "Free money waiting for you!"

    col1, col2 = st.columns(2)
    if col1.button("Generate Ham Example"):
        st.session_state.text = "Hi, I'm just following up on our meeting from yesterday."
    if col2.button("Generate Spam Example"):
        st.session_state.text = "Congratulations! You've won a free cruise to the Bahamas. Click here to claim your prize."

    text = st.text_area("Enter message to classify", value=st.session_state.text, key="text_area")
    if st.button("Predict"):
        if model_bundle is None:
            st.error("No model loaded. Enable default model or upload one.")
        else:
            with st.spinner("Predicting..."):
                label, prob = predict(model_bundle, text)
                st.success(f"Prediction: {label} — score {prob:.4f}")
                st.json({"label": label, "score": prob})

    st.header("Example: batch predictions")
    st.write("Upload a CSV with one text column (no header) to get batch predictions.")
    csv_file = st.file_uploader("Upload CSV for batch predictions", type=["csv"], key="csv")
    if csv_file is not None and model_bundle is not None:
        import csv

        reader = csv.reader(csv_file.getvalue().decode("utf-8").splitlines())
        rows = []
        for r in reader:
            if not r:
                continue
            t = r[0]
            label, prob = predict(model_bundle, t)
            rows.append({"text": t, "label": label, "score": prob})
        st.write(f"Predicted {len(rows)} rows")
        st.dataframe(rows)

    st.sidebar.markdown("---")
    st.sidebar.markdown("If you want me to add a containerized demo or CI steps to run the Streamlit smoke test, tell me and I'll add them.")


if __name__ == "__main__":
    main()
