import sys
from stats import get_word_count, get_each_char_count, get_sorted_list_of_char_counts


def main():
    if len(sys.argv) > 1:
        book_path = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    
    book_text = get_book_text(book_path)
    word_count = get_word_count(book_text)
    each_char_count = get_each_char_count(book_text)
    each_char_count_sorted = get_sorted_list_of_char_counts(each_char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char in each_char_count_sorted:
        if char["char"].isalpha():
            print(f"{char['char']}: {char['num']}")
    print("============= END ===============")

def get_book_text(filepath):
    with open(filepath, "r") as file:
        return file.read()
 
main()