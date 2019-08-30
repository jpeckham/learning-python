# for more https://www.pythonforbeginners.com/basics/string-manipulation-in-python
# can treate like an array
word = "Hello World"
letter = word[0]
print(letter)

# get the length of a string
something = "Hello"
length = len(something)
print(length)

# count number of occurences
something = "abcdefg123123123"
number = something.count('123')
print(number)

# string splitting
something = '1,2,3,4,5,6,7'
tokens = something.split(',')
print(tokens)

# starts/ends
word = "hello world"
starts = word.startswith("H")
print(starts)
ends = word.endswith("d")
print(ends)
ends = word.endswith("w")
print(ends)