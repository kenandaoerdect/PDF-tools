from PyPDF2 import PdfFileReader, PdfFileWriter


def split_pdf_by_page(infn, startpage, endpage):
    pdf_output = PdfFileWriter()
    pdf_input = PdfFileReader(open(infn, 'rb'))
    page_count = pdf_input.getNumPages()
    outfn_name = "".join(infn.split(".")[:-1])

    if startpage > endpage:
        print("startpage > endpage")
        return
    if endpage > page_count:
        print("endpage > page_count")
        return

    for i in range(startpage, endpage):
        pdf_output.addPage(pdf_input.getPage(i))
    pdf_output.write(open(outfn_name+"_"+str(startpage)+"-"+str(endpage)+".pdf", "wb"))


def split_pdf_by_nums(infn, outfnnum=2):
    if outfnnum < 2:
        print("outfnnum must > 1")
        return
    pdf_input = PdfFileReader(open(infn, 'rb'))
    page_count = pdf_input.getNumPages()

    outfn_page = page_count // outfnnum

    for num in range(1, outfnnum + 1):
        pdf_output = PdfFileWriter()
        outfn_name = "".join(infn.split(".")[:-1]) + "_" + str(num) + ".pdf"
        for i in range(outfn_page * (num - 1), outfn_page * num if num != outfnnum else page_count):
            pdf_output.addPage(pdf_input.getPage(i))
        pdf_output.write(open(outfn_name, 'wb'))

if __name__ == '__main__':
    infn = "sample.pdf"
    split_pdf_by_page(infn, 0, 20)
    # split_pdf_by_nums(infn, 5)
