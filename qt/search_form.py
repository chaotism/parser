# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search_form.ui'
#
# Created: Tue Dec 23 13:00:44 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(653, 297)

        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(530, 20, 101, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(550, 120, 51, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.price_min = QtGui.QLineEdit(Dialog)
        self.price_min.setGeometry(QtCore.QRect(500, 150, 61, 26))
        self.price_min.setObjectName(_fromUtf8("price_min"))
        self.price_max = QtGui.QLineEdit(Dialog)
        self.price_max.setGeometry(QtCore.QRect(590, 150, 61, 26))
        self.price_max.setObjectName(_fromUtf8("price_max"))
        self.year_min = QtGui.QLineEdit(Dialog)
        self.year_min.setGeometry(QtCore.QRect(500, 50, 61, 26))
        self.year_min.setObjectName(_fromUtf8("year_min"))
        self.year_max = QtGui.QLineEdit(Dialog)
        self.year_max.setGeometry(QtCore.QRect(590, 50, 61, 26))
        self.year_max.setObjectName(_fromUtf8("year_max"))
        self.label_10 = QtGui.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(570, 50, 16, 20))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(570, 150, 16, 20))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.verticalLayoutWidget = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 151, 71))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.mark = QtGui.QComboBox(self.verticalLayoutWidget)
        self.mark.setObjectName(_fromUtf8("mark"))
        self.verticalLayout.addWidget(self.mark)
        self.verticalLayoutWidget_2 = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(170, 10, 141, 71))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.mark_folder = QtGui.QComboBox(self.verticalLayoutWidget_2)
        self.mark_folder.setObjectName(_fromUtf8("mark_folder"))
        self.verticalLayout_2.addWidget(self.mark_folder)
        self.verticalLayoutWidget_3 = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(330, 10, 151, 71))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_6 = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_3.addWidget(self.label_6)
        self.state = QtGui.QComboBox(self.verticalLayoutWidget_3)
        self.state.setObjectName(_fromUtf8("state"))
        self.verticalLayout_3.addWidget(self.state)
        self.verticalLayoutWidget_4 = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(330, 109, 151, 71))
        self.verticalLayoutWidget_4.setObjectName(_fromUtf8("verticalLayoutWidget_4"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_5 = QtGui.QLabel(self.verticalLayoutWidget_4)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_4.addWidget(self.label_5)
        self.geo_city = QtGui.QComboBox(self.verticalLayoutWidget_4)
        self.geo_city.setObjectName(_fromUtf8("geo_city"))
        self.verticalLayout_4.addWidget(self.geo_city)
        self.verticalLayoutWidget_5 = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(10, 110, 151, 71))
        self.verticalLayoutWidget_5.setObjectName(_fromUtf8("verticalLayoutWidget_5"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setMargin(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_8 = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout_5.addWidget(self.label_8)
        self.send_to = QtGui.QComboBox(self.verticalLayoutWidget_5)
        self.send_to.setObjectName(_fromUtf8("send_to"))
        self.verticalLayout_5.addWidget(self.send_to)
        self.verticalLayoutWidget_6 = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(170, 110, 141, 71))
        self.verticalLayoutWidget_6.setObjectName(_fromUtf8("verticalLayoutWidget_6"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setMargin(0)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.label_7 = QtGui.QLabel(self.verticalLayoutWidget_6)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_6.addWidget(self.label_7)
        self.period = QtGui.QComboBox(self.verticalLayoutWidget_6)
        self.period.setObjectName(_fromUtf8("period"))
        self.verticalLayout_6.addWidget(self.period)
        self.refresh = QtGui.QPushButton(Dialog)
        self.refresh.setGeometry(QtCore.QRect(60, 250, 151, 31))
        self.refresh.setObjectName(_fromUtf8("refresh"))
        self.search = QtGui.QPushButton(Dialog)
        self.search.setGeometry(QtCore.QRect(430, 250, 151, 31))
        self.search.setObjectName(_fromUtf8("search"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label_3.setText(_translate("Dialog", "Год выпуска", None))
        self.label_4.setText(_translate("Dialog", "Цена", None))
        self.label_10.setText(_translate("Dialog", "--", None))
        self.label_11.setText(_translate("Dialog", "--", None))
        self.label_2.setText(_translate("Dialog", "Марка", None))
        self.label.setText(_translate("Dialog", "Модель", None))
        self.label_6.setText(_translate("Dialog", "Состояние", None))
        self.label_5.setText(_translate("Dialog", "Город", None))
        self.label_8.setText(_translate("Dialog", "Отправить на", None))
        self.label_7.setText(_translate("Dialog", "За время", None))
        self.refresh.setText(_translate("Dialog", "Обновить данные", None))
        self.search.setText(_translate("Dialog", "Запустить поиск", None))

