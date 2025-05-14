#  We need to close here
# file = open("my_file.txt")
# content = file.read()
# print(content)
# file.close()

# file will close automatically here
with open("my_file.txt") as file:
    content = file.read()
    print(content)

# write in file(old content wont be availabe(No append))
with open("my_file.txt", mode="w") as file:
    file.write("This is writing the file")

#  if file not exit it will create 
with open("created_file.txt", mode="w") as file:
    file.write("This is creted the file")

# Append while writing
with open("my_file.txt", mode="a") as file:
    file.write("\nThis is appending while writing the file")