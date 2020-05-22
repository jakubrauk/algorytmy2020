from random import randint

class Node:
    """Klasa reprezentująca węzeł listy jednokierunkowej."""
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class SingleList:
    """Klasa reprezentująca całą listę jednokierunkową."""
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.length == 0

    def count(self):
        return self.length

    def insert_head(self, node):
        if self.length == 0:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1

    def insert_tail(self, node):
        if self.length == 0:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    def remove_head(self):
        if self.length == 0:
            raise ValueError("pusta lista")
        node = self.head
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
        node.next = None
        self.length -= 1
        return node

    def print_list(self):
        if self.length == 0:
            print('pusta lista')
        elif self.length == 1:
            print(self.head)
        else:
            print(self.head)
            after = self.head.next
            while after:
                print(after)
                after = after.next


office = [[1, 'A', 0],
         [2, 'A', 0],
         [3, 'A', 0],
         [4, 'B', 0],
         [5, 'B', 0],
         [6, 'B', 0],
         [7, 'C', 0],
         [8, 'C', 0],
         [9, 'C', 0],
         [10, 'E', 0]]

def taskType(n):
    """Zwraca rodzaj sprawy 1 == A, 2 == B, 3 == C"""
    if n == 1:
        return 'A'
    elif n == 2:
        return 'B'
    elif n == 3:
        return 'C'


queue = SingleList()

# Losuję 30 klientów ['typ_zadania', 'złożoność_zadania']
for i in range(30):
    queue.insert_tail(Node(randint(1, 10)))
    queue.insert_tail(Node(taskType(randint(1, 3))))

time = 0
while queue.count() != 0:
    complexity = queue.remove_head()
    task_type = queue.remove_head()
    is_window_matching = False
    for window in office:
        if window[2] == 0: # Jeśli zajętość wynosi 0 - szukaj nowego klienta
            if window[1] == str(task_type) or window[1] == 'E':
                window[2] += int(str(complexity))
                is_window_matching = True
                break
    for window in office:
        if window[2] > 0:
            window[2] -= 1
    if is_window_matching is False:     # Jeśli nie znajdzie się wolne okienko,
        queue.insert_head(task_type)    # klient zostanie ponownie dodany na początek listy
        queue.insert_head(complexity)
    time += 1

last_customer = 0
for window in office:
    if window[2] > last_customer:
        last_customer = window[2]
time += last_customer # Ostatni klient musi być dodany do czasu, ponieważ nie jest widoczny w pętli

print(f'Upłyneło {time} jednostek czasu')


