def extract_title(markdown):
    for line in markdown.split('\n'):
        if line.startswith('# '):
            return line.lstrip('#').lstrip()
    raise Exception("No h1 header found in markdown")
