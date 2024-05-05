def gray_to_binary(gray_string):
    binary_string = ""
    xor_result = 0

    for char in gray_string:
        xor_result ^= int(char)
        binary_string += str(xor_result)

    return binary_string

T = int(input())
for _ in range(T):
    gray_input = input().strip()
    binary_output = gray_to_binary(gray_input)
    print(binary_output)