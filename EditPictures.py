from PIL import Image, ImageOps
if __name__ == '__main__':
    in_img = 'Medallion_pic1.jpg'
    in_img = 'Medallion_pic1_back.jpg'
    out_img = 'butterfly_border_indianred.jpg'
    img = Image.open(in_img)
    width, height = img.size
    print(width,height)
    bimg = ImageOps.expand(img, border=int(width/2), fill='white')
    bimg.save(out_img)