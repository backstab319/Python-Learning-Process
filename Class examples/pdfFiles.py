import PyPDF2
f = open("hello.pdf","rb")
fread = PyPDF2.PdfFileReader(f)
fpage = fread.getPage(0)
print(fpage.extractText())
f.close()