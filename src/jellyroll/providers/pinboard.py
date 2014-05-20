import logging
import urllib

from django.conf import settings
from django.db import transaction
from django.utils.encoding import smart_unicode

from jellyroll.models import Bookmark, Item
from jellyroll.providers import utils


log = logging.getLogger('jellyroll.providers.pinboard_provider')


class PinboardClient(object):
    def __init__(self, username, api_token, method='v1'):
        self.username, self.api_token = username, api_token
        self.method = method

    def __getattr__(self, method):
        return PinboardClient(self.username, self.api_token, '{0}/{1}'.format(self.method, method))

    def __call__(self, **params):
        auth_token = '{0}:{1}'.format(self.username, self.api_token)
        params['auth_token'] = auth_token
        url = ('https://api.pinboard.in/{0}?'.format(self.method)) + urllib.urlencode(params).replace("%3A", ":")
        return utils.getxml(url)


def enabled():
    ok = hasattr(settings, 'PINBOARD_USERNAME') and \
        hasattr(settings, 'PINBOARD_PASSWORD')
    if not ok:
        log.warn('The Pinboard provider is not available because the \
            PINBOARD_USERNAME and/or PINBOARD_PASSWORD settings are \
            undefined.')
    return ok


def string_to_bool(str):
    return str.lower() in ('yes',)


def update():
    pinboard = PinboardClient(settings.PINBOARD_USERNAME, settings.PINBOARD_API_TOKEN)

    last_update_date = Item.objects.get_last_update_of_model(Bookmark)
    last_post_date = utils.parsedate(pinboard.posts.update().get('time'))

    if last_post_date <= last_update_date:
        log.info("Skipping update: last update date: %s; last post date: %s", last_update_date, last_post_date)
        return

    for datenode in reversed(list(pinboard.posts.dates().getiterator('date'))):
        dt = utils.parsedate(datenode.get('date'))
        if dt > last_update_date:
            log.debug("There is a record indicating bookmarks have been added after our last update")
            _update_bookmarks_from_date(pinboard, dt)


def _update_bookmarks_from_date(pinboard, dt):
    log.debug("Reading bookmarks from %s", dt)
    # xml = pinboard.posts.get(dt=dt.strftime("%Y-%m-%d"))
    xml = pinboard.posts.get(dt=dt)
    for post in xml.getiterator('post'):
        info = dict((k, smart_unicode(post.get(k))) for k in post.keys())
        _handle_bookmark(info)
_update_bookmarks_from_date = transaction.commit_on_success(_update_bookmarks_from_date)


def _handle_bookmark(info):
    try:
        to_read = string_to_bool(info['toread'])
    except KeyError:
        to_read = False
    b, created = Bookmark.objects.get_or_create(
        url = info['href'],
        to_read = to_read,
        defaults = dict(
            description = info['description'],
            extended = info.get('extended', ''),
        )
    )
    if not created:
        b.description = info['description']
        b.extended = info.get('extended', '')
        b.save()
    return Item.objects.create_or_update(
        instance = b, 
        timestamp = utils.parsedate(info['time']), 
        tags = info.get('tag', ''),
        source = __name__,
        source_id = info['hash'],
    )
