import sys

if len(sys.argv) != 2:
    print("Please provide the complete file path.")
else:
    path = sys.argv[1]
    total_lines = 0
    total_words = 0
    with open(path) as file:
        for line in file:
            line = line.strip("\n")
            line = line.strip(" ")
            if len(line) > 0:
                total_lines += 1
            words = line.split(" ")
            total_words += len(words)

    print(total_lines)
    print(total_words)

