import random
import string
import pyperclip

from PyQt5 import QtWidgets, QtGui

class PasswordGenerator(QtWidgets.QWidget):
  def __init__(self):
    super().__init__()
    
    # Set up the user interface
    self.initUI()
  
  def initUI(self):
    # Create a spin box to allow the user to specify the password length
    self.lengthSpinBox = QtWidgets.QSpinBox(self)
    self.lengthSpinBox.setRange(8, 16)
    self.lengthSpinBox.setValue(8)
    
    # Create a button to generate a new password
    self.generateButton = QtWidgets.QPushButton("Generate", self)
    self.generateButton.clicked.connect(self.generatePassword)
    
    # Create a text field to display the generated password
    self.passwordField = QtWidgets.QLineEdit(self)
    self.passwordField.setReadOnly(True)
    
    # Create a "Copy" button
    self.copyButton = QtWidgets.QPushButton("Copy", self)
    self.copyButton.clicked.connect(self.copyPassword)
    
    # Create a layout to hold the widgets
    layout = QtWidgets.QHBoxLayout(self)
    layout.addWidget(self.lengthSpinBox)
    layout.addWidget(self.generateButton)
    layout.addWidget(self.passwordField)
    layout.addWidget(self.copyButton)
    
    # Set the window properties
    self.setGeometry(300, 300, 400, 150)
    self.setWindowTitle("Password Generator")
    self.show()
  
  def generatePassword(self):
    # Get the password length from the spin box
    length = self.lengthSpinBox.value()
    
    # Generate a random password
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
    
    # Display the password in the text field
    self.passwordField.setText(password)
  
  def copyPassword(self):
    # Copy the password to the clipboard
    password = self.passwordField.text()
    pyperclip.copy(password)

if __name__ == '__main__':
  app = QtWidgets.QApplication([])
  generator = PasswordGenerator()
  app.exec_()
