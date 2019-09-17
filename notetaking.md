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

### 포트폴리오 만들기 (static file 다루기)

- static file vs dynamic file 
- static file: 미리 서버에 저장되어 있어 서버에 저장된 그대로를 서비스해주는 파일
    - "static" 개발자들이 미리 준비해 둔 파일
    - "media" 웹 서비스 이용자들이 업로드하는 파일
- dynamic file: 서버의 데이터들이 어느 정도 가공된 다음 서비스 되는 파일. (상황에 따라 받는 내용이 달라질 수 있음.)
- Static file의 처리과정: 
    - 1. static file의 위치를 찾고: app폴더 안에 static 폴더 만들고 그 안에 파일 넣기. 
    - 2. static file들을 한 곳에 모은다. settings.py에서 static 폴더 위치 지정하고, $ python manage.py collectstatic으로 한 곳에 모으기. 그리고 html에서 static파일 사용을 선언. 
- settings.py에서 앱 등록, templates 폴더 생성, html 페이지 생성, views.py에서 render 함수 만들고 urls.py에서 portfolio/ path 설정 등은 알아서 해준다. 
- 만든 app 폴더 안에 static 폴더를 만든다. 
- 이제 settings.py에서 STATICFILES_DIRS와 STATIC_ROOT 를 선언해준다. 
- STATICFILES_DIRS는 path를 join하는 것이기 때문에 namespacing하듯 상위폴더부터 순서대로 static이 들어있는 곳을 적어준다. static 파일들이 현재 어디에 있는지 쓰는 것. 
- STATIC_ROOT는 static파일들이 어디로 모일지 써주는 것이다. 경로를 보면 base directory의 최상위 static 폴더에 모여야 한다는 것을 알 수 있다. 이는 따로 만들어줄 필요 없이 collectstatic 명령 시 디렉토리가 생성된다. 
- 이제 $ python manage.py collectstatic을 해준다. 
- html에는 staticfiles 사용 선언을 해준다. {% load staticfiles %}
- static파일을 <img> 에 넣어 사용하려면 <img src="{% static 'foo.jpg' %}"> 와 같이 하면 된다. 

### 포트폴리오 만들기 (media file 다루기)

- static 파일은 외부와의 통신이 없는데, media 파일은 외부와의 통신이 있다. 사용자가 올리는 파일이니까. 
- settings에서 MEDIA_URL과 MEDIA_ROOT를 설정해줘야 한다. 
- MEDIA_URL은 media파일이 어떤 url을 타고 가야 하는지, MEDIA_ROOT는 STATIC_ROOT처럼 어디로 모을 것인지를 설정한다. 
- MEDIA_ROOT는 base directory 다음의 /media로, MEDIA_URL은 /media/ 로 해준다. 
- urls.py에서 django.conf에서 settings와 static을 import 해줘야 한다. 
- urls.py에서 url을 추가할 때도 list에 병렬적으로 더해 path를 추가해준다. 
- 이제 사용자가 url을 타고 들어오는 것 까지는 완성이 되었으니 DB를 추가해준다. models.py에서 .ImageField를 가진 Portfolio model을 만든다. 이 때, upload_to는 'images/' 로 해준다. 이는 media directory 하위로 가게 된다. 
- 이미지를 데이터베이스에 넣고 싶을 땐 pillow 라이브러리를 추가적으로 설치 해주어야 한다. 파이썬으로 이미지를 효율적으로 처리할 수 있게 해주는 라이브러리. 원래는 pil(python image library) 였다. 
- admin.py에서 Portfolio 를 import하고 등록해준다. 
- portfolio을 모든 객체를 띄우도록 views.py를 수정한다. 
- 이제 html에서 이를 써주는데, 여러 장을 순서대로 출력할 것이기 때문에 for문으로 반복시키고 <img src="{{ portfolio.image.url }}">로 써준다. .url을 붙여줘야 한다는 사실에 주의하자. 


### template 상속

