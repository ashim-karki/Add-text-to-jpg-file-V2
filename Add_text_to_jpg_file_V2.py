# Importing the PIL library 
# from typing import List, Tuple
from PIL import Image 
from PIL import ImageDraw 
from PIL import ImageFont 
# from tkinter.font import Font
import csv

with open('your_data_file.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

#Font for 1
myFont1 = ImageFont.truetype(r'Proxima.otf', 140)

#Font for 2
myFont2 = ImageFont.truetype(r'Proxima.otf', 140)

#Font for 3
myFont3 = ImageFont.truetype(r'Proxima.otf', 140)

#You can add as many fonts as you want in similar manner

for i in range(1,len(data)):
    img = Image.open(r'your_template_file.jpg') 
    I1 = ImageDraw.Draw(img) 
    img2 = Image.open('Images/' + data[i][0] + '.jpg') # make sure to add all images in images folder
    img2 = img2.resize((500, 500)) # resize the image to your requirement
    I1.text((1450, 365), data[i][0], font=myFont1, fill =(255, 255, 255)) # this can't be used in a for loop
    I1.text((1650, 465), data[i][1], font=myFont2, fill =(255, 255, 255)) 
    I1.text((1200, 465), data[i][2], font=myFont3, fill =(255, 255, 255))
    #I1.text((1200, 465), data[i][2], font=myFont2, fill =(255, 255, 255)) add as many texts you want in similar manner
    img.paste(img2, (130,778))
    img.save('Final/' + data[i][0] + '.jpg') # all the final templates will be saved in Final folder

