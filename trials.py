"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    for item in items:
        print(item)

def get_all_evens(nums):
    even_nums = []

    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)

def get_odd_indices(items):
    result = []

    for i, item in enumerate(items):
        if i%2 != 0:
            result.append(items[i])

def print_as_numbered_list(items):
    i = 1

    for item in items:
        print(f"{i}. {item}")

        i += 1

def get_range(start, stop):
    nums = []

    # check out l8er
    num = start
    while num < stop:
        nums.append(num)
        num += 1

# for (init; conditional; exp)

# function getRange(start, stop) {
#   const nums = [];

#   for (let num = start; num < stop; num += 1) {
#     nums.push(num);
#   }
# }


def censor_vowels(word):
    chars = []
    # check out l8er and run js version to see behavior
    for letter in word:
        if letter in "aeiou":
            chars.append("*")
        else:
            chars.append(letter)

    return "".join(chars)

def snake_to_camel(string):
    camelCase = []

    for word in string.split("_"):
        camelCase.append(f"{word[0].upper()}{word[1:]}")

    return "".join(camelCase)

def longest_word_length(words):
    longest = len(words[0])

    for word in words:
        if longest < len(word):
            longest = word

    return longest

def truncate(string):
    result = []

    for char in string:
        if len(result) == 0 or char != result[-1]:
            result.append(char)

    return "".join(result)


def has_balanced_parens(string):
    parens = 0

    for char in string:
        if char == "(":
            parens += 1
        elif char == ")":
            parens -= 1

            if parens < 0:
                return False
    
    return parens == 0

def compress(string):
    compressed = []

    currChar = ""
    charCount = 0

    for char in string:
        if char != currChar:
            compressed.append(currChar)
        
            if charCount > 1:
                compressed.append(str(charCount))

            currChar = char
            charCount = 0
        charCount += 1

    compressed.append(currChar)
    if charCount > 1:
        compressed.push(str(charCount))
        
    return "".join(compressed)



# function compress(string) {
#   const compressed = [];

#   let currChar = "";
#   let charCount = 0;
#   for (const char of string) {
#     if (char !== currChar) {
#       compressed.push(currChar);

#       if (charCount > 1) {
#         compressed.push(charCount.toString());
#       }

#       currChar = char;
#       charCount = 0;
#     }

#     charCount += 1;
#   }

#   compressed.push(currChar);
#   if (charCount > 1) {
#     compressed.push(charCount.toString());
#   }

#   return compressed.join("");
# }
