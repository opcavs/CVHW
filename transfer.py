import cv2
img = Image.open('./resource/school.jpg')
print(img.size)
#box=(112,83,112,83)
box=(10,10,10,10)
img=img.crop(box)
img.save('out.jpg')