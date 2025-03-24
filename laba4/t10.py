

def main():
	x  = [12, 16, 21, 26, 30]
	px = [.2, .1, .4, .2, .1]
	arr = [
		'15<X<25',
		'12<X<=20',
		'21<=X',
		'16<X',
		'X<=16'
	]
	for s in arr:
		n = s.find('X')
		a = -99999
		b = 99999
		if n > 0:
			if s[n - 1] == '=':
				a = int(s[:n - 2])
			else:
				a = int(s[:n - 1])
		if n < len(s) - 1:
			if s[n + 2] == '=':
				b = int(s[n + 3:])
			else:
				b = int(s[n + 2:])
		c = 0
		for i in range(len(x)):
			if (a < x[i] and x[i] < b) or \
					(a == x[i] and s[n - 1] == '=') or \
					(b == x[i] and s[i + 2] == '='):
				c += px[i]
		print(f'P({s}) = {c}')


if __name__ == "__main__":
	main()
