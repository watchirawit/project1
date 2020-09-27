def main():
	number = int(input("Your number : "))
	print("Roman numeral is:", end = " ") 
	roman(number) 

def roman(number): 
	num = [1, 4, 5, 9, 10, 40, 50, 90, 
		100, 400, 500, 900, 1000] 
	sym = ["I", "IV", "V", "IX", "X", "XL", 
		"L", "XC", "C", "CD", "D", "CM", "M"] 
	i = 12
	while number: 
		d = number // num[i] 
		number %= num[i] 

		while d: 
			print(sym[i], end = "") 
			d -= 1
		i -= 1

main()
