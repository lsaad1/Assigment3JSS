import sys

Input = open("message1.txt").read()
file = open("encrypt.txt", "w")

key = input('Enter a number: ')

result = " "
for i in Input:
  i.lower()
  if(ord(i) >= ord('a') and ord(i)<= ord('z')):
    character = chr(97 + (ord(i) + key -97 ) % 26)
    file.write(character)
  else:
    file.write(i)

file.close()


