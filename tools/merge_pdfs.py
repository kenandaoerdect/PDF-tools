from PyPDF2 import PdfFileReader, PdfFileWriter


def merge_pdf(pdfs_path_list, outfn):
    pdf_output = PdfFileWriter()
    for infn in pdfs_path_list:
        pdf_input = PdfFileReader(open(infn, 'rb'))
        page_count = pdf_input.getNumPages()

        for i in range(page_count):
            pdf_output.addPage(pdf_input.getPage(i))

    pdf_output.write(open(outfn, 'wb'))


if __name__ == '__main__':
    pdfs = [
        '01.pdf',
        '02.pdf',
        '03.pdf',
        '04.pdf'
    ]
    outfn = 'merged.pdf'
    merge_pdf(pdfs, outfn)
