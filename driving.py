country = input('輸入國家')
age = input('輸入年齡')
age = int(age)
if country == '台灣':
	if age >= 18:
		print('可以考照')
	else:
		print('不能考照')
elif country == '美國':
	if age >=16:
		print('可以考照')
	else:
		print('不能考照')