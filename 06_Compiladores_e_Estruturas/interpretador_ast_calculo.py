# #Interpretador (walk na AST) codigo original


# def interpret(node):
#     if isinstance(node, Number):
#         return node.value
#     if isinstance(node, BinOp):
#         l = interpret(node.left)
#         r = interpret(node.right)
#         if node.op == '+': return l + r
#         if node.op == '*': return l * r

# result = interpret(tree) # 14


class Number:
    def __init__(self, value):
        self.value = value

class BinOp:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

def interpret(node):
    if isinstance(node, Number):
        return node.value
    
    if isinstance(node, BinOp):
        l = interpret(node.left)
        r = interpret(node.right)
        
        if node.op == '+': 
            return l + r
        if node.op == '*': 
            return l * r

# Exemplo para resultar em 14: (2 * 5) + 4
# Estrutura da árvore:
#       +
#      / \
#     * 4
#    / \
#   2   5

tree = BinOp(BinOp(Number(2), '*', Number(5)), '+', Number(4))

result = interpret(tree)
print(f"Resultado: {result}") # Saída: 14