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

### 실습

- pip install djangorestframework 를 한다. 
- 프로젝트 시작 후 settings.py의 INSTALLED_APPS에 'rest_framework'를 등록해준다. 
- 생성한 앱도 등록해준다. 일단 post 앱이면 'post'만 추가하도록 한다. 
- 프로젝트 폴더의 urlpatterns에 include를 사용해 post의 urls를 등록해준다. 
- models.py에서 간단한 모델을 만들어준다. 
- makemigrations, migrate 해준다. 
- post app 폴더 내에 serializer.py를 만들고 모델(Post)과 rest_framework의 serializer를 불러온다. 
- 그리고 form에서 만들었던 것 처럼 class를 만든다. 
- 이제 views.py를 작성한다. 이 때, 만들었던 Post와 PostSerializer와 함께 rest_framework의 viewsets를 import 해주도록 한다. 
- PostSerializer를 사용해 간단히 PostViewSet class를 작성한다. 이는 REST API의 CRUD를 담당하는 것이라 생각하면 된다.   
- 이제 post의 urls.py에서 DefaultRouter를 import 해준다. 만들어놓은 views도 import 해준다. 
- Django rest framework에선 router를 통해 url을 처리한다는 것을 기억하자. 
- views에서 router 를 만들고 이를 register 해준다. 이는 위에서 만든 PostViewSet을 바탕으로 routing을 하는 것이다. 그래도 실제로 url을 결정하는 것은 urlpatterns의 path이다. 
- runserver을 하면 API Root로 가게 된다. 
- 여기서 GET 요청, POST 요청 모두 해볼 수 있다. 다만 post로 보낸 객체가 pk가 없는데, 이는 serializer.py에서 'id'를 추가해주면 된다. (또는 __all__로 해도 된다.)
- 특정 항목에 대해 read_only를 설정할 수 있다. (id는 기본적으로 read_only=True이다.) 이를 위해 serializer.py에서 read_only_fields = (foo,) 형식으로 튜플을 추가해준다. 한 개만 적더라도 꼭 ,를 적어줘야 튜플로 인식된다. 
- 같은 방법으로 write_only_field 도 가능하다.  

## Viewset & Router

### ViewSet에 이르는 과정. 

- 뷰를 간략화하는 과정을 알아보자. 
- APIView --> Mixins --> Generic CBV --> ViewSet 순으로 코드 복잡도는 낮아진다. 
- 상속하는 관계이기 때문에 상위 개념을 알아야 한다. 

### APIView

- 현재의 과정은 모두 django-rest-framework.org/tutorial 의 내용을 바탕으로 한 것임. (현재 3. CBV tutorial)
- APIView를 상속하여 View를 설계할 땐 status와 response를 import 해 직접 응답과정을 만든다. 
- APIView를 상속해 내 View class를 만들 땐 각 함수를 내가 쓰고자 하는 http method로 def 해준다. (def get 와 같이.)
- 그리고 그 method를 어떻게 처리할 지 내가 직접 코드를 짜는 것이다. 그것이 APIView를 상속해 직접 class를 짜는 의의이다. 
- views.py에서 PostList(APIView)를 만들 때, serializer를 many=True로 해줘야 한다. 일단 기억만 하자. 


### mixins

- 대부분의 API의 모델 논리는 비슷하다. List, Detail 등 비슷하다. 따라서 각 모델마다 이런 API 논리를 반복해주는 것은 낭비다. 여기서 탄생한게 mixins이다. 즉, 상속을 통해 또 중복을 제거한다. 
- 이제 views.py에서 rest_famework의 mixins와 generic을 import 한다. 
- 이제 기존의 view를 세 mixins에서 상속하게 만든다. class SnippetList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView): 그러면 이제 내 view를 여러 mixins에서 동시 상속을 하는 class로 만들 수 있다. 
- 그러면 이제 각 get, post 등의 매소드가 한 줄짜리 리턴이 될 수 있다.
- 그 이전에 class variable로 queryset = Snippet.objects.all() 그리고 serializer_class = SnippetSerializer 와 같이 선언을 해줘야 한다. 
- 이는 기존 rest_framework의 소스코드를 보면 알 수 있는데, GenericAPIView에는 둘 모두 일단 =None으로 정의되어 있기에 이를 우리 모델에 맞게 초기화 시켜주는 것이다. 
- 상속을 받았기 때문에 한 줄 return에 self.list와 self.create를 쓸 수 있다. 이들은 이름에서 볼 수 있듯 각각 .ListModelMixin, .CreateModelMixin에서 상속받은 매소드들이다. 
- 이들은 내부적으로 기존에 강의에서 manual하게 코딩해주었던 list해주는 동작과 (.is_valid를 확인 한 다음 동작하는) create 해주는 동작과 매우 유사함을 알 수 있다. 우리가 가져다 쓰는 method는 그렇게 동작하는 것들이다. 
- SnippetDetail에서도 똑같이 여러 메소드를 가져다 쓸 수 있다. 특정 post의 content를 get하는 것에 대해선 retrieve를, put하는 것은 update를, delete는 destroy를 쓴다. 

