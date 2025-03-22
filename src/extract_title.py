def extract_title(markdown):
    # Find the first line that starts with a # and return it
    for line in markdown.split('\n'):
        if line.startswith('#'):
            return line.lstrip('#').lstrip()
