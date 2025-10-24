def get_num_words(text):
    """Return the number of words in the given text."""
    words = text.split()
    return len(words)


def get_char_counts(text):
    """Return a dictionary mapping each character (lowercased) to its count."""
    chars = {}
    for c in text.lower():
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars


def sort_on(item):
    """Helper function for sorting by count."""
    return item["num"]


def chars_dict_to_sorted_list(char_dict):
    """Convert char-count dict to a sorted list of dicts (descending by count)."""
    char_list = []
    for char, count in char_dict.items():
        if char.isalpha():  # Only include letters
            char_list.append({"char": char, "num": count})
    char_list.sort(reverse=True, key=sort_on)
    return char_list
