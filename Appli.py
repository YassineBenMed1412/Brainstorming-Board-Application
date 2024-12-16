import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPainter,QIcon


class ImageLabel(QLabel):
    def __init__(self):
        super().__init__()
      
        self.setAlignment(Qt.AlignCenter)
        self.setText('Start Brainstorming! Drop Images Here!')
        self.setStyleSheet('''
            QLabel {
                border: 4px dashed #aaa;
                color: #64EEFA to #124CA2;
                font-size: 16px;
                padding: 4 px;
            }
             QWidget {
           background: qlineargradient(
            spread: pad, 
            x1: 0, y1: 0, x2: 1, y2: 1, 
            stop: 0 #64EEFA, 
            stop: 1 #124CA2
        );
    }
        
        ''')


class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('icon.ico'))
        self.setWindowTitle("Reference Board !")
        self.resize(600, 600)
        self.setAcceptDrops(True)

        self.images = []  
        self.image_positions = []

        
        self.mainLayout = QVBoxLayout()
        self.image_label = ImageLabel()
        self.mainLayout.addWidget(self.image_label)
        self.setLayout(self.mainLayout)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            for url in event.mimeData().urls():
                file_path = url.toLocalFile()
                pixmap = QPixmap(file_path)
                if not pixmap.isNull():
                    
                    self.images.append(pixmap)
                    self.image_positions.append((len(self.images) * 20, len(self.images) * 20))  #
            self.update()  

    def paintEvent(self, event):
        super().paintEvent(event)
        if self.images:
            painter = QPainter(self)
            for i, pixmap in enumerate(self.images):
                x, y = self.image_positions[i]
                painter.drawPixmap(x, y, pixmap)



app = QApplication(sys.argv)
demo = AppDemo()
demo.show()
sys.exit(app.exec_())
