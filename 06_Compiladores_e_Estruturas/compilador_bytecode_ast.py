# Compilador (gera bytecode) original

# def compile_to_bc(node, instrs):
#     if isinstance(node, Number):
#         instrs.append(('LOAD_CONST', node.value))
#     elif isinstance(node, BinOp):
#         compile_to_bc(node.left, instrs)
#         compile_to_bc(node.right, instrs)
#         instrs.append(('ADD',))
#     return instrs


class Number:
    def __init__(self, value):
        self.value = value

class BinOp:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

def compile_to_bc(node, instrs):
    if isinstance(node, Number):
        # Coloca o valor na "pilha"
        instrs.append(('LOAD_CONST', node.value))
    
    elif isinstance(node, BinOp):
        # Primeiro compila o lado esquerdo, depois o direito
        compile_to_bc(node.left, instrs)
        compile_to_bc(node.right, instrs)
        
        # Adiciona a instrução da operação
        if node.op == '+':
            instrs.append(('ADD',))
        elif node.op == '*':
            instrs.append(('MUL',))
            
    return instrs

# Exemplo: Expressão (2 * 5) + 4
tree = BinOp(BinOp(Number(2), '*', Number(5)), '+', Number(4))

# Gerando o bytecode
bytecode = []
compile_to_bc(tree, bytecode)

# Exibindo as instruções geradas
for i, instr in enumerate(bytecode):
    print(f"{i}: {instr}")