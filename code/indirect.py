import tkinter as tk


OPERATORS = set(['+', '-', '*', '/', '(', ')'])
PRI = {'+': 1, '-': 1, '*': 2, '/': 2}


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
            stack.pop()
        else:
            while stack and stack[-1] != '(' and PRI[ch] <= PRI[stack[-1]]:
                output += stack.pop()
            stack.append(ch)
    while stack:
        output += stack.pop()
    return output


def indirect_triple(expression):
    pos = infix_to_postfix(expression)
    address = dict()
    stack = []
    text1 = " Op  | Arg1 | Arg2 |Statement"
    text2 = "Statement|Location"
    c = 0
    for i in pos:
        if i not in OPERATORS:
            stack.append(i)
        else:
            op1 = stack.pop()
            if stack:
                op2 = stack.pop()
                if str(sorted(op1 + op2 + i)) in address.keys():
                    stack.append("(%s)" % address[str(sorted(op1 + op2 + i))])
                else:
                    text1 += "\n{0:^4s} | {1:^4s} | {2:^4s} | {3:^5d}".format(i, op2, op1, c)
                    address[str(sorted(op1 + op2 + i))] = c
                    stack.append("(%s)" % c)
                    c += 1

    z = 35

    for i in range(c):
        text2 += "\n{0:^8d} |{1:^4d}".format(i, z)
        z += 1

    return text1, text2


def convert_button_click():
    expression = entry.get()
    text1, text2 = indirect_triple(expression)
    text_output1.configure(state='normal')
    text_output2.configure(state='normal')
    text_output1.delete('1.0', 'end')
    text_output2.delete('1.0', 'end')
    text_output1.insert('1.0', text1)
    text_output2.insert('1.0', text2)
    text_output1.configure(state='disabled')
    text_output2.configure(state='disabled')


# Create the main window
window = tk.Tk()
window.title("Indirect Triples")

# Create and place the input label and entry field
label = tk.Label(window, text="Enter an infix expression:")
label.pack()
entry = tk.Entry(window)
entry.pack()

# Create and place the convert button
convert_button = tk.Button(window, text="Convert", command=convert_button_click)
convert_button.pack()

# Create a frame to hold the output text areas
output_frame = tk.Frame(window)
output_frame.pack()

# Create and place the output labels

text_output1 = tk.Text(output_frame, height=10, width=30)
text_output1.configure(state='disabled')
text_output1.pack(side='left')

text_output2 = tk.Text(output_frame, height=10, width=30)
text_output2.configure(state='disabled')
text_output2.pack(side='left')

# Start the GUI event loop
window.mainloop()
