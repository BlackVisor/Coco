from datetime import datetime

time = datetime.now()
a = datetime.strftime(time, '%m%d%H%M%S')
print(a)