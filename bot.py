from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QObject
from PyQt5.QtCore import QThread
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWinExtras import QtWin
import sys
from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Window(QMainWindow):
	def __init__(self):
		self.BetObj = None
		self.Coins = 0
		super().__init__()
		self.setObjectName("Window")
		self.resize(699, 459)
		self.setAutoFillBackground(False)
		self.centralwidget = QtWidgets.QWidget(self)
		self.centralwidget.setObjectName("centralwidget")
		self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
		self.verticalLayout_4.setObjectName("verticalLayout_4")
		self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_5.setObjectName("horizontalLayout_5")
		self.verticalLayout_2 = QtWidgets.QVBoxLayout()
		self.verticalLayout_2.setObjectName("verticalLayout_2")
		self.horizontalLayout = QtWidgets.QHBoxLayout()
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.spinBox.sizePolicy().hasHeightForWidth())
		self.spinBox.setSizePolicy(sizePolicy)
		self.spinBox.setObjectName("spinBox")
		self.horizontalLayout.addWidget(self.spinBox)
		self.label = QtWidgets.QLabel(self.centralwidget)
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.label.setFont(font)
		self.label.setObjectName("label")
		self.horizontalLayout.addWidget(self.label)
		spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout.addItem(spacerItem)
		self.verticalLayout_2.addLayout(self.horizontalLayout)
		self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_6.setObjectName("horizontalLayout_6")
		self.comboBox = QtWidgets.QComboBox(self.centralwidget)
		self.comboBox.setObjectName("comboBox")
		self.comboBox.addItem("")
		self.comboBox.addItem("")
		self.horizontalLayout_6.addWidget(self.comboBox)
		spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_6.addItem(spacerItem1)
		self.verticalLayout_2.addLayout(self.horizontalLayout_6)
		self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_4.setObjectName("horizontalLayout_4")
		self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton_2.setObjectName("pushButton_2")
		self.horizontalLayout_4.addWidget(self.pushButton_2)
		self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton_3.setObjectName("pushButton_3")
		self.horizontalLayout_4.addWidget(self.pushButton_3)
		spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_4.addItem(spacerItem2)
		self.verticalLayout_2.addLayout(self.horizontalLayout_4)
		spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.verticalLayout_2.addItem(spacerItem3)
		self.horizontalLayout_5.addLayout(self.verticalLayout_2)
		spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_5.addItem(spacerItem4)
		self.verticalLayout_3 = QtWidgets.QVBoxLayout()
		self.verticalLayout_3.setObjectName("verticalLayout_3")
		self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_2.setObjectName("horizontalLayout_2")
		spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_2.addItem(spacerItem5)
		self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.spinBox_2.sizePolicy().hasHeightForWidth())
		self.spinBox_2.setSizePolicy(sizePolicy)
		self.spinBox_2.setObjectName("spinBox_2")
		self.horizontalLayout_2.addWidget(self.spinBox_2)
		self.label_2 = QtWidgets.QLabel(self.centralwidget)
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.label_2.setFont(font)
		self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.label_2.setObjectName("label_2")
		self.horizontalLayout_2.addWidget(self.label_2)
		self.verticalLayout_3.addLayout(self.horizontalLayout_2)
		self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_3.setObjectName("horizontalLayout_3")
		spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_3.addItem(spacerItem6)
		self.pushButton = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton.setObjectName("pushButton")
		self.horizontalLayout_3.addWidget(self.pushButton)
		self.verticalLayout_3.addLayout(self.horizontalLayout_3)
		self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_7.setObjectName("horizontalLayout_7")
		spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_7.addItem(spacerItem7)
		self.label_3 = QtWidgets.QLabel(self.centralwidget)
		self.label_3.setMinimumSize(QtCore.QSize(0, 0))
		self.label_3.setObjectName("label_3")
		self.horizontalLayout_7.addWidget(self.label_3)
		self.verticalLayout_3.addLayout(self.horizontalLayout_7)
		spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.verticalLayout_3.addItem(spacerItem8)
		self.horizontalLayout_5.addLayout(self.verticalLayout_3)
		self.verticalLayout = QtWidgets.QVBoxLayout()
		self.verticalLayout.setSpacing(0)
		self.verticalLayout.setObjectName("verticalLayout")
		self.horizontalLayout_5.addLayout(self.verticalLayout)
		self.verticalLayout_4.addLayout(self.horizontalLayout_5)
		self.setCentralWidget(self.centralwidget)

		self.ConfigUi()
		QtCore.QMetaObject.connectSlotsByName(self)

	def ConfigUi(self):
		self.setWindowTitle("Polygon bot by Shersula")
		self.setWindowIcon(QtGui.QIcon("ico.ico"))

		QtWin.setCurrentProcessExplicitAppUserModelID('Bot by Shersula')

		self.label.setText("Ставка")
		self.comboBox.setItemText(0, "Черный")
		self.comboBox.setItemText(1, "Красный")
		self.pushButton_2.setText("Старт")
		self.pushButton_3.setText("Стоп")
		self.label_2.setText("Количество ставок")
		self.pushButton.setText("Рассчитать")
		self.label_3.setText("")

		self.spinBox.setRange(1, 10000)
		self.spinBox_2.setRange(1, 15)

		self.pushButton.clicked.connect(self.Calculate)
		self.pushButton_2.clicked.connect(self.StartBrowser)
		self.pushButton_3.clicked.connect(self.StopBrowser)
		self.pushButton_3.setEnabled(False)

	def closeEvent(self, event):
		if self.BetObj != None: self.StopBrowser()

	def StopBrowser(self):
		self.BetObj.StopBtn = True
		self.label_3.setText(string + "\nКнопка старт станет доступна после закрытия окна браузера\nПеред тем как кнопка станет активна потребуется некоторое время\nчтобы бот завершил очистку всей системной информации")

	def ClearBet(self):
		if self.BetObj.StopBtn == True:
			del self.thread
			self.thread = None
			del self.BetObj
			self.BetObj = None
			self.pushButton_2.setEnabled(True)
			self.pushButton_3.setEnabled(False)

	def StartBrowser(self):
		if self.BetObj != None:
			self.BetObj.StopBtn = False
			try:
				if self.BetObj.driver.current_window_handle == self.BetObj.handle: pass
			except (exceptions.NoSuchWindowException, exceptions.WebDriverException, exceptions.ClosedPoolError): self.thread.start()
		else:
			self.BetObj = Bet()
			self.thread = QThread()
			self.BetObj.moveToThread(self.thread)
			self.thread.started.connect(self.BetObj.StartBet)
			self.thread.finished.connect(self.ClearBet)
			self.thread.start()
			self.pushButton_2.setEnabled(False)
			self.pushButton_3.setEnabled(True)

	def Calculate(self):
		if self.spinBox.value() <= 0: self.label_3.setText("Ставка слишком низкая")
		global string
		string = "Ставки:"
		summ = 0
		for i in range(self.spinBox_2.value()):
			string += "\n" + str(i+1) + " ставка: " + str(self.spinBox.value()*(2**i)) + " coin"
			summ += self.spinBox.value()*(2**i)

		string += "\nВсего нужно: " + str(summ) + " coin"
		self.label_3.setText(string)
		
