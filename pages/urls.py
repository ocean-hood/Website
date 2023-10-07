from django.urls import path
from .views import home_view , begineer_view , intermediate_view , expert_view , about_us_view , intermediate1_view , intermediate2_view , intermediate3_view , intermediate4_view , intermediate5_view , intermediate6_view , intermediate7_view

urlpatterns = [
  path('' , home_view , name='home'),
  path('begineer' , begineer_view , name='begineer'),
  path('intermediate' , intermediate_view , name='intermediate'),
  path('expert' , expert_view , name='advanced'),
  path('about' , about_us_view , name='about'),
  path('paper1' , intermediate1_view , name='paper1'),
  path('paper2' , intermediate2_view , name='paper2'),
  path('paper3' , intermediate3_view , name='paper3'),
  path('paper4' , intermediate4_view , name='paper4'),
  path('paper5' , intermediate5_view , name='paper5'),
  path('paper6' , intermediate6_view , name='paper6'),
  path('paper7' , intermediate7_view , name='paper7'),
]