
""""# We can write to a file by opening a file in write mode and using the method write.
with open("output.txt", "w") as file:
    file.write("some text")
    print(file)
We can also write out multiple lines using the method writelines which takes a list as an argument.
Note, that each line in the list will need to include the end of line character.
lines = ["first line\n", "second line\n", "Third line\n"]
with open("output.txt", "w") as file:
    file.writelines(lines)

                        Task:-
"""
def search(file_name):
    print("Searching...")
    data = {}
    with open("books.txt") as file:
        section_name = ""
        for line in file:
            if (line.startswith("Section")):
                parts = line.split(":")
                section_name = parts[1].strip()
            elif (section_name in data):
                data[section_name].append(line.strip())
            else:
                data[section_name] = [line.strip()]
        print("Done!")
        return data
def run():
    data = search("books.txt")
    with open("generated.csv", "w") as file:
        for section, books in data.items():
            for book in books:
                file.write(f"{section},{book}\n")

run()



