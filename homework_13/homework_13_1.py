import codecs

def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    result = []
    less_greater_flag = False
    for char in html:
        if char == '<':
            less_greater_flag = True
        elif char == '>':
            less_greater_flag = False
        elif not less_greater_flag:
            result.append(char)

    text = ''.join(result)

    lines = text.splitlines()
    new_lines = []
    for line in lines:
        if line.strip():
            new_lines.append(line.strip())

    text = '\n'.join(new_lines)

    with codecs.open(result_file, 'w', 'utf-8') as file:
        file.write(text)

delete_html_tags('draft.html')
