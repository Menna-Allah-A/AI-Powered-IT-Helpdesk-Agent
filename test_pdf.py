
from pathlib import Path
from collections import defaultdict
import hashlib

KB_PATH = Path("knowledge_base/raw")

files = list(KB_PATH.rglob("*.txt"))

print(f"Total documents: {len(files)}")
print("=" * 60)

hash_groups = defaultdict(list)
category_counts = defaultdict(int)

for file in files:
    content = file.read_text(encoding="utf-8").strip()
    category = file.parent.name

    category_counts[category] += 1

    file_hash = hashlib.sha256(content.encode("utf-8")).hexdigest()
    hash_groups[file_hash].append(file)

    word_count = len(content.split())

    if not content:
        print(f"[EMPTY] {file}")

    elif word_count < 100:
        print(f"[SHORT: {word_count} words] {file}")

    elif word_count > 5000:
        print(f"[LONG: {word_count} words] {file}")

print("\nCATEGORY COUNTS")
print("=" * 60)

for category, count in sorted(category_counts.items()):
    print(f"{category}: {count}")

print("\nEXACT DUPLICATES")
print("=" * 60)

duplicates_found = False

for group in hash_groups.values():
    if len(group) > 1:
        duplicates_found = True
        print("\nDuplicate files:")
        for file in group:
            print(f"  {file}")

if not duplicates_found:
    print("No exact duplicate documents found.")
