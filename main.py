from stats import get_word_count, get_character_count, sort_char_by_count as so
import sys
def get_book_text(filePath):
    with open(filePath) as f:
        return f.read()


def main():
    bookPath = sys.argv[1] if len(sys.argv) > 1 else sys.exit("Usage: python3 main.py <path_to_book>")
    bookText = get_book_text(bookPath)
    wordCount = get_word_count(bookText)
    charCount = get_character_count(bookText)
    charCount = so(charCount)
    print_report(bookPath, wordCount, charCount)
    

def print_report(path, wordCount, charCount):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at: {path}...")
    print("----------- Word Count ----------")
    print(f"Found {wordCount} total words")
    print("---------- Character Count -------")
    for char in charCount:
        print(f"{char['char']}: {char['num']} times")
    print("=================================")


main()