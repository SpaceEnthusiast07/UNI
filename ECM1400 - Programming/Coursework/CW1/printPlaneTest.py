
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


print_nose()
for i in range(18):
		# Are we on row 10, if so, print exit row
		if (i == 10):
			print("¦" + " "*14 + "¦")
		else:
			print("| " + "U "*3 + " " + "U "*3 + "|")

print_tail()