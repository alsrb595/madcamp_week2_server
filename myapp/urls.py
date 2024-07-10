from django.urls import path
from .views import save_user, delete_user

urlpatterns = [
    path('save_user/', save_user, name = 'user'),
    path('delete_user/', delete_user, name = 'del_user')
    # 다른 URL 패턴들도 필요에 따라 추가할 수 있습니다.
]


# ~/myapp/ 이렇게 요청이 들어오면 myapp 내부로 들어온 후 뒤에가 ' '이므로 view.index라는 함수를 호출함 
# ~/myapp/hello/ 이런식으로 들어오면 또 path('hello', view.index, name = 'djkd') 이런식으로 해줘야 함
# path() 안의 name은 템플릿이나 뷰에서 index라는 이름으로 해당 url을 참조할 수 있도록 해줌
