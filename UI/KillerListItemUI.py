# -*- coding: utf-8 -*-
from PyQt5 import QtGui, QtWidgets
import time
import threading
from concurrent.futures import ThreadPoolExecutor
from requests_futures.sessions import FuturesSession
import utils.auth as AUTH
import utils.windows as WINDOWS
from settings import KILLER_URL, ADDRESS_ID

class KillerListItemUI(QtWidgets.QWidget):
	def __init__ (self, listview, console=None, parent = None):
		super(KillerListItemUI, self).__init__(parent)
		self.ProductData = ''
		self.KillerThread = None
		self.ThreadRun = False
		self.KillerResult = dict()
		self.listview = listview
		self.listitem = None
		self.console = console
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
		self.KillerThread = threading.Thread(target=self.__killer_thread, args=())
		self.ThreadRun = True
		self.KillerThread.start()

	def stopKiller(self):
		p_id = self.ProductData.get('id', None)
		self.printf('移除秒杀任务 %s' % p_id)
		self.ThreadRun = False
		WINDOWS._killer_list.remove(p_id)

		# 移除秒杀任务
		if self.listitem:
			self.listview.removeItemWidget(self.listitem)
			self.listview.takeItem(self.listview.row(self.listitem))
			self.listitem = None

	def printf(self, msg):
		if self.console:
			try:
				self.console.append(msg)
			except Exception as e:
				pass
		else:
			print(msg)

	def setTextUp(self, i, t):
		self.textUpQLabel.setText('%s %s' % (i, t))

	def setTextMid(self, t):
		self.textMidQLabel.setText('Add: %s' % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(t))))

	def setTextDown(self, t):
		self.textDownQLabel.setText('Start: %s' % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(t))))

	def __killer_cb(self, session, res):
		try:
			res.encoding = 'utf-8'
			res.code = res.json().get('code', -1)
		except:
			res.code = -1

	def __killer_thread(self):
		while self.ThreadRun:
			try:
				p_id = self.ProductData.get('id', None)
				p_start = int(self.ProductData.get('start_at', time.time()))
				# p_start = time.time() + 5
				self.printf('添加秒杀任务 %s %s' % (p_id, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(p_start)))))
				
				#开始秒杀多线程秒杀
				f_session = FuturesSession(executor=ThreadPoolExecutor(max_workers=50), session=AUTH._session)
				data = {'product_id': p_id, 'address_id': ADDRESS_ID}
				res = list()

				# 休眠到开始时间前的一小段时间
				while self.ThreadRun and time.time() < p_start-10:
					time.sleep(9)

				if self.ThreadRun:
					self.printf('开始秒杀任务 %s' % p_id)

				# 休眠到精细时间
				while self.ThreadRun and time.time() < p_start-0.1:
					time.sleep(0.1)

				while self.ThreadRun and time.time() < p_start-0.01:
					pass

				if self.ThreadRun:
					self.printf('%s 开始发送秒杀时间 %s' % (p_id, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))))
					# 请求post数据
					for i in range(300):
						res.append(f_session.post(KILLER_URL, auth=AUTH._auth, data=data, background_callback=self.__killer_cb))
					self.printf('%s 结束发送秒杀时间 %s' % (p_id, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))))

					# 处理秒杀结果
					res_code = dict()
					for r in res:
						code = r.result().code
						res_code[code] = res_code.get(code, 0) + 1

					# 显示秒杀结果
					self.printf('完成秒杀任务 %s\n秒杀结果:' % p_id)
					for k, v in res_code.items():
						self.printf('结果: %s, 次数: %s' % (k, v))

					self.ThreadRun = False

					# 移除秒杀任务
					if self.listitem:
						self.listview.removeItemWidget(self.listitem)
						self.listview.takeItem(self.listview.row(self.listitem))
						self.listitem = None

						WINDOWS._killer_list.remove(p_id)
			except Exception as e:
				self.printf(e)



