# TODO: 2016-08-01, add the possibility to render an entire directory useless :)

import hashlib

filename='file.txt'

with open(filename, 'r') as file:
    read_data = file.read()
read_data = read_data.encode('utf-8')

codedString = hashlib.sha512(read_data)

print("Files contents were encrypted.")

filename=filename[0:5] + 'fkd'
with open(filename, 'wb+') as file:
    file.write(codedString.digest())

print("File operation completed contents encrypted")
print("Programme ended.")