# 장고 심화. 

## RESTful API in Django

### json 

- Requests & Response data만 주고받는다. XML도 있다. 
- request를 보내면 json response를 보내주는 API를 만들자. (RESTful API server.)
- 자바스크립트 문법(객체) 대신 만국 공통형 자료형인 문자열로 보낸다. 이를 직렬화(Serializing)이라고 부른다. 
- Python Standard Library에 포함되어 import json으로 간단히 호출 가능하다.
- json.dumps(foobar_dic)를 통해 dictionary를 json으로 바꿀 수 있다. 
- json.loads(foobar_json)을 통해 역변환한다. 

### HTTP Request & Method

- HTTP는 통신규약이다. 대표적으로 get, post가 있다. 
- 더 다양한 methods가 존재한다. 
    - GET: 요청받은 URI의 정보를 검색하여 응답. 
    - POST: 요청된 자원을 생성(CREATE)함. 
    - PUT: 요청된 자원을 수정(UPDATE)함. 
    - DELETE: 요청된 자원을 삭제함. 
    - PATCH: 요청된 자원의 일부를 교체(수정)한다. 
    - OPTION: 웹서버에서 지원되는 메소드의 종류 확인. 
- HTTP Response의 종류
    - 1xx (정보): 요청을 받았고 프로세스를 계속한다. 
    - 2xx (성공): 요청을 성공적으로 받았으며 인식했고 수용했다. 
    - 3xx (리다이렉션): 요청 완료를 위해 추가 작업 조치가 필요하다. 
    - 4xx (클라이언트 오류): 요청의 문법이 잘못되었거나 요청을 처리할 수 없다. 
    - 5xx (서버 오류): 서버가 명백히 유효한 요청에 대해 충족을 실패했다. 

### HTTPie

- pip install httpie
- 명령어: http [flag] [METHOD] URL [ITEM [ITEM]] 마지막은 인자. 
    - POST, PUT 요청: =로 표현. 
    - GET 요청: ==로 표현. 
- json 형식 요청: http --json POST 대상주소 GET인자==값 POST인자=값
- http form 형식의 요청: http --form POST 대상주소 GET인자==값 POST인자=값 
- 인자는 모두 optional 하다. 
- json 형식으로 보냈을 때 data는 string화 되어 보내진다. 


### REpresentational State Transfer, REST Architecture

- HTTP를 이용해 통신하는 네트워크상에서 정한 약속. 분산 하이퍼미디어 시스템을 위한 소프트웨어 설계 형식
- 자원을 '대표'하는 단어/식별자로 자원의 '상태'를 '전송'하는 방법
- 자원을 일음으로 구분하여 상태를 전송하는 방법. post/1와 같이 첫 번 째 post라는 자원을 이름붙여 전송. 
- 다양한 서버와 클라이언트가 연결되어있는 네트워크에서 하위호환을 깨뜨리지 않고 독립적으로 발전할 수 있는 설계 방법. 뭐 하나가 업데이트 됐을 때 통신 규약만 지키면 문제 없이 소통 가능. 
- RESTful 필요충분조건: 
    - Server-Client 서버와 클라이언트가 존재
    - Stateless 클라이언트의 이전 상태를 기록하지 않는 연결방식
    - Cache 캐시 처리 기능
    - Uniform Interface 일관된 인터페이스 
    - Layered System 다층적 구성
    - Code-On-Demand JS처럼 서버에서 원격제어한 코드로 실행시킬 수 있는 것. 
- API는 웨이터와 같은 개념이다. RESTful 한 API를 만드는 것은 중요하다. 
- 요즘 API들은 완전히 RESTful하지는 못하다. 왜냐하면 Uniform Interface를 가지려면 아래 조건들을 충족해줘야 하는데,
    - Identification of Resources
    - Manipulation of resources through representations 
    - self-descriptive messages
    - hypermedia as the engine of application state (HATEOAS)
- 요즘 API들은 3,4는 잘 지키지 못한다. 
    - 3과 관련하여 json은 Host domain, Content type header, json 명세 등을 담고 있어야 하지만 보통 그렇지 않고 그냥 json만 보낸다. 
    - 4와 관련하여 원래 app의 상태는 예측 가능성과 투명한 정보 전이를 위해 하이퍼링크를 통해 전이되어야 하는데, 잘 쓰이지 않음. 

## JSON Serialization 

### (Model) Form vs (Model) Serializer

- 그냥 Django에 Form/ModelForm이 있다면 Django REST Framework에는 Serializer와 ModelSerializer가 있다. 
- 둘 다 Model로부터 Field를 읽어오고 유효성 검사를 해준다. 
- 하지만 Form은 HTML Form을 생성해주는 반면 Serializer은 JSON 문자열을 생성한다. 
- 즉, 둘은 전송가능 형식을 어떤 것으로 만드느냐의 차이일 뿐, 그 전후의 Field 생성이나 유효성 검사는 똑같이 한다. 

