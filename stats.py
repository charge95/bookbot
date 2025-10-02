def count_words(text):
    words = text.split()
    return len(words)

def count_char(text):
    letters = list(text.lower())
    char_dict = {}
    for cha in letters:
        if cha.isalpha():
            if cha in char_dict:
                char_dict[cha] += 1
            else:
                char_dict[cha] = 1
    sorted_chars = dict(sorted(char_dict.items(), key=lambda item: item[1], reverse=True))
    return sorted_chars