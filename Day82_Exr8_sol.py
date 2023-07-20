from PyPDF2 import PdWriter
import os
merger = PdWriter()
files = [file for file in  os.listdir() if file.endwith(".pdf")]

for pdf in files:
    merger.append(pdf)
    
merger.writer("merged-pdf.pdf")
merger.close()