
from zipfile36 import ZipFile
import glob, os 
from PyPDF2 import PdfFileReader, PdfFileWriter
import random as r
from string import ascii_uppercase
import string
import shutil

absPath = "/Users/visveshnaraharisetty/Desktop/RandomPdfGenerator"
def ranString(length = 10):
    res = ''.join(r.choices(string.ascii_uppercase + string.digits, k = length)) 
    return res

def createFolder():
    name = ranString()
    os.system("mkdir " + absPath +  "/src/uploads/folder%s"%name) 
    return name
#------------------

def generatePdfZip(num_groups, num_pages , input_pdf):
    """
    creates the pdfs files and zips them.
    """
    path = "/Users/visveshnaraharisetty/Desktop/RandomPdfGenerator/src/uploads/folder" + createFolder() + "/"
    input_pdf = PdfFileReader(input_pdf)

    TotalPages = input_pdf.numPages

    if num_groups > 10:
        raise ValueError("The number of groups is too many")

        
    if num_pages >= TotalPages:
        raise ValueError("Select fewer pages")


    for g in range(num_groups):

        pdf_writer = PdfFileWriter()

        for i in range(num_pages):
            n = r.randrange(1, TotalPages)
            page = input_pdf.getPage(n)
            pdf_writer.addPage(page)


        with open(path + "Group%s.pdf"%(ascii_uppercase[g]), mode="wb") as output_file:
            pdf_writer.write(output_file)

    # with  ZipFile(path + 'result.zip', 'w') as zipObj: 

    #     for file in glob.glob("G*.pdf"):
    #         print(file)
    #         zipObj.write(file)
    
    # zipObj.close()
    # os.system("zip -r "  + path + "result"  )
    

    shutil.make_archive(path + 'result', 'zip', path)

    os.system("rm %sGr*.pdf"%path)
    return path



if __name__ == "__main__":
    num_groups = int(input("no. of group: "))
    num_pages = int(input("no. of pages: "))
    input_pdf = "./dump/"+ input("File path:  ")
    generatePdfZip(num_groups, num_pages ,input_pdf)

