# podpunkt a z zadania 3
def lsc(word1, word2):
    """Funkcja zwraca największą długość wsólnego podciągu dwóch wyrazów (bez przerw między charakterami)"""
    len1 = len(word1)
    len2 = len(word2)
    counter = [[0] * (1 + len2) for i in range(1 + len1)]  # Odzwierciedlenie pustej macierzy, licznik kolejnych podobieństw
    i_longest = 0
    combo = 0
    for i in range(1, 1 + len1):
        for j in range(1, 1 + len2):                       # iterujemy przez oba wyrazy porównując kolejne wyrazy
            if word1[i - 1] == word2[j - 1]:
                counter[i][j] = counter[i - 1][j - 1] + 1  # Jeśli poprzedni znak był taki sam, to sumuje licznik
                if counter[i][j] > combo:
                    combo = counter[i][j]
                    i_longest = i                          # Zapisuje od któreg miejsca zaczyna się najdłuższy podciąg
            else:
                counter[i][j] = 0                          # Jeśli
    return len(word1[i_longest - combo: i_longest])        # Zwraca długość najdłuższgeo podciągu

# podpunkt b z zadania 3
def lsc2(word1, word2):
    """Zwraca długość najdłuższego wspólnego podciągu znaków dla dwóch tekstów (z przerwami)"""
    len1 = len(word1)
    len2 = len(word2)
    counter = [[0] * (1 + len2) for i in range(1 + len1)]
    for i in range(len1):
        for j in range(len2):
            if word1[i] == word2[j]:
                counter[i + 1][j + 1] = counter[i][j] + 1
            else:
                counter[i + 1][j + 1] = max(counter[i][j+1], counter[i + 1][j])
    return counter[-1][-1]


word1 = 'ApqBCrDsEF'
word2 = 'tABuCvDEwxFyz'
word3 = 'konwalia'
word4 = 'zawalina'

print('=====Sprawdzenie dla ciagu bez przerw=====')
print(lsc(word3, word4))
print('=====Sprawdzenie dla ciagu z dopuszczalnymi przerwami=====')
print(lsc2(word1, word2))