- redundant한 html header, template 상속으로 중복을 줄이자. base.html을 써야 한다. (특히 navbar는 redundant해지면 링크도 다 따로 설정해줘야 해서 매우 비효율적이 된다.)
- 프로젝트 폴더에 templates 폴더 생성 후 안에 base.html을 만들고 여기에 공통코드를 넣고 settings.py에 base.html 위치를 알려주고 상속받는 html들에서 겹치는 내용들을 삭제하고 base.html을 불러오면 된다. 
- base.html에서 공통된 부분을 작성해주고, (bootstrap CDN, navbar 등)  body 부분엔 template tag의 block을 이용해 어떤 컨텐츠 블록이 올 것인지 정해준다. {% block contents %} 와 같이 해주면 되고, contents 대신 title 등이 와도 된다. 
- 이제 자식 html들에 가서 공통된 부분을 지워주고 {% extends 'base.html' %}을 통해 공통 html을 받아온다. 

### url 관리

- 전체 url의 관리를 위해 각 app 관련 url을 각 app에 넣는 것이 효율적일 것이다. 모든 것을 settings.py에 넣기에는 불편하다. 
- app폴더 안에 urls.py를 만들고 똑같이 urlpatterns를 선언한다. (필수적인 것들 import 해야.) 그리고 blog/ 를 제외한 경로를 그대로 적는다. (이미 app 안에 있으니까.)
- 그리고 settings.py에서도 ...import path, include 로 include를 추가 import 해주고 기존 blog/ url 대신 path('blog/', include('blog.urls')) 로 대체해준다. 

## 계정정보 다루기 / pagination

### 회원가입 로그인 로그아웃 함수 만들기 

- views.py에서 함수로 처리한다. ...import User, ...import auth 를 해준다. 
- User는 마치 model 처럼 새로운 데이터를 생성하는 것. 
- auth는 로그인, 로그아웃을 담당한다. 

### 참고: HTTP method

- 정보를 주고받는 방식, 왜 method를 나누는 것인가? 
- form action 으로 그냥 url을 보냈을 때 따로 method를 지정하지 않았으니 GET을 쓴 것이다. 그리고 request.GET['foo'] 를 통해 데이터를 가져온 것이다. 
- 여러 방식이 있다. 
    - 데이터 조회: GET
    - 데이터 생성: POST
    - 데이터 수정: PUT
    - 데이터 삭제: DELETE

### 실습

- blog의 views.py에서 User와 auth를 import하고 signup, login 함수를 만든다. 
- login/signup 페이지에서는 form에서 method='POST'로 전달하고 이하 {% csrf_token %} 를 적어 보안상 csrf를 대비해줘야 한다. 

### pagination (1)

- Django에서 제공하는 paginator를 import하고 
- views.py 에서 어떤 객체를 한 페이지 당 몇 개씩 pagination 시킬 것인지 결정하고 (by paginator) 특정 페이지를 가져온다. (by .get_page(n)) ?page=2 이런 식으로. 그리고 마지막으로 html에서 페이지 객체의 매소드 함수 및 template language로 표시.  
- Paginator Class와 Page Class는 다르다. paginator는 어떤 객체를 몇 페이지씩 자를 것인지 정하는 것이고, Page 객체는 각 페이지를 말한다. 
- page 객체의 메소드 함수로는 page.count(), page.num_pages(), page.page(n), page.page_range(), page.get_page(n), page.has_next(), page.has_previous(), page.previous_page_number() 등등이 있다. 
- 사용자가 request하는 페이지 번호는 어떻게 알 것인가? page = request.GET.get('page')를 통해 알 수 있다. 여기서 .get()은 dictionary에서 key를 인자로 주면 value 반환하는 함수이다. 
- request.GET은 사실 dictionary이다. www.google.com?fookey=3&barkey=hello 라는 url이 request되면 request.GET = {'fookey':3, 'barkey':"hello"} 이다. Pagination에서는 {'page':3} 와 같이 받을 것이다. 
- 즉, request.GET.get('page')에는 원하는 페이지의 번호가 담긴다. 이제 paginator.get_page()를 통해 해당 페이지를 실제로 불러온다. 

### pagination (2)

