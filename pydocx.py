import glob
import os
import win32com.client

# Paths
pdfs_path = "./pdf/"
reqs_path = "./reqs/"

# Ensure output folder exists
os.makedirs(reqs_path, exist_ok=True)

# Start Word
word = win32com.client.Dispatch("Word.Application")
word.Visible = 0

# Loop through PDFs
for doc_path in glob.iglob(os.path.join(pdfs_path, "*.pdf")):
    try:
        print("Processing:", doc_path)
        filename = os.path.basename(doc_path)
        in_file = os.path.abspath(doc_path)
        out_file = os.path.abspath(os.path.join(reqs_path, filename[:-4] + ".docx"))

        wb = word.Documents.Open(in_file)
        wb.SaveAs2(out_file, FileFormat=16)  # FileFormat=16 means .docx
        wb.Close()
        print("Saved to:", out_file)

    except Exception as e:
        print("Error:", e)

# Quit Word
word.Quit()
