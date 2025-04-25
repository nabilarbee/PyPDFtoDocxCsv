import pdfplumber
import pandas as pd

multipleHeaders = False

if multipleHeaders:

    pgsToSplit = []
    print("Multiple headers detected")
else:
    dataTable = []
    with pdfplumber.open("./pdfs/dummy_spreadsheet.pdf") as pdf:
        for page in pdf.pages:
            dataTable = page.extract_table()













# setting header to the first row, and starting the second row, it will be as table data
# dFrame = pd.DataFrame(dataTable[1:], columns=dataTable[0])
# dFrame.to_csv("output.csv", index=False)
# print("CSV saved as output.csv")


# full_text = ""
# with pdfplumber.open("./pdfs/file-example_PDF_500_kB.pdf") as pdf:
#     for page in pdf.pages:
#         full_text += page.extract_text() + "\n"
#
# print(full_text)