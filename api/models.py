from django.db import models


class Article(models.Model):
    AVAILABLE_CATEGORIES = [
        ("Artykuły", "Artykuły"),
        ("Postacie", "Postacie"),
        ("Miejsca", "Miejsca"),
        ("Przedmioty", "Przedmioty"),
        ("Stworzenia", "Stworzenia"),
        ("Książki/Filmy", "Książki/Filmy"),
        ("Inne", "Inne"),
    ]
    image_confirm = models.BooleanField(default=False)
    confirmed = models.BooleanField(default=False)
    main_page = models.BooleanField(default=False)
    title = models.CharField(max_length=24)
    slug = models.CharField(max_length=100, unique=True)
    category = models.CharField(max_length=15, choices=AVAILABLE_CATEGORIES)
    description = models.CharField(max_length=160)
    author = models.CharField(max_length=24)
    created_time = models.DateTimeField(auto_now=True)
    created = models.DateField(auto_now=True)
    image = models.ImageField(blank=True)
    source = models.CharField(max_length=160, default="", blank=True)
    like = models.IntegerField(default=0)

    class Meta:
        ordering = ['-created_time']

    def __str__(self):
        return self.title

class Version(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now=True)
    created = models.DateField(auto_now=True)
    text = models.TextField()
    confirm = models.BooleanField(default=False)

    class Meta:
        ordering = ['-confirm', '-created_time']