- views.py에서 paginator를 import 해준다. 
- def home 에서 blog를 paginator에 담아준다. page에는 'page'를 key로 value를 반환해 request된 페이지 번호를 저장한다. posts에는 이미 선언한 전체 객체가 들어있는 paginator에서 해당 page를 입력받아 객체들을 불러온다. 
- 그리고 return render 시에 해당 값을 context로 같이 보내준다. 
- 이제 home.html에서 blog.all이 아닌 posts에서 돌도록 html을 수정해준다. 즉, request로 받은 어떤 page의 글만 load되고 표시가 되는 것이다. 
- 이제 pagination buttons를 생성한다. \

### 참고: faker

- 가짜 데이터를 생성해주는 Faker. 많은 데이터가 있는 상황을 염두해뒀을 때 테스트 할 수 있게 해줌. 
- $ pip install Faker / from faker import Faker
- Faker()의 메소드를 통해 어떤 종류의 가짜 데이터를 뽑아낼 지 결정할 수 있다. 
- .name() .address() .text() .state() .sentence() .random_number() 등. 
- default는 영어고, 한국어로 local을 변경 가능하다. Faker('ko_KR')
- 가짜 데이터를 저장하기 필요한 것이 seed파일이다. Faker객체.seed(seed번호) 방식으로 생성 가능하다. 
- 이를 이용하여 seed DB를 만들 수 있을 것이다. views에서 for문을 써 만들어보자. 

## Form 이론

### Form (1)

- html로 일일이 form tag를 만드는 것은 힘들다. 또한 유효성 검사를 매번 처리하는 것도 힘들다. 한계가 있다. 
- Django에서 기본 제공하는 form.py를 만들어 해결한다. models.py가 DB에 대응된다면, form.py는 templates에 응된다. 
- 이는 모델의 기반으로 한 입력공간을 만들거나 임의의 입력 공간을 만드는 것 둘 다 가능하다. 
    - 모델 기반: ...import forms.ModelForm
    - 임의의 공간: ...import forms.Form
- 참고: Meta class https://stackoverflow.com/a/6581949/8491363
- Form을 class로 만들고, 그 class 안에 class Meta로 어떤 모델을 기반으로 한 입력공간인지, 그 모델 중 어떤 항목을 입력받을 것인지 적어줘야 한다. 
- 임의의 입력 공간은 더 간단하다. 그냥 만드는 form의 class attributes로 img, text, time 등을 집어넣어 주면 된다.
- 이 form.py에서 myForm class를 만들었으면 이를 views.py에서 import 해준다. def create 할 때 아래 두 가지를 수행할 수 있도록 한다. 
    - 1. 처음 new.html에 들어갔을 때 빈 입력공간을 띄우고 --> GET
    - 2. 이용자가 입력하면 그 입력값들을 처리하는 역할 --> POST
- 둘 중 어떤 케이스인지 구분하기 위해선 GET인지 POST인지 if문으로 판별하면 된다. 
- 입력받을 때도 모델의 일부항목에 대해서만 직접 입력받고 나머지 항목은 자동으로 채워지게 (작성일시 등) 하고싶을 수도 있다. 
- 또한 입력값을 처리하는 POST 방식일 때 .is_valid 를 사용하여 적절한 값이 입력되었는지 확인하는 절차를 거친다. 이 is_valid는 적절한 값을 입력하라고 알려주는 기능도 가진다. 그리고 저장하기 전 model 객체에 접근해 date 변수를 써주는 식으로 저장을 완료한다. 
- form.save(commit=False)를 통해 바로 DB에 저장하지 않고 그냥 객체를 반환받는 것이 가능하다. 
- form은 {{form}} 으로 띄울 수 있으나, 근야 쭈르륵 나오므로 template tag로 보내기 전에 안의 내용을 어떤 태그로 감싸서 보낼지 미리 결정해서 보내야 한다. (Django의 기능)
- {{form.as_table}}, {{form.as_p}}, {{form.as_ul}} 등이 있다. 

### Form (2)

