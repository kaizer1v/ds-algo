'''
Dijkstra's two stack algorithm

For a given expression `(1 + ( (2 + 3) * (4 * 5) ))`
if the char is not a number, put it in the operator stack, if it's a number
put it in the value stack
'''
from stack import StackUsingList

o = StackUsingList()    # operator stack
v = StackUsingList()    # value stack

def walk(expr):
    for c in expr:
        if c != '(':
            try:
                v.push(int(c))
            except:
                o.push(c)
        elif c == ')':
            x = v.pop()
            y = v.pop()
            opr = o.pop()
            v.push(eval('{} {} {}'.format(x, opr, y)))
    return v.pop()


print(walk('(1 + ( (2 + 3) * (4 * 5) ))'))
