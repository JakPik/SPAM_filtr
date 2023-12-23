def read_classification_from_file(file_path):
    dictonary = {}
    with open(file_path, "rt", encoding="UTF-8") as f:
        for line in f:
            words = []
            words = line.split()
            dictonary[words[0]] = words[1]
    return dictonary

if __name__ == "__main__":
    DIC = read_classification_from_file("./spam_text")
    for key, value in DIC.items():
        print(f"{key}: {value}")