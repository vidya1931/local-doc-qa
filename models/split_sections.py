import json

with open("document.md", "r", encoding="utf-8") as f:
    text = f.read()

chunks = text.split("--- PAGE")

sections = []

for i, chunk in enumerate(chunks):
    chunk = chunk.strip()

    if len(chunk) > 50:
        sections.append({
            "id": i,
            "content": chunk
        })

with open("sections.json", "w", encoding="utf-8") as f:
    json.dump(sections, f, indent=2)

print("Created", len(sections), "sections")

