strings = input().split(' ')
searched_palindrome = input()
palindromes = []

for word in strings:
    if word == ''.join(reversed(word)):
        palindromes.append(word)

found_palindrome = palindromes.count(searched_palindrome)

print(f'{palindromes}')
print(f'Found palindrome {found_palindrome} times')
