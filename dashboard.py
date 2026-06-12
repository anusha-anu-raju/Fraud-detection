import streamlit as st
import joblib
import pandas as pd

model = joblib.load("fraud_model.pkl")

st.set_page_config(page_title="Fraud Detection", layout="wide")
st.title("Credit Card Fraud Detection")
st.write("Enter the transaction features below and click Predict.")

with st.form(key="fraud_form"):
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        time = st.number_input("Time", value=0.0, format="%.6f")
        v1 = st.number_input("V1", value=0.0, format="%.6f")
        v5 = st.number_input("V5", value=0.0, format="%.6f")
        v9 = st.number_input("V9", value=0.0, format="%.6f")
        v13 = st.number_input("V13", value=0.0, format="%.6f")
        v17 = st.number_input("V17", value=0.0, format="%.6f")
        v21 = st.number_input("V21", value=0.0, format="%.6f")
        v25 = st.number_input("V25", value=0.0, format="%.6f")
        amount = st.number_input("Amount", value=0.0, format="%.2f")

    with col2:
        v2 = st.number_input("V2", value=0.0, format="%.6f")
        v6 = st.number_input("V6", value=0.0, format="%.6f")
        v10 = st.number_input("V10", value=0.0, format="%.6f")
        v14 = st.number_input("V14", value=0.0, format="%.6f")
        v18 = st.number_input("V18", value=0.0, format="%.6f")
        v22 = st.number_input("V22", value=0.0, format="%.6f")
        v26 = st.number_input("V26", value=0.0, format="%.6f")

    with col3:
        v3 = st.number_input("V3", value=0.0, format="%.6f")
        v7 = st.number_input("V7", value=0.0, format="%.6f")
        v11 = st.number_input("V11", value=0.0, format="%.6f")
        v15 = st.number_input("V15", value=0.0, format="%.6f")
        v19 = st.number_input("V19", value=0.0, format="%.6f")
        v23 = st.number_input("V23", value=0.0, format="%.6f")
        v27 = st.number_input("V27", value=0.0, format="%.6f")

    with col4:
        v4 = st.number_input("V4", value=0.0, format="%.6f")
        v8 = st.number_input("V8", value=0.0, format="%.6f")
        v12 = st.number_input("V12", value=0.0, format="%.6f")
        v16 = st.number_input("V16", value=0.0, format="%.6f")
        v20 = st.number_input("V20", value=0.0, format="%.6f")
        v24 = st.number_input("V24", value=0.0, format="%.6f")
        v28 = st.number_input("V28", value=0.0, format="%.6f")

    submitted = st.form_submit_button("Predict")

if submitted:
    transaction = {
        "Time": time,
        "V1": v1,
        "V2": v2,
        "V3": v3,
        "V4": v4,
        "V5": v5,
        "V6": v6,
        "V7": v7,
        "V8": v8,
        "V9": v9,
        "V10": v10,
        "V11": v11,
        "V12": v12,
        "V13": v13,
        "V14": v14,
        "V15": v15,
        "V16": v16,
        "V17": v17,
        "V18": v18,
        "V19": v19,
        "V20": v20,
        "V21": v21,
        "V22": v22,
        "V23": v23,
        "V24": v24,
        "V25": v25,
        "V26": v26,
        "V27": v27,
        "V28": v28,
        "Amount": amount,
    }

    df = pd.DataFrame([transaction])
    prediction = model.predict(df)
    result = "Fraud" if int(prediction[0]) == 1 else "Not Fraud"

    st.markdown("---")
    st.subheader("Prediction Result")
    st.write(f"**{result}**")
    st.json({"fraud": int(prediction[0])})
