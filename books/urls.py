from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import *
from bot.views import BotViewset,ChangeLang
router = DefaultRouter()
router.register('category',CategoryViewset)
router.register('books',BooksViewset)
router.register('booklist',BooksList)
router.register('comments',CommentsViewset)
router.register('bot',BotViewset)
urlpatterns = [
    path('',include(router.urls)),
    path('like/<int:id>/',GetLikeBooks.as_view()),
    path('change/<str:t_id>/<str:language>/',ChangeLang.as_view())
]
