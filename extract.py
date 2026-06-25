import pymupdf4llm

markdown = pymupdf4llm.to_markdown(
    "documents/awp notes.pdf"
)

with open("document.md", "w", encoding="utf-8") as f:
    f.write(markdown)

print("PDF converted successfully!")


