import datetime
from django.test import TestCase
from django.conf import settings
from jellyroll.models import Item

class CalendarViewTest(TestCase):
    fixtures = ["bookmarks.json", "photos.json", "tracks.json", "videos.json", "websearches.json"]
    
    def setUp(self):
        settings.ROOT_URLCONF = "jellyroll.urls.calendar"
        
    def callView(self, url):
        today = datetime.date.today()
        response = self.client.get(today.strftime(url).lower())
        if isinstance(response.context, list):
            context = response.context[0]
        else:
            context = response.context
        return today, response, context
        
    def testYearView(self):
        today, response, context = self.callView("/%Y/")
        self.assertEqual(context["year"].year, today.year)
        self.assertEqual(len(context["items"]), Item.objects.count())
        
    def testMonthView(self):
        today, response, context = self.callView("/%Y/%b/")
        self.assertEqual(context["month"].year, today.year)
        self.assertEqual(context["month"].month, today.month)
        self.assertEqual(len(context["items"]), Item.objects.count())
        
    def testDayView(self):
        today, response, context = self.callView("/%Y/%b/%d/")
        self.assertEqual(context["day"], today)
        self.assertEqual(len(context["items"]), Item.objects.count())
        
    def testArchiveIndexView(self):
        today, response, context = self.callView("/")
        self.assertEqual(len(context["items"]), Item.objects.count())
        self.assertTemplateUsed(response, "jellyroll/calendar/archive.html")
        
    def testDayViewOrdering(self):
        today, response, context = self.callView("/%Y/%b/%d/")
        oldest = context['items'].reverse()[0].timestamp
        newest = context['items'][0].timestamp
        self.assert_(newest > oldest, "newest: %s, oldest: %s" % (newest, oldest))
        
    def testArchiveIndexViewOrdering(self):
        today, response, context = self.callView("/")
        oldest = context['items'].reverse()[0].timestamp
        newest = context["items"][0].timestamp
        self.assert_(newest > oldest, "newest: %s, oldest: %s" % (newest, oldest))
