eng_letter_freq = {
    'a': 8.167,
    'b': 1.492,
    'c': 2.782,
    'd': 4.253,
    'e': 12.702,
    'f': 2.228,
    'g': 2.015,
    'h': 6.094,
    'i': 6.966,
    'j': 0.153,
    'k': 0.772,
    'l': 4.025,
    'm': 2.406,
    'n': 6.749,
    'o': 7.507,
    'p': 1.929,
    'q': 0.095,
    'r': 5.987,
    's': 6.327,
    't': 9.056,
    'u': 2.758,
    'v': 0.978,
    'w': 2.360,
    'x': 0.150,
    'y': 1.974,
    'z': 0.074
}

pl_letter_freq = {
    'a': 10.503 + 0.699,
    'b': 1.740,
    'c': 3.895 + 0.743,
    'd': 3.725,
    'e': 7.352 + 1.035,
    'f': 0.143,
    'g': 1.731,
    'h': 1.015,
    'i': 8.328,
    'j': 1.836,
    'k': 2.753,
    'l': 2.564 + 2.109,
    'm': 2.515,
    'n': 6.237 + 0.362,
    'o': 6.667 + 1.141,
    'p': 2.445,
    'q': 0,
    'r': 5.243,
    's': 5.224 + 0.814,
    't': 2.475,
    'u': 2.062,
    'v': 0.012,
    'w': 5.813,
    'x': 0.004,
    'y': 3.206,
    'z': 4.852 + 0.078 + 0.706
}
de_letter_freq = {
    'a': 6.516 + 0.578,
    'b': 1.886,
    'c': 2.732,
    'd': 5.076,
    'e': 16.396,
    'f': 1.656,
    'g': 3.009,
    'h': 4.577,
    'i': 6.550,
    'j': 0.268,
    'k': 1.417,
    'l': 3.437,
    'm': 2.534,
    'n': 9.776,
    'o': 2.594 + 0.443,
    'p': 0.670,
    'q': 0.018,
    'r': 7.003,
    's': 7.270,
    't': 6.154,
    'u': 4.166 + 0.995,
    'v': 0.846,
    'w': 1.921,
    'x': 0.034,
    'y': 0.039,
    'z': 1.134
}

def checkCorrect():
    """Sprawdzenie poprawności tablicy częstości,
    jeśli suma jest blisk 100 == good"""
    eng_sum = 0
    for k in eng_letter_freq:
        eng_sum += eng_letter_freq[k]
    pl_sum = 0
    for k in pl_letter_freq:
        pl_sum += pl_letter_freq[k]
    de_sum = 0
    for k in de_letter_freq:
        de_sum += de_letter_freq[k]
    print('suma w jezyku ang ' + str(eng_sum))
    print('suma w jezyku pl ' + str(pl_sum))
    print('suma w jezyku de ' + str(de_sum))

def isalpha(x):
    """Zwraca true jeśli x jest litrą"""
    return x in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def count_all_letters(text):
    """Zwraca liczbę wszystkich liter łacińskich w text"""
    counter = 0
    text = text.lower()
    for char_ in text:
        if isalpha(char_):
            counter += 1
    return counter


def whatLanguage(text, pl_letter_freq, eng_letter_freq, de_letter_freq):
    """Zwraca nazwę języka, na podstawie róznic w tablicach częstosći,
    Im mniejsza róznica, tym bardziej dokładny wynik"""

    freq = {} # pusta dict częstości
    for x in 'abcdefghijklmnopqrstuvwxyz':
        freq[x] = 0
    for letter in text: # pętla wypełniająca tablice częstości występowaniami liter w podanym tekście
        if isalpha(letter):
            letter = letter.lower()
            freq[str(letter)] += 1

    for key in freq:
        freq[str(key)] = (freq[str(key)] / count_all_letters(text)) * 100 # Procentowy wynik
        # print(str(key) + ' ' + str(freq[key]))

    diff = [{}, {}, {}]
    sum = [0, 0, 0]

    for key in freq: # pętla obliczająca róznicę (odległość) między tablicami
        diff[0][key] = abs(pl_letter_freq[key] - freq[key])
        sum[0] += diff[0][key]

        diff[1][key] = abs(eng_letter_freq[key] - freq[key])
        sum[1] += diff[1][str(key)]

        diff[2][key] = abs(de_letter_freq[key] - freq[key])
        sum[2] += diff[2][str(key)]

    # Jeśli różnica == najmniejsza w tablicy sum, zwróć nazwę języka
    if min(sum) == sum[0]:
        return 'polsih'
    elif min(sum) == sum[1]:
        return 'english'
    elif min(sum) == sum[2]:
        return 'german'


def isVowel(x): # samogłoska
    return x in 'aeyiou'

def isConsonant(x): # spółgłoska
    return x in 'bcdfghjklmnprstwyz'


