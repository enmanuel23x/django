from django.db import models

# Create your models here.
class Banner(models.Model):
    """TODO Model definition for Carousel."""

    Title = models.CharField(max_length=100, null=True)
    Image = models.ImageField(upload_to="webBeconsult/img/uploads", null=True) #TODO
    URL = models.URLField(blank=True, null=True)
    Description = models.CharField(max_length=500, null=True)
    
    # Creado y actualizado
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Carousel."""

        verbose_name = 'Banner de bienvenida'
        verbose_name_plural = 'Banners'

    def __str__(self):
        """Unicode representation of Carousel."""
        return self.Title

class Carousel(models.Model):
    """TODO Model definition for Carousel."""

    Title = models.CharField(max_length=100, null=True)
    Image = models.ImageField(upload_to="webBeconsult/img/uploads", null=True) #TODO
    URL = models.URLField(blank=True, null=True)
    Description = models.CharField(max_length=500, null=True)
    
    # Creado y actualizado
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Carousel."""

        verbose_name = 'Carousel'
        verbose_name_plural = 'Carousels'

    def __str__(self):
        """Unicode representation of Carousel."""
        return self.Title

class JobOffer(models.Model):
    """TODO Model definition for JobOffer."""
    id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=120, null=True)
    Description = models.TextField(null=True)
    Tags_en_Perfil = models.TextField(max_length=250, null=True)
    Offer_ID = models.PositiveIntegerField(default=1)
    # Creado y actualizado
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for JobOffer."""

        verbose_name = 'Oferta de Trabajo'
        verbose_name_plural = 'Ofertas'

    def __str__(self):
        """Unicode representation of JobOffer."""
        return self.Title
    def getForm(self):
        return ("/form/"+str(self.Offer_ID))
    def getTags(self):
        return str(self.Tags_en_Perfil).split("&")
            

class Employees(models.Model):
    """TODO Model definition for JobOffer."""
    Name = models.CharField(max_length=120, null=True)
    Title = models.CharField(max_length=120, null=True)
    Image = models.ImageField(upload_to="webBeconsult/img/uploads/empleados", null=True) #TODO
    Description = models.TextField(null=True)

    # Creado y actualizado
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Employees."""

        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self):
        """Unicode representation of Employess."""
        return self.Name