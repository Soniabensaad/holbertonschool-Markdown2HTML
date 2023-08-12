#!/usr/bin/python3
"""
markdown2html.py - Convert Markdown to HTML

Usage:
    markdown2html.py <input_file> <output_file>

Arguments:
    <input_file>     Path to the input Markdown file.
    <output_file>    Path to the output HTML file.

Description:
    This script takes an input Markdown file and converts its content to HTML,
    saving the resulting HTML content to an output file. It utilizes the 'markdown'
    library for the conversion process.

Examples:
    $ ./markdown2html.py input.md output.html
        Converts 'input.md' to HTML and saves the result in 'output.html'.

    $ ./markdown2html.py input.md /path/to/output.html
        Converts 'input.md' to HTML and saves the result in the specified path.

Note:
    - Both the input and output file paths should be provided as arguments.
    - If the input file is not found, an error message will be displayed.
"""

import sys
import markdown

def convert_markdown_to_html(input_file, output_file):
    """
    Convert Markdown content to HTML and save to an output file.

    Args:
        input_file (str): Path to the input Markdown file.
        output_file (str): Path to the output HTML file.

    Raises:
        FileNotFoundError: If the input Markdown file is not found.
    """
    try:
        with open(input_file, 'r') as md_file:
            markdown_content = md_file.read()
            html_content = markdown.markdown(markdown_content)
            with open(output_file, 'w') as html_file:
                html_file.write(html_content)
    except FileNotFoundError:
        sys.stderr.write(f"Error: Input file '{input_file}' not found.\n")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py <input_file> <output_file>\n")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    convert_markdown_to_html(input_file, output_file)
    
