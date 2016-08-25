#!D:\Python34\python.exe
# -*- coding: utf-8 -*-

'same登录'

__author__ = 'litter_zhang'

from PyQt5 import QtWidgets
from UI.KillerUI import KillerUI
from UI.ProductListItemUI import ProductListItemUI
from UI.KillerListItemUI import KillerListItemUI
from settings import SENSES_URL, ADDRESS_ID, KILLER_URL, TIME_URL
import auth as AUTH
import lists as LIST
import windows
from threadpool import ThreadPool, makeRequests
import threading
import time

class killer_win(QtWidgets.QMainWindow, KillerUI):
	def __init__(self):
		super(killer_win, self).__init__()
		self.setupUi(self)

		# 显示可秒杀的商品列表
		products = load_product_list()
		for product in products:
			p_item = ProductListItemUI(self.SameProductList)
			p_item.setProductData(product)

		self.Add.clicked.connect(self.start_killer)

	def start_killer(self):
		#获取要秒杀的商品id
		# for selected in self.SameProductList.selectedItems():
			# selected_index = selected.row()
			# selected_data = selected.data()
			# print(selected.sizeHint())
			# 开启秒杀线程
			# try:
			# 	product = LIST._product_list[selected_index]

			# 	if get_time() > int(product['start_at']):
			# 		windows.killer_show.Console.append('%s 错过了秒杀时间' % product['id'])
			# 	else:
			# 		t = threading.Thread(target=killer_thread, args=(product['id'], int(product['start_at'])))
			# 		LIST.add_killer(t)
			# 		t.start()

			# 		#显示秒杀任务
			# 		self.SameKillerList.addItem(selected_data)
			# except Exception as e:
			# 	print(e)

		# t = threading.Thread(target=killer_thread, args=(1, 1))
		# t.start()

		# 获取选中商品
		for selected in self.SameProductList.selectedItems():
			selected.setSelected(False)

			item = self.SameProductList.itemWidget(selected)
			product = item.ProductData
			
			if item.Selected:
				self.Console.append('%s 已经在秒杀列表!' % product.get('id', ''))
			else:
				item.select()
				# 显示到带秒杀列表中
				k_item = KillerListItemUI(self.SameKillerList)
				k_item.setProductData(product)

#统计秒杀请求结果
def killer_callback(req, res):
	pass
	# windows.killer_show.Console.append(res)

#秒杀请求
def killer_req(url, data, time_ms):
	if time.time()<time_ms - 0.2:
		time.sleep(time_ms - time.time() - 0.2)

	r = AUTH._session.post(url, data=data, auth=AUTH._auth)
	r.encoding = 'utf-8'

	print(r.json())
	return '%s 秒杀结果 %s' % (data['product_id'], r.json().get('code', 0))

#秒杀
def killer_thread(product_id, start_at):
	time_now = get_time()

	if time_now - start_at > 5:
		time.sleep(time_now - start_at - 5)

	# 开始秒杀线程
	data = {'product_id': product_id, 'address_id': ADDRESS_ID}
	url = KILLER_URL
	
	pool = ThreadPool(50)
	reqs = makeRequests(killer_req, [((url, data, start_at), {}) for i in range(200)], killer_callback)
	[pool.putRequest(req) for req in reqs]
	pool.wait()

	#删除秒杀任务


#获取系统时间
def get_time():
	url = TIME_URL

	try:
		r = AUTH._session.get(url, auth=AUTH._auth)
		r.encoding = 'utf-8'

		time = r.json()['data']['time']

		return time/1000
	except Exception as e:
		print(e)
		raise Exception('获取当前时间出错')

#加载商品列表
def load_product_list():
	url = SENSES_URL

	try:
		r = AUTH._session.get(url, auth=AUTH._auth)
		r.encoding = 'utf-8'

		products = [it['media']['product'] for it in r.json()['data']['results']]
		products = list(filter(lambda x: x['count_remaining'] is not 0, products))
		
		return products
	except Exception as e:
		print(e)

	# products_show = ['商品Id: %s\n商品名称: %s\n剩余数量: %s\n秒杀时间: %s' % (it['id'], it['title'],\
	# 	it['count_remaining'], it['start_at']) for it in products]
	# LIST.change_product_list(products)
