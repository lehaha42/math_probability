from formulas import C


def main():
	for i in range(7):
		print(f'P(x={i}) = {C(i, 6)*C(6-i, 39)/C(6, 45)}')


if __name__ == "__main__":
	main()
