"""
URLs for doing a jellyroll site by date (i.e. ``2007/``, ``2007/may/``, etc.)
"""
from django.conf.urls import patterns, url
from jellyroll.views import calendar


urlpatterns = patterns(
    '',
    url(r'^$', calendar.ItemArchiveIndex.as_view(), name='jellyroll_calendar_today'),
    url(r'^(?P<year>\d{4})/$', calendar.ItemYearArchive.as_view(), name='jellyroll_calendar_year'),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/$', calendar.ItemMonthArchive.as_view(), name='jellyroll_calendar_month'),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{1,2})/$', calendar.ItemDayArchive.as_view(), name='jellyroll_calendar_day'),
)
