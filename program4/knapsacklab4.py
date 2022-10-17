#to understand the knapsackproblem and find out the maximum profit
def Knapsack(List_of_weights, List_of_profits, Capacity):
    n = min(len(List_of_weights), len(List_of_profits))
    s_a = [(List_of_weights[i], List_of_profits[i]) for i in range(n)]
    s_a.sort(key=lambda i: i[1], reverse=True)
#let total profit=0
    total_profit = 0
    result = []
#for loop for getting result with profit
    for item in s_a:
        if item[0] <= Capacity:
            total_profit += item[1]
            Capacity -= item[0]
            result.append(item)

    return (result, total_profit)
#driver code
weights = [10, 16, 37, 53]
profits = [200, 150, 300, 100]
weight = 20
print(Knapsack(weights, profits, weight))


#first answer is weights 
#seond one is corresponding  maximum profits
#third one is maximum weight it can get