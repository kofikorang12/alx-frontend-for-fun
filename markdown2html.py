#!/usr/bin/python3
"""
Markdown to HTML Converter

This script converts a Markdown file to HTML.

Usage:
    ./markdown2html.py [input_file] [output_file]

Args:
    input_file:  The Markdown file to be converted.
    output_file: The HTML file to be generated.

Example:
    ./markdown2html.py README.md README.html
"""

import argparse
import pathlib
import re
import sys

def convert_md_to_html(input_file, output_file):
    """Converts Markdown file to HTML."""
    try:
        # Read the contents of the input file
        with open(input_file, encoding='utf-8') as f:
            md_content = f.readlines()

        # Process Markdown content line by line
        html_content = []
        for line in md_content:
            # Check if the line is a heading
            match = re.match(r'(#){1,6} (.*)', line)
            if match:
                # Get the level of the heading
                h_level = len(match.group(1))
                # Get the content of the heading
                h_content = match.group(2)
                # Append the HTML equivalent of the heading
                html_content.append(f'<h{h_level}>{h_content}</h{h_level}>\n')
            else:
                html_content.append(line)

        # Write the HTML content to the output file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.writelines(html_content)

        print(f"Markdown file '{input_file}' converted to HTML and saved as '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: Input Markdown file '{input_file}' not found.", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Convert Markdown to HTML')
    parser.add_argument('input_file', help='Path to input Markdown file')
    parser.add_argument('output_file', help='Path to output HTML file')
    args = parser.parse_args()

    # Check if the input file exists
    input_path = pathlib.Path(args.input_file)
    if not input_path.is_file():
        print(f"Error: Input Markdown file '{args.input_file}' not found.", file=sys.stderr)
        sys.exit(1)

    # Convert the Markdown file to HTML
    convert_md_to_html(args.input_file, args.output_file)