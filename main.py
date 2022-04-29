import random
import word_file


# load word file
def load_word_set(path: str):
    word_set = set()
    with open(path, "r") as f:
        for line in f.readlines():
            word = line.strip().upper()
            word_set.add(word)
    return word_set

word_list = load_word_set("sgb-words.txt")
answer = random.choice(list(word_list))


# check letters  g=green(correct), y=yellow(incorrect)
def get_clue(ans, guess):
  clue = ""
  for idx, letter in enumerate(guess):
    
    if letter == ans[idx]:
      clue += "G"
    elif letter in ans:
      clue += "Y"
    else:
      clue += "-"
      
  return clue


# loop for guess 6 times 
for x in range(1,7):    
    guess = input("Guess the word: ")[0:5]
    print(get_clue(answer, guess), x)
    if answer == guess:
        break
# print the ans if word not able to find
else:
    print(answer)
    