## 다음(Daum) 뉴스 댓글 감정 분석 프로젝트

- 다음(Daum) 뉴스 포탈에서 수집한 댓글 데이터 2,393,070개에 대한 6가지 감정 분석
- 2018년 KHCI 학회 Best Poster Award
	- 한재호, 김우정, 한경식. (2018). 인터넷 뉴스 댓글 기반의 다중 감정 분석 모델 개발 및 적용. 한국HCI학회 학술대회, (), 893-897.
- 2018년 한국차세대컴퓨팅학회 최우수 논문 선정


### 1. 데이터 수집 및 전처리
- 뉴스 데이터 크롤링 (코드 없음)
- 뉴스의 댓글 데이터로 word embedding model 만들기 
	- 댓글 토큰화 and 특정 품사만 추출 
	- konlpy Twitter (Okt) 패키지 기준 ['Noun', "Verb", 'Adjective', "Adverb", "Determiner", "Exclamation", "Emotion"]
		- word2vec
		- fastText
	- 자모 단위 토큰으로 학습된 fastText
- [[Code]](https://github.com/woodongk/Daum-News-Comments_Sentiment_Analysis/blob/master/01.%20Word%20Embedding.ipynb)

### 2. 댓글에 감정 레이블 부여하기 
- 참고문헌 : 홍종선, 정연주. (2009). 감정동사의 범주 규정과 유형 분류. 한국어학, 45(), 387-420.
- 감정동사를 Ekman의 6가지 감정(‘기쁨’, ‘슬픔’, ‘혐오’, ’놀람’, ‘공포’, ‘분노’) 으로 분류하여 감성사전 구축
6 emotion : happy, sad, disgust, angry, surprised, fear
- [[Code]](https://github.com/woodongk/Daum-News-Comments_Sentiment_Analysis/blob/master/02.%20Labeling%20Emotions%20on%20Comments.ipynb)

### 3. Text-CNN 모델 구축
- 
  


### Contact
- 김우정 [gks3284@ajou.ac.kr]
- 한재호 [woghrnt2@ajou.ac.kr]
