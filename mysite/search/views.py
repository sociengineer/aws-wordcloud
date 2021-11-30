from django.shortcuts import render
import pandas as pd

from search.filters import ReviewFilter
from .models import Review
from django_filters.views import FilterView
import json
from datetime import datetime
# from .models import Review

# Create your views here.

df = pd.read_csv('search/static/data/tokens.csv')
df['reviews.date'] = df['reviews.date'].fillna('2013-07-01')
df['date'] = df['reviews.date'].apply(lambda x: str(x).split('T')[0])
print(df)
for index, review in df.iterrows():
    Review.objects.create(
        categories = review['categories'],
        city = review['city'],
        country = review['country'],
        name = review['name'],
        date = review['date'],
        rating = review['reviews.rating'],
        tokens = json.dumps(review['tokens'])
        # tokens.set_tokens(review['tokens'])
        )
print('reviews are successfully uploaded')


# class WordCloud()


# def search(request):
#     review_list = Review.objects.all()
#     review_filter = ReviewFilter(request.GET, queryset=review_list)
#     context = {'filter' : review_filter}
#     return render(request, 'search/user_list.html', context)

# class ReviewFilterView(FilterView):
#     template_name = 'search/user_list.html'
#     model =  Review
#     filterset_class = ReviewFilter

#     def get_context_data(self, *args, **kwargs):
#         context = super(ReviewFilterView, self).get_context_data(*args, **kwargs)
#         context['qs'] = Review.objects.all()
#         context['data'] = data
#         return context