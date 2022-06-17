from django.db import models

# Create your models here.
class FidCarteFidelite(models.Model):
    type_contrat = models.TextField(db_collation='utf8_bin', blank=True, null=True)
    id_admin_creation = models.BigIntegerField(blank=True, null=True)
    code = models.TextField(db_collation='utf8_bin', blank=True, null=True)
    montant_achat_dt_field = models.BigIntegerField(db_column='montant_achat (DT)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    id_marque = models.BigIntegerField(blank=True, null=True)
    frais_contrat = models.BigIntegerField(db_column='Frais_contrat', blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField(primary_key=True)
    roi = models.FloatField(db_column='ROI', blank=True, null=True)  # Field name made lowercase.
    nom = models.TextField(db_collation='utf8_bin', blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fid_carte_fidelite'