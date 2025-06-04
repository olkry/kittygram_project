from django.urls import path, include
from rest_framework.routers import SimpleRouter

# from cats.views import cat_list, hello, cat_detail ФУНЦИИ view
# from cats.views import APICat, APICatDetail  Низкоуровневые view-классы в DRF
# from cats.views import CatList, CatDetail  Высокоуровневые view-классы в DRF, дженерики
from cats.views import CatViewSet

# Создаётся роутер
router = SimpleRouter()
# Вызываем метод .register с нужными параметрами
router.register('cats', CatViewSet)
# В роутере можно зарегистрировать любое количество пар "URL, viewset":
# например
# router.register('owners', OwnerViewSet)
# Но нам это пока не нужно


urlpatterns = [
    # path('cats/<int:pk>/', cat_detail),   ФУНЦИИ view
    # path('cats/', cat_list),  ФУНЦИИ view
    # path('hello/', hello),  ФУНЦИИ view
    # path('cats/<int:pk>/', APICatDetail.as_view()),  Низкоуровневые view-классы в DRF
    # path('cats/', APICat.as_view())  Низкоуровневые view-классы в DRF
    # path('cats/<int:pk>/', CatDetail.as_view()),  Высокоуровневые view-классы в DRF, дженерики
    # path('cats/', CatList.as_view())  Высокоуровневые view-классы в DRF, дженерики
    path('', include(router.urls)),
]
