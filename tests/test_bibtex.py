# tests/test_bibtex.py
import pytest
from texhelper.bibtex import capitalize_title, process_bibtex

def test_capitalize_title():
    assert capitalize_title("the quick brown fox jumps over the lazy dog") == "The Quick Brown Fox Jumps Over the Lazy Dog"

def test_process_bibtex():
    bib_content = [
        'author={John Doe},\n',
        'title={the quick brown fox jumps over the lazy dog},\n',
        'year={2024},\n'
    ]
    processed = process_bibtex(bib_content)
    assert 'title={The Quick Brown Fox Jumps Over the Lazy Dog},\n' in processed
