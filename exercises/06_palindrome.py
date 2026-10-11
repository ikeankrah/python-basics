# Palindrome checker
def is_palindrome(text):
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

for word in ["level", "Python", "never odd or even"]:
    print(word, "->", is_palindrome(word))
