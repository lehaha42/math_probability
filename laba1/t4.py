from formulas import C


def main():
	print(f'вероятность правильного набора пароля с первого раза: {1/C(7, 10)}')


if __name__ == "__main__":
	main()
