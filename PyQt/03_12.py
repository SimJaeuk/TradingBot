import sys
from PyQt5.QtWidgets import *
# from PyQt5.QtGui import QIcon

app = QApplication(sys.argv)            # QApplication 객체 생성

label = QLabel("Hello")
label.show()

app.exec_()                             # 이벤트 루프 생성

