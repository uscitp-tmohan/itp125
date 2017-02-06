with open('text.txt','r+') as my_file:
    my_file.write('hello')
if my_file.close():
    my_file.closed
print my_file.closed