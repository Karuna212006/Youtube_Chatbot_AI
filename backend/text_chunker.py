"""
Text Chunker - Splits transcript into smaller chunks for RAG
"""

from langchain_text_splitters import RecursiveCharacterTextSplitter


def create_chunker(chunk_size: int = 500, chunk_overlap: int = 50):
    """
    Create a text splitter with given settings.

    Args:
        chunk_size   : Max characters per chunk (default 500)
        chunk_overlap: Overlapping characters between chunks (default 50)
    """
    return RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ".", " ", ""],  # tries each in order
    )


def chunk_transcript(text: str, chunk_size: int = 500, chunk_overlap: int = 50) -> list:
    """
    Split a transcript into chunks.

    Args:
        text         : Full transcript text
        chunk_size   : Max characters per chunk
        chunk_overlap: Shared characters between consecutive chunks

    Returns:
        List of text chunk strings
    """
    chunker = create_chunker(chunk_size, chunk_overlap)
    chunks = chunker.split_text(text)
    return chunks


if __name__ == "__main__":
    # Sample transcript for testing
    sample_text = (
        "LangChain is a framework for building applications powered by language models. "
        "It provides tools for chaining together different components like prompts, models, and memory. "
        "One of its most useful features is the ability to build RAG systems. "
        "RAG stands for Retrieval-Augmented Generation. "
        "In a RAG system, we first retrieve relevant chunks of text from a knowledge base. "
        "Then we pass those chunks along with the user question to an AI model. "
        "The AI model uses both the retrieved context and its own knowledge to generate an answer. "
        "This approach is more accurate than using the AI model alone because it grounds answers in real data. "
        "YouTube transcripts are a perfect use case for RAG because videos can be very long. "
        "By chunking the transcript and storing it in a vector database, we can quickly find relevant parts. "
        "The chatbot then only reads the relevant chunks instead of the entire transcript."
    )

    print("Original text length:", len(sample_text), "characters")
    print("-" * 50)

    chunks = chunk_transcript(sample_text, chunk_size=200, chunk_overlap=30)

    print(f"Total chunks created: {len(chunks)}")
    print("-" * 50)

    for i, chunk in enumerate(chunks, 1):
        print(f"\nChunk {i} ({len(chunk)} chars):")
        print(chunk)
