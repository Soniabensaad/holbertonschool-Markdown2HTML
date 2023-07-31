import sys

def markdown_file(name, output):
    try:
        with open(name, 'r') as file:
            markdown_content = file.read()

        with open(output, 'w') as file:
            file.write(markdown_content)

    except FileNotFoundError:
        sys.stderr.write(f"Missing '{name}'\n")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)

    markdown_file(sys.argv[1], sys.argv[2])
