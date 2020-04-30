from django.db import models

# Create your models here.
class Carousel(models.Model):
    """TODO Model definition for Carousel."""

    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="webBeconsult/img/uploads", null=False) #TODO
    url = models.URLField(blank=True, null=True)
    description = models.CharField(max_length=500)
    
    # Creado y actualizado
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Carousel."""

        verbose_name = 'Carousel'
        verbose_name_plural = 'Carousels'

    def __str__(self):
        """Unicode representation of Carousel."""
        return self.title

class JobOffer(models.Model):
    """TODO Model definition for JobOffer."""

    title = models.CharField(max_length=30)
    description = models.TextField()
    profile = models.TextField()

    # Creado y actualizado
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for JobOffer."""

        verbose_name = 'Oferta de Trabajo'
        verbose_name_plural = 'Ofertas'

    def __str__(self):
        """Unicode representation of JobOffer."""
        return self.title