from llama_cpp import Llama

llm = Llama(
    model_path="tinyllama.gguf",
    n_ctx=2048
)

response = llm(
    "What is HTML?",
    max_tokens=50
)

print(response["choices"][0]["text"])
