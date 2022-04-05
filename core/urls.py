from .views import ProductViewset

from django.urls import path,url




urlpatterns = [
url(r'^snippets/', ProductViewset.as_view()),
url(r'^snippets/(?P<pk>[0-9]+)/$', ProductViewset.as_view()),
]