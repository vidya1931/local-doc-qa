import streamlit as st
import json
from llama_cpp import Llama
from translator import load_language

# Language selector
language = st.sidebar.selectbox(
    "Select Language",
    ["English", "తెలుగు"]
)

# Load translations
if language == "English":
    lang = load_language("en")
else:
    lang = load_language("te")

# Load model
llm = Llama(
    model_path="models/tinyllama.gguf",
    n_ctx=2048
)

# Title
st.title(lang["title"])

# Question box
question = st.text_input(lang["question"])

if question:

    with open("sections.json", "r", encoding="utf-8") as f:
        sections = json.load(f)

    best_section = None
    best_score = 0

    for section in sections:

        score = 0

        for word in question.lower().split():
            if word in section["content"].lower():
                score += 1

        if score > best_score:
            best_score = score
            best_section = section

    prompt = f"""
Context:
{best_section['content']}

Question:
{question}

Answer:
"""

    with st.spinner(lang["processing"]):
        response = llm(prompt, max_tokens=200)

    st.subheader(lang["answer"])
    st.write(response["choices"][0]["text"])
