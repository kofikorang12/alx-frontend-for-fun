#!/usr/bin/python3

import sys
import os
import markdown

def convert_markdown_to_html(input_file, output_file):
    # Check if input Markdown file exists
    if not os.path.exists(input_file):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    try:
        with open(input_file, 'r') as md_file:
            markdown_text = md_file.read()

            # Convert Markdown to HTML
            html_content = markdown.markdown(markdown_text)

        with open(output_file, 'w') as html_file:
            html_file.write(html_content)

    except FileNotFoundError:
        print("Error: Input Markdown file not found.", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    # Check if correct number of arguments provided
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py <input_markdown_file> <output_html_file>", file=sys.stderr)
        sys.exit(1)
    
    input_markdown_file = sys.argv[1]
    output_html_file = sys.argv[2]

    convert_markdown_to_html(input_markdown_file, output_html_file)

    sys.exit(0)
