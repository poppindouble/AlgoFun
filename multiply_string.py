def multiply(num1, num2):
    # if len(num1) > len(num2):
    #     return multiply(num2, num1)

    num1 = num1[::-1]
    num2 = num2[::-1]
    arr = [0 for i in range(len(num1) + len(num2))]
    for i in range(len(num1)):
        for j in range(len(num2)):
            arr[i + j] += int(num1[i]) * int(num2[j])

    carry = 0
    for i in range(len(arr)):
        temp = carry + arr[i]
        arr[i] = temp % 10
        carry = temp // 10
    arr = arr[::-1]
    i = 0
    for num in arr:
        if num != 0:
            break
        i += 1
    if not arr[i:]:
        return "0"
    return "".join(list(map(lambda x: str(x), arr[i:])))

def main():
    print(multiply("32", "1243"))
    print(multiply("1", "10"))
    print(multiply("9", "20"))
    print(multiply("10", "100"))
    print(multiply("100", "0"))
    

if __name__ == "__main__":
    main()