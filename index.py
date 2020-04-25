from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
okunan=pytesseract.image_to_string(Image.open('1.jpg'), lang="tur")
print(okunan)