# 🔎 LLM Drift Visualizer

[![Streamlit](https://img.shields.io/badge/Streamlit-App-green)](https://llm-drift-visualizer-hrv8yrnp4wffcgeynmd9f4.streamlit.app/)

## Description

An interactive Streamlit app to visualize and compare outputs from different versions or models of Large Language Models (LLMs).  
See behavioral and stylistic “drifts” between two texts with easy-to-understand metrics and visual diffs.

---
# LLM Drift Visualizer

## 🧠 Project Summary

Large Language Models (LLMs) like GPT-4 and Claude continuously evolve due to fine-tuning, alignment updates, and infrastructure changes. These updates often cause silent shifts in model behavior, referred to as **semantic drift** or **alignment drift**.

This project provides a **lightweight evaluation framework** to visualize and measure such drift across LLM versions using embedding-based metrics, prompt consistency, and groundedness degradation. The goal is to give AI/ML practitioners, evaluators, and safety teams tools to:

* Quantify how model responses change
* Identify which prompts are most sensitive to drift
* Track hallucination and retrieval-coherence divergence over time

---

## 🚀 Use Cases

* **LLM Regression Testing**: Detect when newer models produce inconsistent or degraded outputs
* **Alignment Audits**: Check if model outputs become overly oblique, evasive, or "aligned to avoidance"
* **Drift-aware Prompting**: Identify which prompt structures are more robust to updates
* **Trust & Safety Monitoring**: Track factual grounding or hallucination rate after updates

---

## 📊 Features

* Embedding-based drift score (Cosine similarity distance between outputs)
* Support for multiple model versions: GPT-4, Claude, Mistral, etc.
* JSON-based prompt-output input files for easy evaluation
* Visualizations: Drift heatmaps, time-series drift trend, token-level change markers
* Extensible: Plug in your own metrics (e.g. perplexity delta, novelty score, groundedness checks)

---

## 🧰 Tech Stack

* Python 3.10+
* `transformers`, `sentence-transformers`, `openai`, `numpy`, `matplotlib`
* `scikit-learn`, `pandas`, `json`

---

## 📁 Project Structure

```
llm-drift-visualizer/
├── README.md
├── requirements.txt
├── notebooks/
│   └── drift_analysis.ipynb          # Core metrics + plots
├── scripts/
│   └── compute_drift.py              # Command-line tool for batch drift calc
├── data/
│   ├── gpt4_outputs_v1.json
│   └── gpt4_outputs_v2.json
├── plots/
    └── sample_drift_plot.png
```

---

## 📥 Input Format (JSON)

```json
[
  {
    "prompt": "What is the capital of France?",
    "output_v1": "The capital of France is Paris.",
    "output_v2": "Paris is the capital of France."
  },
  ...
]
```

---

## 📈 Sample Output

![example](plots/sample_drift_plot.png)

---

## 📌 Example Metrics (extensible)

* **Cosine Drift**: Distance between output embeddings
* **Style Drift**: Change in length, tone, verbosity
* **Groundedness Drop**: Decreased coherence with retrieved documents
* **Prompt Sensitivity Index**: Std dev of drift over variants of same query

---

## 💡 Next Steps

* [ ] Add hallucination detection via retrieval-grounding mismatch
* [ ] Integrate perplexity metrics for fluency change
* [ ] Add CLI interface for model-agnostic batch comparison
* [ ] Export drift reports in markdown or HTML for auditability

---

## 👤 Author

Eva Paunova
AI/ML Researcher | LLM Evaluation | Drift Analysis | Applied Safety
[https://github.com/epaunova](https://github.com/epaunova)

---

## 📜 License

MIT
