print("Uma criança esta com fome e sua mãe vai ao mercado para comprar um suco e um doce")
print("\nTente advinhar o que a criança gosta, mas precisa escrever certinho em letra minuscula para que funcione")
print("\nAs opções são as seguintes: uva, banana, mamão, limão, chocolate, bala, piriluto")

fruta = input("\nVoce chegou no mercado e esta no seção de frutas, tente adivinhar a fruta favorita da criança: ")
if fruta == "uva":
    print("\nParabéns você acertou!")

    doce = input("\nTente adivinhar o doce favorita da criança: ")

    if doce == "chocolate":
        print("\nParabéns voce acertou!")
        print("\nPode passar a mercadoria e realizar a compra")
    else: 
        print("Errou")

else: 
    print("Errou")



