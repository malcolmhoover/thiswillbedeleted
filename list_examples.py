#list
x = 43
y = ['42', '5', ['bye']]
z = [3, 5, 7, 9, 11, 56, 89]
#lst = [x, x, x, y, 'another string']
lst = [23, 53, 3, 7, 19]
#print(lst[3][2][0])
#for x in lst:
#    x += 5
    #print(x)

rng = list(range(10))
print(lst)
#print(len(lst))
for index in range(len(z)):
    z[index] += 5
    print('index: {}, value: {}' .format(index, z[index]))
