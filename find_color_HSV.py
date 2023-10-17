import cv2
image = cv2.imread('pic.jpg')
cv2.imshow("Original", image)
# конвертируем исходное изображение в HSV,
# результат присваиваем переменной hsv_img
hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# нижняя граница — это темный ненасыщенный цвет
color_low = (0,70,50)
# верхняя граница — это яркий насыщенный цвет
color_high = (11,255,255)
# наложение цветовой маски на HSV-изображение,
# результат присваиваем переменной only_object
only_object = cv2.inRange(hsv_img, color_low, color_high)
# вывод отфильтрованного изображения на экран
cv2.imshow('color_hsv', only_object)
cv2.waitKey(0)
