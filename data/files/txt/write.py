def search(file_path):
    print("Searching...")
    sections = []
    books = []
    with open(file_path) as file:
        for line in file:
            if line.startswith("Section"):
                section_name = line.split(":")[1]
                sections.append(section_name.strip())
            else:
                books.append(line.strip())
    print("Done!")
    return (sections, books)
def save(file_path, data):
    print("Saving...", end="")
    with open(file_path, "w") as file:
        file.write(f"Sections: {data[0]}\n")
        file.write(f"Books: {data[1]}\n")
    print("Done!")
def run():
    data = search("books.txt")
    save("section-books.txt", data)

run()
