def count_words(book: str):
    words = book.split()
    return len(words)

def count_letters(book: str):
    total = {}
    for letter in book:
        letter = letter.lower()
        if letter.isalpha():
            if letter not in total:
                total[letter] = 1
            else:
                total[letter] += 1
    total_sorted_value = sorted(total.items(), key=lambda item: item[1], reverse=True)
    total_sorted = {key: value for key, value in total_sorted_value}
    return total_sorted
