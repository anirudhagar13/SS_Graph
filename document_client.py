import os, sys, string
import PyPDF2 as pypdf
from Commons import Pickledump, Pickleload
from compute_graph import get_words, remove_overlap_words

if __name__ == "__main__":

    file_extensions = list()
    file_text = dict()
    filenames = [sys.argv[1], sys.argv[2]]

    for i in filenames:
        file_extensions.append(os.path.splitext(i)[1])

    for i in range(0,len(filenames)):
        #file_text = dict()
        if file_extensions[i] == '.txt':
            try:
                with open(filenames[i], 'r') as f:
                    file_text[i] = list()
                    for line in f:
                        line = line.translate(None, string.punctuation)
                        tokens_2 = get_words(input_str=line,size_=2)
                        tokens_1 = get_words(input_str=line,size_=1)
                        tokens_1 = remove_overlap_words(tokens_1,tokens_2)
                        file_text[i].extend(tokens_1+tokens_2)
                    #Pickledump(file_text[i], 'file_text.pkl')
            except:
                print 'Unable to read txt file'

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

    Pickledump(file_text, 'file_text.pkl')
    '''
    #for debugging
    data = Pickleload('file_text.pkl')
    print data
    '''
