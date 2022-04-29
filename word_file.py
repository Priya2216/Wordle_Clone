def main():
    input_file_path = "sgb-words.txt"
    output_file_path = "sgb-words.txt"
    five_letter_words = []

    with open(input_file_path, "r") as f:
        for line in f.readlines():
            word = line.strip()
            if len(word) == 5:
                five_letter_words.append(word)

    with open(output_file_path, "w") as f:
        for word in five_letter_words:
            f.write(word + "\n")

    print(f"Total letters in file are: {len(five_letter_words)}")


if __name__ == "__main__":
    main()