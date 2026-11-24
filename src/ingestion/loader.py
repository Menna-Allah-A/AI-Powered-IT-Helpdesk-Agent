
from pathlib import Path

from llama_index.core import SimpleDirectoryReader
from llama_index.readers.file import PyMuPDFReader


def load_documents(data_dir: str = "knowledge_base/raw"):

    file_extractor = {
        ".pdf": PyMuPDFReader()
    }

    reader = SimpleDirectoryReader(
        input_dir=data_dir,
        recursive=True,
        required_exts=[".txt", ".pdf"],
        file_extractor=file_extractor
    )

    documents = reader.load_data()

    for document in documents:
        file_path = Path(document.metadata["file_path"])

        document.metadata["category"] = file_path.parent.name
        document.metadata["file_name"] = file_path.name

    return documents
