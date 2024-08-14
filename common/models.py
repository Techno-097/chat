from django.db import models

class Home(models.Model):
    title = models.CharField("name", max_length=256)
    description = models.TextField("description")
    image = models.ImageField("image", upload_to="home/%Y/%m")

    class Meta:
        db_table = "Home"
        verbose_name = "Home"
        verbose_name_plural = "Homes"

    def __str__(self):
        return f"{self.title}"




class Not(models.Model):
    image = models.ImageField("image", upload_to="not/%Y/%m")
    title = models.CharField("title", max_length=256)
    text = models.TextField("text")

    class Meta:
        db_table = "Not"
        verbose_name = "Not"
        verbose_name_plural = "Nots"

    def __str__(self):
        return f"{self.title}"



class Image(models.Model):
    image = models.ImageField("image", upload_to="image/%Y/%m")
    text = models.TextField("text")
    name_position = models.CharField("position", max_length=256)

    class Meta:
        db_table = "Image"
        verbose_name = "Image"
        verbose_name_plural = "Images"
    def __str__(self):
        return f"{self.image}"




class Useful(models.Model):
    image = models.ImageField("image", upload_to="image/%Y/%m")
    text = models.TextField("text")
    about = models.CharField("about", max_length=256)
    boss_first_name = models.CharField("name", max_length=256)


    class Meta:
        db_table = "Useful"
        verbose_name = "Useful"
        verbose_name_plural = "Usefuls"

    def __str__(self):
        return f"{self.image}"




class All(models.Model):
    image = models.ImageField("image", upload_to="image/%Y/%m")
    number_of_project = models.IntegerField("project", max_length=256)
    category_of_project = models.CharField("category", max_length=256)

    class Meta:
        db_table = "All"
        verbose_name = "All"
        verbose_name_plural = "Alls"

    def __str__(self):
        return f"{self.image}"


# Create your models here.
