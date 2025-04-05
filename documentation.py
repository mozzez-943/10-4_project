# open_docs.py
import webbrowser
from pathlib import Path

def open_docs():
    # Get the absolute path to this script's directory
    base_dir = Path(__file__).parent.resolve()
    doc_path = base_dir / "docs" / "build" / "html" / "index.html"

    if doc_path.exists():
        webbrowser.open(f"file://{doc_path}")
    else:
        print(f"Documentation file not found at: {doc_path}")

if __name__ == "__main__":
    open_docs()
