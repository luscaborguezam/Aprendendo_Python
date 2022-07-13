#Tipos de erro:
print("Erro de sintaxe\n"
      "O código está escrito errado. Ex:"
      "primt()")

print("Exceção(Exception)\n"
      "Exception --> classe principal das exceções\n"
      "Tem muitas."
      "https://docs.python.org/3/library/exceptions.html\n")
print("""
# Erro (de semantico/significado)lógico. são chamados de exceção
# ex: a variavel x não foi inicializada.
# Exceçãp... NameError: name 'x' is not defined
# print(x)
# Exceçãp... ZeroDivisionError: division by zero
r = 8 / 0# Erro se da porque na matemática divisão por 0 não existe
-------------------------------------------------------""")
print("""
Usaremos 
Try:
    Operação
except:
    Falhou
else:
    Deu certo
finally:
    Ocorre com ou sem exceções
-----------------------------------------------------------""")
try:
    a = int(input("1° Valor: "))
    b = int(input("2° Valor: "))
    r = a / b
except Exception as erro:
    print("O problema encontrado \n"
          f"Classe do problma: {erro.__class__} :(\n"
          f"Causa do problma: {erro.__cause__} :(\n"
          f"Contexto do problma: {erro.__context__} :(")

else:
    print(f"O Resultado é {r:.1f}")
finally:
    print("Volte sempre! Muito Obrigado")

print("""--------------------------------------------------------------
Um Try pode ter varios exceptions
------------------------------------------------------------------""")

try:
    a = int(input("1° Valor: "))
    b = int(input("2° Valor: "))
    r = a / b
except (ValueError, TypeError):
    print("Problema com os tipos de dadps que você digitou")
except (ZeroDivisionError):
    print("Não é possivel dividir um número por zero!")
except (KeyboardInterrupt):
    print("O usuário preferiu não informar os dados")
except Exception as erro:
    print(f"O erro encontrado foi {erro.__cause__ }")
else:
    print(f"O Resultado é {r:.1f}")
finally:
    print("Volte sempre! Muito Obrigado")