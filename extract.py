import PyPDF2 as p
import textract

def get_text(path=''):

    # Opening in binary mode
    file_con = open(path, 'rb')
    pdf_con = p.PdfFileReader(file_con)
    n = pdf_con.numPages

    i = 0
    text = ''
    while(i < n ):

        temp = pdf_con.getPage(i)

        text = text + temp.extractText()
        i=i+1

    if(text == ''):
        # if text is empty use OCR optical character recognition
        text = textract.process(file_con, method='tesseract', encoding='utf-8')
       
    return text

if __name__ == '__main__': 

    pdfFilePath = '../test.pdf'
   
    pdfText = get_text(pdfFilePath)
    print(pdfText)  