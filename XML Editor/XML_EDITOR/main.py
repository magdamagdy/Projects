from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
#from PyQt5.uic import loadUiType
#from pyqt5_plugins.examplebutton import QtWidgets
#from pyqt5_plugins.examplebuttonplugin import QtGui
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPlainTextEdit, QVBoxLayout
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QColor, QRegExpValidator, QSyntaxHighlighter, QTextCharFormat
from error_2 import *
from mini import *
from beautify import *
from compression import *
from decompression import*
from json_convert import*
#MainUI, _ = loadUiType('GUI.ui')

from output import Ui_MainWindow

class Main(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):  # push button hena &&& ay 7aga tab3 el ui
        super(Main, self).__init__(parent)

        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("Xml Editor")

        ####################Functions####################################
        self.fname.textChanged.connect(self.Path)
        self.browse.clicked.connect(self.browse_files)
        self.save.clicked.connect(self.file_save)
        self.get_consistant_Xml_2.clicked.connect(self.get_consistant_Xml)
        self.minify_2.clicked.connect(self.minify)
        self.prettify_2.clicked.connect(self.prettify)
        self.convert_to_json_2.clicked.connect(self.convert_to_json)
        self.compress_2.clicked.connect(self.compress)
        self.decompress.clicked.connect(self.decompress_file)


    def Path(self):
        p = self.fname.text()

    def browse_files (self):
        filename=QFileDialog.getOpenFileName(self, 'Open file', 'D:', 'All Files(*.*)')
        self.fname.setText(filename[0])
        if filename[0]:
            f = open(filename[0], 'r')
            with f:
                data = f.read()
                self.original_file_2.setPlainText(data)



    def file_save(self):
        with open(filename2, "r") as f:
            transcript = f.readlines()
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File", "",
                                                  "XML files (*.xml);;JSON files (*.json);;Text files (*.txt);;All Files(*.*) ")
        with open(filePath, 'w') as f:
            #print(filePath)
            #print ("trans",transcript)
            for line in transcript:
                f.write(line)
        f.close()

    def get_consistant_Xml(self):
        p = self.fname.text()
        filename2,error_list= caller(p)
        f = open(filename2, "r")
        with f:
            data = f.read()
            self.after_mod_2.setPlainText(data)
        with open(filename2, "r") as f:
            transcript = f.readlines()
        if error_list != "":
            h=0
            error =''
            while h<(len(error_list)):
                index = error_list[h][1]
                error += 'Error around line number '+ str(index+1)+'\n'

                #line=transcript[index]
                #self.after_mod_2.insert(line.setBackground(QColor('yellow')))
                #line.setBackground(QColor('yellow'))
                h+=1
            self.textEdit.setText(error)

    def minify(self):
        p = self.fname.text()
        filename2 = caller2(p)
        f = open(filename2, "r")
        with f:
            data = f.read()
            self.after_mod_2.setPlainText(data)

    def prettify(self):
        p = self.fname.text()
        filename2 = caller3(p)
        f = open(filename2, "r")
        with f:
            data = f.read()
            self.after_mod_2.setPlainText(data)

    def compress(self):
        p = self.fname.text()
        filename2 = caller4(p)

    def decompress_file(self):
        p = self.fname.text()
        filename2 = caller5()
        f = open(filename2, "r")
        with f:
            data = f.read()
            self.after_mod_2.setPlainText(data)

    def convert_to_json(self):
        p = self.fname.text()
        filename2 = caller6(p)
        f = open(filename2, "r")
        with f:
            data = f.read()
            self.after_mod_2.setPlainText(data)



######################################
#filename='data.adj.xml'

#def open_file(filename):
 #   with open(filename,"r") as f:
  #      transcript = f.readlines()
   #     return transcript


#######################################
def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
