
import cv2
import pytesseract
from tkinter import filedialog
import PIL.Image
from PIL import ImageTk
from tkinter import *

root: Tk = Tk()
root.title('image browser')
root.filename = 'NULL'


def browse():
    global myimage, my_label, myimage_label
    root.filename = filedialog.askopenfilename(initialdir=r"\Users\hp\Desktop recognition",title="Select an image",filetypes=(("PNG FILES", ".png"), ("ALL FILES", "*.*")))
    print(root.filename)
    pytesseract.pytesseract.tesseract_cmd =r'C:\Users\hp\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
    # img = cv2.imread('GU.jpg')
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    if root.filename!='':
     #my_label = Label(root, text=root.filename).pack()
     #myimage = PIL.ImageTk.PhotoImage(PIL.Image.open(root.filename))
     #myimage_label = Label(image=myimage).pack()

     try:
       img = cv2.imread(root.filename)
     except:
        pass

    # image to string

     text = pytesseract.image_to_string(PIL.Image.open(root.filename))
     print(text)

     with open('data.txt', mode='w') as file:
         file.write(text)
     # Detecting characters
     hImg, wImg, _ = img.shape
     boxes = pytesseract.image_to_boxes(img)
     for b in boxes.splitlines():
         print(b)
         b = b.split(' ')
         print(b)
         x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
         cv2.rectangle(img, (x, hImg - y), (w, hImg - h), (50, 50, 255), 1)
         cv2.putText(img, b[0], (x, hImg - y + 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (50, 50, 255), 1)

     cv2.imshow('img', img)
     cv2.waitKey(0)


my_btn = Button(root, text="BROWSE FILE", command=browse).pack()
my_btn = Button(root, text="ABORT", command=root.destroy).pack()

root.mainloop()
