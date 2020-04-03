from itertools import chain

def get_word_embedding(comment_tokenized_int, word_embedding_model):
    # 토큰으로 이루어진 리스트 (문장 X, 단어만으로)
    tokens_data = list(chain(*comment_tokenized_int))

    # None 제거
    remove_none_comment_tokenized_int = comment_tokenized_int.copy()

    times = 0
    for i in range(0, 100):
        p_count = 0
        i = 0
        times += 1
        temp = []

        for line in remove_none_comment_tokenized_int:
            j = 0
            for word in line:
                if word == None:
                    # print ("i : {0}, j: {1}".format(i,j))
                    temp = remove_none_comment_tokenized_int[i].pop(j)
                    p_count += 1
                j += 1
            i += 1
        print("p_count: ", p_count)
        print("times: ", times)

        if p_count == 0: break

    print("")
    print("p_count: ", p_count)
    print(len(comment_tokenized_int2))
    print15(comment_tokenized_int2)

    # 문장 별로 아니고 풀어 헤쳐서 모은 것.
    all_word_index = []

    for tokens in comment_tokenized_int2:
        for token in tokens:
            all_word_index.append(token)

    print(len(all_word_index))
    print(type(all_word_index))
    print15(all_word_index)

    # Word2Vec 사용
    empty = 0
    w2v_embedding = []
    w2v_temp = []  # 문장 별로 아니고 풀어 헤쳐서 모은 것.

    # Word2vec embedding
    for tokens in total_token_data:
        w2v_line = []
        for token in tokens:
            try:
                temp = w2v_model[token]
                w2v_line.append(temp)
                w2v_temp.append(temp)
            except:
                # 단어 없을 때 None 추가
                w2v_temp.append(None)
                # w2v_line.append([])
                empty += 1

        w2v_line = np.array(w2v_line)

        if w2v_line.size > 0:
            w2v_embedding.append(w2v_line)
            # print(w2v_line.mean(axis=1))
            # w2v_embedding_mean.append(w2v_line.mean(axis=0))
        else:
            # w2v_embedding_mean.append([])
            w2v_embedding.append([])

    print("")
    print("len: ", len(total_token_data))
    print("empty: ", empty)

    print("")
    print("check word embedding")
    i = 0
    for a in w2v_embedding:
        i += 1
        print(a)
        print("")
        if i > 3: break

    print("")
    print("w2v_temp")
    print(type(w2v_temp))
    print(len(w2v_temp))
    print15(w2v_temp)

    # embeddings_index = { 단어 : W2V(단어) }
    embeddings_index = {}
    embeddings_index = dict(zip(tokens_data, w2v_temp))
    i = 0

    print("")
    for word, value in embeddings_index.items():
        print(word, value)
        print("")
        i += 1
        if i > 3: break

    # None 갯수 측정
    count = 0
    i = 0
    print("")
    print("embeddings_index: ", len(embeddings_index))

    for word, value in embeddings_index.items():
        if value is None:
            count += 1

    print(count)

    # embedding_matrix 초기화
    EMBEDDING_DIM = 200

    # word_index = 단어에 index 부여
    embedding_matrix = np.zeros((len(word_index), EMBEDDING_DIM))
    print("embedding_matrix.shape: ", embedding_matrix.shape)
    for word, i in word_index.items():
        embedding_vector = embeddings_index.get(word)
        if embedding_vector is not None:
            embedding_matrix[i] = embedding_vector

    print("")
    print("embedding_matrix.shape: ", embedding_matrix.shape)
    print(embedding_matrix.shape)
    print15(embedding_matrix)
