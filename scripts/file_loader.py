def load_html(fileName):
    with open(fileName, 'r', encoding='utf-8') as file:
        data = file.read().replace('  ', ' ')
    return data