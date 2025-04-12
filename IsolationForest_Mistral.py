from langchain_community.llms import Ollama
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest
# from langchain.llms import Ollama
import streamlit as st

# Initialize Ollama
llm = Ollama(model="mistral")  # You can also use 'llama3' or other models


def detect_anomalies(df):
    scaler = StandardScaler()
    df['Amount_1'] = pd.to_numeric(df['Amount'].astype(str).str.replace('[\$,]', '', regex=True), errors='coerce')
    df['Amount_1'] = scaler.fit_transform(df[['Amount_1']])

    model = IsolationForest(n_estimators=100, contamination=0.02, random_state=42)
    model.fit(df[['Amount_1']])

    df['Anomaly'] = model.predict(df[['Amount_1']])
    # Count anomalies
    print(df['Anomaly'].value_counts())
    anomalies_1 = df[df['Anomaly'] == -1]

    return anomalies_1

def explain_anomaly(row):
    prompt = f"""
    This is a financial transaction with the following details:
    - Transaction Amount: {row['Amount']}
    - Detected as Fraud: Yes
    - Provide a reason why this transaction might be suspicious.
    """
    return llm.invoke(prompt)

# For Excel files, we don't need to specify encoding
try:
    # Streamlit UI
    st.title("🔍 AI-Powered Fraud Detection System")

    uploaded_file = st.file_uploader("Upload Excell file", type=["xlsx"])
    # -- "/Users/elangovanmadhivanan/Documents/GitHub/FraudDetect/Dataset/Chase7001_20250101_20250329.xlsx"

    if uploaded_file:
        df = pd.read_excel(uploaded_file)
        anomalies = detect_anomalies(df)

        st.subheader("🚨 Detected Anomalies")
    # Apply explanation function to anomalies
        anomalies['Explanation'] = anomalies.apply(explain_anomaly, axis=1)
        st.write(anomalies[['Amount', 'Explanation']])
    
except Exception as e:
    print(f"Error reading Excel file: {str(e)}")
