import sys
from utiles import drawPatchwork
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QFormLayout, QMessageBox
from PyQt5.QtGui import QIcon

acceptableSizes = [5, 7, 9]
acceptableColours = ["red", "green", "blue", "magenta", "orange", "pink"]
abbbrevColours = ['r', 'g', 'b', 'm', 'o', 'p']

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.input_fields = []  # List to store input QLineEdit widgets

        self.init_ui()

    def init_ui(self):
        # Create widgets
        self.setWindowIcon(QIcon('Logo.png'))
        self.output_display = QLabel(self)
        self.calculate_button = QPushButton('execute', self)
        self.reverse_button = QPushButton("Reverse 'x'", self)
        self.delete_all_button = QPushButton("Delete All 'd'", self)

        # Set up layout
        layout = QVBoxLayout()

        # Form layout for main and additional input fields
        self.form_layout = QFormLayout()
        layout.addLayout(self.form_layout)
         # Adjust the spacing as needed
        self.add_text_between_fields('Sizes available are 5x5, 7x7, 9x9')
        self.add_input_field(name="Patchwork Size")
        
        self.add_text_between_fields("")
        self.add_text_between_fields('Available Colors are | red - green - blue - magenta - orange - pink |  or their abbreviations of first letter e.g. green : g')
        self.add_input_field(name="First Color")
        self.add_input_field(name="Second Color")
        self.add_input_field(name="Third Color")

        self.add_text_between_fields("")
        # Additional text between input fields
        layout.addWidget(self.output_display)
        layout.addWidget(self.calculate_button)
        layout.addWidget(self.reverse_button)
        layout.addWidget(self.delete_all_button)

        # Set up connections
        self.calculate_button.clicked.connect(self.calculate)
        self.reverse_button.clicked.connect(self.reverse)
        self.delete_all_button.clicked.connect(self.delete_all_fields)

        # Set the layout for the main window
        self.setLayout(layout)

        # Set window properties
        self.setGeometry(300, 300, 400, 200)
        self.setWindowTitle('Python Courswork')
        self.show()

    def add_input_field(self, name=None):
        if name is not None:
            input_label = QLabel(f'{name}:')
        else: input_label = QLabel(f'Input {len(self.input_fields) + 1}:')

        input_edit = QLineEdit(self)
        self.input_fields.append(input_edit)

        # Add the input field to the form layout
        self.form_layout.addRow(input_label, input_edit)
    
    def add_text_between_fields(self, text):
        # Add text label between input fields
        text_label = QLabel(text)
        self.form_layout.addRow(text_label)

    def reverse(self):
        # Get input from all QLineEdit fields
        input_texts = [input_field.text() for input_field in self.input_fields]
        size = int(input_texts[0])

        # Check if any input field is empty
        if any(input_field.text() == '' for input_field in self.input_fields):
            QMessageBox.critical(self, 'Error', 'Please fill in all input fields.', QMessageBox.Ok)
            return
        
        # Check if User entered eligible size
        if size not in acceptableSizes:
            QMessageBox.critical(self, 'Error', 'Please modify your Size input - Available Sizes (5x5 | 7x7 | 9x9)', QMessageBox.Ok)
            return
        
        if len(list(set(input_texts[1:]))) < 3:
            QMessageBox.critical(self, 'Error', "Sorry, You can't enter single color Twice", QMessageBox.Ok)
            return
        
        # All colours entered by user input.
        colourList = []
        
        for i in input_texts[1:]:
            # Check if input color is eligible
            if (i not in abbbrevColours) and (i not in acceptableColours):
                QMessageBox.critical(self, 'Error', "You entered a Color that's not eligible", QMessageBox.Ok)
                return
            
            if len(i) == 1 and i in abbbrevColours:
                colourList.append(acceptableColours[abbbrevColours.index(i)])
            elif len(i) > 1 and i in acceptableColours:
                colourList.append(i)

        colourList.reverse()
        drawPatchwork(size=size, colourList=colourList)

    def calculate(self):
        # Check if any input field is empty
        if any(input_field.text() == '' for input_field in self.input_fields):
            QMessageBox.critical(self, 'Error', 'Please fill in all input fields.', QMessageBox.Ok)
            return
        
        # Get input from all QLineEdit fields
        input_texts = [input_field.text() for input_field in self.input_fields]
        size = int(input_texts[0])

        # Check if User entered eligible size
        if size not in acceptableSizes:
            QMessageBox.critical(self, 'Error', 'Please modify your Size input - Available Sizes (5x5 | 7x7 | 9x9)', QMessageBox.Ok)
            return
        
        if len(list(set(input_texts[1:]))) < 3:
            QMessageBox.critical(self, 'Error', "Sorry, You can't enter single color Twice", QMessageBox.Ok)
            return
        
        # All colours entered by user input.
        colourList = []
        
        for i in input_texts[1:]:
            # Check if input color is eligible
            if (i not in abbbrevColours) and (i not in acceptableColours):
                QMessageBox.critical(self, 'Error', "You entered a Color that's not eligible", QMessageBox.Ok)
                return
            
            if len(i) == 1 and i in abbbrevColours:
                colourList.append(acceptableColours[abbbrevColours.index(i)])
            elif len(i) > 1 and i in acceptableColours:
                colourList.append(i)

        drawPatchwork(size=size, colourList=colourList)

    def delete_all_fields(self):
        # Delete all input fields
        for input_field in self.input_fields:
            input_field.clear()

def main():
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
