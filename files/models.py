from django.db import models
from .validators import validate_extension
from account.models import Account
# Create your models here.

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/files_{0}/{1}'.format(instance.user.id, filename)

class ExcelDocument(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Account, editable=False, null=True, blank=True, on_delete=models.CASCADE)
    upload = models.FileField(upload_to=user_directory_path, validators=[validate_extension])

    def retrieve_data(request):
        # This query will yield you the files that are relevant to the specifc user.
        data = ExcelDocument.objects.filter(user=request.user.id)
        if data is None:
            return []
        else:
            return data
    
    def __str__(self):
        return str(self.upload)