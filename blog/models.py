from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()    
    image = models.ImageField(upload_to='images/')
    


# Create a blog model.

# add blog app to settings.
# create a migration.
# migrate.
# add to the admin.
