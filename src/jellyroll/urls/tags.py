from django.conf.urls import *

from jellyroll.views.tags import TagList, TagItemList


urlpatterns = patterns('',
    url(r'^$', TagList.as_view(), name='jellyroll_tag_list'),
    url(r'^(?P<tag>[-\.\'\:\w]+)/$', TagItemList.as_view(), name="jellyroll_tag_item_list"),
)
