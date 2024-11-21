"""
Laboratory Work #3 starter.
"""

# pylint:disable=duplicate-code, too-many-locals, too-many-statements, unused-variable
from pathlib import Path

from lab_3_ann_retriever.main import BasicSearchEngine, Tokenizer, Vectorizer


def open_files() -> tuple[list[str], list[str]]:
    """
    # stubs: keep.

    Open files.

    Returns:
        tuple[list[str], list[str]]: Documents and stopwords
    """
    documents = []
    for path in sorted(Path("assets/articles").glob("*.txt")):
        with open(path, "r", encoding="utf-8") as file:
            documents.append(file.read())
    with open("assets/stopwords.txt", "r", encoding="utf-8") as file:
        stopwords = file.read().split("\n")
    return (documents, stopwords)


def main() -> None:
    """
    Launch an implementation.
    """
    with open("assets/secrets/secret_1.txt", "r", encoding="utf-8") as text_file:
        text = text_file.read()
    stopwords = open_files()[1]
    docs = open_files()[0]
    tokenizer = Tokenizer(stopwords)
    tokenized_docs = tokenizer.tokenize_documents(docs)

    vectorizer = Vectorizer(tokenized_docs)
    vectorizer.build()
    secret_vector = tuple(float(value) for value in text.split(','))
    secret_tokens = vectorizer.vector2tokens(secret_vector)
    print(secret_tokens)

    basic_search_engine = BasicSearchEngine(vectorizer, tokenizer)
    basic_search_engine.index_documents(docs)
    result = basic_search_engine.retrieve_vectorized(secret_vector)
    print(result)
    assert result, "Result is None"


if __name__ == "__main__":
    main()
