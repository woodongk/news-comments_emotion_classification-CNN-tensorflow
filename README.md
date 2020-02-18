# Daum-News-Comments_Sentiment_Analysis
다음(Daum) 뉴스 (2017. 7-12) 에서 수집한 댓글 데이터 2,393,070개에 대한 6가지 감정 분석

## Researcher
- 김우정 [아주대학교 컴퓨터공학과 / gks3284@ajou.ac.kr]
- 한재호 [아주대학교 컴퓨터공학과 / woghrnt2@ajou.ac.kr]

## 연구 기간
[2017.8 - 2018.5]
학부생 3,4 학년 시절에 연구 인턴을 하면서 진행했던 프로젝트. 리마인드 차원에서 깃허브에 자료와 코드를 정리하려함. 

## 프로젝트 요약
- 다음(Daum) 뉴스 (2017. 7-12) 에서 수집한 댓글 데이터 2,393,070개에 대한 6가지 감정 분석
- 인터넷 뉴스 댓글에 감정 사전을 적용하여 Ekman의 6가지 감정(‘기쁨’, ‘슬픔’, ‘혐오’, ’놀람’, ‘공포’, ‘분노’)으로 분류된 데이터셋 구축
- 댓글 감정 데이터셋을 바탕으로 CNN 기반의 감정 분석 모델을 구축하여 결과적으로 약 74%의 정확도를 달성

## 프로젝트 순서

### 1. 크롤링한 데이터 정리 
  1. news_token_word2vec
  다음 뉴스 댓글 데이터를 불러오기
  댓글 tokenizer하기 (명사 추출)
  최종 데이터 형태: news_id, comment_id, comment, token
  gensim의 word2vec 활용 (size 200)
  word2vec model 저장

### 2. 감정 사전 적용
 2. emotion_data
  happy, sad, disgust, angry, surprised, fear 감정 사전 불러오기
  토큰화 된 데이터에서 6가지의 감정 비율이 어느정도 되는지 확인
  일정 비율 이상으로 토큰화 데이터에 감정 레이블 달기
  D:\\WorkSpace\\뉴스 데이터\\id_emotion661245_0403.pickle -> total data
  
### 3. CNN Model
  3. word_index
  embedding layer에 붙이기 위한 word_index 만드는 파트
  D:\\WorkSpace\\뉴스 데이터\\word_index0327.pickle -> word_index file
  4. modeling
  각 감정마다 만개씩 추출
  one-hot encoding으로 y값 설정
  embedding_matrix 설정 -> (총 단어 수, 차원 수)
  pad_sequence(20)으로 문장 길이 채움
  embedding layer의 weights는 embedding_matrix로 설정
  그 후 Conv layer 결합
