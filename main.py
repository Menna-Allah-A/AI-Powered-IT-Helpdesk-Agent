from src.ingestion.loader import load_documents

documents = load_documents()

print(f"Total documents loaded: {len(documents)}")

for doc in documents[:3]:
    print("\n--- DOCUMENT ---")
    print("Metadata:", doc.metadata)
    print("Text preview:", doc.text[:200])

    from collections import Counter
from src.ingestion.loader import load_documents

documents = load_documents()

category_counts = Counter(
    doc.metadata["category"] for doc in documents
)

print(f"Total documents: {len(documents)}")
print("\nDocuments per category:")

for category, count in sorted(category_counts.items()):
    print(f"{category}: {count}")