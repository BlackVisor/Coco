import uiautomator2 as u2
from time import sleep
import unittest


class Product(unittest.TestCase):

	"""docstring for Product"""
	def setUp(self):

		ip = "192.168.1.110"
		# ip = input("请输入手机IP:")
		self.samsang = u2.connect(ip)
		self.App = "com.oujia.offerplus"


	def test_1_login(self):
		self.samsang.app_start(self.App)
		sleep(2)
		self.samsang(className="android.widget.EditText")[0].click()
		#self.samsang(text="Email/Account ID/Phone Number").click()
		self.samsang.set_fastinput_ime(True)
		self.samsang.clear_text()
		self.samsang.send_keys("1001135")
		sleep(1)
		self.samsang(className="android.widget.EditText")[1].click()
		#self.samsang(text="Password").click()
		sleep(1)
		self.samsang.send_keys("Aa123456")
		self.samsang.set_fastinput_ime(False)
		self.samsang.press("back")
		sleep(2)
		self.samsang(resourceId="com.oujia.offerplus:id/fragment_sign_in_next_bt").click()
		sleep(2)
		self.samsang(resourceId="com.oujia.offerplus:id/home_foot_btn04").click()
		sleep(1)
		if self.samsang.exists(text="Me"):
			print("登陆成功")
		else:
			print("登陆失败")

	def test_2_product_new(self):
		self.samsang(resourceId="com.oujia.offerplus:id/home_foot_btn02").click()
		self.samsang(text="Product").click()
		sleep(1)
		self.samsang(text="Picture").click()
		sleep(1)
		self.samsang(resourceId="com.oujia.offerplus:id/record_button").click()
		self.samsang(resourceId="com.oujia.offerplus:id/iv_item").wait(timeout=10.0)
		self.samsang(resourceId="com.oujia.offerplus:id/tv_photos").click()
		sleep(1)
		# self.samsang(resourceId="com.oujia.offerplus:id/item_fragment_make_offer_choose_photo_check_iv")[0].click()
		self.samsang(resourceId="com.oujia.offerplus:id/item_fragment_make_offer_choose_photo_check_iv")[1].click()
		self.samsang(resourceId="com.oujia.offerplus:id/item_fragment_make_offer_choose_photo_check_iv")[2].click()
		self.samsang(resourceId="com.oujia.offerplus:id/item_fragment_make_offer_choose_photo_check_iv")[3].click()
		# self.samsang.click(0.241, 0.163)#保存图片
		self.samsang(text="Save").click()
		sleep(1)
		# samsang(text="Save").click()
		# sleep(1)
		self.samsang(text="Name").click()
		self.samsang.set_fastinput_ime(True)
		self.samsang.send_keys("offerplus")
		self.samsang.set_fastinput_ime(False)
		sleep(1)
		self.samsang(text="Description").click()
		self.samsang.set_fastinput_ime(True)
		self.samsang.send_keys("offerplus")
		self.samsang.set_fastinput_ime(False)
		self.samsang.press("back")
		if self.samsang.exists(text="Cancel"):
			self.samsang(text="Cancel").click()
		else:
			pass
		self.samsang(text="Save & Next").click()
		sleep(1)
		# self.samsang(text="Success").wait(timeout=3.0)
		self.samsang.press("back")
		self.samsang(resourceId="com.oujia.offerplus:id/home_foot_btn00").click()
		self.samsang(text="PRODUCT").click()
		sleep(3)
		if self.samsang.exists(text = "offerplus"):
			print("新建成功")
		else:
			print("产品没有新建")
		self.samsang.press("back")
		# self.samsang(description="‎‏‎‎‎‎‎‏‎‏‏‏‎‎‎‎‎‏‎‎‏‎‎‎‎‏‏‏‏‏‎‏‏‎‏‏‎‎‎‎‏‏‏‏‏‏‏‎‏‏‏‏‏‎‏‎‎‏‏‎‏‎‎‎‎‎‏‏‏‎‏‎‎‎‎‎‏‏‎‏‏‎‎‏‎‏‎‏‏‏‏‏‎‎Navigate up‎‏‎‎‏‎").click()

	def test_3_product_edit(self):
		self.samsang(resourceId="com.oujia.offerplus:id/home_foot_btn00").click()
		self.samsang(text="PRODUCT").click()
		sleep(3)
		#点击进去编辑
		self.samsang(text="offerplus").click(timeout = 10)#这里可以加个if来判断10s没加载出来判断不通过
		self.samsang(text="offerplus")[0].click()
		self.samsang(resourceId="com.oujia.offerplus:id/layout_product_bottom_send_inquiry_bt").click()
		#self.samsang(text="EDIT").click()
		self.samsang(resourceId="com.oujia.offerplus:id/item_fragment_make_offer_photo_pic_delete")[0].click()
		self.samsang(resourceId="com.oujia.offerplus:id/fragment_make_offer_title_et")[0].click()
		#elf.samsang(text="Name").click()
		self.samsang.set_fastinput_ime(True)
		sleep(1)
		self.samsang.clear_text()
		sleep(1)
		self.samsang.send_keys("offerplus_change")
		sleep(1)
		self.samsang.set_fastinput_ime(False)
		sleep(1)
		self.samsang.press("back")
		sleep(1)
		self.samsang(text="Save").click()
		# self.samsang.press("back")
		if self.samsang.exists(text = "offerplus_change"):
			print("编辑成功")
		else:
			print("编辑失败")
		# self.samsang(description="‎‏‎‎‎‎‎‏‎‏‏‏‎‎‎‎‎‏‎‎‏‎‎‎‎‏‏‏‏‏‎‏‏‎‏‏‎‎‎‎‏‏‏‏‏‏‏‎‏‏‏‏‏‎‏‎‎‏‏‎‏‎‎‎‎‎‏‏‏‎‏‎‎‎‎‎‏‏‎‏‏‎‎‏‎‏‎‏‏‏‏‏‎‎Navigate up‎‏‎‎‏‎").click()
		sleep(1)
		# 右滑点击编辑键编辑
		self.samsang.press("back")
		self.samsang(text="PRODUCT").click()
		self.samsang(resourceId="com.oujia.offerplus:id/item_offer_title_tv")[0].drag_to(0.091, 0.242,duration = 0.1)
		# self.samsang.swipe((0.66, 0.238),(0.333, 0.244),0.1)
		self.samsang(text="Edit").click()
		self.samsang(resourceId="com.oujia.offerplus:id/item_fragment_make_offer_photo_pic_delete")[0].click()
		self.samsang(resourceId="com.oujia.offerplus:id/fragment_make_offer_title_et")[0].click()
		# self.samsang(text="Name").click()
		self.samsang.set_fastinput_ime(True)
		self.samsang.clear_text()
		self.samsang.send_keys("offerplus_change_1")
		self.samsang.set_fastinput_ime(False)
		self.samsang.press("back")
		sleep(1)
		self.samsang(text="Save").click()
		# self.samsang.press("back")
		if self.samsang.exists(text = "offerplus_change_1"):
			print("编辑成功")
		else:
			print("编辑失败")
		# self.samsang(description="‎‏‎‎‎‎‎‏‎‏‏‏‎‎‎‎‎‏‎‎‏‎‎‎‎‏‏‏‏‏‎‏‏‎‏‏‎‎‎‎‏‏‏‏‏‏‏‎‏‏‏‏‏‎‏‎‎‏‏‎‏‎‎‎‎‎‏‏‏‎‏‎‎‎‎‎‏‏‎‏‏‎‎‏‎‏‎‏‏‏‏‏‎‎Navigate up‎‏‎‎‏‎").click()
		self.samsang.press("back")

	def test_4_product_delete(self):
		self.samsang(resourceId="com.oujia.offerplus:id/home_foot_btn00").click()
		self.samsang(text="PRODUCT").click()
		sleep(3)
		# self.samsang.swipe((0.66, 0.238),(0.333, 0.244),0.1)
		self.samsang(resourceId="com.oujia.offerplus:id/item_offer_title_tv")[0].drag_to(0.091, 0.242,duration = 0.1) 
		self.samsang(text="Delete").click()
		self.samsang(text="Cancel").click()
		if self.samsang.exists(text="offerplus_change_1"):
			print("取消删除成功")
		else:
			print("列表已经没有该产品")
		self.samsang(resourceId="com.oujia.offerplus:id/item_offer_title_tv")[0].drag_to(0.091, 0.242,duration = 0.1)
		# self.samsang.swipe((0.66, 0.238),(0.333, 0.244),0.1)
		self.samsang(text="Delete").click()
		self.samsang(text="OK").click()
		self.samsang(text="Delete Success").wait(timeout=3.0)
		if self.samsang.exists(text="offerplus_change_1"):
			print("删除失败")
		else:
			print ("删除成功")
		self.samsang.press("back")

	def test_5_logout(self):
		self.samsang(resourceId="com.oujia.offerplus:id/home_foot_btn04").click()
		self.samsang(resourceId="com.oujia.offerplus:id/tv_username").click()
		sleep(1)
		self.samsang(resourceId="com.oujia.offerplus:id/log_out_tv").click()
		sleep(1)
		self.samsang(text="Yes").click()
		if self.samsang.exists(text="Sign In"):
			print("登出成功")
		else:
			print("登出失败")
		self.samsang.app_stop(self.App)

	def tearDown(self):
		self.samsang.app_stop(self.App)


if __name__ == '__main__':
	unittest.main()
