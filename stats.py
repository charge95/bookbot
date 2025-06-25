def get_word_count(text):
    return len(text.split())

def get_character_count(text):
    charDict = {}
    for char in text.lower():
        if char in charDict:
            charDict[char] += 1
        else:
            charDict[char] = 1
    return charDict

def sort_on(d):
    return d["num"]

def sort_char_by_count(charDict):
    sortedList =[]
    for char in charDict:
        sortedList.append({"char": char, "num": charDict[char]})
    sortedList.sort(key=sort_on, reverse=True)
    return sortedList