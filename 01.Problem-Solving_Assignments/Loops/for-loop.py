#Q1
user=input("Enter a string: ")
upper= lower= digit= whtspace= splchar=0
for char in user:
    if char.isupper(): upper+=1
    elif char.islower(): lower+=1
    elif char.isdigit(): digit+=1
    elif char.isspace(): whtspace+=1
    else: splchar+=1

chars=[upper, lower, digit, whtspace, splchar]
names=["Uppercase", "Lowercase", "Digits", "Spaces", "Special Character"]
highest=max(chars)

if chars.count(highest)>1 : print("Tie")
else: print(f"{names[chars.index(highest)]} has the highest count.")


#Q2
cfail=cpass=cgood=cexcellent=0
for i in range(10):
    marks=int(input("Enter marks: "))

    if marks>100 or marks<0: print("Invalid Marks")
    elif marks>=75:
        cexcellent+=1
        print("Excellent")
    elif marks>=50:
        cgood+=1
        print("Good")
    elif marks>=35:
        cpass+=1
        print("Pass")
    else:
        cfail+=1
        print("Fail")

print(f"Number of students scoring 'Excellent' : {cexcellent}")
print(f"Number of students scoring 'Good' : {cgood}")
print(f"Number of students 'Passed' : {cpass}")
print(f"Number of students 'failed' : {cfail}")

#Q3
sentence=input("Enter a sentence: ").split()

highest_score=-1
hs_word=None

for word in sentence:
    score=0
    for char in word:
        if char.lower() in "aeiou": score+=2
        elif char.isalpha(): score+=1
        elif char.isdigit(): score+=3
        else: score+=4

if score>highest_score:
    highest_score=score
    hs_word=word

print(f"'{hs_word}' is the word with highest score: {highest_score}")


#Q4
password_type=None
for i in range(5):
    password=input("Enter Password: ")

    digit=splchar=upper=lower=0
    length=len(password)
    
    for char in password:
        if char.islower(): lower+=1
        elif char.isupper(): upper+=1
        elif char.isdigit(): digit+=1
        elif not char.isalnum(): splchar+=1

    if digit>=1 and splchar>=1 and upper>=1 and lower>=1 and length>=8: password_type="Strong"
    elif length >= 8 and (
        (digit >= 1 and upper >= 1 and lower >= 1) or
        (digit >= 1 and splchar >= 1 and lower >= 1) or
        (upper >= 1 and splchar >= 1 and lower >= 1)
    ):
        password_type = "Medium"
    else: password_type="Weak"

    print(f" Your Password is: {password_type}")


#Q5
sentence=input("Enter a Sentence: ").split()
short=medium=long=0

for word in sentence:
    length=len(word)
    word_type=None

    if length<=3: 
        word_type="Short"
        short+=1
    elif 4<=length<=6: 
        word_type="Medium"
        medium+=1
    else: 
        word_type="Long"
        long+=1

    print(f"Length of the word is {length} and it is {word_type}")
print(f"Short: {short}")
print(f"Medium: {medium}")
print(f"Long: {long}")


#Q6
for i in range(5):
    number=input("Enter a number: ").strip()
    odd=even=0

    for each in number:
        if each.isdigit():
            each=int(each)
            if each%2==0: even+=1
            else: odd+=1

    if odd>even: print("Odd")
    elif even>odd: print("Even")
    else: print("Equal")


#Q7
word=input("Enter a Word").strip().lower()
processed=[]

for each in word:
    if each in processed:
        continue

    repititions=0
    for char in word:
        if char==each: repititions+=1

    processed.append(each)

    if repititions>=2: 
        print(char)
        if repititions<=3: print("Duplicate")
        elif repititions<=5: print("Repeated")
        else: print("Highly Repeated")

#Q8
total=0
budget=Regular=Premium=Luxury=0
invaild=False

for i in range(8):
    price=int(input("Enter price of product: "))
    total+=price

    if price<0: invaild=True
    elif price>0 and price<500: budget+=1
    elif price<2000: Regular+=1
    elif price<5000: Premium+=1
    else: Luxury+=1

if invaild: print("Enter Valid price")
else:
    print(f"Total amount: {total}")
    print(f"Average price: {total/8}")
    print(f"Budget: {budget}")
    print(f"Regular: {Regular}")
    print(f"Premium: {Premium}")
    print(f"Luxury: {Luxury}")


#Q9
word=input("Enter a String: ").strip().lower()
vowel="aeiou"
consonants="bcdfghjklmnpqrstvwxyz"
vc=cc=dc=sc=0

for index,char in enumerate(word):
    print(f"Character: {char} Position: {index}")

    if word.index(char)==0: print("Zeroth Position")
    elif word.index(char)%2==0: print("Position is Even")
    else: print("Position is Odd")

    if char in vowel:
        print("Vowel")
        vc+=1
    elif char in consonants:
        print("Vowel")
        cc+=1
    elif char.isdigit():
        print("Digit")
        dc+=1
    else:
        print("Special Character\n\n")
        sc+=1

print(f"Total Vowels: {vc}")
print(f"Total Consonants: {cc}")
print(f"Total Digits: {dc}")
print(f"Total Special Characters: {sc}")

#Q10
