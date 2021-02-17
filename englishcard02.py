import random
from termcolor import colored

d = {'cat': 'ネコ', 'dog': 'イヌ', 'rabbit': 'ウサギ'}

template = '*' * 15 + '\n英単語：{}\n日本語訳を入力してください！\n' + '*' * 15

while True:
    # 英単語を表示する
    word = random.choice(list(d.keys()))
    print(colored(template.format(word), 'yellow'))

    # 自分が日本語を表示する
    answer = input()
    # 自分の日本語と、答えが合っているか確認する
    if answer == '0':
        print('~~終了します~~')
        break
    elif answer == d[word]:
        print(colored('正解！', 'blue'))
    else:
        print(colored('不正解', 'red'))


