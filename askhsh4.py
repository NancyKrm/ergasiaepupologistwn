while True:
	number = int(input("pliktrologhste enan thetiko akeraio arithmo: "))
	if number > 0:
		if number <= 1000000:
			break
		else:
			print("oi arithmoi prepei na einai mikroteroi apo 1000000!!")
	else:
		print("monoi thetikoi arithmoi!!")
				
value = ""
numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

def int_to_roman(a):
   return {
        1 :   "I",
        4 :   "IV",
        5 :   "V",
        9 :   "IX",
        10:   "X",
        40:   "XL",
        50:   "L",
        90:   "XC",
        100:  "C",
        400:  "CD",
        500:  "D",
        900:  "CM",
        1000: "M"
    }[a]

for i in numbers:
    for _ in range(0, number//i):
        value += int_to_roman(i)
    number = number%i


print(value)