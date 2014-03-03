from jellyroll.views import tags
from django.conf.urls import *


urlpatterns = patterns('',

    url(r'^$', tags.tag_list, {}, name='jellyroll_tag_list'),
    url(r'^(?P<tag>[-\.\'\:\w]+)/$',tags.tag_item_list, {}, name="jellyroll_tag_item_list"),
)
