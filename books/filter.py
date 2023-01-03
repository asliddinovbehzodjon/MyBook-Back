from django_filters import rest_framework as filters

from books.models import Book
from bot.models import BotUsers


class BookFilter(filters.FilterSet):
    class Meta:
        model = Book
        fields ={
            'name':['icontains'],
            'author':['icontains'],
            'about':['icontains']
        }
class BotFilter(filters.FilterSet):
    class Meta:
        model = BotUsers
        fields ={
            't_id':['iexact']
                }