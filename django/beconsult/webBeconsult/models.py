from django.db import models

# Create your models here.
class Carousel(models.Model):
    """TODO Model definition for Carousel."""

    Titulo = models.CharField(max_length=100)
    Imagen = models.ImageField(upload_to="webBeconsult/img/uploads", null=True) #TODO
    URL = models.URLField(blank=True, null=True)
    Descripcion = models.CharField(max_length=500)
    
    # Creado y actualizado
    Creado = models.DateTimeField(auto_now_add=True)
    Actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Carousel."""

        verbose_name = 'Carousel'
        verbose_name_plural = 'Carousels'

    def __str__(self):
        """Unicode representation of Carousel."""
        return self.Titulo

class JobOffer(models.Model):
    """TODO Model definition for JobOffer."""
    id = models.AutoField(primary_key=True)
    Titulo = models.CharField(max_length=120)
    Descripcion = models.TextField()
    Tags_en_Perfil = models.TextField(max_length=250, null=True)
    # Creado y actualizado
    Creado = models.DateTimeField(auto_now_add=True)
    Actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for JobOffer."""

        verbose_name = 'Oferta de Trabajo'
        verbose_name_plural = 'Ofertas'

    def __str__(self):
        """Unicode representation of JobOffer."""
        return self.Titulo
    def getTags(self):
        return str(self.Tags_en_Perfil).split("&")
            

class Employees(models.Model):
    """TODO Model definition for JobOffer."""
    Nombre = models.CharField(max_length=120)
    Titulo = models.CharField(max_length=120)
    Imagen = models.ImageField(upload_to="webBeconsult/img/uploads/empleados", null=True) #TODO
    Descripcion = models.TextField()

    # Creado y actualizado
    Creado = models.DateTimeField(auto_now_add=True)
    Actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Employees."""

        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self):
        """Unicode representation of Employess."""
        return self.Nombre