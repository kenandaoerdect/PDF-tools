import fitz
import os

doc = fitz.open('sample.pdf')
save_img_path = 'img/'

if not os.path.exists(save_img_path):
    os.mkdir(save_img_path)

for pg in range(doc.pageCount):
    page = doc[pg]
    rotate = int(0)
    zoom_x = 4.0
    zoom_y = 4.0
    trans = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
    pm = page.getPixmap(matrix=trans, alpha=False)
    pm.writePNG(save_img_path+'%03d.png' % int(pg))
