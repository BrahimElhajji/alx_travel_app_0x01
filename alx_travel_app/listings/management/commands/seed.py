from django.core.management.base import BaseCommand
from listings.models import Listing
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Seed database with sample listings'

    def handle(self, *args, **kwargs):
        # Create a test user or get existing
        user, created = User.objects.get_or_create(username='testuser')
        if created:
            user.set_password('password123')
            user.save()

        # Clear existing listings to avoid duplicates
        Listing.objects.all().delete()

        # Sample data list
        sample_listings = [
            {'title': 'Cozy Apartment', 'description': 'Nice and cozy apartment in city center.', 'price_per_night': 50.0, 'location': 'New York', 'owner': user},
            {'title': 'Beach House', 'description': 'Beautiful house by the beach.', 'price_per_night': 120.0, 'location': 'California', 'owner': user},
            {'title': 'Mountain Cabin', 'description': 'Quiet cabin in the mountains.', 'price_per_night': 80.0, 'location': 'Colorado', 'owner': user},
        ]

        for listing_data in sample_listings:
            Listing.objects.create(**listing_data)

        self.stdout.write(self.style.SUCCESS('Successfully seeded listings data'))
