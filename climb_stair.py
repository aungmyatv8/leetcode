def climb_stairs(n):
    if n <= 2:
        return n

    # Initialize an array to store the number of ways for each step
    ways = [0] * (n + 1)
    ways[1] = 1
    ways[2] = 2

    # print(ways)
    for i in range(3, n + 1):
        # print(i)
         ways[i] = ways[i - 1] + ways[i - 2]
         print(ways)
    return ways[n]


n1 = 2
n2 = 5
result1 = climb_stairs(n1)
result2 = climb_stairs(n2)
# climb_stairs(n2)

print(f"Number of distinct ways to climb {n2} steps: {result2}")
print(f"Number of distinct ways to climb {n2} steps: {result2}")