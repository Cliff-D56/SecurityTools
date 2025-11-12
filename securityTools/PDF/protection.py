import pypdf
import sys

print("Starting Encyption operation") 

def create_password_protect_pdf(input_pdf, output_pdf, password):
    try:
        with open(input_pdf, 'rb') as inputFile:
            pdf_reader = pypdf.PdfReader(inputFile)
            pdf_writer = pypdf.PdfWriter()

            for page_num in range(len(pdf_reader.pages)):
                pdf_writer.add_page(pdf_reader.pages[page_num])

            pdf_writer.encrypt(password)

            with open(output_pdf, 'wb') as outputFile:
                pdf_writer.write(output_pdf)
            print(f"Password protected PDF saved as {output_pdf}")
    except Exception as e:
        print(f"{e}")
    except pypdf.utils.PdfReaderError:
        print("HI")

def main():
    if(len(sys.argv) != 4):
        print("Usage: python3 script.py <input_pdf> <output_pdf> <password>")
        sys.exit(1)

    input_pdf = sys.argv[1]
    output_pdf = sys.argv[2]
    password = sys.argv[3]

    create_password_protect_pdf(input_pdf,output_pdf,password)

if __name__== "__main__":
    main()