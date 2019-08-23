# 환경 설정

## venv vs pipenv 

# 장고 시작

## project와 app 시작: hello world!

- 프로젝트를 시작하기 위하여 $ django-admin startproject 프로젝트_이름
- cd <프로젝트 이름 디렉토리> 후, $ python manage.py runserver 로 서버 동작 확인. 
- app. 프로젝트의 구성단위로, python manage.py startapp app_이름
- 만들어진 app 폴더 내에 templates라는 이름의 폴더를 생성한다. 
- app을 추가했으면 settings.py의 INSTALLED_APPS에 추가해줘야 한다. 형식은 app이름.apps.첫글자대문자app이름Config 그 이유는, app폴더의 apps.py에 가보면 첫글자대문자app이름COnfig 라는 이름의 Class가 선언되어있기 때문이다. 이 클래스를 연결시킨 것이다. 
- 이걸 잘못 쓰면 runserver 할 때 [WinError 123]이 뜬다. 하지만 진짜 문제는 에러메세지 중간의 ModuleNotFoundError: No module named 'practicesite.apps' 부분이다. 
- views.py에서 함수를 만든다. 일단 render로 간단히 작성한다. 
- 그리고 프로젝트 폴더 내의 urls.py를 통해 urlpatterns를 추가해준다. 이 때, 앱폴더 내의 views.py에서 쓰는 함수들을 쓰고싶으므로 이를 urls.py내에서 import 해준다. --> import practiceapp.views
- path('', practiceapp.views.home, name='home') 를 urlpatterns에 추가해주는데, 그 의미는 1st argument와 같은 pattern이 왔을 때 2nd argument의 함수를 실행하고 싶다는 것이고, 이 path 전체의 이름을 'home'이라고 하겠다는 것이다. 보통 이 url의 name은 함수와 동일한 이름으로 짓는 것이 convention이다. 이 때, url은 /로 마쳐준다. 

## MTV 패턴

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