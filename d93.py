#pdf text extractor 
import PyPDF2
pdf=PyPDF2.PdfReader("class.pdf")
text=""
for page in pdf.pages:
    text += page.extract_text()
print(text)
    