import json
from llama_cpp import Llama

llm = Llama(
    model_path="models/tinyllama.gguf",
    n_ctx=2048
)

question = input("Ask a question: ")

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

context = best_section["content"]

prompt = f"""
Answer only from the provided context.

Context:
{context}

Question:
{question}

Answer:
"""

response = llm(
    prompt,
    max_tokens=200
)

print("\nAnswer:\n")
print(response["choices"][0]["text"])

