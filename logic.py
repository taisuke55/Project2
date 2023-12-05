from PyQt6.QtWidgets import *
from gui import *
import csv

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.amount_label.setVisible(False)
        self.lineEdit.setVisible(False)
        self.food_radioButton.setVisible(False)
        self.clothes_radioButton.setVisible(False)
        self.houseware_radioButton.setVisible(False)
        self.transportation_radioButton.setVisible(False)
        self.education_radioButton.setVisible(False)
        self.others_radioButton.setVisible(False)
        self.add_pushButton.setVisible(False)
        self.error_label.setVisible(True)
        self.summary_label.setVisible(False)
        self.show_pushButton.setVisible(False)

        self.changewindow_pushButton.clicked.connect(lambda:self.change_window())
        self.add_pushButton.clicked.connect(lambda:self.add())
        self.show_pushButton.clicked.connect(lambda:self.show_balance())

    def change_window(self):
        self.error_label.setText('')
        if self.summary_radioButton.isChecked():
            self.amount_label.setVisible(False)
            self.lineEdit.setVisible(False)
            self.food_radioButton.setVisible(False)
            self.clothes_radioButton.setVisible(False)
            self.houseware_radioButton.setVisible(False)
            self.transportation_radioButton.setVisible(False)
            self.education_radioButton.setVisible(False)
            self.others_radioButton.setVisible(False)
            self.add_pushButton.setVisible(False)
            self.error_label.setVisible(False)
            self.summary_label.setVisible(True)
            self.show_pushButton.setVisible(True)
            self.lineEdit.setText('')
        else:
            self.amount_label.setVisible(True)
            self.lineEdit.setVisible(True)
            self.add_pushButton.setVisible(True)
            self.summary_label.setVisible(False)
            self.show_pushButton.setVisible(False)
            self.lineEdit.setText('')
            if self.expenses_radioButton.isChecked():
                self.food_radioButton.setVisible(True)
                self.clothes_radioButton.setVisible(True)
                self.houseware_radioButton.setVisible(True)
                self.transportation_radioButton.setVisible(True)
                self.education_radioButton.setVisible(True)
                self.others_radioButton.setVisible(True)
            else:
                self.food_radioButton.setVisible(False)
                self.clothes_radioButton.setVisible(False)
                self.houseware_radioButton.setVisible(False)
                self.transportation_radioButton.setVisible(False)
                self.education_radioButton.setVisible(False)
                self.others_radioButton.setVisible(False)

    def add(self):
        try:
            self.__amount = float(self.lineEdit.text())
            if self.incomes_radioButton.isChecked():
                if self.food_radioButton.setVisible() == False:
                    self.__category = "incomes"
                else:
                    raise EOFError
            else:
                if self.food_radioButton.setVisible():
                    if self.food_radioButton.isChecked():
                        self.__category = "food"
                    elif self.clothes_radioButton.isChecked():
                        self.__category = "clothes"
                    elif self.houseware_radioButton.isChecked():
                        self.__category = "houseware"
                    elif self.transportation_radioButton.isChecked():
                        self.__category = "transportation"
                    elif self.education_radioButton.isChecked():
                        self.__category = "education"
                    else:
                        self.__category = "others"
                else:
                    raise EOFError

            self.__input = [self.__category, self.__amount]

            with open('household.csv', 'a', newline='') as csvfile:
                self.__content = csv.writer(csvfile)

                self.__content.writerow(self.__input)

            self.lineEdit.setText('')

        except ValueError:
            self.error_label.setText('The amount need to be numeric\ne.g. 10.25 not $10.25')
        except:
            self.error_label.setText('Press the button "Change window"')


    def show_balance(self):
        self.__incomes = 0.00
        self.__food = 0.00
        self.__clothes = 0.00
        self.__houseware = 0.00
        self.__transportation = 0.00
        self.__education = 0.00
        self.__others = 0.00

        with open('household.csv', 'r') as self.__csvfile:
            self.__content = csv.reader(self.__csvfile, delimiter=',')

            for self.__line in self.__content:
                if  self.__line[0] == "incomes":
                    self.__incomes = self.__incomes + float(self.__line[1])
                elif self.__line[0] == "food":
                    self.__food = self.__food + float(self.__line[1])
                elif self.__line[0] == "clothes":
                    self.__clothes = self.__clothes + float(self.__line[1])
                elif self.__line[0] == "houseware":
                    self.__houseware = self.__houseware + float(self.__line[1])
                elif self.__line[0] == "transportation":
                    self.__transportation = self.__transportation + float(self.__line[1])
                elif self.__line[0] == "education":
                    self.__education = self.__education + float(self.__line[1])
                elif self.__line[0] == "others":
                    self.__others = self.__others + float(self.__line[1])
            
        self.__total = self.__incomes - (self.__food + self.__clothes + self.__houseware + self.__transportation + self.__education + self.__others)
            
        self.summary_label.setText(f'\t\t\tSummary\nFood =\t\t\t${self.__food}\t\tIncomes =\t${self.__incomes}\nClothes =\t\t${self.__clothes}\nHouseware =\t\t${self.__houseware}\nTransportation =\t${self.__transportation}\nEducation =\t\t${self.__education}\nOthers =\t\t${self.__others}\t\tTotal =\t\t${self.__total}')