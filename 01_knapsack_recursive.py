# input:
weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
W = 10

def knapsack(wts, vals, W, n):
	if W == 0 or n == 0:
		return 0
	elif wts[n-1] <= W:
		return max(vals[n-1]+knapsack(wts, vals, W-wts[n-1], n-1), knapsack(wts, vals, W, n-1))
	elif wts[n-1] > W:
		return knapsack(wts, vals, W, n-1)

ans = knapsack(weights, values, W, len(weights))
print(ans)