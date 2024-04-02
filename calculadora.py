def displayOptions():
    print("- Digite 1 para somar dois valores")
    print("- Digite 2 para subtrair dois valores")
    print("- Digite 3 para multiplicar dois valores")
    print("- Digite 4 para dividir dois valores")
    print("- Digite 5 para realizar uma potência entre dois valores")
    print("- Digite 6 para realizar uma radiciação entre dois valores")
    print("- Digite qualquer outro número para sair")
displayOptions()

inicio = True
opcao = 0
while opcao in range(1,7) or inicio:
    displayOptions()
    opcao = int(input("Digite sua opção:"))
    if opcao == 1:
         a = int(input("Digite o valor de a:"))
         b = int(input("Digite o valor de b:"))
         print("Soma dos valores: ",(a+b))
    elif opcao == 2:
        a = int(input("Digite o valor de a:"))
        b = int(input("Digite o valor de b:"))
        print("Diferença dos valores: ",(a-b))
    elif opcao == 3:
        a = int(input("Digite o valor de a:"))
        b = int(input("Digite o valor de b:"))
        print("Produto dos valores: ",(a*b))
    elif opcao == 4:
      a = int(input("Digite o valor de a:"))
      b = int(input("Digite o valor de b:"))
      if b != 0:
       print("Divisão dos valores: ",(a/b))
      else:
       print("Não posso dividir por zero.")
    elif opcao == 5:
      a = int(input("Digite o valor de a:"))
      b = int(input("Digite o valor de b:"))
      print("a elevado a b: ",(a**b))
    elif opcao == 6:
      a = int(input("Digite o valor de a:"))
      b = int(input("Digite o valor de b:"))
      print("Raiz (fator b) de a: ",(a**(1/b)))
    else:
        # Se o usuário escolher uma opção inválida, o loop termina
        print("Saindo do programa.")
        break