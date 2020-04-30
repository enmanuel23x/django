from django.db import models

# Create your models here.
class Carousel(models.Model):
    """TODO Model definition for Carousel."""

    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="webBeconsult/img/uploads", null=True) #TODO
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
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=45)
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

class Employees(models.Model):
    """TODO Model definition for JobOffer."""
    name = models.CharField(max_length=45)
    title = models.CharField(max_length=45)
    image = models.ImageField(upload_to="webBeconsult/img/uploads/empleados", null=True) #TODO
    description = models.TextField()

    # Creado y actualizado
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Employees."""

        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self):
        """Unicode representation of Employess."""
        return self.name