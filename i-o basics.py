# f = open('text.txt')  # file pointer creation, second argument is file type
"""
"r" - open file for reading
"w" - open a file for writing
"x" - create file if not exists
"a" - Append mode (Add more content to a file)
"t" - text mode
"b" - binary mode
"+" - read write both
writing to a file functions
read() - reads a file.
close() - closes a file.
readline() - prints the lines in the file.
readlines() - make a list out of the lines.
write() - writing to a file.
read() - reading a file.
tell() - tells on which character the cursor is.
seek() - brings the cursor to a certain character.
with keyword
in append mode we use the write function to write to the file but the file content is harmed during the process.
"""
# content = f.read()
# print(content)
#
# for line in f:
#     print(line)
#
# f.close()  # standard practice in order maintain pc resources.

# append mode
# f = open("text.txt", "a")
# f.write("Lets talk")
# f.close()

# read and write mode.
# f = open("text.txt", "w")
# print(f.read())
# f.write("Lets talk")
# f.close()
with open("text.txt") as f:
    a = f.readlines()
    print(a)

# read and write mode.
f = open("text.txt", "r")
print(f.read())

f.close()
