
def print_nose():
	print(" "*7 + "/\\" + " "*7)
	print(" "*6 + "/  \\" + " "*6)
	print(" "*5 + "/    \\" + " "*5)
	print(" "*4 + "/      \\" + " "*4)
	print(" "*3 + "/        \\" + " "*3)
	print(" "*2 + "/          \\" + " "*2)
	print(" "*1 + "/            \\" + " "*1)
	print("/              \\")


def print_tail():
	print("\\              /")
	print(" "*1 + "\\            /" + " "*1)
	print("  \\          /" + " "*2)
	print(" / \\        / \\" + " "*3)
	print("/   \\      /   \\" + " "*4)
	print("-----\\    /-----" + " "*5)
	print(" "*6 + "\\  /" + " "*6)
	print(" "*7 + "\\/" + " "*7)


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




print_nose()
rowString = "| "
for i in range(len(plane)):
		# If on row 11 (index 10), print exit row
		if i == 10:
			print("|" + " "*(len(rowString) - 2) + "|")
		
		rowString = "| "
		for j in range(len(plane[i])):
			# If on seat 4 (index 3), add "  " to rowString
			if j == 3:
				rowString += "  "
			
			# If current seat empty, add "U " to rowString
			if plane[i][j] == "empty":
				rowString += "U "
			elif plane[i][j] == "booked":
				rowString += "# "
			
		# Add right wall to rowString
		rowString += "|"

		# Output the current row
		print(rowString)

print_tail()