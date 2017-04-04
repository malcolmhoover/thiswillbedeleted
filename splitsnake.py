#snake_case to Camel Case

snake = input('give me something in snake case: ')

camel = snake.split("_")
reggie = []
for i in camel:
    reggie.append(i.capitalize())
newword = ''.join(reggie)
print(newword)
