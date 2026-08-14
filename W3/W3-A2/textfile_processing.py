
# Open the junk.txt file and count the number of lines
with open("W3\\W3-A2\\junk.txt", "r") as file:
    lines = file.readlines()

print("Total number of lines:", len(lines))


# Add the required text at the end of the file
with open("W3\\W3-A2\\junk.txt", "a") as file:
    file.write("text file analysis\n")


# Read the updated file
with open("W3\\W3-A2\\junk.txt", "r") as file:
    data = file.read()


# Convert all text to lowercase
data = data.lower()


# Save the processed data back to junk.txt
with open("W3\\W3-A2\\junk.txt", "w") as file:
    file.write(data)


print("File processing completed.")