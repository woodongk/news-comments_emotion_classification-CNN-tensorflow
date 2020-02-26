# Daum-News-Comments_Sentiment_Analysis
**다음(Daum) 뉴스 (2017. 7-12) 에서 수집한 댓글 데이터 2,393,070개에 대한 6가지 감정 분석 프로젝트**   
학부생 3,4 학년 시절 (2017.8 - 2018.5)에 연구 인턴을 하면서 진행했던 프로젝트입니다.


## 📖 Introduction
- 다음(Daum) 뉴스 (2017. 7-12) 에서 수집한 댓글 데이터 2,393,070개에 대한 6가지 감정 분석
- 인터넷 뉴스 댓글에 감정 사전을 적용하여 Ekman의 6가지 감정(‘기쁨’, ‘슬픔’, ‘혐오’, ’놀람’, ‘공포’, ‘분노’)으로 분류된 데이터셋 구축
- 댓글 감정 데이터셋을 바탕으로 CNN 기반의 감정 분석 모델을 구축하여 약 74%의 정확도를 달성

## 🐥 데이터 분석 과정

##### 1. 데이터 전처리

- 뉴스 데이터 크롤링
- 뉴스의 댓글 데이터로 word2vec 모델 학습시키기
    - `01. Train word2vec model.ipynb`

##### 2. 감정사전 적용 
- happy, sad, disgust, angry, surprised, fear 6가지 감정에 해당하는 감정 사전 데이터 불러오기 
    - 관련연구 ""
- 일정 비율 이상의 단어 등장 -> 댓글 데이터에 감정 레이블 달기 

##### 3. Train CNN Model   
- 
  

## Contact
- 김우정 [gks3284@ajou.ac.kr]
- 한재호 [woghrnt2@ajou.ac.kr]


