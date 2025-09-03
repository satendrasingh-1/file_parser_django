from django.db import models
import uuid

class UploadedFile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file = models.FileField(upload_to="uploads/")
    filename = models.CharField(max_length=255)
    status = models.CharField(
        max_length=20,
        choices=[("uploading", "Uploading"),
                 ("processing", "Processing"),
                 ("ready", "Ready"),
                 ("failed", "Failed")],
        default="uploading"
    )
    progress = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    parsed_content = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.filename

