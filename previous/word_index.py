def get_word_to_int(token_data):
    unique_comment_tokenized = [list(i) for i in set(tuple(i) for i in token_data)]
    word_dic = {}

    for words in unique_comment_tokenized:
        for word in words:
            if not (word in word_dic):
                word_dic[word] = 0
            word_dic[word] += 1

    keys = sorted(word_dic.items(), key = lambda x: x[1], reverse = True)
    for word, count in keys[:15]:
        print("{0}({1}) ".format(word, count), end = "")

    # [] 없애주는 코드
    from itertools import chain
    words = set(chain(*unique_comment_tokenized))

    # create mapping of unique chars to integers
    word_to_int = dict((c, i) for i, c in enumerate(words))
    n_vocab = len(word_to_int)

    print("")
    print("Total Vocab: ", n_vocab)
    print("")
    comment_tokenized_int = []

    for comment in token_data:
        item_int = []
        for item in comment:
            item_int.append(word_to_int.get(item))
        comment_tokenized_int.append(item_int)

    return comment_tokenized_int, n_vocab, word_to_int