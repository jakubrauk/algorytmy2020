from random import randint

def graphDfs(graph):
    """Podział grafu na składowe spójne"""
    """Algorytm wzorowany na algorytmie ze materiałów pomocniczych:
    https://eduinf.waw.pl/inf/alg/001_search/0129.php"""

    anchor_amount = 0
    for anchor in graph:
        anchor_amount += 1

    c = [0] * anchor_amount
    cn = 0 # Ilość połączonych wierzchołków
    stack = []
    for i in range(anchor_amount):
        if c[i] > 0:
            continue
        cn += 1
        stack.append(i)
        c[i] = cn
        while len(stack) > 0:
            v = stack.pop()
            for u in graph[v]:
                if c[u] > 0:
                    continue
                stack.append(u)
                c[u] = cn
    print('Ilość składowych: ', cn)

    for i in range(1, cn + 1):
        print(f'Składowa {i}:')
        for j in range(anchor_amount):
            if c[j] == i:
                print(j)

def generateRandomGraph(anchor_amount):
    graph = {}  # Pusty graf

    # Losowanie grafu
    # Możliwe jest połączenie miedzy jednym, tym samym wierzchołkiem (pętelka)
    for i in range(anchor_amount):
        graph.update({i: [randint(1, anchor_amount - 1)]})
    # W tym momencie grapf nie pokazuje wszystkich krawędzi (nie są one kompletne)

    # Uzupełnienie grafu o brakujące krawędzie
    # Połączenia miedzy wierzchołkami
    for i in range(anchor_amount):
        for anchor in graph[i]:
            if i not in graph[anchor]:
                graph[anchor].append(i)
    return graph

def printGraph(graph):
    print('Wylosowany graf: ')
    for i in graph:
        print(i, ': ', graph[i])

if __name__ == '__main__':
    anchor_amount = int(input('Podaj ilość wierzchołków: '))
    graph = generateRandomGraph(anchor_amount)
    printGraph(graph)
    graphDfs(graph)



