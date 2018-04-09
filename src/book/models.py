from django.db.models import Q

from book.utils import unique_slug_generator
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_save
from django.urls import reverse


class Writer(models.Model):
    writer = models.CharField(max_length=30)

    def __str__(self):
        return self.writer


class Publisher(models.Model):
    publisher = models.CharField(max_length=30)

    def __str__(self):
        return self.publisher


class BookQueryset(models.query.QuerySet):
    def search(self, query):
        if query:
            query = query.strip()
            return self.filter(
                Q(book_name__icontains=query) |
                Q(writer__writer__icontains=query) |
                Q(genre__icontains=query) |
                Q(publisher__publisher__icontains=query)
            ).all()
        return self.none()


class BookManager(models.Manager):

    def get_queryset(self):
        return BookQueryset(self.model, using=self._db)

    def search(self, query):

        return self.get_queryset().search(query)


class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=200)
    writer = models.ForeignKey(Writer, on_delete=models.CASCADE)
    genre = models.CharField(max_length=50)
    review = models.CharField(max_length=250)
    publisher = models.ForeignKey(Publisher,on_delete=models.CASCADE)
    price = models.CharField(max_length=100)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=True, blank=True)

    objects = BookManager()

    def __str__(self):
        return self.book_name

    def get_absolute_url(self):
        return reverse('book-update', kwargs={'slug': self.slug})


def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(rl_pre_save_receiver, sender=Book)