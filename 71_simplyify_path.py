import re

def simplifyPath(path: str) -> str:
    path = re.split('[/]', path)
    stack = []

    for file in path:
        if file == '..':
            if stack:
                stack = stack[:-1]
        elif file and file != '.':
            stack.append(file)

    return '/' + '/'.join(stack)

# Notes: First time solution achieved. No real issues. Read up on re maybe.

if __name__ == '__main__':
    print(simplifyPath('/home/user/Documents/../Pictures'))
