print("Uma criança está com fome e sua mãe vai ao mercado para comprar um suco e um doce.")
print("\nTente adivinhar o que a criança gosta, mas precisa escrever certinho em letra minúscula para que funcione.")
print("\nAs opções são as seguintes: uva, banana, mamão, limão, chocolate, bala, piriluto")

fruta = input("\nVocê chegou no mercado e está na seção de frutas. Tente adivinhar a fruta favorita da criança: ")

if fruta == "uva":
    print("\nParabéns, você acertou!")

    quantidade = int(input("Quantas frutas vai escolher? "))
    
    if quantidade == 1:
        print("Voce escolheu 1 fruta, eu acho pouco, mas serve só pra criança comer")
    elif quantidade == 2:
        print("Voce escolheu 2 frutas, ta ótimo, serve por hoje, pode ser pra voce e uma pra criança ")
    elif quantidade == 3: 
        print("Voce escolheu 3 frutas, ta ótimo, pode ser duas pra voce e uma pra criança")
    elif 3 <= quantidade <= 10:
        print("Voce escolheu de 3 até 10 frutas, uma boa quantidade")
    elif quantidade > 10:
        print("Muita fruta, voce vai utilizar até 10 frutas, o restante vai ser preciso doar")
    else:
        print("Error: Quantidade inválida")
        exit()

    doce = input("\nAgora tente adivinhar o doce favorito da criança: ")
    
    if doce == "chocolate":
        print("\nParabéns, você acertou!")
        
        print("\nAgora escolha a forma de pagamento: dinheiro, cartão ou pix")
        pagamento = input("Forma de pagamento: ")
        
        if pagamento in ["dinheiro", "cartão", "pix"]:
            print(f"\nCompra finalizada com {pagamento}. A criança está feliz! 🎉")
        else:
            print("\nForma de pagamento inválida!")
    else:
        print("\nErrou o doce favorito 😢")

else:
    print("\nErrou a fruta favorita 😢")
