import os
import PyPDF2 as pypdf
import sys

if __name__ == "__main__":

    filenames = list()
    file_extensions = list()
    file_text = list()
    filenames.append(sys.argv[1])
    #filenames.append(sys.argv[2])
    for i in filenames:
        file_extensions.append(os.path.splitext(i)[1])
    print file_extensions

    for i in range(0,len(filenames)):
        file_text.append('')
        if file_extensions[i] == '.txt':
            try:
                with open(filenames[i], 'r') as f:
                    for line in f:
                        file_text[i] += line
            except:
                print 'Unable to open / read txt file'
        elif file_extensions[i] == '.pdf':
            try:
                pdf_file_obj = open(filenames[i],'rb')
                pdf_reader = pypdf.PdfFileReader(pdf_file_obj)
                numpages = pdf_reader.numPages
                for page in range(0,numpages):
                    page_obj = pdf_reader.getPage(page)
                    val = str(page_obj.extractText())
                    with open('output.txt', 'a') as f:
                        f.write(val)
                    file_text[i] += page_obj.extractText()
            except:
                print 'Unable to open / read pdf file'
        else:
            print 'Unsupported file type!'

    #print sys.getsizeof(file_text[0])
    #print type(file_text[0])
