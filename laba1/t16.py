from formulas import C

def main():
	n = 0
	for i in range(3):
		n += C(1+i, 12)*C(2-i, 16)/C(3,28)*(1-(1-.7)**(i+1))
	print(n)


if __name__ == "__main__":
	main()
