with open("names.txt", "r") as fp:
    lines = fp.readlines()

with open("names.txt", "w") as fp:
    for line in lines:
        if line.strip("\n") != "the word":
            fp.write(line)