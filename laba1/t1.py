from formulas import C

def main():
	b = 6
	w = 4
	print(f'вероятность того, что они разного цвета: {C(1, w)*C(1, b)/C(2, b+w)}')


if __name__ == "__main__":
	main()
