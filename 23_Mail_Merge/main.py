#TODO: Create a letter using starting_letter.txt

PLACEHOLDER = "[name]"
#for each name in invited_names.txt
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    print(names)

#Replace the [name] placeholder with the actual name.
with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    # print(f"Template content: {letter_contents}")

    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        # print(new_letter)
#Save the letters in the folder "ReadyToSend".
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
