# find numbers n such that n and n^2 have same digit sum

def sum_digit(i):
	"""Die Funktion berechnet die Quersumme von i."""
	summe = 0
	for digit in str(i):
		summe += int(digit)
	return summe

def check_same_digit(m, exponent):
	"""Die Funktion checkt, welche Zahlen von 0 bis m die gleiche Quersumme wie ihre Quadratzahlen haben."""
	i = 0
	while i <= m:
		if sum_digit(i) == sum_digit(i**exponent):
			numbers.append(i)
		else:
			pass
		i += 1

numbers = []
check_same_digit(1000, 2)
print(numbers)
