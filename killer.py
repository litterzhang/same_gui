#!D:\Python34\python.exe
# -*- coding: utf-8 -*-

'same登录'

__author__ = 'litter_zhang'

from PyQt5 import QtWidgets
from UI.KillerUI import KillerUI
from settings import SENSES_URL, ADDRESS_ID, KILLER_URL
import auth as AUTH
import lists as LIST
from threadpool import ThreadPool, makeRequests
import threading

class killer_win(QtWidgets.QMainWindow, KillerUI):
	def __init__(self):
		super(killer_win, self).__init__()
		self.setupUi(self)
		self.Add.clicked.connect(self.start_killer)

		products = load_product_list()
		for product in products:
			self.SameProductList.addItem(product)

	def start_killer(self):
		t = threading.Thread(target=killer_thread, args=(1, 1))
		t.start()

#统计秒杀请求结果
def killer_callback(req, code):
	pass

#秒杀请求
def killer_req(url, data):
	print('hello')

#秒杀
def killer_thread(product_id, start_at):
	print(product_id, start_at)
	data = {'product_id': product_id, 'address_id': ADDRESS_ID}
	url = KILLER_URL
	
	pool = ThreadPool(20)
	reqs = makeRequests(killer_req, [((url, data), {}) for i in range(200)], killer_callback)
	[pool.putRequest(req) for req in reqs]
	pool.wait()

def load_product_list():
	url = SENSES_URL
	r = AUTH._session.get(url, auth=AUTH._auth)
	r.encoding = 'utf-8'

	products = [it['media']['product'] for it in r.json()['data']['results']]
	products = list(filter(lambda x: x['count_remaining'] is not 0, products))
	products_show = ['商品Id: %s\n商品名称: %s\n剩余数量: %s\n秒杀时间: %s' % (it['id'], it['title'],\
		it['count_remaining'], it['start_at']) for it in products]
	LIST.change_product_list(products)
	return products_show