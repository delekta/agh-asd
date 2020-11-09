# Kod ASCII

# Array in which index 0 corresponds to the number of letter "a" in word
arr = [0] * 26
word = 'ala'
for letter in word:
    # function ord() would get int value of the char
    arr[ord(letter) - 97] += 1

print(arr)

