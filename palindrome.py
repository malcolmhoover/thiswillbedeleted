def is_palindrome(string):
    if string == string[::-1]:
        print('awesome! it\'s a palindrome')
    else:
        print('that\'s not a palindrome homey')
pal = input('give me a word: ')
is_palindrome(pal)
