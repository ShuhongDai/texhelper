# TexHelper

TexHelper is a Python library designed to assist with various tasks related to LaTeX files, including automating title formatting, processing BibTeX files, and more. It is particularly useful for anyone working with LaTeX documents who needs to handle common formatting issues and improve productivity.

## Features

- **Title Formatting**: Automatically capitalizes the words in titles while respecting common style rules (e.g., only capitalizing the first and last words, and specific important words).
- **BibTeX Processing**: Supports processing and formatting of BibTeX entries (e.g., fixing capitalization in titles).
- **Extensible**: The library is designed to be modular, allowing for easy addition of new features.

## Installation

You can install **TexHelper** directly from PyPI using `pip`:

```bash
pip install texhelper
```

## Usage

After installation, you can import and use the functions in your Python code.

### Example: Capitalizing Titles

Here’s an example of how to use the `capitalize_title` function, which formats titles according to common capitalization rules.

```python
from texhelper.bibtex import capitalize_title

title = "the quick brown fox jumps over the lazy dog"
formatted_title = capitalize_title(title)
print(formatted_title)
```

**Output:**
```
The Quick Brown Fox Jumps Over the Lazy Dog
```

### Example: Processing a BibTeX Entry

You can also use **TexHelper** to process BibTeX files, applying the correct title capitalization.

```python
from texhelper.bibtex import process_bibtex

bib_content = [
    'author={John Doe},\n',
    'title={the quick brown fox jumps over the lazy dog},\n',
    'year={2024},\n'
]

processed_bib = process_bibtex(bib_content)
print(''.join(processed_bib))
```

**Output:**
```
author={John Doe},
  title={The Quick Brown Fox Jumps Over the Lazy Dog},
year={2024},
```

## License

This project is licensed under the [Apache 2.0 License](LICENSE) - see the LICENSE file for details.

## Contributing

We welcome contributions! To contribute to **TexHelper**, please fork the repository and create a pull request. Here are some ways you can help:

- **Bug Reports**: If you find a bug, please report it in the [Issues](https://github.com/ShuhongDai/texhelper/issues) section of the GitHub repository.
- **Feature Requests**: Suggest new features or improvements.
- **Code Improvements**: If you see areas where the code can be improved, feel free to submit a pull request with your changes.

## Credits

**TexHelper** was created and is maintained by [Shuhong Dai](https://github.com/ShuhongDai).

## Acknowledgements

- Thanks to the open-source community for their valuable libraries and tools that made this project possible.
- Special thanks to [PyPI](https://pypi.org) for providing a platform for publishing Python packages.

## Support

For any questions or support, feel free to open an issue on the [GitHub Issues page](https://github.com/ShuhongDai/texhelper/issues).

---

