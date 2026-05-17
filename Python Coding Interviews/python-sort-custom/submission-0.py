from typing import List

# define get_word_length bc `key` parameter only accepts function
def get_word_length(word: str) -> int:
    return len(word)

# sort based on descending length
def sort_words(words: List[str]) -> List[str]:
    words.sort(key=get_word_length, reverse=True)
    return words

# use abs() to get absolute value of a number
def get_num_length(number: str) -> int:
    return abs(number)

# sort based on ascending length
def sort_numbers(numbers: List[int]) -> List[int]:
    numbers.sort(key=get_num_length)
    return numbers


# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))

"""
Your Output:


['watermelon', 'blueberry', 'zucchini', 'cherry', 'banana', 'apple', 'kiwi', 'pear']
[1, 2, -2, 2, -3, 4, -4, -5, 5, -6, 6, 7, 9, 11, -19]
"""
