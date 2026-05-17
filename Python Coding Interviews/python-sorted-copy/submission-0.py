from typing import List

# sorted(): returns a new list w/ the elements sorted in specified order w/o changing original list

# sort in ascending order
def sort_words(words: List[str]) -> List[str]:
    words = sorted(words)
    return words

# sort in descending order based on absolute value
def sort_numbers(numbers: List[int]) -> List[int]:
    numbers = sorted(numbers, key=abs, reverse=True)
    return numbers


# do not modify below this line
original_words = ["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]

print(original_words)
print(sort_words(original_words))

original_numbers = [1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]

print(original_numbers)
print(sort_numbers(original_numbers))

"""
Expected output:


['cherry', 'apple', 'blueberry', 'banana', 'watermelon', 'zucchini', 'kiwi', 'pear']
['apple', 'banana', 'blueberry', 'cherry', 'kiwi', 'pear', 'watermelon', 'zucchini']
[1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]
[-19, 11, 9, 7, -6, 6, -5, 5, 4, -4, -3, 2, -2, 2, 1]
"""