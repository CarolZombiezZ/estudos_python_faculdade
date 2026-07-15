try:
  print(10 / 2)
except ZeroDivisionError:
  print("Ops! Não é possível dividir por zero.")
else:
  print("Divisão feita com sucesso!")
finally:
  print("Esse bloco sempre será executado.")