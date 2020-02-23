from django.urls import path
from . import views
from . views import sentiments_with_js_chart

urlpatterns = [
			   path("", views.sentiments_with_js_chart, 
			   name="sentiments_with_js_chart"),
			  ]
