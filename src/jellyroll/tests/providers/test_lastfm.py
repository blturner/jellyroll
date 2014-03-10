import mock

from django.conf import settings
from django.test import TestCase
from django.utils.timezone import is_aware

from jellyroll.models import Item
from jellyroll.providers import lastfm
from jellyroll.providers.utils.anyetree import etree


LASTFM_XML_STRING =  '<?xml version="1.0" encoding="UTF-8"?> \
                        <recenttracks user="blturner"> \
                            <track streamable="true"> \
                                <artist mbid="5334edc0-5faf-4ca5-b1df-000de3e1f752">St. Vincent</artist> \
                                <name>Regret</name> \
                                <mbid>9c9e69c5-5e8e-470a-a06d-e29d532eddd0</mbid> \
                                <album mbid="8adcba3d-7ac2-416d-9b8c-2c41b67da61d">St. Vincent</album> \
                                <url>http://www.last.fm/music/St.+Vincent/_/Regret</url> \
                                <date uts="1394405815">9 Mar 2014, 22:56</date> \
                            </track> \
                        </recenttracks>'
LASTFM_XML_RESPONSE = etree.fromstring(LASTFM_XML_STRING)


mock_getxml = mock.Mock()
mock_getxml.return_value = LASTFM_XML_RESPONSE


class LastFmProviderTests(TestCase):
    def test_enabled(self):
        self.assertEqual(lastfm.enabled(), True)

    @mock.patch('jellyroll.providers.utils.getxml', mock_getxml)
    def test_update(self):
        lastfm.update()
        items = Item.objects.filter(content_type__model='track')
        self.assertEqual(len(items), 1)
        if settings.USE_TZ:
            self.assertTrue(is_aware(items[0].timestamp))
