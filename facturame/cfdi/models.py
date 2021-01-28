from django.db import models

class CfdiModel(models.Model):
    id = models.AutoField(primary_key=True)
    issuer_name = models.CharField(max_length=100)
    date_issued = models.DateTimeField(auto_now_add=True)
    issuer_rfc = models.CharField(max_length=13)
    cfdi_xml = models.TextField()
    total_ammount= models.DecimalField(max_digits=15, decimal_places=2)