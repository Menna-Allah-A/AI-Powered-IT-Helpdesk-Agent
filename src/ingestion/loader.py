
from llama_index.core import SimpleDirectoryReader
from llama_index.readers.file import PyMuPDFReader


def load_documents(data_dir: str = "knowledge_base/raw"):

    file_extractor = {
        ".pdf": PyMuPDFReader()
    }

    reader = SimpleDirectoryReader(
        input_dir=data_dir,
        recursive=True,
        file_extractor=file_extractor
    )

    documents = reader.load_data()

    return documents
