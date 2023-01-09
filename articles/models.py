from django.db import models

# Create your models here.
class Articles(models.Model):
    CATEGORY = (
        ('fashion', "Fashion"),
        ('internation', 'International'),
        ('tech', 'Technology'),
        ('politics', 'Politics')
    )
    STATUS = (
        (0, "Draft"),
        (1, "Publish")
    )
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, null=True)
    description = models.TextField()
    content = models.TextField(null=True)
    category = models.CharField(choices=CATEGORY, default='tech', max_length=32)
    featured_image = models.ImageField(upload_to="static/uploads", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateField(auto_now_add=True, null=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title
    
class CalltoAction(models.Model):
    heading = models.CharField(max_length=255)
    tagline = models.CharField(max_length=255)
    button_text = models.CharField(max_length=55)
    btn_url = models.CharField(max_length=255)

    def __str__(self):
        return self.heading
    
class Categories(models.Model):
    category = models.CharField(max_length=255)
    def __str__(self):
        return self.category

class Tags(models.Model)    :
    tag = models.CharField(max_length=255)

    def __str__(self):
        return self.tag
    
