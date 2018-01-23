def CheckOrder(a,b):
	#function to make sure a is larger than b
	#if not then perform tuple swap
	if b > a:
		a, b = b, a
		return a, b
	else:
		return a,b

def CheckGCD(a,b):
	#this function returns the GCD
	CheckOrder(a,b)
	#this takes a and b arguments and verifies a is larger than b
	g = int(a / b)
	remainder = (g * b)
	result = 1
	solution = 0
	while int(remainder) >= 0:
		remainder = int(a - ((int(g) * b)))
		try: 
			result = int((b / remainder));		
		except ZeroDivisionError:
			return(b)
			break		
		a = b
		b = remainder
		g = int(a / b)
	return b
def main():
	print("This application will take two positive integers and find the GCD")
	print("via a euclid algorithim")
	a = int(input("What is the first number: "))
	b = int(input("What is the second number: "))
	print (str(CheckGCD(a,b)))
if __name__ == "__main__":
    main()

