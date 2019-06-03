# simple voting
def simple_voting(p1, p2):
	return 1/2 * (p1 + p2)

# weighted voting
def weighted_voting(p1, p2, k1, k2):
	return 1/2 * (k1 * p1 + k2 * p2)