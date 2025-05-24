# 🤖 LLM Hallucination & Robustness Detector (Single Mode)

[![Streamlit](https://img.shields.io/badge/Streamlit-App-green)](https://share.streamlit.io/epaunova/llm-hallucination-detector/main/hallucination_app.py)

Welcome! This Streamlit app is designed to help you quickly spot hallucination patterns and toxicity in outputs from large language models (LLMs) like GPT and others.

---

## What it does

This simple but effective tool lets you:

- Highlight common hallucination trigger phrases  
- Manually rate the factual accuracy with an intuitive slider  
- Run a quick simulated LLM evaluation for instant feedback  
- Detect toxic or offensive language to keep your outputs clean  
- Visualize hallucination triggers frequency in a clear bar chart  

---

## How to use

Just paste a single LLM output into the text area and explore the insights. It’s perfect for fast checks and debugging prompts.

---

## Installation

```bash
pip install streamlit pandas
Running locally
bash
Copy
streamlit run hallucination_app.py
Example text for testing
pgsql
Copy
As far as I know, there is no evidence for this. Some sources claim it is fictional.
Author
Eva Paunova — AI Enthusiast & Product Architect
GitHub | LinkedIn

License
MIT License

