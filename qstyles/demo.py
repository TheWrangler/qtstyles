from qtpy import QtWidgets
from loader import StylePicker
from widget import StylePickerWidget

'''
Includes a run_demo() function that acts as a basic demo for our 
   StylePicker and StylePickerWidget classes
'''

def run_demo():
    '''
    This function provides a demonstration in changing the application style sheet.
    1) The first option is to set the style sheet once with 
       app.setStyleSheet(StylePicker("default").get_sheet())
    2) The second option is to include a style picker widget (QComboBox) that'll 
       change the application style sheet when a new style is selected 
       grid.addWidget(StylePickerWidget(), 2, 0)
    '''
    picker = StylePicker()
    
    app = QtWidgets.QApplication.instance()
    if not app:
        app = QtWidgets.QApplication([])

    win = QtWidgets.QMainWindow()
    win.setWindowTitle("Style Sheets")

    frame = QtWidgets.QFrame()
    win.setCentralWidget(frame)
    
    grid = QtWidgets.QGridLayout(frame)
    grid.setHorizontalSpacing(5)
    grid.setVerticalSpacing(5)
    grid.addWidget(QtWidgets.QLabel("Username"), 0, 0)
    grid.addWidget(QtWidgets.QLabel("Password"), 1, 0)
    grid.addWidget(QtWidgets.QLineEdit(), 0, 1)
    grid.addWidget(QtWidgets.QLineEdit(), 1, 1)
    grid.addWidget(StylePickerWidget(), 2, 0)
    grid.addWidget(QtWidgets.QPushButton("Submit"), 2, 1)
    win.show()

    app.setStyleSheet(StylePicker("default").get_sheet())
    app.exec_()

'''
def main():
    run_demo()

if __name__ == "__main__":
    main()
'''