- form을 만드려는 app 폴더 속에 form.py를 만든다. 
- Model 기반 form은 forms.ModelForm을 상속받고 free form은 forms.Form을 상속받아 form class를 만든다. 
- 이 떄, model의 모든 field를 입력받고 싶으면 fields = '__all__' 를 써주면 된다. 하지만 timezone 같은 것은 직접 입력받지 말아야 하기 때문에 잘 써야 한다. 
- 어떤 model을 기반으로 할 것인지, 어떤 field를 쓸 것인지 적어준다. 
- urls.py에서 views.py에서 정의할 새로운 blogpost 함수를 실행시키는 url을 만든다. 
- views.py에서 blogpost 함수를 만든다. 
- 이제 new.html가서 만든 form을 활용하여 페이지를 만들어준다. 

## 소셜 로그인/API

### 소셜 로그인 (1)

- 기능 위주로 수업을 한다. 
- Django에서 social login 기능은 allauth가 꽤 보편적이다. 
- 기존 방식은 db.sqlite3를 썼지만, 이는 development에서만 임의적으로 그렇게 하는 것이고 db는 원래 매우 중요하기 때문에 따로 관리를 해줘야 한다. 
- 전자는 db와 db를 다루는 로직이 한 공간에 있는 것이고 후자는 db와 db를 다루는 로직이 다른 공간에 존재하게 되는 것이다. 
- 기존엔 views.py에 login, signup, logout을 구현했었다. 이는 사용자에게 request를 받아서 우리가 처리하는 방식이었고, social 로그인은 구글 등의 서비스와 request, token 등을 주고받으며 authenticate하는 방식이다. 
- 기존의 방법을 가져다 쓰는 것이니 더 안정적일 것이다. 
- session 상태에 따른 처리도 가능하다. 

### 소셜 로그인 (2) 

- 새로 프로젝트를 시작하고 login 앱을 만든다. 
- django-allauth 라이브러리를 설치한다. 
- settings.py의 INSTALLED_APPS에서 django.contrib.sites 를 추가해준다. 순서는 크게 상관 없을 수도 있으나, 일단 auth아래에 설치해준다. 
- 또 거기에 'allauth', 'allauth.account', 'allauth.socialaccount'를 추가해준다. 그 아래에 또 providers 들을 써준다. 
- 그리고 settings.py 하단에 AUTHENTICATION_BACKENDS 등의 코드를 추가해준다. 
- 이제 urls.py에서 'accounts/' 관련 경로를 include 시켜준다. 이는 allauth.urls 에 들어있는 여러 가지 signup, login, 등등의 로그인 경로들을 가져다 쓰는 것이다. 
- 이제 migrate를 한 번 해준다. 
- /admin에서 확인하면 다양한 User 관련 모델들이 생성되어 있다. Sites에 들어가 로컬 서버 주소인 127.0.0.1:8000으로 바꿔준다. 
- Social applications에서 add social application에 들어가 Google을 추가해준다. 
- Cliend ID와 Secret Key를 Google에서 받아야 한다. Google Dev console에 들어가 project를 만들고 OAuth client id를 선택한다. client id와 secret key가 제공되면 이를 admin에 들어가 입력해준다. 
- 이제 home.html에 들어가 {% load socialaccount %} 를 해주고 이하 내용을 작성해준다. 이를 통해 session을 손쉽게 관리할 수 있다. (by .is_authenticated)
- accounts/signup url을 만든적이 없음에도 allauth에서 제공해주기에 url이 작동한다. 
- login page로 가기 위해선 {% provider_login_url 'provider이름' %} 을 사용해야 해당 provider에게 연결됨을 기억하자. 

### API 

- Application Programming Interface. 우리가 만든 서비스에서 외부의 기능을 사용하도록 제어할 수 있는 연결통로 (인터페이스)
- Naver의 ncloud.com 에서 지도를 가져올 수 있다. 

### 썸네일 만들기 (실습 생략)

