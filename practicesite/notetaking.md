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
- path('', practiceapp.views.home, name='home') 를 urlpatterns에 추가해주는데, 그 의미는 1st argument와 같은 pattern이 왔을 때 2nd argument의 함수를 실행하고 싶다는 것이고, 이 path 전체의 이름을 'home'이라고 하겠다는 것이다. 보통 이 url의 name은 함수와 동일한 이름으로 짓는 것이 convention이다. 
- 