"""
Views for looking at Jellyroll items by tag.
"""
from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType
from django.views.generic.list import ListView
from jellyroll.models import Item
from tagging.models import TaggedItem, Tag


class TagList(ListView):
    context_object_name = 'tag_list'
    template_name = 'jellyroll/tags/tag_list.html'

    def get_queryset(self):
        item_ct = ContentType.objects.get_for_model(Item)
        tag_items = TaggedItem.objects.filter(content_type=item_ct)
        queryset = Tag.objects.filter(pk__in=[tag_item.tag.pk for tag_item in tag_items])
        return queryset


class TagItemList(ListView):
    context_object_name = 'item_list'
    template_name = 'jellyroll/tags/tag_item_list.html'

    def get_context_data(self, **kwargs):
        context = super(TagItemList, self).get_context_data(**kwargs)
        tag = get_object_or_404(Tag, name=self.kwargs['tag'])
        context['tag'] = tag
        return context

    def get_queryset(self):
        name = self.kwargs['tag']
        tag = get_object_or_404(Tag, name=name)
        queryset = TaggedItem.objects.get_by_model(Item, tag)
        return queryset
