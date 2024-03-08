from PIL import Image, ImageOps

"""Изменение размера"""
image = Image.open("osen-park-skameika-autumn-fall-colors-park.jpg")
new_size = (100, 100)

resized_image = image.resize(new_size)
resized_image.save("resized_osen-park-skameika-autumn-fall-colors-park.jpg")



"""Преобразование изображения в черно-белое"""
image = Image.open("osen-park-skameika-autumn-fall-colors-park.jpg")

grayscale_image = ImageOps.grayscale(image)
grayscale_image.save("grayscale_osen-park-skameika-autumn-fall-colors-park.jpg")





import requests

r = requests.get('https://ya.ru/')
print(r)




import numpy as np
a = np.array([20, 30, 40, 50])
b = np.arange(1, 5)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a ** b)
print(a % b)






import numpy as np
import matplotlib.pyplot as plt

phi = np.linspace(0, 2.*np.pi, 100)
plt.plot(phi, np.sin(phi))
plt.plot(phi, np.cos(phi))

plt.show()
plt.close()