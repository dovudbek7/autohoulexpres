from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from mdeditor.fields import MDTextField

from .managers import PostManager


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Make(models.Model):
    name = models.CharField(max_length=255, help_text="Enter the car manufacturer (e.g. Toyota, Ford)")

    def __str__(self):
        return self.name


class Model(models.Model):
    name = models.CharField(max_length=255, help_text="Enter the car model (e.g. Corolla, Civic)")
    make = models.ForeignKey(Make, on_delete=models.CASCADE, related_name='models', help_text="Select the car make")

    def __str__(self):
        return f"{self.make.name} {self.name}"  # Example: Toyota Corolla


class Year(models.Model):
    year = models.IntegerField(help_text="Enter the manufacturing year (e.g. 2020)")

    def __str__(self):
        return str(self.year)


class Orders(models.Model):
    TRANSPORT_TYPE_CHOICES = [
        ('open', 'Open'),
        ('enclosed', 'Enclosed'),
    ]
    OPERABLE = [
        ('yes', 'Yes'),
        ('no', 'NO'),
    ]

    pick_up_location = models.CharField(max_length=255, help_text="Enter the pick-up city or ZIP code")
    delivery_location = models.CharField(max_length=255, help_text="Enter the delivery city or ZIP code")
    open_enclosed = models.CharField(max_length=10, choices=TRANSPORT_TYPE_CHOICES, default='open')
    operable = models.CharField(max_length=10, choices=OPERABLE, default='yes')
    make = models.ForeignKey(Make, on_delete=models.CASCADE, help_text="Select the car make (company)")
    model = models.ForeignKey(Model, on_delete=models.CASCADE, help_text="Select the car model")
    year = models.ForeignKey(Year, on_delete=models.CASCADE, help_text="Select the car year")
    name = models.CharField(max_length=255, help_text="Enter your full name")
    email = models.EmailField(help_text="Enter your email address")
    phone_number = models.CharField(max_length=15, help_text="Enter your phone number")
    date = models.DateField(help_text="Enter the current date")
    condition = models.BooleanField(default=False)

    def __str__(self):
        return f"Order by {self.name} for {self.make.name} {self.model.name} ({self.year.year})"


class Post(BaseModel):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    image = models.ImageField(upload_to='media/')
    body = MDTextField(null=True, blank=True)
    status = models.BooleanField(default=True)
    publish = models.DateTimeField(default=timezone.now)

    objects = models.Manager()  # Default manager
    published = PostManager()  # Custom manager for published posts

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('auto:post_detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])

    class Meta:
        ordering = ['-updated']
        indexes = [
            models.Index(fields=['-updated']),
            models.Index(fields=['-publish']),
        ]


class Comment(BaseModel):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    active = models.BooleanField(default=True)
    publish = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f'Comment by {self.name} on {self.post.title}'

    class Meta:
        ordering = ['-updated']
        indexes = [
            models.Index(fields=['-updated']),
            models.Index(fields=['-publish']),
        ]


class ContactMessage(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    message = models.TextField()

    def __str__(self):
        return f"Message from {self.full_name}"


class Photos(models.Model):
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.image.name
