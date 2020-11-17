# this python code converts the text to speech
import pyttsx3
import PyPDF2
# pdf open
book = open('oop.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
# how many pages are there
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
for num in pages(7, pages):       # start page to end of the page
    page = pdfReader.getPage()
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()


    # install pip install pyttsx3 and pip install PyPDF2
