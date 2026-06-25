import json

question = input("Ask a question: ").lower()

with open("sections.json", "r", encoding="utf-8") as f:
    sections = json.load(f)

best_section = None
best_score = 0

for section in sections:

    score = 0

    for word in question.split():
        if word in section["content"].lower():
            score += 1

    if score > best_score:
        best_score = score
        best_section = section

print("\nRelevant Content:\n")
print(best_section["content"][:2000])