class Bet(QObject):
	def __init__(self):
		super(Bet, self).__init__()
		#From Yandex Browser
		self.options = webdriver.ChromeOptions()
		self.path = Service('yandexdriver.exe')

		#From Chrome Browser
		"""
		self.options = webdriver.ChromeOptions()
		"""

		#From Edge Browser
		"""
		self.options = webdriver.EdgeOptions()
		"""

		#From Firefox Browser
		"""
		self.options = webdriver.FirefoxOptions()
		"""

		#From Internet Explorer Browser
		"""
		self.options = webdriver.IEOptions()
		"""
		
		self.driver = None
		self.LoopTimer = None
		self.StopBtn = False
		self.Bet = False
		self.LastBet = 0
		self.LastBetSet = False

	def StartBet(self):
		self.UserName = "tyskie2016"
		self.Password = "Warning2002"

		if self.driver != None:
			del self.driver
			self.driver = None

		#From Yandex Browser
		self.driver = webdriver.Chrome(service=self.path, options=self.options)

		#From Chrome Browser
		"""
		self.driver = webdriver.Chrome(options=self.options)
		"""

		#From Edge Browser
		"""
		self.driver = webdriver.Edge(options=self.options)
		"""

		#From Firefox Browser
		"""
		self.driver = webdriver.Firefox(options=self.options)
		"""

		#From Internet Explorer Browser
		"""
		self.driver = webdriver.Ie(options=self.options)
		"""

		self.driver.get('https://csgopolygon.gg')
		self.handle = self.driver.current_window_handle

		if self.LoopTimer != None:
			del self.LoopTimer
			self.LoopTimer = None
		self.LoopTimer = QTimer()
		self.LoopTimer.timeout.connect(self.Loop)

		self.LoopTimer.start(500)

		#element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@class='textField'][@type='text'][@name='username'][@id='steamAccountName']")))
	
	def Loop(self):
		try:
			if self.driver.current_window_handle == self.handle: pass
		except (exceptions.NoSuchWindowException, exceptions.WebDriverException):
			if self.StopBtn == True:
				if self.LoopTimer != None:
					self.LoopTimer.stop()
					del self.LoopTimer
					self.LoopTimer = None

				if self.driver != None:
					self.driver.quit()
					del self.driver
					self.driver = None
				self.thread().exit()
			else:
				self.driver.quit()
				if self.driver != None:
					del self.driver
					self.driver = None
				self.driver = webdriver.Chrome(service=self.path, options=self.options)
				self.driver.get('https://csgopolygon.gg')
				self.handle = self.driver.current_window_handle
		if self.StopBtn != True:
			try:
				element = self.driver.find_element(By.XPATH, '//div[@class="user"]')
				element = self.driver.find_element(By.XPATH, '//b[@id="balance_r"]').text



				window.label_3.setText(string + "\nБаланс: " + element)
				window.label_3.setText(string + "\nБаланс: " + element + "\nЗаработано за пероид работы бота: " + str(window.Coins))

				if window.comboBox.currentIndex() == 0: #black
					if self.Bet == False:
						element = self.driver.find_element(By.XPATH, "//*[@id='select_roulette']/div[1]/div[1]/span")
						if element.text != "***ROLLING***":
							element = self.driver.find_element(By.XPATH, "//*[@id='black_bets_my']/span")
							if(element.text == "0"):
								element = self.driver.find_element(By.XPATH, "//input[@type='text'][@id='roulette_amount']")
								element.clear()
								if self.LastBet == 0: element.send_keys(str(window.spinBox.value()))
								else: element.send_keys(str(self.LastBet))

								element = self.driver.find_element(By.XPATH, "//button[@type='button'][@name='button'][@class='dark_button betButton']")
								element.click()

								element = self.driver.find_element(By.XPATH, "//*[@id='black_bets_my']/span")
							else:
								self.Bet = True
								if self.LastBet == 0: self.LastBet = window.spinBox.value()
					else:
						element = self.driver.find_element(By.XPATH, "//*[@id='black_bets_my']/span")
						if element.text.find("+") != -1 and self.LastBetSet == False:
							self.LastBet = 0
							window.Coins += window.spinBox.value()
							self.LastBetSet = True
						elif element.text.find("-") != -1 and self.LastBetSet == False:
							self.LastBet *= 2
							self.LastBetSet = True
						elif(element.text == "0"):
							self.driver.get('https://csgopolygon.gg')
							self.Bet = False
							self.LastBetSet = False

				elif window.comboBox.currentIndex() == 1: #red
					if self.Bet == False:
						element = self.driver.find_element(By.XPATH, "//*[@id='select_roulette']/div[1]/div[1]/span")
						if element.text != "***ROLLING***":
							element = self.driver.find_element(By.XPATH, "//*[@id='red_bets_my']/span")
							if(element.text == "0"):
								element = self.driver.find_element(By.XPATH, "//input[@type='text'][@id='roulette_amount']")
								element.clear()
								if self.LastBet == 0: element.send_keys(str(window.spinBox.value()))
								else: element.send_keys(str(self.LastBet))

								element = self.driver.find_element(By.XPATH, "//button[@type='button'][@name='button'][@class='red_button betButton']")
								element.click()

								element = self.driver.find_element(By.XPATH, "//*[@id='red_bets_my']/span")
							else:
								self.Bet = True
								if self.LastBet == 0: self.LastBet = window.spinBox.value()
					else:
						element = self.driver.find_element(By.XPATH, "//*[@id='red_bets_my']/span")
						if element.text.find("+") != -1 and self.LastBetSet == False:
							self.LastBet = 0
							window.Coins += window.spinBox.value()
							self.LastBetSet = True
						elif element.text.find("-") != -1 and self.LastBetSet == False:
							self.LastBet *= 2
							self.LastBetSet = True
						elif(element.text == "0"):
							self.driver.get('https://csgopolygon.gg')
							self.Bet = False
							self.LastBetSet = False

			except exceptions.NoSuchElementException:
				window.label_3.setText(string + "\nДля запуска бота вам нужно авторизироваться")

def Application():
	app = QApplication(sys.argv)
	global window
	window = Window()
	window.Calculate()

	window.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	Application()