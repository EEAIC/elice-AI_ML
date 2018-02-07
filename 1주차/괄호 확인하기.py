def main():
    tc = int(input("testcases > "))
    for i in range(tc):
        text = input("text > ")
        if check_parenthesis(text) == True:
            print("통과")
        else:
            print("거부")

def check_parenthesis(text):
    stack = []
    que = []
    paren = '({[)}]'
    for i in text:
        if i in paren:
            que.append(i)
    if not que:
        return True
    for c in que:
        if not stack:
            if not c in paren[0:3]:
                return False
            stack.append(c)
        elif c in paren[0:3]:
            if paren.index(stack[-1]) < paren.index(c):
                return False
            stack.append(c)
        else:
            if paren.index(stack[-1]) != paren.index(c) - 3:
                return False
            stack.pop()
    if stack:
        return False
    return True

if __name__ == "__main__":
    main()
