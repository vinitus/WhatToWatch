# WhatToWatch

OTT 플랫폼을 종합한 컨텐츠 추천 웹 사이트

### team

**강신욱 - PE, 소셜 로그인, ERD, 검색 자동 완성**
**이준혁 - BE, 추천 알고리즘**

### 서비스 초기 구현 목표
- 고객 맞춤 추천을 위한 interaction 요구를 게임같은 재미 요소를 반영(명대사 맞추기, 포스터 보고 영화 제목 맞추기 등)
- 아이템 기반 추천, 유저 기반 추천 구현
- 검색 자동 완성 기능 구현
- 영화 탭, 시리즈 탭 나눠서 구현
- 현재 상영관에서 개봉중인 영화 순위 보여주기
- 가로 스크롤 기능
- DB에 데이터 많이 채우기


### 실제 구현
- OTT사이트 인기 컨텐츠 목록 보여주기
    - 크롤링을 통한 데이터 수집(넷플릭스, 왓챠)
- 추천을 위한 interaction => 본 영화 고르기로 수정
- 아이템 기반 추천 X
- 장르, 배우, 감독, 유저 유사도 추천 O
- 검색 자동 완성 기능 구현(초성 검색도 가능)
- 시리즈 X, 영화 O
- 가로 스크롤 구현
- 영화, 배우, 감독 데이터 80만개 이상 저장


### 추천 알고리즘 설명

1. 유저의 영화 취향 수집을 위한 interection
    - 유저의 평점을 입력받는 것 대신 영화 시청 유무를 통해서 유저가 흥미를 갖는 장르나 배우, 감독을 선정하여 추천하기로 함
2. 장르 기반 추천
    - 유저가 제출한 본 영화 목록을 DB에 요청해서 장르 count -> 가장 많이 나온 장르를 선호하는 것으로 가정.
    - DB 목록에 영화들 중 선호 장르의 영화 & popularity 50 이상으로 필터링 후 남은 영화 추천
3. 배우 기반 추천
    - 장르 기반 추천과 마찬가지로 장르를 배우로 바꾸어 점수계산 & 추천
4. 감독 기반 추천
    - 2, 3과 동일
5. 유저 유사도 기반 추천
    - 모든 유저를 row, 모든 유저의 본 영화 목록을 column으로 table을 만들어서 영화를 봤으면 1, 안봤으면 0으로 설정
    - 코사인 유사도를 계산하여 가장 유사한 유저가 본 영화들 중 로그인 한 유저가 시청하지 않은 영화들을 추천

### 서비스 대표 기능
1. 소셜 로그인(카카오)
2. OTT별 인기 영화 확인 가능
3. 사용자의 영화 시청 데이터를 기반으로 맞춤 추천 기능
4. 영화 검색 가능
5. 영화 Detail 페이지에서 찜, 봄, 선택 후 프로필에서 확인 가능
6. 영화 별 제공하는 OTT사이트 확인 가능


### 배포 진행 중...

### 프로젝트를 통해 느낀 점

1. 소통의 중요성
    - 코드를 공유하기 때문에 서로 어느 부분을 맡을 것인지, 데이터는 어떻게 넘겨줄 것인지, 브랜치는 어떻게 파고 merge할 것인지 등등.. 끊임없이 소통을 통해서 소통의 부재로 인한 불상사를 방지할 수 있었다.

2. 기획의 중요성
    - 처음에 프로젝트의 기획을 나름 잘 작성하고 따라간다 생각했지만, 예상치 못한 부분에서 시간이 많이 소요되면서 자칫 잘못하면 MVP기능을 구현하지 못할 뻔 했다.
    - 그래도 초반에 기획을 잘 작성했기에 남은 시간과 구현 정도를 살펴가면서 프로젝트를 잘 마칠 수 있었다.

3. 중요한 것은 꺾이지 않는 마음
    - 실제로 프로젝트 진행 중에 사소한 것에 막히고, 실수로 많은 시간을 날리고.. 의지가 점점 꺾여 갈 때 옆에서 묵묵히 자신의 역할을 다하고 있는 동료를 보면서 버틸 수 있었던 것 같다. 