# open file on read mode
with open('file.txt')as file:
    contents = file.read()
    print(contents)

# open file on write mode
with open('file1.txt', mode='w')as file:
    file.write('write File')

# open file on append mode
with open('file1.txt', mode='a')as file:
    file.write('\nappend line')
