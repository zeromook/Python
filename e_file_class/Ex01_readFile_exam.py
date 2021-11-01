""" [연습]
    함수 정의 : count_words
    인자 : filename

    인자로 받은 파일명을 open 하여 파일을 읽어서 단어를 수를 출력한다.
    존재하지 않는 파일명으로 예외가 발생해도 아무런 일을 하지 않는다
"""
def count_words(filename):
    try:
        with open('./data/'+filename, 'r', encoding='utf-8') as re:
            num = len(re.read().split())

    except FileNotFoundError as error:
        print('%s 파일은 존재하지 않습니다. 에러코드 - %s' % (filename,error))
    else:
        print('%s 파일의 단어수는 %d개 입니다' % (filename,num))


filenames = ['sample.xml', 'xxxx.xxx', 'temp.json']
for filename in filenames:
    count_words(filename)