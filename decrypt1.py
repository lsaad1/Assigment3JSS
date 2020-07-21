def Key(Input):
    number=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    alpha='abcdefghijklmnopqrstuvwxyz'

    for i in Input:
        if i in alpha:
            index = alpha.find(i)
            number[index] = number[index] + 1

    Max1 = 0
    Index1 = 0
    for j in range(26):
        if(Max1 < number[j]):
            Max1 = number[j]
            Index1 = j  #swap
    
    key = Index1 - 4
    if(key<0):
        key+=26

    return key

filename = raw_input("Enter the file name: ")
Input = open("{0}".format(filename)).read()
key = Key(Input)
print("The key is: {0}".format(key))

