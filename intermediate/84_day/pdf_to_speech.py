import PyPDF2
import pyttsx3


def pdf_to_speech(pdf_file):
    try:
        # Ler o PDF
        with open(pdf_file, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ''
            for page_num in range(len(reader.pages)):
                text += reader.pages[page_num].extract_text()

        if text:
            # Iniciar o motor de fala
            engine = pyttsx3.init()
            engine.say(text)
            engine.runAndWait()
        else:
            print("❌ Nenhum texto encontrado no PDF.")

    except FileNotFoundError:
        print(f"❌ Arquivo '{pdf_file}' não encontrado.")
    except Exception as e:
        print(f"❌ Erro ao converter o PDF: {e}")


# Exemplo de uso:
if __name__ == "__main__":
    pdf_path = input("Digite o caminho do arquivo PDF: ")
    pdf_to_speech(pdf_path)
