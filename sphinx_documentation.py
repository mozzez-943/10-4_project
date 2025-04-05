# open_docs.py
import webbrowser
from pathlib import Path

def open_docs():
    doc_path = Path("docs/build/html/index.html").resolve()
    if doc_path.exists():
        webbrowser.open(f"file://{doc_path}")
    else:
        print(f"Documentation file not found at: {doc_path}")

if __name__ == "__main__":
    open_docs()
