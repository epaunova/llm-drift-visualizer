# 🔎 LLM Drift Visualizer

[![Streamlit](https://img.shields.io/badge/Streamlit-App-green)](https://llm-drift-visualizer-hrv8yrnp4wffcgeynmd9f4.streamlit.app/)

## Description

An interactive Streamlit app to visualize and compare outputs from different versions or models of Large Language Models (LLMs).  
See behavioral and stylistic “drifts” between two texts with easy-to-understand metrics and visual diffs.

---

## Key Features

- Visual diff highlighting differences between two texts  
- BLEU similarity score calculation  
- Drift score to measure output divergence  
- Length difference comparison  
- Jaccard similarity (shared token overlap)  
- Unique word listings per output  
- Manual factuality scoring slider  
- Clean and intuitive user interface  

---

## How to Use

1. Paste two LLM outputs (from different models or versions) in the text areas.  
2. Click "Compare".  
3. View visual diffs, similarity metrics, and scoring.

---

## Installation

```bash
pip install streamlit nltk
Run Locally
bash
Copy
streamlit run drift_app.py
Live Demo
Open live demo

Author
Eva Paunova — AI Enthusiast & Product Architect
GitHub | LinkedIn

License
MIT License

yaml
Copy
