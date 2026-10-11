# Count vowels in a string
def count_vowels(text):
    return sum(1 for ch in text.lower() if ch in "aeiou")

print(count_vowels("Microbiology"))
print(count_vowels("University of Cape Coast"))
