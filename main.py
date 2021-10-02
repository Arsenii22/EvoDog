from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from ui import Ui_MainWindow
import sys
import random
import os

os.remove("sobaki.db")

import data



app = QApplication(sys.argv)
Form = QWidget()
ui = Ui_MainWindow()
ui.setupUi(Form)
Form.show()


data.sd(3)


data.s({'h':[0.2,0,0,0],'rd':[1,0,0]})
data.s({'h':[0.3,0,0,0],'rd':[0,1,0]})
data.s({'h':[0.75,0,0,0],'rd':[0,0,1]})
data.z()
import math

pogr = 0.005

table = data.vv()
print(table)


def ozenka(char1,charn):
	k=0
	for i in range(len(char1)):
		k+=math.fabs(charn[i]-char1[i])
	return k

def scrst(sob1,sob2):
	sob3={
		'rd' : [],
		'h' : []
	}

	for i in range(len(sob1['rd'])):
		sob3['rd'].append((sob1['rd'][i]+sob2['rd'][i])/2)

	for i in range(len(sob1['h'])):
		sob3['h'].append((sob1['h'][i]+sob2['h'][i])/2)

	return sob3

def ifrod(sob1,sob2):
	vos=True
	for i in range(len(sob1['rd'])):
		if sob1['rd'][i] > 0.1 and sob2['rd'][i] > 0.1 and math.fabs(sob1['rd'][i]-sob2['rd'][i])<0.1:
			
			vos=False
			break
	return vos


def search(char):
	table2=[]
	klm=[]

	l=0
	vos=True
	tekm2={}
	while vos:
		if l>=3:
			break
		for i in range(len(table)):
			for j in range(len(table)):
				if not (str(i)+'00000'+str(j)) in klm and ifrod(table[i],table[j]):
					klm.append(str(i)+'00000'+str(j))
					klm.append(str(j)+'00000'+str(i))
					tek=scrst(table[i],table[j])
					tek['roditeli']=[i,j]
					oz=ozenka(tek['h'],char)
					if oz < 5:
						table2.append(tek)
					if oz<pogr:
						tekm2=tek
						print("fdo")
						vos=False
						break
			if not vos:
				break
		for i in table2:
			table.append(i)
		table2=[]
		l+=1
	rodich=[]
	print(tekm2)

	def rod(tek):
		try:
			print(tek)
			if tek['roditeli']:
				rodich.append(tek['roditeli'])
				rod(table[tek['roditeli'][0]])
				rod(table[tek['roditeli'][1]])
		except:
			pass
	rod(tekm2)

	rodich.reverse()
	return [rodich, l]

m_choice = []
fem_choice = []

for i in data.vv():
	m_choice.append(QRadioButton(f"Собака {i['ind']}"))
	fem_choice.append(QRadioButton(f"Собака {i['ind']}"))
	ui.males_list.setItemWidget(QListWidgetItem(ui.males_list), m_choice[i['ind'] - 1])
	ui.females_list.setItemWidget(QListWidgetItem(ui.females_list), fem_choice[i['ind'] - 1])

def get_data():
	ch = [ui.spinBox_first.value() / 1000, ui.spinBox_second.value() / 1000, ui.spinBox_third.value() / 1000, ui.spinBox_fourth.value() / 1000]
	res = search(ch)
	msgBox = QMessageBox()
	msgBox.setIcon(QMessageBox.Information)
	text = f'''
Чтобы вывести эту породу вам примерно понадобится {res[1]} лет(года)
И вам надо будет скрестить:
	'''
	for i in res[0]:
		text += f'''
{i[0] + 1} и {i[1] + 1} собаку, тогда получится собака {2 + i[1]}
		'''

	msgBox.setText(text)
	msgBox.setWindowTitle("Выведение породы")
	msgBox.setStandardButtons(QMessageBox.Ok)
	msgBox.exec()

def get_child():
	for i in range(len(m_choice)):
		if m_choice[i].isChecked():
			dog1 = data.vn(i)

	for i in range(len(fem_choice)):
		if fem_choice[i].isChecked():
			dog2 = data.vn(i)

	if dog1 == dog2:
		msgBox = QMessageBox()
		msgBox.setIcon(QMessageBox.Critical)
		text = f'''Нельзя скрестить собаку саму с собой'''
		msgBox.setText(text)
		msgBox.setWindowTitle("Ошибка")
		msgBox.setStandardButtons(QMessageBox.Ok)
		msgBox.exec()
	else:
		dog3 = scrst(dog1, dog2)

		msgBox = QMessageBox()
		msgBox.setIcon(QMessageBox.Information)
		text = f'''
У щенка данных родителей будет:
Острота слуха - {int(dog3['h'][0] * 1000)} из 1000,
Длина шерсти - {int(dog3['h'][1] * 1000)} из 1000,
Размер хвоста - {int(dog3['h'][2] * 1000)} из 1000,
Размер туловища - {int(dog3['h'][3] * 1000)} из 1000.
		'''
		msgBox.setText(text)
		msgBox.setWindowTitle("Щенок")
		msgBox.setStandardButtons(QMessageBox.Ok)
		msgBox.exec()

ui.submit.clicked.connect(get_data)
ui.submit_2.clicked.connect(get_child)
sys.exit(app.exec_())