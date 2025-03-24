

def main():
	x = [-2, 0, 3, 7]
	px = [.4, .1, .3, .2]
	arr = [
		'-1<X<5',
		'4<X<=10',
		'X<=2',
		'3<=X<=7',
		'7<X'
	]
	for s in arr:
		n = s.find('X')
		a = -99999
		b = 99999
		if n > 0:
			if s[n-1] == '=':
				a = int(s[:n - 2])
			else:
				a = int(s[:n - 1])
		if n < len(s)-1:
			if s[n+2] == '=':
				b = int(s[n+3:])
			else:
				b = int(s[n+2:])
		c = 0
		for i in range(len(x)):
			if (a < x[i] and x[i] < b) or \
					(a == x[i] and s[n-1] == '=') or\
					(b == x[i] and s[i+2] == '='):
				c += px[i]
		print(f'P({s}) = {c}')


if __name__ == "__main__":
	main()
