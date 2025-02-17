from formulas import C


def main():
	print(f'вероятность того, что среди них будут король и дама: {4*4*34/C(3,36)}')


if __name__ == "__main__":
	main()
