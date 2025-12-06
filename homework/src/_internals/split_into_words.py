def split_lines_into_words(lines):
    words = []
    for line in lines:
        words.extend(line.split())
        words = [word.strip(".,!?;:\"'()[]{}") for word in words]
    return words
