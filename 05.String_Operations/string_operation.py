
# Part 2 - Question 1
text = "Python"
print(text[0])
print(text[3])
print(text[-1])
print(text[-2])




# Part 2 - Question 2
text = "Programming"
print(text[0:4])
print(text[3:8])
print(text[:5])
print(text[5:])




# Part 2 - Question 3
text = "Python"
print(text[::2])
print(text[1::2])
print(text[::-1])




# Part 2 - Question 4
text = "Hello World"
print(len(text))
print(text[5])
print(text[-1])




# Part 2 - Question 5
text = "Python Programming"
print("Python" in text)
print("Java" in text)
print("Java" not in text)




# Part 2 - Question 6
text = "banana"
print(text.find("a"))
print(text.find("z"))
print(text.count("a"))




# Part 2 - Question 7
text = "Python"
print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title())
print(text.swapcase())




# Part 2 - Question 8
text = "I like Java"
print(text.replace("Java", "Python"))
print(text)




# Part 2 - Question 9
text = "Hello"
print(text + " World")
print(text * 3)




# Part 3 - Task 1
name = 'Alex'
city = "New York"
language = 'Python'
message = "Hello, Python programmers!"
print(name)
print(city)
print(language)
print(message)




# Part 3 - Task 2
empty_str = ""
print(empty_str)
print(len(empty_str))
print(type(empty_str))




# Part 3 - Task 3
text = "Python Programming"
print(text)
print(len(text))
print(text[0])
print(text[-1])
print(text[2])
print(text[-2])




# Part 4 - Task 4
text = "Programming"
print(text[0])
print(text[1])
print(text[4])
print(text[len(text) - 1])




# Part 4 - Task 5
text = "Programming"
print(text[-1])
print(text[-2])
print(text[-3])
print(text[-len(text)])




# Part 4 - Task 6
full_name = "John Doe"
print(full_name[0])
print(full_name[-1])
print(full_name[5])




# Part 5 - Task 7
text = "Python Programming"
print(text[0:6])
print(text[7:])
print(text[:])
print(text[:5])
print(text[-5:])




# Part 5 - Task 8
text = "ABCDEFGHIJKL"
print(text[::2])
print(text[::3])
print(text[1:8:2])
print(text[::-1])




# Part 5 - Task 9
text = "Python Programming"
print(text[-5:])
print(text[-10:])
print(text[::-1])




# Part 5 - Task 10
text = "Hello World!"
print(text[:3])
print(text[-3:])
print(text[::2])
print(text[::-1])
print(text[1:-1])




# Part 6 - Task 11
word = "Python"
sentence1 = "Hello World"
sentence2 = "  Python programming is fun  "
print(len(word))
print(len(sentence1))
print(len(sentence2))




# Part 6 - Task 12
text = "Python Programming"
last_index = len(text) - 1
print(text[last_index])




# Part 7 - Task 13
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)




# Part 7 - Task 14
name = "Alice"
age = 22
city = "Seattle"
language = "Python"
sentence = name + " is " + str(age) + " years old, lives in " + city + " and codes in " + language + "."
print(sentence)




# Part 7 - Task 15
try:
    print("Age: " + 20)
except TypeError as e:
    print(e)

print("Age: " + str(20))




# Part 8 - Task 16
symbol = "*"
print(symbol * 3)
print(symbol * 5)
print(symbol * 10)




# Part 8 - Task 17
pattern = "*" * 10
print(pattern)




# Part 9 - Task 18
text = "python programming language"
print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title())
print(text.swapcase())




# Part 9 - Task 19
str1 = "Python"
str2 = "python"
print(str1 == str2)
print(str1.lower() == str2.lower())




# Part 10 - Task 20
text = "Python is a programming language"
print("Python" in text)
print("programming" in text)
print("Java" in text)
print("language" in text)




# Part 10 - Task 21
text = "Python is a programming language"
print(text.find("Python"))
print(text.find("programming"))
print(text.find("language"))
print(text.find("Java"))




# Part 10 - Task 22
text = "Python is a programming language"
print(text.index("Python"))
print(text.index("programming"))
print(text.index("language"))
try:
    print(text.index("Java"))
except ValueError as e:
    print(e)




# Part 10 - Task 23
text = "banana"
print(text.count("a"))
print(text.count("n"))
print(text.count("b"))




# Part 10 - Task 24
filename = "student_notes.pdf"
print(filename.startswith("student"))
print(filename.endswith(".pdf"))
print(filename.endswith(".txt"))




# Part 11 - Task 25
text = "I am learning Java"
new_text = text.replace("Java", "Python")
print(new_text)




# Part 11 - Task 26
text = "apple apple apple"
print(text.replace("apple", "mango"))




# Part 11 - Task 27
text = "apple apple apple"
print(text.replace("apple", "mango", 1))




# Part 11 - Task 28
text = "Python"
text.upper()
print(text)
text = text.upper()
print(text)




# Part 12 - Task 29
text = "   Python Programming   "
print(text.strip())
print(text.lstrip())
print(text.rstrip())




# Part 12 - Task 30
user_input = "  John Doe  "
cleaned_name = user_input.strip()
print(cleaned_name)




# Part 13 - Task 31
text = "Python is easy to learn"
words = text.split()
print(words)




# Part 13 - Task 32
text = "apple,banana,mango,orange"
fruits = text.split(",")
print(fruits)




# Part 13 - Task 33
words = ["Python", "is", "easy"]
sentence = " ".join(words)
print(sentence)




# Part 13 - Task 34
words = ["Python", "is", "easy"]
print("-".join(words))
print("/".join(words))




# Part 14 - Task 35
name = "Alice"
age = 22
city = "Seattle"
sentence = f"My name is {name}, I am {age} years old and I live in {city}."
print(sentence)




# Part 14 - Task 36
a = 10
b = 20
print(f"The sum is {a + b}")




# Part 15 - Task 37
try:
    text = "Python"
    print(text[20])
except IndexError as e:
    print(e)

try:
    text = "Python"
    text[0] = "J"
except TypeError as e:
    print(e)

try:
    age = 20
    print("Age: " + age)
except TypeError as e:
    print(e)

try:
    text = "Python"
    print(text.index("Java"))
except ValueError as e:
    print(e)




# Part 16 - Task 38
full_name_input = "   Jane Elizabeth Doe   "
cleaned = full_name_input.strip()
print(full_name_input)
print(cleaned)
print(cleaned.upper())
print(cleaned.lower())
print(cleaned.title())
print(len(cleaned))
print(cleaned[0])
print(cleaned[-1])
print("a" in cleaned)




# Part 17 - Task 39
sentence_input = "Python programming is versatile and powerful."
print(sentence_input)
print(len(sentence_input))
print(len(sentence_input.split()))
print(sentence_input[0])
print(sentence_input[-1])
print(sentence_input.upper())
print(sentence_input.lower())
print(sentence_input.title())
print("Python" in sentence_input)
print(sentence_input.count("a"))




# Part 18 - Task 40
first_name = "  John  "
last_name = "  Smith  "
city = "  Chicago  "
course = "  Python Programming  "
age = 20

first_name = first_name.strip()
last_name = last_name.strip()
city = city.strip()
course = course.strip()

full_name = first_name + " " + last_name
print(full_name.title())
print(full_name.upper())
print(full_name.lower())
print(len(full_name))
print(full_name[0])
print(full_name[-1])
print(f"City: {city}, Course: {course}")
print(f"Age: {age}")
print("Python" in course)
print(course.replace("Programming", "Development"))
print(len(course.split()))