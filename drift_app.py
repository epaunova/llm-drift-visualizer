import streamlit as st
from difflib import HtmlDiff
from nltk.translate.bleu_score import sentence_bleu
from textblob import TextBlob
import matplotlib.pyplot as plt

def jaccard_similarity(list1, list2):
    set1, set2 = set(list1), set(list2)
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    return len(intersection) / len(union) if union else 0

def get_sentiment(text):
    tb = TextBlob(text)
    polarity = tb.sentiment.polarity
    if polarity > 0.1:
        return "Positive", polarity
    elif polarity < -0.1:
        return "Negative", polarity
    else:
        return "Neutral", polarity

# --- HEADER & BRANDING ---
st.markdown(
    """
    <h1 style='color:#222e50;'>🔎 LLM Drift Visualizer</h1>
    <p style='font-size:1.1em; color:#464646;'>
        Compare outputs from different LLM versions and see where their behavior or style "drifts".<br>
        <b>By Eva Paunova | <a href='https://www.linkedin.com/in/eva-hristova-paunova-a194b3210' target='_blank'>LinkedIn</a> | <a href='https://github.com/epaunova' target='_blank'>GitHub</a></b>
    </p>
    """, unsafe_allow_html=True)

st.markdown("> **Paste two LLM outputs below (from different models or versions):**")
output1 = st.text_area("LLM Output 1", height=120)
output2 = st.text_area("LLM Output 2", height=120)

if st.button("Compare"):
    if output1 and output2:
        # Visual diff
        d = HtmlDiff()
        html_diff = d.make_table(output1.splitlines(), output2.splitlines(), "Output 1", "Output 2")
        st.markdown("### 🔍 Textual Differences", unsafe_allow_html=True)
        st.components.v1.html(html_diff, height=250, scrolling=True)

        # BLEU Score (simple similarity)
        try:
            bleu = sentence_bleu([output1.split()], output2.split())
            st.success(f"**BLEU Similarity Score:** {bleu:.2f} _(1 = identical, 0 = totally different)_")
        except Exception as e:
            bleu = None
            st.error(f"Could not compute BLEU score: {e}")

        # Drift Score
        drift = 1 - bleu if bleu is not None else None
        if drift is not None:
            st.markdown(f"**Drift Score:** `{drift:.2f}`")

        # Length Diff
        len1 = len(output1.split())
        len2 = len(output2.split())
        length_diff = abs(len1 - len2)
        st.markdown(f"**Length (Output 1):** {len1} words  \n**Length (Output 2):** {len2} words")
        st.markdown(f"**Length difference:** {length_diff} words")

        # Lexical Jaccard Similarity
        jaccard = jaccard_similarity(output1.split(), output2.split())
        st.markdown(f"**Token Overlap (Jaccard):** {jaccard:.2f} _(1 = identical words, 0 = no overlap)_")

        # Unique Words Difference
        unique1 = set(output1.split())
        unique2 = set(output2.split())
        only_in_1 = unique1 - unique2
        only_in_2 = unique2 - unique1
        st.markdown("**Unique words only in Output 1:** " + ", ".join(only_in_1) if only_in_1 else "None")
        st.markdown("**Unique words only in Output 2:** " + ", ".join(only_in_2) if only_in_2 else "None")
        
        # Manual factuality score (for demo)
        st.markdown("### 🧠 Manual scoring (optional)")
        fact_score = st.slider("Manual Factuality (0 = hallucinated, 1 = fully factual):", 0.0, 1.0, 0.5, 0.01)
        st.info(f"Manual Factuality score set to: {fact_score:.2f}")

        # Sentiment analysis
        st.markdown("### 📊 Sentiment Analysis")
        sent1, pol1 = get_sentiment(output1)
        sent2, pol2 = get_sentiment(output2)
        st.markdown(f"**Output 1:** {sent1} (score: {pol1:.2f})")
        st.markdown(f"**Output 2:** {sent2} (score: {pol2:.2f})")

        # Bar chart for metrics
        st.markdown("### 📈 Key Metrics Bar Chart")
        metrics = {
            'BLEU': bleu if bleu is not None else 0,
            'Drift': drift if drift is not None else 0,
            'Token Overlap': jaccard,
            'Length Diff': length_diff / max(len1, len2, 1)  # normalized
        }
        fig, ax = plt.subplots()
        ax.bar(metrics.keys(), metrics.values(), color=['#3e78b2', '#f6511d', '#7fb800', '#b2b2b2'])
        ax.set_ylabel('Score')
        st.pyplot(fig)

    else:
        st.warning("Please paste both outputs to compare.")

# --- FOOTER ---
st.markdown("""
---
<small>
Made by <a href='https://www.linkedin.com/in/eva-hristova-paunova-a194b3210' target='_blank'>Eva Paunova</a> | 
<a href='https://github.com/epaunova' target='_blank'>GitHub</a> |
Demo for LLM evaluation, drift & prompt engineering prototyping
</small>
""", unsafe_allow_html=True)
