OPERATORS = set(['+', '-', '*', '/', '(', ')'])
PRI = {'+': 1, '-': 1, '*': 2, '/': 2}



### INFIX ===> POSTFIX ###
def infix_to_postfix(formula):
    stack = [] 
    output = ''
    for ch in formula:
        if ch not in OPERATORS:
            output += ch
        elif ch == '(':
            stack.append('(')
        elif ch == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop()  # pop '('
        else:
            while stack and stack[-1] != '(' and PRI[ch] <= PRI[stack[-1]]:
                output += stack.pop()
            stack.append(ch)
    # leftover
    while stack:
        output += stack.pop()
    #print(f'POSTFIX: {output}')
    return output

def IndirectTriple(expres):
    pos = infix_to_postfix(expres)
    address=dict()
    stack = []
    text1=" Op  | Arg1 | Arg2 |Statement"
    text2="Statement|Location"
    c = 0
    for i in pos:
        if i not in OPERATORS:
            stack.append(i)
        else:
            op1 = stack.pop()
            if stack != []:
                op2 = stack.pop()
                if str(sorted(op1+op2+i)) in address.keys():
                    stack.append("(%s)" % address[str(sorted(op1+op2+i))])
                else:
                    text1+="\n{0:^4s} | {1:^4s} | {2:^4s} | {3:^5d}".format(i, op2, op1, c)
                    address[str(sorted(op1+op2+i))]=c
                    stack.append("(%s)" % c)
                    c = c+1

    z = 35
    
    for i in range(0, c):
        text2+="\n{0:^8d} |{1:^4d}".format(i, z)
        z = z+1
    return text1,text2








