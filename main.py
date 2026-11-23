from src.ingestion.loader import load_documents

documents = load_documents()

print(f"Total documents loaded: {len(documents)}")

for i, document in enumerate(documents):
    print(f"\n--- Document {i + 1} ---")
    print("File:", document.metadata.get("file_name"))
    print("Content preview:", document.text[:500])