- django-imagekit 썸네일 라이브러리를 썼을 때의 장점:
    - 1. 썸네일 파일 지정 용이
    - 2. 파일 용량 관리. (확장자, 압축방식, 중복사용 방지)
    - 3. 파일 분류에 효율적. (thumbnail은 thumbnail directory에, 원본은 원본 디렉토리에.)
- 이미지 static 사용하던 방법과 똑같이 이미지를 넣는다. 
- pip install 후 INSTALLED_APPS에 'imagekit'을 등록해준다. 
- 이후 models.py에서 image를 넣기 위한 class를 만들 때 아래 두 개를 import 해준다. 
    - from imagekit.models import ImageSpecField (썸네일을 만듦)
    - from imagekit.processors import ResizeToFill (크기조정 용이하게 해줌)
- 기본적인 ImageField를 만든 다음 다음과 같이 추가해준다. 
    - image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(120, 60)])
    - 여기서 source는 어떤 것을 썸네일 만들 소스로 삼느냐인데, 기존에 입력한 image = models.ImageField(upload_to='blogimg')가 이에 해당한다. ResizeToFill은 썸네일의 크기를 정한다. 
    - ImageSpecField는 format='JPEG', options=압축 퀄리티 등등을 지정해 줄 수 있다. 

- 이제 home.html에 썸네일을 띄우기만 하면 된다. template variable을 통해 띄운다. 
- <img src='{{ blog.image_thumbnail.url }}'> 와 같이 넣는다. 

## APP 재사용

### APP 재사용 (1)

- account, comment 같은 것은 다른 프로젝트에서도 재사용하게되는 app들이다. 
- 이를 packaging하여 쓰는 방법을 알아보자. pip install 하듯, package인 것이다. 
- app의 재사용 == app의 packaging. 앱을 묶고, 푸는 것이다. 푸는 것은 pip install 로 하는 것이니 app을 묶는 것만 배우면 된다. 
- 파일을 4개 만들어야 한다. 
    - 1. 패키지의 소개/사용설명서/기능명세서 README.rst
    - 2. 라이센스 LICENSE
    - 3. 설치의 방법 과정 setup.py
    - 4. 파이썬 파일이 아닌 파일들 명시 MANIFEST.in

### APP 재사용 (2)

- 프로젝트 외부에 새로운 패키징 폴더를 만들고, 재사용할 앱을 이동시킨다. 그리고 위에서 설명한 4개의 파일을 만든다. 
- 장고 공식문제에서 복붙을 한다. README에선 한글을 쓰지 않는 것이 좋다. 
- 라이센스는 BSD 등 다양한 것을 가져다 쓴다. Django tutorial의 범위를 벗어나는 부분인데, 라이센스가 없는 패키지는 쓸모 없는 패키지라는 것을 기억하자. 
- MANIFEST.in은 python 이외의 다른 것을 모두 적어놓는데, recursive-include login/templates * 그리고 recursive-include login/migrations * 등을 적어놓으면 재귀적으로 include하고 각각은 include LICENSE 와 같이 적는다. 
- 이제 모든 것이 준비되었으니 해당 디렉토리로 이동하여 $ python setup.py sdist 를 통해 짐을 싼다. 그러면 압축파일 하나가 생성된다. 이제 이 패키지를 pip install 해주면 앱의 재사용이 가능하다. 
- 기존 프로젝트는 현재 앱이 빠져있으니 에러가 날 것이다. 따라서 방금 만든 패키지를 장고에서 다시 설치해주도록 한다. 패키징 한 폴더 안으로 들어가 pip install dist/패키지압축파일명 을 해주면 앱이 설치된다. 
- 그렇게 하면 프로젝트 내에 앱 폴더가 없어도 앱 패키지가 설치가 되었기에 다시 정상 작동한다. 

## PostgreSQL

