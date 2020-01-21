#モールス信号をキー、仮名をバリュとした辞書を作成
dict_morse = {}
with open('data_morse.csv', encoding='utf-8') as f:
    for row in f:
        columns = row.strip().split(',')
        ka = columns[0]
        morse = columns[1]
        kana = ka.replace('\u3000', '').replace('\ufeff', '')

        dict_morse[morse] = kana

encryption = '-・-・--・-・・・・・-・-・-・・・--・-・・・-・--・---・----・--・'
en = encryption.strip()
#辞書のキーをkeyに代入していく

lis = []

for key in dict_morse:
    words = []
    en = encryption.strip()
    #keyが暗号文の先頭に一致するかどうか
    if en.startswith(key):
        #一致する場合、辞書のキーに対応するカナをwordsリストに追加
        words.append(dict_morse[key])
        lis.append(words)
        #暗号文の先頭からkeyを削除して、それを暗号文とする
        en = en[len(key):]

print(lis)

