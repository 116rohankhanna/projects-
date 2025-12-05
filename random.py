
def count(num):
    ccount =0
    for i in num:
        ccount+= str(i).count('1')
    return ccount

a= input("enter the no :- ")
num = list(str(a.split()))

print(f"the total no of ones are {count(num)}")


def find_palindromes(word):
    palindromes = []

    # Check every possible substring
    for i in range(len(word)):
        for j in range(i + 1, len(word) + 1):
            sub = word[i:j]

            # Check palindrome and length ≥ 2 (optional)
            if sub == sub[::-1] and len(sub) >= 2:
                palindromes.append(sub)

    return palindromes


# Take input from user
user_word = input("Enter a word: ")

result = find_palindromes(user_word)

if result:
    print("Palindrome substrings found:", result)
else:
    print("No palindrome substrings found!")
