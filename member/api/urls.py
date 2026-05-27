from django.urls import path
from member.api.view import membercreate, memberlist

urlpatterns = [
    path('', memberlist, name="member-list"),
    path('create', membercreate, name="member-create"),
]