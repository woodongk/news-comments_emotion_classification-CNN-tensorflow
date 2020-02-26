import pandas as pd
import numpy as np
from konlpy.tag import Okt

def load_data(path):
    """
    :param path: 파일 주소
    :return: 뉴스 댓글 dataframe
    """
    # mac
    all_daum_txt = open(path, 'r',encoding='cp949')
    i = 0
    news_id = []
    comment_id = []
    comments = []

    while True:
        line = all_daum_txt.readline()
        if not line: break
        n_id = line.split("|$|")[0]  # news_id
        news_id.append(n_id)
        c_id = line.split("|$|")[1]  # comment_id
        comment_id.append(c_id)
        temp = line.split("|$|")[4]  # comment
        comments.append(temp)
        i += 1

    print(i)
    print("@@@@@@")

    daum_data = pd.DataFrame([news_id, comment_id, comments])
    daum_data = daum_data.T
    daum_data.columns = ["news_id", "comment_id", "comment"]
    return daum_data


def tokenize_comment(comment):
    """ 
    ** 참고 - konlpy.Okt 패키지 사용 **
    
    :param comment: 뉴스 댓글 문장 하나
    :return: 문장을 token단위로 쪼갠 후 리스트로 반환
    
    """
    okt = Okt()
    i = 0
    malist = okt.pos(comment)
    r = []

    tag = ["Noun", "Adjective"]
    stopwords = ["것", "이", "안", "더", "왜", "때", "좀", "뭐", "거", "저", "뿐", "머"]

    try:
        for word in malist:
            # 어미/조사/구두점/ㅋㅋ^^ㅎㅎ/음표살림/Alphabet/부사는 대상에서 제외
            if word[1] in tag:
                if not (word[0] in r) and not (word[0] in stopwords):
                    # 숫자, 특수문자 제거.
                    r.append(word[0])
        return r

    except Exception as e:
        print(e)


def count_comment(token_data):
    unique_comment_tokenized = [list(i) for i in set(tuple(i) for i in token_data)]
    word_dic = {}

    # word count
    for words in unique_comment_tokenized:
        for word in words:
            if not (word in word_dic):
                word_dic[word] = 0
            word_dic[word] += 1

    keys = sorted(word_dic.items(), key = lambda x: x[1], reverse = True)
    for word, count in keys[:50]:
        print("{0}({1}) ".format(word, count), end = "")

    # [] 없애주는 코드
    from itertools import chain
    words = set(chain(*unique_comment_tokenized))

    n_vocab = len(words)
    print("")
    print("Total Vocab: ", n_vocab)
    print("")

    return keys, n_vocab