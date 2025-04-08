alphabeth = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u' , 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input('Type your message:\n').lower()
shift = int(input('Type the shift number:\n'))

def encrypt(original_text, shift_amount):
     cipher_text = ''
     for letter in original_text:
          shifted_position = alphabeth.index(letter) + shift_amount

          shifted_position %= len(alphabeth)
          cipher_text += alphabeth[shifted_position]
    
     print(f"Here is the encoded result: {cipher_text}") 

encrypt(original_text=text, shift_amount=shift)
            