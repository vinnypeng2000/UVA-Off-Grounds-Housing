from django.db import models
import geocoder
from multiselectfield import MultiSelectField
from django.db.models.deletion import CASCADE
from django.core.validators import MaxValueValidator, MinValueValidator
mapbox_access_token = 'pk.eyJ1Ijoic2hpdmFtYW4iLCJhIjoiY2t2cHZjOTY2MmlodzJvbXRuOXMzMTRpNiJ9.8mKcr3_Z1IcZMKpO3VRC6A'


class Housing(models.Model):
    image = models.ImageField(upload_to='cover', blank = True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)

    def save(self, *args, **kwargs):
        g = geocoder.mapbox(self.address, key=mapbox_access_token)
        g = g.latlng  # [lat,long]
        self.lat = g[0]
        self.long = g[1]
        return super(Housing, self).save(*args, **kwargs)

    HOUSING_TYPES = [
        ("Apartment", "Apartment"),
        ("House", "House"),
        ("Town_House", "Town House"),
    ]
    housing_type = models.CharField(
        max_length=10, choices=HOUSING_TYPES, blank=False)
    pub_date = models.DateTimeField('date published')
    admin_check = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Housing_People(models.Model):
    people = models.IntegerField(default=0)

    def __str__(self):
        return str(self.people)


class Housing_Bed(models.Model):
    beds = models.IntegerField(default=0)

    def __str__(self):
        return str(self.beds)


class Housing_Bath(models.Model):
    baths = models.IntegerField(default=0)

    def __str__(self):
        return str(self.baths)


class Style(models.Model):
    name = models.ForeignKey(Housing, on_delete=models.CASCADE)
    people = models.ForeignKey(Housing_People, on_delete=CASCADE)
    beds = models.ForeignKey(Housing_Bed, on_delete=CASCADE)
    baths = models.ForeignKey(Housing_Bath, on_delete=CASCADE)
    rent = models.IntegerField(default=0)

    def __str__(self):
        return self.name.name


class Amenity(models.Model):
    name = models.ForeignKey(Housing, on_delete=models.CASCADE)
    ALL_AMEN = (
        ('Air Conditioning', 'Air Conditioning'),
        ('Internet', 'Internet'),
        ('Disability Access', 'Disablity Access'),
        ('Intercom', 'Intercom'),
        ('Exterior Lighting', 'Exterior Lighting'),
        ('Security System', 'Security System'),
        ('Smoke Free', 'Smoke Free'),
        ('Washing Machine', 'Washing Machine'),
        ('Dryer', 'Dryer'),
        ('Furnished', 'Furnished'),
        ('Hardwood Floor', 'Hardwood Floor'),
        ('Dishwasher', 'Dishwasher'),
        ('Gym', 'Gym'),
        ('Pool', 'Pool'),
        ('Garden', 'Garden'),
        ('Patio/Balcony', 'Patio/Balcony'),
        ('Parking', 'Parking')
    )
    amenities = MultiSelectField(choices=ALL_AMEN, default="")

    ALL_UTIL = (
        ('Water', 'Water'),
        ('Electricity', 'Electricity'),
        ('Sewer', 'Sewer'),
        ('Gas', 'Gas'),
        ('Trash', 'Trash'),
    )
    utilities = MultiSelectField(choices=ALL_UTIL, default="")

    def __str__(self):
        return self.name.name


class Review(models.Model):
    housing = models.ForeignKey(Housing, on_delete=models.CASCADE)
    review = models.TextField(blank = True)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    date_added = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default="False")

    def __str__(self):
        return self.review

class Images(models.Model):
    name = models.ForeignKey(Housing, on_delete=models.CASCADE)
    pic1 = models.ImageField(upload_to='gallery', blank=True)
    pic2 = models.ImageField(upload_to='gallery', blank=True)
    pic3 = models.ImageField(upload_to='gallery', blank=True)

    def __str__(self):
        return self.name.name
