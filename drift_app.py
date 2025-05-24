import streamlit as st
from difflib import HtmlDiff

st.title("LLM Drift Visualizer")
st.write("Сравни два LLM отговора и виж къде се разминават. Просто копирай текстовете и натисни Compare.")

output1 = st.text_area("LLM Output 1", height=150)
output2 = st.text_area("LLM Output 2", height=150)

if st.button("Compare"):
    if output1 and output2:
        d = HtmlDiff()
        html_diff = d.make_table(output1.splitlines(), output2.splitlines(), "Output 1", "Output 2")
        st.markdown("### Разлики:", unsafe_allow_html=True)
        st.components.v1.html(html_diff, height=300, scrolling=True)
    else:
        st.warning("Попълни и двата текста за сравнение.")
