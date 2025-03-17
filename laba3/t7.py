

def main():
	t = 96
	p = .08
	a = []
	for i in range(100):
		if t * p - (1 - p) <= i and i <= (t + 1) * p:
			a.append(i)
	print(a)


if __name__ == "__main__":
	main()
