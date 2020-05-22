from queue import deque

class Node:
    """Klasa reprezentująca węzeł drzewa binarnego."""

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

def dfs(top):
    """Przeszukanie DFS"""
    if top is None:
        return
    print(top)
    dfs(top.left)
    dfs(top.right)

def bfs(top):
    if top is None:
        return
    Q =  deque()
    Q.append(top)
    while len(Q) > 0:
        node = Q.popleft()
        print(node)
        if node.left:
            Q.append(node.left)
        if node.right:
            Q.append(node.right)

root = Node(1)
# Pierwszy poziom
root.left = Node(2)
root.right = Node(3)

# Drugi poziom lewo
root.left.left = Node(4)
root.left.right = Node(5)
# Drugi poziom prawo
root.right.left = Node(6)
root.right.right = Node(7)

# Trzeci poziom lewo
root.left.left.left = Node(8)
root.left.left.right = Node(9)
root.left.right.left = Node(10)
root.left.right.right = Node(11)

# Trzeci poziom prawo
root.right.left.left = Node(12)
root.right.left.right = Node(13)
root.right.right.left = Node(14)
root.right.right.right = Node(15)

print('METODA DFS PREORDER')
dfs(root)
print('METODA BFS')
bfs(root)