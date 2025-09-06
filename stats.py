def get_num_words(text):
    return len(text.split())

def count_letters(text):
    empty_dict = {}
    for letter in text:
        lower_letter = letter.lower()
        if lower_letter in empty_dict:
            empty_dict[lower_letter] += 1
        else:
            empty_dict[lower_letter] = 1
    return empty_dict

def sort_on(items):
    return items["num"]

def sort_dict(text):
    empty_dict = count_letters(text)
    result = [{"char": a, "num": b} for a, b in empty_dict.items()]

    result.sort(key=sort_on, reverse=True)
    return result