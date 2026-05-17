from typing import List


# sort based on descending order
# using lambda function
def sort_words(words: List[str]) -> List[str]:
    words.sort(key=lambda word: len(word), reverse=True)
    return words

# sort based on ascending order
# using lambda function
def sort_numbers(numbers: List[int]) -> List[int]:
    numbers.sort(key=lambda number: abs(number))
    return numbers


# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))

"""
Your Output:

['watermelon', 'blueberry', 'zucchini', 'cherry', 'banana', 'apple', 'kiwi', 'pear']
[1, 2, -2, 2, -3, 4, -4, -5, 5, -6, 6, 7, 9, 11, -19]
"""