- 디폴트 sqlite3는 스케일이 커지면 다른 db로 대체해야 한다. 
- 지금껏 sqlite를 어떻게 사용했는지, 앞으로 PostgreSQL을 어떻게 사용할지 알아보자. 
- 장고 프로젝트는 어떤 db를 가리키고 연결되어 있는 것이다. 이는 settings.py에 명시되어 있다. (가리킴)
- 다른 DB와 연결까지 하기 위해선 우선 DB를 설치하고, 가리키고, migrate로 연결해줘야 한다. 
- PostgreSQL을 설치 후 pgAdmin을 킨다. Database > create에서 db를 생성한다. 
- blog의 settings.py에서 DATABASES를 수정해준다. 이 때 PASSWORD는 진짜 PostgreSQL에서 사용한 유저의 password를 적어줘야 한다. 
- 이제 migrate를 시킨다. 나의 경우는 psycopg2 module이 없다고 에러가 나서

## AWS 배포

- Will visit later

## ORM & CRUD

### Object Relational Mapping

- (클래스)객체로 관계형 DB를 다룬다. 
- 주로 데이터를 CRUD로 다룬다. 

### 함수형 view CRUD

- 모든 기본 세팅을 해준다. 
- 새로 functioncrud와 classcrud 앱을 만든다. 
- 이 때, templates 안에 namespacing을 통해 정확하게 알 수 있도록 각 앱의 이름으로 다시 한 번 분류해준다. 
- create가 new의 역할도 한다는 것을 알아두자. if문으로 method를 구분하여 new를 띄울지, create 기능을 수행할지 정하게 된다. 
- C R(list)는 pk가 필요 없지만 R(detail) U D는 pk가 필요하다. 따라서 삭제 링크를 만들 때도 blog.id를 포함하여 보내줄 수 있도록 해야 한다. 

### 클래스형 view CRUD (1)

- Generic View - RESTful API in Django
- 왜 class view를 쓰는지, 함수형 view와 차이는 뭔지 알아본다. 
- function과 class는 모두 callable object이다. views.py는 사실 호출가능한 객체로 정의하는 것이었던 것이다. 
- class는 상속이 있고 function은 상속이 없다. 
- Class Based View(generic view)에선 대신 '약속된' 것이 많다. (conventions) 
- FBV도 실무에서 많이 쓰긴 한다. 무조건 CBV > FBV는 아니다. 

### 클래스형 view CRUD (2)

- views를 class를 사용하여 작성해 준다. 장고에서 generic으로 구현되어있는 django.views.generic 에서 가져다 쓰는 것이 중요하다. 
- ListView는 model = 담을 모델객체 만 선택해주면 알아서 나머지를 list 하게 해준다. 
- CreateView는 model = 모델객체 선택하고 입력할 fields만 선택해준다. 그리고 reverse_lazy() 를 이용해 list로 돌아간다. 참고로 .get_absolute_url(), .reverse() 도 있으니 추후 활용하자. 
- UpdateView 는 위와 유사하다. 
- 하지만 CBV에는 약속된 규약들이 있다. 바로 각 class view에는 이에 필수적인 html이 필요한 것이다. 
    - ListView는 리스트를 담은 html template을 --> 소문자모델_list.html
    - CreateView는 form을 가진 html을 --> 소문자모델_form.html
    - DetailView는 상세페이지를 담은 html을 --> 소문자모델_detail.html
    - UpdateView는 CreateView와 마찬가지로 form을 가지 html을  --> 소문자모델_form.html
    - DeleteView는 삭제를 확인하는 html을 --> 소문자모델_confirm_delete.html
- html에서도 다르게 불러준다. model = ClassBlog와 같이 모델만 지정해줬기 때문에 object_list 라는 context로 보내서 {% for blog in object_list %} 와 같이 반복문을 돌리면 해당 모델로 생성된 모든 객체를 순회할 수 있다. 
- _detail.html에서도 해당 pk값을 가진 모델 객체는 단순히 object 로 호출이 가능하다. object.title 와 같이 호출 가능하다. 
- 만약 default html이 아닌 custom html을 쓰고 싶다면 ListView에서 template_name = 하고 override를 해줘야 한다. 
- 서로 다른 객체 목록은 어떻게 구분하는가? obejct / object_list 하나로 통일되어 있으니. 따라서 default를 customize 해줘야 할 수 있다. 이 경우 context_object_name = 'foo' 로 바꿔준다. 