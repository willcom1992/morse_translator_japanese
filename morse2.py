#'data_morse.csv'から読み込み、モールス信号をキー、仮名をバリューとした辞書を作成
dict_morse = {}
with open('data_morse.csv', encoding='utf-8') as f:
    for row in f:
        columns = row.strip().split(',')
        morse = columns[1]
        kana = columns[0].replace('\u3000', '').replace('\ufeff', '')
        dict_morse[morse] = kana

print('短点は、（・）、長点は（-）、区切りは（ ）で入力してね！')
morse_signal = input()
print(morse_signal)
morse_sig = morse_signal.split(' ')

for key in dict_morse.keys():
    if key in morse_sig:
        n = morse_sig.index(key)
        morse_sig[n] = dict_morse[key]
    if key in morse_sig:
        n = morse_sig.index(key)
        morse_sig[n] = dict_morse[key]
answer = ''
for i in morse_sig:
    answer += i
print(answer)
