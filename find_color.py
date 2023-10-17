import cv2
image = cv2.imread('photo.jpg')
cv2.imshow("Original", image)
# задаем границы диапазона:
# нижнюю
low_color = (0,0,150)
# и верхнюю
high_color = (130,130,255)
# наложение цветовой маски на исходное изображение,
# результат присваиваем переменной only_object
only_object = cv2.inRange(image, low_color, high_color)
# вывод отфильтрованного изображения на экран
cv2.imshow('only object', only_object)
cv2.waitKey(0)
#поиск красного
