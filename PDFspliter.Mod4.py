#--------PROGRAM: Split specific pages from a PDF and save into a new PDF

from PyPDF2 import PdfReader, PdfWriter  # Import tools to read and write PDFs

pdf_file_path = "file1.pdf"  # Name of the PDF file
pdf = PdfReader(pdf_file_path)  # Open the PDF file

pdfwriter = PdfWriter()  # Create a new empty PDF

pages = [0, 2, 4]  # Pages we want (page 1, 3, 5)

# Loop through selected pages
for page_num in pages:
    pdfwriter.add_page(pdf.pages[page_num])  # Add that page to new PDF

# Save the new PDF file
with open("output.pdf", "wb") as out:
    pdfwriter.write(out)

print("PDF file has been split")


#----Open a PDF file and save pages 3–6 into a new PDF

from PyPDF2 import PdfReader, PdfWriter
import os

pdf_file_path = "file1.pdf" # 1 Open the PDF file
pdf = PdfReader(pdf_file_path)

pdfwriter = PdfWriter() #  Create a new empty PDF

# (Remember: Python starts counting at 0)
for page_num in range(2, 6):   # 2,3,4,5 # Select pages 3–6
    pdfwriter.add_page(pdf.pages[page_num])

output_file = "newoutput.pdf" # Save the new PDF file
with open(output_file, "wb") as out:
    pdfwriter.write(out)

print("PDF file has been split successfully!")

print("Saved in folder:", os.getcwd()) # Show where the file was saved


#-------Merge 2 PDF
from PyPDF2 import PdfMerger
import os

# Create merger object
merger = PdfMerger()

# Add PDFs
merger.append("file1.pdf")
merger.append("file2.pdf")

# Write merged file
with open("merged.pdf", "wb") as f:
    merger.write(f)

# Close merger
merger.close()

print("Merged successfully!")
print("Saved in:", os.getcwd())


#-------Reads a PDF file, turns all the text into speech, and saves it as an MP3

from gtts import gTTS              # turns text into audio (speech)
from PyPDF2 import PdfReader       # reads PDF files
import os                          # helps open files using the computer

book = open("Cover.pdf", "rb")   # opens the PDF (rb = read binary)
pdfReader = PdfReader(book)        # makes a PDF reader object

pages = len(pdfReader.pages)       # counts how many pages are in the PDF
full_text = ""                     # empty string to store ALL PDF text

# loop through every page and grab the text
for num in range(pages):                   # repeat for each page number
    page = pdfReader.pages[num]            # gets one page
    text = page.extract_text()             # pulls text from that page
    if text:                               # if it found text (not blank)
        full_text += text                  # add it to full_text

book.close()

tts = gTTS(text=full_text, lang="en")  # turns the text into speech (English)
tts.save("Cover_audiobook.mp3")  # saves speech to an MP3 file

print("Playing the audiobook...")
os.system("open Cover_audiobook.mp3")   # Mac version