string = "HelloHowAreYouToday"
string_list = []
last_index = 0
for i in range(len(string)):
    if string[i].isupper():
        if i != 0:
            string_list.append(string[last_index:i])
            last_index = i
print('_'.join(string_list).lower())
