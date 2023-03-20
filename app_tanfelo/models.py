from django.db import models

# Create your models here.

   
class Tantargy(models.Model):
    """Model definition for Tantargy."""

    # TODO: Define fields here

    nev = models.CharField(max_length=100)


    class Meta:
        """Meta definition for Tantargy."""

        verbose_name = 'Tantárgy'
        verbose_name_plural = 'Tantárgyak'

    def __str__(self):
        return self.nev
    
class Tanar(models.Model):
    """Model definition for Tanar."""

    # TODO: Define fields here

    nev = models.CharField(max_length=100)
    tantargyai = models.ManyToManyField(Tantargy)


    class Meta:
        """Meta definition for Tanar."""

        verbose_name = 'Tanár'
        verbose_name_plural = 'Tanárok'

    def __str__(self):
        return self.nev

