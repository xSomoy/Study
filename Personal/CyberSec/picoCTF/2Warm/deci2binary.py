def decimal_to_binary(decimal_value):
    return bin(decimal_value).replace("0b", "")

decimal_value = int(input("Enter a decimal value: "))
print(decimal_to_binary(decimal_value))
