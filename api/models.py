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
    image_confirm = models.BooleanField(default=False, verbose_name="zdjęcie zatwierdzone")
    confirmed = models.BooleanField(default=False, verbose_name="zatwierdzony")
    main_page = models.BooleanField(default=False, verbose_name="strona główna")
    title = models.CharField(max_length=24, unique=True, verbose_name="tytuł")
    slug = models.CharField(max_length=100, unique=True, verbose_name="slug")
    category = models.CharField(max_length=15, choices=AVAILABLE_CATEGORIES, verbose_name="kategoria")
    description = models.CharField(max_length=160, verbose_name="opis")
    author = models.CharField(max_length=24, verbose_name="autor")
    created_time = models.DateTimeField(auto_now=True)
    created = models.DateField(auto_now=True, verbose_name="utworzono")
    image = models.ImageField(blank=True, verbose_name="zdjęcie")
    source = models.CharField(max_length=160, default="", blank=True, verbose_name="źródło")
    like = models.IntegerField(default=0)
    views = models.IntegerField(default=0, verbose_name="wejścia")

    class Meta:
        ordering = ['confirmed', '-created_time']
        verbose_name = "artykuł"
        verbose_name_plural = "artykuły"

    def __str__(self):
        return self.title

class Version(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="artykuł")
    created_time = models.DateTimeField(auto_now=True)
    created = models.DateField(auto_now=True, verbose_name="utworzono")
    text = models.TextField(verbose_name="tekst")
    confirm = models.BooleanField(default=False, verbose_name="zatwierdzona")
    archived = models.BooleanField(default=False, verbose_name="archiwum")

    class Meta:
        ordering = ['archived', 'confirm', '-created_time',]
        verbose_name = "wersja"
        verbose_name_plural = "wersje"


class DailySimpleHit(models.Model):
    date = models.DateField(primary_key=True, verbose_name="data")
    home_hits = models.IntegerField(default=0, verbose_name="strona główna")
    category_hits = models.IntegerField(default=0, verbose_name="kategorie")
    article_hits = models.IntegerField(default=0, verbose_name="artykuły")

    class Meta:
        ordering = ["-date"]
        verbose_name = "dzienne wejście"
        verbose_name_plural = "dzienne wejścia"
    
    def __str__(self):
        return str(self.date)