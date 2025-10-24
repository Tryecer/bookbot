# main.py
import sys
from stats import get_num_words, get_char_counts, chars_dict_to_sorted_list

def get_book_text(filepath):
    """Read and return the entire contents of filepath."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def print_report(path, text):
    """Print the Bookbot report for the given text."""
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    # Word count
    num_words = get_num_words(text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    # Character counts
    char_counts = get_char_counts(text)
    sorted_chars = chars_dict_to_sorted_list(char_counts)

    print("--------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

def main():
    # Expect exactly one argument after the script name:
    # python3 main.py <path_to_book>
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    try:
        text = get_book_text(book_path)
    except FileNotFoundError:
        print(f"Error: file not found: {book_path}")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file {book_path}: {e}")
        sys.exit(1)

    print_report(book_path, text)


if __name__ == "__main__":
    main()