def whatLanguageVowelConsonant(text, pl_freq, eng_freq, de_freq):
    """Zwraca nazwę języka na podstawie częstości spółgłosek i samogłosek"""

    # pusty dict częstości
    freq = {
        'vowel': 0,
        'consonant': 0
    }
    for letter in text:
        if isalpha(text):
            letter = letter.lower()
            if isVowel(letter):
                freq['vowel'] += 1
            else:
                freq['consonant'] += 1
    amount_of_letters = count_all_letters(text)
    freq['vowel'] = (freq['vowel'] / amount_of_letters) * 100
    freq['consonant'] = (freq['consonant'] / amount_of_letters) * 100

    diff = [{}, {}, {}]
    sum = [0, 0, 0]


    diff[0]['vowel'] = abs(pl_freq['vowel'] - freq['vowel'])
    diff[0]['consonant'] = abs(pl_freq['consonant'] - freq['consonant'])
    sum[0] = diff[0]['vowel'] + diff[0]['consonant']

    diff[1]['vowel'] = abs(eng_freq['vowel'] - freq['vowel'])
    diff[1]['consonant'] = abs(eng_freq['consonant'] - freq['consonant'])
    sum[1] = diff[1]['vowel'] + diff[1]['consonant']

    diff[2]['vowel'] = abs(de_freq['vowel'] - freq['vowel'])
    diff[2]['consonant'] = abs(de_freq['consonant'] - freq['consonant'])
    sum[2] = diff[2]['vowel'] + diff[2]['consonant']

    if min(sum) == sum[0]:
        return 'polsih'
    elif min(sum) == sum[1]:
        return 'english'
    elif min(sum) == sum[2]:
        return 'german'

if __name__ == '__main__':
    # Wczytanie tekstów
    with open('polish_text.txt', 'r') as f:
        pl_text = f.read()

    with open('english_text.txt', 'r') as f:
        eng_text = f.read()

    with open('german_text.txt', 'r') as f:
        de_text = f.read()

    # Stworzone zerowe tablice czestośći dla każdego z języków
    pl_freq = {}
    for x in 'abcdefghijklmnopqrstuvwxyz':
        pl_freq[x] = 0
    eng_freq = pl_freq
    de_freq = pl_freq

    print(whatLanguage(pl_text, pl_letter_freq, eng_letter_freq, de_letter_freq))
    print(whatLanguage(de_text, pl_letter_freq, eng_letter_freq, de_letter_freq))
    print(whatLanguage(eng_text, pl_letter_freq, eng_letter_freq, de_letter_freq))

    print('================ ZADANIE 2C ==================')

    # Puste tablice samogłosek i spółgłosek
    pl_vowel_and_consonant_freq = {
        'vowel': 0,
        'consonant': 0
    }
    eng_vowel_and_consonant_freq = {
        'vowel': 0,
        'consonant': 0
    }
    de_vowel_and_consonant_freq = {
        'vowel': 0,
        'consonant': 0
    }
    for key in pl_letter_freq:
        if isVowel(key):
            pl_vowel_and_consonant_freq['vowel'] += pl_letter_freq[key]
        else:
            pl_vowel_and_consonant_freq['consonant'] += pl_letter_freq[key]
    for key in eng_letter_freq:
        if isVowel(key):
            eng_vowel_and_consonant_freq['vowel'] += eng_letter_freq[key]
        else:
            eng_vowel_and_consonant_freq['consonant'] += eng_letter_freq[key]
    for key in de_letter_freq:
        if isVowel(key):
            de_vowel_and_consonant_freq['vowel'] += de_letter_freq[key]
        else:
            de_vowel_and_consonant_freq['consonant'] += de_letter_freq[key]

    print('samogloski w jezyku polskim: ' + str(pl_vowel_and_consonant_freq['vowel']) + ', ' + 'samogłoski w jezyku polskim: ' + str(pl_vowel_and_consonant_freq['consonant']))
    print('samogloski w jezyku angielskim: ' + str(eng_vowel_and_consonant_freq['vowel']) + ', ' + 'samogłoski w jezyku angielskim: ' + str(eng_vowel_and_consonant_freq['consonant']))
    print('samogloski w jezyku niemieckim: ' + str(de_vowel_and_consonant_freq['vowel']) + ', ' + 'samogłoski w jezyku niemieckim: ' + str(de_vowel_and_consonant_freq['consonant']))

    print(whatLanguageVowelConsonant(pl_text, pl_vowel_and_consonant_freq, eng_vowel_and_consonant_freq, de_vowel_and_consonant_freq))
    print(whatLanguageVowelConsonant(eng_text, pl_vowel_and_consonant_freq, eng_vowel_and_consonant_freq, de_vowel_and_consonant_freq))
    print(whatLanguageVowelConsonant(de_text, pl_vowel_and_consonant_freq, eng_vowel_and_consonant_freq, de_vowel_and_consonant_freq))

    """Przy tak małej ilości tekstu, ciężej jest rozpoznać język,
    różnice między występowaniem spółgłosek i samogłosek są też znacznie mniejsze"""