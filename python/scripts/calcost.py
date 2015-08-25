def main():
	itemPrice = 80000
	buyDayNeed = 3
	dayMonth  = 31

	freeFromBuy = dayMonth / buyDayNeed
	dayNeedToBuy = dayMonth - freeFromBuy

	print dayNeedToBuy
	cost = dayNeedToBuy * itemPrice

	print cost

if __name__ == '__main__':
	main()

