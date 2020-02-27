# # 01. Naive Solution
# def solve(dataset):
# 	return [0]

# 02. Greedy Solution
def greedy(dataset):
	slices = 0
	solution = []
	for i in range(len(dataset['pizzas'])):
		if slices + dataset['pizzas'][i] <= dataset['knapsize']:
			solution.append(i)
	return solution

# 03. Solving the knapsack
# !pip install progressbar2
import progressbar
def knapsolve(dataset):
    maxscore = dataset['knapsize']
    dp = [None for _ in range(maxscore+1)]
    dp[0] = []
    for idx, item in progressbar.progressbar(list(enumerate(dataset['pizzas']))):
        for i in range(maxscore - item, -1, -1):
            if dp[i] is None: continue            
            dp[i+item] = dp[i] + [idx]
    i = -1
    while dp[i] is None: i -= 1
    return dp[i]

# 04. Optimizing the knapsack : partial reconstruction
def rebuild(solution, dataset):
    newsol = list(solution)
    for i in range(min(len(newsol),3)):
        idx = random.randrange(len(newsol))
        print(idx, dataset['pizzas'][newsol[idx]])
        del newsol[idx]
    newscore = scorer.score(newsol, dataset)
    remaining = dataset['knapsize'] - newscore
    st = set(newsol)
    newpizz = []
    for i in range(len(dataset['pizzas'])):
        if i in st:
			# Pizzas already used in the solution are replaced with infinite slices
			# so we avoid selecting them twice while keeping the list indices correct
            newpizz.append(99**99)
        else:
            newpizz.append(dataset['pizzas'][i])
    print('rem', remaining)
    reco = knapsolve({'pizzas':newpizz, 'knapsize':remaining})
    return sorted(newsol + reco)

# 05. Upping the ante
import random
def solvemc(dataset):
    capa = dataset['knapsize']
    sol = []
    for i in range(len(dataset['pizzas'])-1, -1, -1):
        if random.getrandbits(2) and capa >= dataset['pizzas'][i]:
            sol.append(i)
            capa -= dataset['pizzas'][i]
    st = set(sol)
    for i in range(len(dataset['pizzas'])-1, -1, -1):
        if i not in st and capa >= dataset['pizzas'][i]:
            sol.append(i)
            capa -= dataset['pizzas'][i]
    return sol
