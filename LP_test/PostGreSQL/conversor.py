# Specify the path to the Latin1 encoded text file
input_file = "cinemas.txt"

# Specify the path to the output UTF-8 encoded text file
output_file = "cine.txt"

# Read the contents of the input file in Latin1 encoding
with open(input_file, "r", encoding="ISO-8859-1") as file:
    contents = file.read()

# Write the contents to the output file in UTF-8 encoding
with open(output_file, "w", encoding="utf-8") as file:
    file.write(contents)