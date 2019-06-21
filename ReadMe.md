框架参考来源：
https://www.cnblogs.com/wangxiaoqun/p/6924797.html

1.先把web UI自动化框架搭起来
2.再往里面加接口自动化框架，目前取名叫Fiber
3.然后再搭前后端服务来控制测试用例和显示测试报告
4.publicdata=重新封装find_element等方法，自定义断言

myunit=定义了setUpClass和tearDownClass
opt=定义ip，文件路径，密码等配置项目