from pytesseract import pytesseract
from googletrans import Translator

t = Translator()
path =  r"C:\Program Files\Tesseract-OCR\tesseract.exe"
image = r'img_name.png'

pytesseract.tesseract_cmd = path_to_tesseract


img = Image.open(image)
text = pytesseract.image_to_string(img)
after_translate = t.translate(text[:-1], dest="he")


print(after_translate.text[::-1]) ### you dont have to add the [::-1] i added it because vs prints hebrew reversed
