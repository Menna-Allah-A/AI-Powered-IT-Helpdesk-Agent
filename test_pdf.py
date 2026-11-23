import pymupdf

pdf_path = "knowledge_base/raw/networking/Wireless network connectivity issues tr...pdf"

doc = pymupdf.open(pdf_path)

print("Total pages:", len(doc))

for page_number in range(min(3, len(doc))):
    text = doc[page_number].get_text("text")

    print(f"\n--- Page {page_number + 1} ---")
    print("Extracted characters:", len(text))
    print(repr(text[:500]))