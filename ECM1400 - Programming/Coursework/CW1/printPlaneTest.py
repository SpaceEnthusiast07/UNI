
def print_nose():
	print(" "*9 + "/\\" + " "*7)
	print(" "*8 + "/  \\" + " "*6)
	print(" "*7 + "/    \\" + " "*5)
	print(" "*6 + "/      \\" + " "*4)
	print(" "*5 + "/        \\" + " "*3)
	print(" "*4 + "/          \\" + " "*2)
	print(" "*3 + "/            \\" + " "*1)
	print("  /              \\")


def print_tail():
	print("  \\              /")
	print(" "*3 + "\\            /" + " "*1)
	print("    \\          /" + " "*2)
	print("   / \\        / \\" + " "*3)
	print("  /   \\      /   \\" + " "*4)
	print("  -----\\    /-----" + " "*5)
	print(" "*8 + "\\  /" + " "*6)
	print(" "*9 + "\\/" + " "*7)


plane = [["empty","empty","empty","empty","empty","empty"],
		 ["empty","empty","empty","empty","empty","empty"],
		 ["empty","empty","empty","empty","empty","empty"],
		 ["empty","empty","empty","empty","empty","empty"],
		 ["empty","empty","empty","empty","empty","empty"],
		 ["empty","empty","empty","empty","empty","empty"],
		 ["empty","empty","empty","empty","empty","empty"],
		 ["empty","empty","empty","empty","empty","empty"],
		 ["empty","empty","empty","empty","empty","empty"],
		 ["empty","empty","empty","empty","empty","empty"],
		 ["empty","empty","empty","booked","empty","empty"],
		 ["empty","empty","empty","empty","empty","empty"],
		 ["empty","empty","empty","empty","empty","empty"],
		 ["booked","booked","booked","empty","empty","empty"],
		 ["empty","empty","empty","empty","empty","empty"],
		 ["empty","empty","empty","booked","booked","empty"],
		 ["empty","empty","empty","empty","empty","empty"],
		 ["empty","empty","empty","empty","empty","empty"]]


letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

print_nose()
# Print the column numbers
print("    1 2 3   4 5 6")
# Initialise the row string
rowString = "| "
# Loop through each row of the plane
for i in range(len(plane)):
		# If on row 11 (index 10), print exit row
		if i == 10:
			print("  ¦" + " "*(len(rowString) - 4) + "¦")
		
		# Reset row string
		rowString = letters[i] + " | "
		# Loop through each seat in the current row
		for j in range(len(plane[i])):
			# If on seat 4 (index 3), add "  " to rowString for isle
			if j == 3:
				rowString += "  "
			
			# If current seat empty, add "U " to rowString
			if plane[i][j] == "empty":
				rowString += "U "
			# If current seat is booked, add "# " to rowString
			elif plane[i][j] == "booked":
				rowString += "# "
			
		# Add right wall to rowString
		rowString += "|"

		# Output the current row
		print(rowString)



# Print the plaen's tail
print_tail()