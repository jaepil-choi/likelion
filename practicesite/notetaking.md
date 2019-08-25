# 환경 설정

## venv vs pipenv 

# 장고 강의

## project 시작

### project와 app 시작: hello world!

- 프로젝트를 시작하기 위하여 $ django-admin startproject 프로젝트_이름
- cd <프로젝트 이름 디렉토리> 후, $ python manage.py runserver 로 서버 동작 확인. 
- app. 프로젝트의 구성단위로, python manage.py startapp app_이름
- 만들어진 app 폴더 내에 templates라는 이름의 폴더를 생성한다. 
- app을 추가했으면 settings.py의 INSTALLED_APPS에 추가해줘야 한다. 형식은 app이름.apps.첫글자대문자app이름Config 그 이유는, app폴더의 apps.py에 가보면 첫글자대문자app이름Config 라는 이름의 Class가 선언되어있기 때문이다. 이 클래스를 연결시킨 것이다. 
- 이걸 잘못 쓰면 runserver 할 때 [WinError 123]이 뜬다. 하지만 진짜 문제는 에러메세지 중간의 ModuleNotFoundError: No module named 'practicesite.apps' 부분이다. 
- views.py에서 함수를 만든다. 일단 render로 간단히 작성한다. 
- 그리고 프로젝트 폴더 내의 urls.py를 통해 urlpatterns를 추가해준다. 이 때, 앱폴더 내의 views.py에서 쓰는 함수들을 쓰고싶으므로 이를 urls.py내에서 import 해준다. --> import practiceapp.views
- path('', practiceapp.views.home, name='home') 를 urlpatterns에 추가해주는데, 그 의미는 1st argument와 같은 pattern이 왔을 때 2nd argument의 함수를 실행하고 싶다는 것이고, 이 path 전체의 이름을 'home'이라고 하겠다는 것이다. 보통 이 url의 name은 함수와 동일한 이름으로 짓는 것이 convention이다. 이 때, url은 /로 마쳐준다. 

### MTV 패턴

- Model: DB, Template: show html, View: function (controller)
- MVC에선 Model: DB, View: show html, Cotnroller: function. MTV는 MVC를 차용. 

### wordcount 실습 

