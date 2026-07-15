def apresentar_produto(nome, preco="Preço não informado"):
    print(f"Produto: {nome} - Valor: {preco}")

# Chamada da função com um argumento (preço padrão será usado)
apresentar_produto("Notebook") # Saída: Produto: Notebook - Valor: Preço não informado
apresentar_produto("Mouse", "R$ 50") # Saída: Produto: Mouse - Valor: R$ 50