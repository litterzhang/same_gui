# -*- coding: utf-8 -*-
from PyQt5 import QtGui, QtWidgets
import time

class KillerListItemUI(QtWidgets.QWidget):
	def __init__ (self, listview, parent = None):
		super(KillerListItemUI, self).__init__(parent)
		self.ProductData = ''
		self.KillerThread = None
		self.KillerResult = dict()
		self.listview = listview
		self.listitem = None
		self.textQVBoxLayout = QtWidgets.QVBoxLayout()
		self.textUpQLabel    = QtWidgets.QLabel()
		self.textMidQLabel   = QtWidgets.QLabel()
		self.textDownQLabel  = QtWidgets.QLabel()
		self.textQVBoxLayout.addWidget(self.textUpQLabel)
		self.textQVBoxLayout.addWidget(self.textMidQLabel)
		self.textQVBoxLayout.addWidget(self.textDownQLabel)
		self.setLayout(self.textQVBoxLayout)
		# setStyleSheet
		self.textUpQLabel.setStyleSheet('''
			color: rgb(0, 0, 255);
		''')
		self.textMidQLabel.setStyleSheet('''
			color: rgb(0, 255, 0);
		''')
		self.textDownQLabel.setStyleSheet('''
			color: rgb(255, 0, 0);
		''')

	def setProductData(self, product):
		self.ProductData = product

		p_id = product.get('id', None)
		p_title = product.get('title', None)
		p_start = product.get('start_at', None)
		p_add = time.time()
		if p_id and p_title and p_start:
			self.setTextUp(p_id, p_title)
			self.setTextMid(p_add)
			self.setTextDown(p_start)

		p_list_item = QtWidgets.QListWidgetItem(self.listview)
		p_list_item.setSizeHint(self.sizeHint())
		self.listview.addItem(p_list_item)
		self.listview.setItemWidget(p_list_item, self)
		self.listitem = p_list_item

		# 开启秒杀线程线程
		
	def setTextUp(self, i, t):
		self.textUpQLabel.setText('%s %s' % (i, t))

	def setTextMid(self, t):
		self.textMidQLabel.setText('Add: %s' % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(t))))

	def setTextDown(self, t):
		self.textDownQLabel.setText('Start: %s' % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(t))))
