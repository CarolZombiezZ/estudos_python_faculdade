try:
    # Simulando um erro de propósito
    raise ValueError("Este é um erro forçado para teste!")
    
except ValueError as erro:
    # Código executado quando o erro ocorre
    print(f"Erro capturado: {erro}")
    
else:
    # Código executado APENAS se nenhum erro acontecer no try
    print("Sucesso! Nenhum erro ocorreu.")
    
finally:
    # Código executado SEMPRE, independentemente de erro ou sucesso
    print("Bloco finally: limpeza ou finalização concluída.")
