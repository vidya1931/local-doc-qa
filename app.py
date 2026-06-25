import streamlit as st
import json
from llama_cpp import Llama

llm = Llama(
    model_path="models/tinyllama.gguf",
    n_ctx=2048
)

st.title("Local Document Q&A")

question = st.text_input("Ask a question")

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

    response = llm(prompt, max_tokens=200)

    st.write(response["choices"][0]["text"])