### generic CBV

- mixins를 써서 간단히 설계했지만, mixin조차도 생략하고 generic CBV로 더 쉽게 설계할 수 있다. 
- 이번엔 rest_framework로부터 mixin이 아닌 generics를 import 해온다. 
- 이제 generic.ListCreateAPIView와 generic.RetrieveUpdateDestroyAPIView 를 가져다 쓴다. 그 내부는 어떻게 생겼을까? 
- SnippetList와 SnippetDetail 둘 다 여전히 최초의 초기화는 필요하지만, 그 내부는 결국 이전에 했던 mixins를 합친 모양이 될 것이다. .ListCreateAPIView의 소스코드를 참고하면, mixins 실습에서 했던 것과 완전히 같은 모양의 self.list, self.create를 가지고 있다. 
- 즉, view를 설계할 때 내가 어느 것이 필요한가? 를 생각하고 만들어주면 된다. 

### ViewSet

- 마찬가지로 공식 튜토리얼을 참고한다. 
- ViewSet은 소스코드를 보며 이해해보자. ViewSet은 말 그대로, literally, view클래스를 set, 즉 묶은 것이다. 소스코드 상에서 class GenericViewSet(ViewSetMixin, generics.GenericAPIView): 를 상속받은 후 이하의 내용은 pass 밖에 없으며 단지 두 클래스를 동시 상속 받는다는 것 자체가 이 ViewSet을 정의한다. 묶어주는 것에 불과하다. 
- 총 4개의 ViewSet이 있지만, ReadOnlyModelViewSet과 ModelViewSet만 다뤄보자. 나머지 ViewSet과 GenericViewSet은 이것만 배우면 자동적으로 이해된다. 
- ReadOnlyModelViewSet은 먼저 retrieve하고 이를 list하는, 또 말 그대로 read-only한 기능을 수행한다. 
- 이제 이를 views.py에서 import한다. rest_framework의 viewsets를 import하면 된다. 
- 참고: @+함수들 --> decorator이다. 개념을 알아두자. 
- ViewSet을 쓰면 CRUD는 간단히 할 수 있다는 것을 알았는데, CRUD외의 로직을 함께 쓰고 싶으면 어떻게 해야할까? 나의 custom api는 어떻게 쓸까? 
- custom api를 위해서 view에서 rest_framework.decorators에서 action을, rest_framework.response에서 Response를 import해준다. 
- 이 때 @action decorator을 사용한다. 여기서 어떤 rederer을 쓸지 정하는 등 설정이 가능하다. 
- 대표적으로 JSONRenderer, BrowsableAPIRenderer을 많이 사용한다. 
- custom api는 default로 get 방식으로 처리가 되는데, 다른 방식을 원하면 action의 methods= 인자로 지정 가능하다. 
- custom api는 마음대로 작성하면 된다. 이 때 url은 highlight가 custom api라면 이대로 하면 자동으로 post/2/highlight와 같은 식으로 나오는데, 이에 유의하여 url을 설계하자. 

### Router

- urlpatterns에서 router로 발전하는 과정을 살펴보자. 
- ViewSet은 하나의 path 함수로 처리할 수 없다. ReadOnlyModelViewSet은 pk를 필요로 하지 않고 ModelViewSet은 pk를 필요로 하는 것 부터 서로 다른 모양새를 띈다. 
- 따라서 여러 path를 묶어줘야 한다. == path의 두 번째 인자로 묶는다. 
- path(요청처리할url, 요청을인자로받아처리할함수, namespace) 이기 떄문에 2번째 인자에 list(), create(), retrieve() 등의 함수를 묶어야 한다. 
- 이는 as_view()를 통해 할 수 있다. as_view({'http메소드':'처리할함수'})와 같은 꼴로 넣어주면 된다. 
- 이런 mapping 역시 redundant하기에 router가 있는 것이다. 
- 이는 router=DefaultRouter()을 선언한 뒤 router.register(r'prefix가될단어', vies.SnippetViewSet) 와 같이 사용한다. 
- 후반부의 설명은 실습 없이 진행되었고 설명이 부실하기 때문에 Official documentation의 tutorial을 직접 참고할 필요가 있다. 