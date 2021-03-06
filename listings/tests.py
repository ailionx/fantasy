import datetime
from django.test import TestCase

from .models import TNZRegion
from .models import TNZListing


class TNZRegionTests(TestCase):

    def test_listings_market(self):
        region = TNZRegion(label='test_label')
        TNZListing(regionname='test_label', market='cn', unique_id=1).save()
        TNZListing(regionname='test_label', market='en', unique_id=2).save()
        for listing in region.listings():
            self.assertEqual(listing.market, 'cn')
