def Key(Input):
    number = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    alpha = "abcdefghijklmnopqrstuvwxyz"

    for i in Input:
        if i in alpha:
            index = alpha.find(i)
            number[index] += 1

    Max1 = 0
    Index1 = 0
    for j in range(26):
        if(Max1 < number[j]):
            Max1 = number[j]
            Index1 = j   #swap
    
    key = Index1 - 4
    if(key<0):
        key+=26

    return key

def get_text(Input,key):
    result = ""
    for i in range(len(Input)):
        c = Input[i]
        if(c.isupper()):
            c=c.lower()
        if(c.isalpha()):
            if(ord(c) - key < 0):
                result += chr((ord(c) - key + 26 - 97) %26 +97)
            else:
                result += chr((ord(c) - key - 97) %26 +97)
	else:
            result += c
    return result


filename = raw_input("Enter the file name: ")
Input = open("{0}".format(filename)).read()
key = Key(Input)
print("The key is: {0} \n".format(key))
print("Recovered text: \n {0}".format(get_text(Input,key)))

