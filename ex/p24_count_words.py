

# Wrong
with open("./rsc/email-addresses.txt", "r") as f:
    counter = 0

    for line in f:
        counter += len(line.split(" "))

print(counter)
