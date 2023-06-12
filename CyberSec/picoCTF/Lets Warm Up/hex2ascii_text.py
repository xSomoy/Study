def hex_to_int(hex_value):
    return int(hex_value, 16)

hex_value = input("Enter a hexadecimal value: ")
print(hex_to_int(hex_value))

def ascii_to_text(ascii_code):
    return chr(ascii_code)

print(ascii_to_text(hex_to_int(hex_value))) # 'p'