def evalRPN(tokens):
    stack = []
    for token in tokens:
        if token != "+" and token != "-" and token != "*" and token != "/":
            stack.append(int(token))
        else:
            a = stack.pop()
            b = stack.pop()
            if token == "+":
                stack.append(a + b)
            if token == "-":
                stack.append(b - a)
            if token == "*":
                stack.append(b * a)
            if token == "/":
                if a*b < 0:
                    stack.append(-1 * (-b // a))
                else:
                    stack.append(b // a)
    return stack.pop()

result = evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
print(result)