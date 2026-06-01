from django.urls import path

from subscription.api.views import GymMemeberView, SubscriptionUpdateAndDelete, SubscriptionView
urlpatterns = [
    path('', SubscriptionView.as_view(), name="subscription"),
    path('<int:pk>', SubscriptionUpdateAndDelete.as_view(),name="subscription-update"),
     path('member',GymMemeberView.as_view()),
]