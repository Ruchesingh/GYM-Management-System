from django.urls import path
from dietPlan.api.views import DietPlanView, DietPlanUpdateAndDelete

urlpatterns = [
    path('', DietPlanView.as_view(), name='diet-plan'),
    path('<int:pk>', DietPlanUpdateAndDelete.as_view(), name='diet-plan-update-delete'),]