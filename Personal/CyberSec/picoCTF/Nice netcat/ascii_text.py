def ascii_to_text(ascii_code):
    return chr(ascii_code)

filename = input("Enter the name of the file: ")
with open(filename, 'r') as file:
    ascii_codes = file.read().splitlines()

text = ""
for ascii_code in ascii_codes:
    text += ascii_to_text(int(ascii_code))

print(text)
