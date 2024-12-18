# TexHelper

**TexHelper** is a Python library designed to assist with various tasks related to LaTeX files, including automating title formatting, processing BibTeX files, and more. It is particularly useful for anyone working with LaTeX documents who needs to handle common formatting issues and improve productivity.

## Features

- **Title Formatting**: Automatically capitalizes the words in titles while respecting common style rules (e.g., only capitalizing the first and last words, and specific important words).
- **BibTeX Processing**: Supports processing and formatting of BibTeX entries, including fixing capitalization in titles and beautifying BibTeX files.
- **File Processing**: Allows reading and processing `.bib` files, capitalizing the titles in the entries and saving the results to new files.
- **BibTeX Beautification**: Beautifies BibTeX files by formatting each entry with consistent field order and proper spacing.
- **Extensible**: The library is designed to be modular, allowing for easy addition of new features.

## Installation

You can install **TexHelper** directly from PyPI using `pip`:

```bash
pip install texhelper
```

## Usage

After installation, you can import and use the functions in your Python code.

### Example: Capitalizing Titles

Here’s an example of how to use the `title_case_only` function, which formats multiple titles according to common capitalization rules.

```python
from texhelper.bibtex import title_case_only

titles = "{the quick brown fox jumps over the lazy dog}{a quick overview of deep learning}"
formatted_titles = title_case_only(titles)
print(formatted_titles)
```

**Output:**
```
The Quick Brown Fox Jumps Over the Lazy Dog The Quick Overview of Deep Learning
```

### Example: Processing a BibTeX Entry

You can also use **TexHelper** to process BibTeX files, applying the correct title capitalization.

```python
from texhelper.bibtex import title_case_bibtex

bib_content = [
    'author={John Doe},\n',
    'title={the quick brown fox jumps over the lazy dog},\n',
    'year={2024},\n'
]

processed_bib = title_case_bibtex(bib_content)
print(''.join(processed_bib))
```

**Output:**
```
author={John Doe},
title={The Quick Brown Fox Jumps Over the Lazy Dog},
year={2024},
```

### Example: Processing a BibTeX File

You can use **TexHelper** to read a `.bib` file, process the titles, and save the results to a new file.

```python
from texhelper.bibtex import title_case_file

input_filepath = "input.bib"
output_filepath = "output.bib"

title_case_file(input_filepath, output_filepath)
```

This function reads the `.bib` file, capitalizes all titles, and saves the processed content to the output file.

### Example: Beautifying a BibTeX File

The `beautify_bibtex_file` function formats and beautifies a `.bib` file by ensuring proper field order and spacing.

```python
from texhelper.bibtex import beautify_bibtex_file

input_file = "input.bib"
output_file = "output.bib"

beautify_bibtex_file(input_file, output_file)
```

This function reads the `.bib` file, formats the entries, and saves the beautified content to a new file.

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
