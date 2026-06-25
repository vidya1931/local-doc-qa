import fitz
import pytesseract
from PIL import Image
import io

pdf = fitz.open("documents/awp notes.pdf")

full_text = ""

for page_num in range(len(pdf)):
    page = pdf[page_num]

    pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))

    img_bytes = pix.tobytes("png")

    image = Image.open(io.BytesIO(img_bytes))

    text = pytesseract.image_to_string(image)

    full_text += f"\n\n--- PAGE {page_num+1} ---\n\n"
    full_text += text

with open("document.md", "w", encoding="utf-8") as f:
    f.write(full_text)

print("OCR Extraction Completed!")
