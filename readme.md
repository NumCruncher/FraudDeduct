Here’s how to run your Fraud Detection project:
1. Start the Ollama Service
This project uses the Mistral LLM via Ollama. Start the Ollama service (if not already running):
Apply to readme.md
ollama
Or, if you don’t want it as a background service:
Apply to readme.md
serve

2. Start the Mistral Model
Make sure the Mistral model is available in Ollama. If not, you can pull it with:
Apply to readme.md
mistral

3. Run the Streamlit App
From the FraudDetect directory, run:
Apply to readme.md
py
This will launch a web interface in your browser.

4. Upload a File
Use the web UI to upload an Excel file (e.g., one from the Dataset folder).
The app will detect anomalies and provide explanations for suspicious transactions.

Summary of requirements:
Python (with pandas, scikit-learn, streamlit, langchain-community)
Ollama (with the Mistral model pulled)
Excel file with a column named Amount
Let me know if you want a requirements.txt or run into any issues!

Stop the Mistral Model
This will stop the Mistral model if it is running:
Apply to readme.md
mistral
Stop the Ollama Service
If you started Ollama as a background service with Homebrew, stop it with:
Apply to readme.md
ollama
Or, if you started it manually (with ollama serve), just press Ctrl+C in the terminal where it is running.
Let me know if you want these commands run for you!




To start LLM Runner - ollama now and restart at login:
```
brew services start ollama
```
 How to start LLM model Mistral using Runner Ollama?
```
  ollama run mistral
```

How to run the Isolation Forest ML algorithm to deduct anomaly?

Streamlit is a **Python framework** that makes it super easy to build **interactive web apps for data science, machine learning, and analytics** — all with just a few lines of Python.

Or, if you don't want/need a background service you can just run:

```
 /opt/homebrew/opt/ollama/bin/ollama serve
 streamlit run /Users/elangovanmadhivanan/Documents/GitHub/FraudDetect/IsolationForest_Mistral.py "<filename>"
```

How to start/stop the LLM model from running ?
```
/opt/homebrew/opt/ollama/bin/ollama start mistral
/opt/homebrew/opt/ollama/bin/ollama stop mistral
```


