"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django_filters.views import FilterView
from search.filters import ReviewFilter
from django.views.generic import TemplateView
# import pandas as pd

# data = []
# df = pd.read_csv('search/static/data/hotel_review.csv')
# df = df.fillna('')
# for index, review in df.iterrows():
#     temp_dict = {}
#     temp_dict['text'] = review['text']
#     temp_dict['size'] = review['size']
#     data.append(temp_dict)


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('search/', ReviewFilterView, name='search'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('search/', FilterView.as_view(filterset_class=ReviewFilter, template_name='search/user_list.html'), name='search'),
]
