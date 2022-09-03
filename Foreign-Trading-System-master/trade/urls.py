from django.conf.urls import url
from .views import homePageView, aboutView
from .views import commodityCreateView, myCommoditiesView, my_view, requestsShow, requestsSentShow, requestAccept
urlpatterns = [
    url(r'^$', homePageView, name='home'),
    url(r'^commodity/add/$', commodityCreateView, name='commodity-add'),
    url(r'^commodity/buy/$', my_view, name='commodity-buy'),
    url(r'^commodity/requests/received$', requestsShow, name='requests-view'),
    url(r'^commodity/requests/sent$', requestsSentShow, name='requests-view-sent'),
    url(r'^details/(?P<id>\d+)/$', requestAccept, name='details'),
    url(r'^mycommodities/view/$', myCommoditiesView, name='mycommodities-view'),
    url(r'^about/$', aboutView, name='about-view'),

]
