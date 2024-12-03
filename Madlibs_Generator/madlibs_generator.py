
with open("/Users/beniaminenahid/Documents/python_projects/Madlibs_Generator/story.txt", "r") as f:
    content = f.read()

words = set() # we are using set to avoid duplicates
start_of_word = -1

target_start = "<"
target_end = ">"

for i, char in enumerate(content): # enumerate gives us the index and the charactr of the string
    if char == target_start:
        start_of_word = i # we are saving the index of the start of the word

    if char == target_end and start_of_word != -1:
        word = content[start_of_word: i + 1] # start_of_word is the start of the word and i is the end of the word
        words.add(word)
        start_of_word = -1


answers = {}

for word in words:
    answer = input(f"Enter a word for {word}: ")
    answers[word] = answer

for word in words:
    content = content.replace(word, answers[word] )

print(content)
    



