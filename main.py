import pyttsx3
import PyPDF2
bolt = pyttsx3.init()
book_read = open('oop.pdf','rb')
book_pdf_reader = PyPDF2.PdfFileReader(book_read)
pages = book_pdf_reader.numPages
page = book_pdf_reader.getPage(1)
text = page.extractText()
bolt.say(text)
bolt.runAndWait()
