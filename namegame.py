name = input('what is the your name?:')
valid_int = False
num = 0
while not valid_int:
    try:
        age = int(input('Hello {}, how old are you?: '.format(name)))
        valid_int = True
    except ValueError:
        print('that is not a valid integer, please try again.')
if age > 100:
    print('you should be dead already')
elif age > 20:
    print('old already.')
else:
    print('too young, get off my lawn')

if age == 20:
    print('you win.')
