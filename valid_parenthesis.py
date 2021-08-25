
s = '(]'
def isValid(s: str) -> bool:
    open_list = ["[","{","("]
    close_list = ["]","}",")"]
    stack = []
    for i in s:
        if i in open_list:
            stack.append(i)
            print(f'stack is current: {stack}')
        elif i in close_list:
            pos = close_list.index(i)
            print(f'pos is {pos}')
            if (len(stack) > 0) and (open_list[pos] == stack[len(stack)-1]):
                print(f'length of stack is {len(stack)}')
                print(f'open_list[pos] == {open_list[pos]} and stack[len(stack)-1] == {stack[len(stack)-1]}')
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False

print(isValid(s))