- Template 변수: {{ }}
- Template 필터: {{ value | filter}}
- Template Tag: html 상에서 파이썬 문법을 사용, url 생성 등의 기능 제공. {% %} 닫는 태그가 필요하다. 예를 들어 for 문을 쓴다면, {% for foo in bar %} ...을 한 다음에 끝에 {% endfor %}로 닫아줘야 한다. 
- Template Tag로 url을 생성할 수도 있다. {% url 'url_name' %}
- Template 상속 (추후 다룸)
- views.py의 render 함수는 render(request객체, 템플릿.html, 딕셔너리 객체) 
- href를 달 때, template tag를 사용하여 <a href="{% url 'about' %}">FOO</a> 이렇게 써줘야 한다. 
- html에서 tag의 name을 정해주면 이는 views.py에서 손쉽게 foo = request.GET['bar']를 통해 전달받을 수 있다. ROR에서 배웠던 params랑 비슷한 역할이다.
- views.py에서 결과값을 return하여 보낼 떄 render 내에서 3번째 파라미터로 방금 받은 parmas 같은 값을 딕셔너리로 매칭시켜 보낼 수 있다. {'spam': foo} 처럼. 이걸 html template에서 {{spam}} 으로 부를 수 있다. 
- 참고: app을 지우고 싶을 땐 어떻게 할까? 그냥 directory를 지우고 그 app이랑 연관된 코드들을 수동으로 지워준다. (https://stackoverflow.com/questions/11382734/how-to-delete-an-app-from-a-django-project)

## model & admin

### model & admin 이론

- 포인트1: Model의 DB를 Views로 어떻게 옮길 것인가? 
- 포인트2: Django Admin은 어떻게 이용하는가? 
- Models.py 안에 class로 데이터 형태를 설정한다. 
- DB는 Django와 별개이다. default는 sqllite3이지만 바꿀 수 있음. 
- $ python manage.py makemigrations 마이그레이션 파일을 만들고 / $ python manage.py migrate 만든 models.py를 적용시킴
- admin 계정 만들기: $ python manage.py createsuperuser 이후 admin.py에 데이터 등록

### model & admin 실습 (1)

- blog app을 새로 만들어 시작한다. INSTALLED_APPS에 추가해준다. 
- 우선 models.py에서 모델 class를 만든다. models.Model에서 상속을 받도록 한다. 
- 이후 이를 db와 연결시키기 위해 $ python manage.py makemigrations / $ python manage.py migrate 를 한다. 
- 이제 admin 계정을 만들기 위해 $ python manage.py createsuperuser 을 통해 admin 계정을 만든다. 
- admin.py에서 from .models import Blog 를 통해 모델을 import 해주고 admin.site.register(Blog) 를 통해 모델을 등록한다. 
- 그러면 Blog object(1)와 같이 생기는데, 이를 object가 아닌 title로 나타내기 위하여 models.py에 def __str__(self): \n return self.title 를 쓴다. 
- 이제 views.py에서 해당 모델의 데이터를 보낼 수 있도록 함수를 짜자. 우선 from .models import Blog 를 통해 import 후, def home(request): 이하 코드를 작성한다. 
- 이 때 Blog.objects 는 모델로부터 객체 목록을 전달받을 수 있도록 해준다. 이를 Query Set 이라고 부른다. 추후 이를 정렬하거나 기능을 표시해주는 것은 method를 통해 해준다. 
- 우선 url 연결을 위해 urlpatterns에 blog를 등록해준다. 물론 이 때도 blog.views 를 import 해줘야 한다. 안해주면 runserver에서 오류가 나고, pylint로도 표시가 된다. (일단 home으로)
- 참고: pylint는 때로 Django 상의 logic을 오류로 표시할 때가 있다. (models.py에서 Blog class가 명시적으로 .objects 메소드를 가지가 있지 않으므로 그냥 오류로 표시함.)
- .html에서 전달된 {{blog}}와 같이 표시하면 오브젝트 객체명만 뜬다. 이 안의 콘텐츠를 가져오기 위해선 Query set method를 써줘야 한다. 
- Query set method는 [모델.쿼리셋objects.메소드] 의 형식을 가진다. .all, .count, .first, .last 등 여러 가지가 있다. 추후 정리한다. 
- 중요 참고: settings.py의 INSTALLED_APP의 순서는 중요하다. 이를 순서대로 읽어 처리하기 때문에 홈페이지에 올 것을 가장 먼저 적어주는 것이 좋다. 또한 namespacing도 중요하다. 같은 'home'이라고 naming을 하면 추후 잘못 reference 되는 등의 문제가 생길 수 있다. 따라서 최대한 explicit하게 namespacing을 하여 표현해 주는 것이 중요하다. 
- VSCode Django extension 참고: Django extension (by Baptiste Darthenay)를 설치하면 {% %} template tag 내의 python syntax highlighting이 가능하다. 하지만 이를 설치하면 /templates/*.html들은 django-html으로 분류되어 emmet(자동완성)이 꺼지게 되는데, 이를 켜주기 위해선 VSCode의 settings.json (globally 적용되는 User settings) 에서 "emmet.includeLanguages": {"django-html": "html"}, 를 추가해줘야 한다. (VSCode extension 페이지 참조. https://marketplace.visualstudio.com/items?itemName=batisteo.vscode-django)

### bootstrap 보강

- Bootstrap은 CDN을 쓴다. (<head></head> 내에 포함 )
- https://getbootstrap.com/
- https://startbootstrap.com/

### model & admin 실습 (2)

- 1. pk --> Primary Key. x 번째 블로그 객체를 넘버링하기 위해 필요
- 2. path Converter --> /blog/1 이런 식으로 여러 객체를 다루는 계층적인 url path를 자동생성할 때 유리. /<타입:변수이름> 과 같은 형식. views.py에서도 request외의 인자로 전달해줘야 한다. 
- 3. get_object_or_404 --> 404. get_object_or_404(어떤클래스, 검색조건) 검색조건에 pk 사용 가능. views에서 사용하기 전에 render와 같이 import 해줘야 함. 
- 우선 views.py에서 def detail(request, blog_id) 를 통해 detail.html에 블로그 내용 객체를 render를 통해 보내준다.
- url 상에서 이 동작을 수행하기 위해 path를 pk를 이용하여 적어준다. 
- detail.html에서 views에서 받은 객체를 통해 렌더한다. 
- home.html에서 a태그를 통해 path converter로 이동시키려면, blog.id 를 통해 블로그 객체의 번호를 표시해준다. {% url 'detail' blog.id %}
- 이제 admin이 아닌 home에서 새 글을 작성하면 글이 띄워지도록 해보자. 
- home.html에서 우선 bootstrap CDN을 넣어준 후 버튼을 만들어 new.html로 갈 수 있는 글쓰기 버튼을 만든다. 
- views.py에서 def new(request) 를 통해 new.html을 render 해준다. 
- /templates 에 new.html을 만들고 <form action={% url 'create' %}> 이하 코드를 작성한다. 여기서 {%%}는 ""로 감싸줘도 되고 안감싸줘도 둘 다 작동한다.
- views.py에서 def create(request) 를 통해 새 글 작성 함수를 써준다. DB에 저장될 빈 클래스 인스턴스 blog=Blog()를 만들고 request를 통해 form에서 저장되어 날라온 title과 body를 .GET['foo'] 해준다. 그리고 .save() 해준다. 그리고 글을 저장했으니 방금 쓴 글 화면으로 redirect 해준다. (redirect도 import 해줘야 한다.)
- 간단히 말해 redirect는 render과 달리 프로젝트 외의 외부 url로도 연결 가능. 쓰임이 다르다. 

## 여러 파일 다뤄보기

### 포트폴리오 만들기

