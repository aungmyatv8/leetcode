def add_binary(a, b):
    return bin(int(a, 2) + int(b, 2) )[2:]


a = "1101"
b = "101"
result = add_binary(a, b)
print(result)