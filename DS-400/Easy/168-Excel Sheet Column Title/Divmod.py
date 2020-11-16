def convertToTitle(self, n: int) -> str:
	alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	alen = len(alphabet)
	base = ''

	while n > 0 :
		n -= 1
		n, j = divmod(n, alen)
		base += alphabet[j] # + base

	return base[::-1]