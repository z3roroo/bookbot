def get_word_count(text):
    return len(text.split())

def get_each_char_count(text):
    char_count = {}
    for char in text:
        if char.lower() in char_count:
            char_count[char.lower()] += 1
        else:
            char_count[char.lower()] = 1
    return char_count

def sort_on(items):
    return items["num"]

def get_sorted_list_of_char_counts(char_count):
    char_count_list = []
    for char, count in char_count.items():
        char_count_list.append({"char": char, "num": count})
    char_count_list.sort(key=sort_on, reverse=True)
    return char_count_list