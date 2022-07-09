# インポート
import numpy as np  # numpy
import cv2  # OpenCV

# メインプログラム
img = cv2.imread("sample.jpg")

# 画像の表示
cv2.imshow("Hello World", img)
cv2.waitKey(0)

# 全てのウインドウをキル
cv2.destroyAllWindows()
