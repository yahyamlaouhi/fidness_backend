from django.db import models

# Create your models here.
class FidAdmin(models.Model):
    id = models.AutoField(primary_key=True)
    id_marque = models.BigIntegerField(blank=True, null=True)
    id_pdv = models.BigIntegerField(blank=True, null=True)
    id_carte_magnetique = models.FloatField(blank=True, null=True)
    nom = models.TextField(blank=True, null=True)
    prenom = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    login = models.TextField(blank=True, null=True)
    mot_passe = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fid_admin'