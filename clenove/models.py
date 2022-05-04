from django.db import models
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.

class Skaut(models.Model):
    jmeno = models.CharField("Jméno", max_length=100)
    prezdivka = models.CharField("Přezdívka",
        help_text="Prosím, zadávejte bez diakritiky",
        max_length=100)
    vek = models.IntegerField("Věk")
    slug = models.SlugField()
    splneno = models.BooleanField("Splněno", default=False, help_text="Už splnil skautskou zkoušku?")

    def get_absolute_url(self):
        return reverse("detail_clena", args = [self.slug])
    
    
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.prezdivka)
    #     print("Chxes me ulozit?")
    #     super().save(*args, **kwargs)
        
    
    def __str__(self):
        return f"{self.jmeno} - {self.prezdivka}"

    class Meta:
        verbose_name_plural = "Skauti"

# positional arguments
# keyword arguments