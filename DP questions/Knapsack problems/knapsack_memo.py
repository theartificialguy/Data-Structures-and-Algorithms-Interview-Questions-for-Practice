# input:
weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
W = 7

def knapsack(wts, vals, W, n):
	dp = {}
	if n == 0 or W == 0:
		return 0
	if (W, n) in dp:
		return dp[(W, n)]
	elif wts[n-1] <= W:
		dp[(W, n)] = max(vals[n-1]+knapsack(wts, vals, W-wts[n-1], n-1), knapsack(wts, vals, W, n-1))
		return dp[(W, n)]
	elif wts[n-1] > W:
		dp[(W, n)] = knapsack(wts, vals, W, n-1)
		return dp[(W, n)]

ans = knapsack(weights, values, W, len(weights))
print(ans)
