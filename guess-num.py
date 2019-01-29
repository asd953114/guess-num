import random

start = input("請決定隨機數字範圍開始值:")
end = input("請決定隨機數字範圍結束值: ")
start = int(start)
end = int(end)

i = input("想要猜幾次:")
i = int(i)
start = int(start)
end = int(end)

r = random.randint(start, end)

count = 0
while count < i:
	count += 1
	num = input("請猜輸字: ")
	num = int(num)
	if num == r :
		print("你猜對了！")
		print("這是你猜的第", count, "次")
		break
	elif num > r:
		print("比答案大:")
	elif num < r:
		print("比答案小")
	print("這是你猜的第", count, "次")
print("已達到", i,"次")