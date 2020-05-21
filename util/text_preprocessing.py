import pandas as pd
import numpy as np
from konlpy.tag import Okt
from konlpy.tag import Mecab

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

def load_news_data(path):
    """
    :param path: 파일 주소
    :return: 뉴스 dataframe
    """
    # mac
    all_daum_txt = open(path, 'r',encoding='cp949')
    i = 0
    news_id = []
    news_title = []
    news_content = []

    while True:
        line = all_daum_txt.readline()
        if not line: break
        n_id = line.split("|$|")[0]  # news_id
        news_id.append(n_id)
        n_title = line.split("|$|")[1]  # news_title
        news_title.append(n_title)
        n_content = line.split("|$|")[2]  # news_contents
        news_content.append(n_content)
        i += 1

    print(i)
    print("@@@@@@")

    daum_news_df = pd.DataFrame([news_id, news_title, news_content])
    daum_news_df = daum_news_df.T
    daum_news_df.columns = ["news_id", "title", "content"]
    return daum_news_df


def tokenize_okt(comment):
    """
    ** 참고 - konlpy.Okt 패키지 사용 **

    :param comment: 뉴스 댓글 문장 하나
    :return: 문장을 token단위로 쪼갠 후 리스트로 반환

    """
    okt = Okt()
    malist = okt.pos(comment, norm=True, stem=True)
    r = []

    tag_list = ['Noun', "Verb", 'Adjective', "Adverb", "Determiner", "Exclamation", "Emotion"]

    # 불용어 추가
    stopwords = ['하다', ',', '들', '이', '..', '.', '것', '다', '이다', '~', '그', '그녀', '저', '...', '"', '~~']

    try:
        for word, tag in malist:
            if tag in tag_list:
                if not word in stopwords:
                    r.append(word)
        return r
    except Exception as e:
        print(e)

def tokenize_mecab(sentence):
    mecab = Mecab()
    result = [x for x in mecab.nouns(sentence) if len(x)>1]
    return result


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