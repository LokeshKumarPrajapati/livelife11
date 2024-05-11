from django.db import models



class DonationCause(models.Model):

    cause_title = models.CharField(max_length=255)
    cause_description = models.TextField()
    goal_amount = models.DecimalField(max_digits=10, decimal_places=2)
    raised_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    image = models.ImageField(upload_to='donation_cause_images/', blank=True)
    # image = models.ImageField(upload_to='donationimages/', blank=True)  # Optional image field
    def __str__(self):
      return self.cause_title


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/', blank=True)  # Optional image field
    pub_date = models.DateTimeField(auto_now_add=True)  # Automatic timestamp on creation

    def __str__(self):
        return self.title

class Donor(models.Model):
  name = models.CharField(max_length=100)


  def __str__(self):
    return self.name
  


class ContactForm(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    purpose = models.CharField(max_length=20, choices=[('general', 'General Inquiry'), ('event_join', 'Join Event')])
    event_name = models.CharField(max_length=255, blank=True)  # Optional field for event name
    submitted_at = models.DateTimeField(auto_now_add=True)  # Automatically record submission time

    def __str__(self):
        return f"{self.name} - {self.purpose}"


class Sponsor(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='sponsors/')  # Adjust upload path as needed

    def __str__(self):
        return self.name