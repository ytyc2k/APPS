from PIL import Image, ImageOps
if __name__ == '__main__':
    P='C:\\Users\\T180P\\Desktop\\Tong\\WixWeb\\Pictures\\'
    in_img = P+'Q10_2.jpg'
    out_img = P+'Q10_2_edit.jpg'
    img = Image.open(in_img)
    width, height = img.size
    print(width,height)
    bimg = ImageOps.expand(img, border=int(width/2), fill='white')
    bimg.save(out_img)