from stats import get_word_count

def get_book_text(filePath):
    with open(filePath) as f:
        return f.read()


def main():
    frankensteinPath = "books/frankenstein.txt"
    bookText = get_book_text(frankensteinPath)
    wordCount = get_word_count(bookText)
    print(f"{wordCount} words found in the document")

main()