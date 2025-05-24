import streamlit as st
from difflib import HtmlDiff
from nltk.translate.bleu_score import sentence_bleu

# --- HEADER & BRANDING ---
st.markdown(
    """
    <h1 style='color:#222e50;'>🔎 LLM Drift Visualizer</h1>
    <p style='font-size:1.1em; color:#464646;'>
        Compare outputs from different LLM versions and see where their behavior or style "drifts".<br>
        <b>By Eva Paunova | <a href='https://www.linkedin.com/in/eva-hristova-paunova-a194b3210' target='_blank'>LinkedIn</a> | <a href='https://github.com/epaunova' target='_blank'>GitHub</a></b>
    </p>
    """, unsafe_allow_html=True)

# --- INPUT FIELDS ---
st.markdown("#### Paste two LLM outputs below (from different models or versions):")
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
            if bleu > 0.8:
                st.info("Outputs are very similar.")
            elif bleu > 0.4:
                st.warning("Moderate drift detected.")
            else:
                st.error("Significant drift detected!")
        except Exception as e:
            st.error(f"Could not compute BLEU score: {e}")

        # Drift Score (just for demo)
        drift = 1 - bleu if 'bleu' in locals() else None
        if drift is not None:
            st.markdown(f"**Drift Score:** `{drift:.2f}`")
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
