from pypdf import PdfReader
from pypdf import PdfWriter

reader = PdfReader("Py1.pdf")  # read pdf file
number_of_pages = len(reader.pages)  # get the length of pages in pdf
page = reader.pages[0]  # extract page 1 using index 0
text = page.extract_text()  # get the text of pdf page using extract_text


for i in range(0, 17):
    page = reader.pages[i]  # extract page one by one using index
    text = page.extract_text() # get the text of pdf page one by one using index
    print(text) # print the text of the page


