from django.views.generic import ArchiveIndexView, YearArchiveView, MonthArchiveView, DayArchiveView

from jellyroll.models import Item


class ItemMixin(object):
    context_object_name = 'items'
    date_field = 'timestamp'
    make_object_list = True
    model = Item
    paginate_by = 20


class ItemArchiveIndex(ItemMixin, ArchiveIndexView):
    template_name = 'jellyroll/calendar/archive.html'


class ItemYearArchive(ItemMixin, YearArchiveView):
    template_name = 'jellyroll/calendar/year.html'


class ItemMonthArchive(ItemMixin, MonthArchiveView):
    template_name = 'jellyroll/calendar/month.html'


class ItemDayArchive(ItemMixin, DayArchiveView):
    template_name = 'jellyroll/calendar/day.html'
