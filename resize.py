# добавляем необходимый пакет с opencv
import cv2
# загружаем изображение
image = cv2.imread("testfile.jpg")
# задаем ширину изображения в пикселях
wide = 250
# вычисляем коэффициент, чтобы сохранить соотношение сторон
f = float(wide) / image.shape[1]
# формируем кортеж (x,y) с размерами изображения
new_size = (wide, int(image.shape[0] * f))
# изменяем изображение и возвращаем его в переменную res
res = cv2.resize(image, new_size, interpolation = cv2.INTER_AREA)
# выводим изображение res на экран в окне Resize image
cv2.imshow("Resize image", res)
# выводим изображение image на экран в окне Original
cv2.imshow("Original", image)
# ожидаем нажатия любой клавиши
cv2.waitKey(0)
