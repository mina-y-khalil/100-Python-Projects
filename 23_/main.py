with open("my_file.txt") as file: #  This is a better way to remember to close the file to avoid using unnecessary computer resources.
    contents = file.read()
    print(contents)
    # file.close() #with using (with) we don't have to remember closing the file manually

with open("new_file.txt", mode="w") as file2:
    file2.write("\nand this is my new message")
