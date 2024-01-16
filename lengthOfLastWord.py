def lengthOfLastWord(s):
    split_words =  s.strip().split(" ")
    return len(split_words[-1])

# s = "Hello World"
# s = "   fly me   to   the moon  "
# s = "luffy is still joyboy"
print(lengthOfLastWord(s))