from django.db import models

# Create your models here.
class FidClient(models.Model):
    id = models.AutoField(primary_key=True)
    civilite = models.FloatField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    date_naissance = models.DateField(blank=True, null=True)
    date_inscription = models.DateField(blank=True, null=True)
    id_gouvernorat = models.FloatField(blank=True, null=True)
    nom_prenom = models.TextField(blank=True, null=True)
    pays = models.TextField(blank=True, null=True)
    sexe = models.TextField(blank=True, null=True)
    age = models.BigIntegerField(blank=True, null=True)
    a_une_carte = models.BigIntegerField(blank=True, null=True)
    nbre_total_tampon = models.BigIntegerField(blank=True, null=True)
    nombre_annees = models.BigIntegerField(blank=True, null=True)
    quitte = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fid_client'