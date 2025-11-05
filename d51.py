#palindrome checker(string program)
def is_palindrome(text):
    text = text.replace("","").lower()
    return text == text[::-1]
word = input("enter a word:")
print("palindrome!" if is_palindrome(word) else "not a palindrome!")