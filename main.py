"""Boot.dev"""


def count_words_and_characters(string_to_count):
    """Split string by space and return the sum of words
    and an array of dictionaries for count per letter."""
    count = 0
    character_dictionary = {}
    char_dic_array = []
    for word in string_to_count.split():
        count += 1
        for letter in word:
            if not letter.isalpha():
                continue
            character_dictionary[letter.lower()] = (
                character_dictionary.setdefault(letter.lower(), 0) + 1
            )
    char_dic_array = convert_dict_to_array_of_dict(character_dictionary)
    return count, char_dic_array


def convert_dict_to_array_of_dict(dict_to_conv):
    """Converts the keys and values of an dictionary to an array
    of dictionaries with predefined keys."""
    arr = []
    for dict_key in dict_to_conv:
        arr.append({"char": dict_key, "num": dict_to_conv[dict_key]})
    return arr


def sort_on(dict_to_sort):
    """Return the value from a dictionary to sort it."""
    return dict_to_sort["num"]


def print_header(file_path, words_in_file):
    """Static print with the number of total words."""
    print(f"--- Begin report of {file_path} ---")
    print(f"{words_in_file} words in the document")
    print()


def print_array(arr):
    """A static print for each element in the array of character dictionary."""
    for el in arr:
        print(f"The '{el["char"]}' character was found {el["num"]} times")
    print("--- End report ---")


def main():
    """Main method."""
    file_path = "books/frankestein.txt"
    file_contents = None
    with open(file_path) as f:
        file_contents = f.read()
    words_in_file, characters_in_file = count_words_and_characters(file_contents)
    characters_in_file.sort(reverse=True, key=sort_on)
    print_header(file_path, words_in_file)
    print_array(characters_in_file)


main()
