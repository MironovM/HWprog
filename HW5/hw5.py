#вариант 2
word = 'Начнем, пожалуй.'
while len(word) > 0:
    word = input ('Введите слово (пустое слово, если хотите закончить): ')
    if len(word) > 4:
        with open("text.txt", "a", encoding="utf-8") as f:
            f.write(word)
            f.write("\n")
