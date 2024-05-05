def equal(result, string):
    if len(result) != len(string):
        return False
    else:
        for i in range(len(string)):
            if result[i] != string[i] and string[i] != "?":
                return False
        return True


def generate_number(nums):
    X = "0123456789"
    if nums[0] == "?":
        for i in range(1, 10):
            result = X[i]
            if nums[1] == "?":
                for j in range(10):
                    yield result + X[j]
            else:
                yield X[i] + nums[1]
    else:
        result = nums[0]
        if nums[1] == "?":
            for i in range(10):
                yield nums[0] + X[i]
        else:
            yield nums


def generate_operator(operator):
    if operator == "?":
        for i in ['-', '+']:
            yield i

    else:
        yield operator


def function():
    calculation = input().split()
    for i in generate_number(calculation[0]):
        for k in generate_number(calculation[2]):
            for j in generate_operator(calculation[1]):
                string = i + " " + j + " " + k
                result = eval(string)
                if equal(str(result), calculation[4]) and result >= 10:
                    print(string + " =", result)
                    return
    print("WRONG PROBLEM!")


if __name__ == "__main__":
    for i in range(int(input())):
        function()
