numeros = [10, 15, 3, 7]
goal = 18
# 18 es el goal

def find_first_sum(numeros, goal):
    for i in range(len(numeros)):
        for j in range(i + 1, len(numeros)):
            if numeros[i] + numeros[j] == goal:
                return (i, j)
    return None

print(find_first_sum(numeros, goal))