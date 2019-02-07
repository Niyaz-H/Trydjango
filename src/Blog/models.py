from django.db import models
from django.urls import reverse

# Create your models here.
class Article(models.Model):
    title           = models.CharField(max_length=20)
    text            = models.TextField(blank=False, null=True)
    reference       = models.TextField(blank=True, null=True)
    email           = models.EmailField(max_length=50, null="No email given")

    def get_absolute_url(self):
        return reverse("articles:article-detail", kwargs={"id": self.id}) #f"/products/{self.id}/"
