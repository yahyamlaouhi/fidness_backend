# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthentificationNote(models.Model):
    id = models.BigAutoField(primary_key=True)
    body = models.TextField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'authentification_note'


class Client(models.Model):
    id = models.AutoField(primary_key=True)
    civilite = models.BigIntegerField(blank=True, null=True)
    nom_prenom = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    date_naissance = models.TextField(blank=True, null=True)
    date_inscription = models.TextField(blank=True, null=True)
    id_gouvernorat = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'client'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class FidAdmin(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    id =models.AutoField(primary_key=True)
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


class FidCarteMagnetique(models.Model):
    email_responsable = models.TextField(db_collation='utf8_bin', blank=True, null=True)
    enseigne = models.TextField(db_collation='utf8_bin', blank=True, null=True)
    id_admin_creation = models.BigIntegerField(blank=True, null=True)
    index = models.BigIntegerField(blank=True, null=True)
    telephone = models.BigIntegerField(blank=True, null=True)
    id = models.AutoField(primary_key=True)
    id_secteur_activite = models.BigIntegerField(blank=True, null=True)
    email_contact = models.TextField(db_collation='utf8_bin', blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fid_carte_magnetique'


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


class FidClientCarteMagnetique(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    id = models.AutoField(primary_key=True)
    id_client = models.BigIntegerField(blank=True, null=True)
    id_carte_magnetique = models.BigIntegerField(blank=True, null=True)
    numero_carte = models.BigIntegerField(blank=True, null=True)
    date_creation = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fid_client_carte_magnetique'


class FidClientMarque(models.Model):
    nbre_produit_achat = models.BigIntegerField(blank=True, null=True)
    id_marque = models.BigIntegerField(blank=True, null=True)
    date_achat = models.TextField(db_collation='utf8_bin', blank=True, null=True)
    nbre_point_fid_global = models.BigIntegerField(blank=True, null=True)
    id_client = models.BigIntegerField(blank=True, null=True)
    nbre_point_fid_achat = models.BigIntegerField(blank=True, null=True)
    nom_produit = models.TextField(db_collation='utf8_bin', blank=True, null=True)
    id = models.AutoField(primary_key=True)
    nbre_point_fid_actuel = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fid_client_marque'


class FidClientPalierTampon(models.Model):
    id = models.AutoField(primary_key=True)
    id_carte_fidelite = models.BigIntegerField(blank=True, null=True)
    id_client = models.BigIntegerField(blank=True, null=True)
    id_marque = models.BigIntegerField(blank=True, null=True)
    nbre_tampon_global = models.BigIntegerField(blank=True, null=True)
    nbre_tampon_actuelle = models.BigIntegerField(blank=True, null=True)
    date_achat = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fid_client_palier_tampon'


class FidDroitAccess(models.Model):
    id = models.AutoField(primary_key=True)
    label = models.TextField(db_collation='utf8_bin', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fid_droit_access'


class FidGouvernorat(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    id = models.AutoField(primary_key=True)
    nom = models.TextField(db_collation='utf8_bin', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fid_gouvernorat'


class FidMarque(models.Model):
    code_postal = models.TextField(db_collation='utf8_bin', blank=True, null=True)
    prenom_responsable = models.TextField(db_collation='utf8_bin', blank=True, null=True)
    id_admin_creation = models.BigIntegerField(blank=True, null=True)
    telephone = models.TextField(db_collation='utf8_bin', blank=True, null=True)
    id_gouvernorat = models.BigIntegerField(blank=True, null=True)
    nom_prenom_responsable = models.TextField(db_collation='utf8_bin', blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    email_responsable = models.TextField(db_collation='utf8_bin', blank=True, null=True)
    telephone_responsable = models.TextField(db_collation='utf8_bin', blank=True, null=True)
    id = models.AutoField(primary_key=True)
    id_secteur_activite = models.BigIntegerField(blank=True, null=True)
    email_contact = models.TextField(db_collation='utf8_bin', blank=True, null=True)
    raison_sociale = models.TextField(db_collation='utf8_bin', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fid_marque'


class FidPdv(models.Model):
    code_postal = models.TextField(db_collation='utf8_bin', blank=True, null=True)
    id_admin_creation = models.BigIntegerField(blank=True, null=True)
    id_marque = models.BigIntegerField(blank=True, null=True)
    titre_responsable = models.TextField(db_collation='utf8_bin', blank=True, null=True)
    index = models.BigIntegerField(blank=True, null=True)
    telephone = models.TextField(db_collation='utf8_bin', blank=True, null=True)
    id_gouvernorat = models.BigIntegerField(blank=True, null=True)
    nom_prenom_responsable = models.TextField(db_collation='utf8_bin', blank=True, null=True)
    date_creation = models.DateTimeField(blank=True, null=True)
    email_responsable = models.TextField(db_collation='utf8_bin', blank=True, null=True)
    enseigne = models.TextField(db_collation='utf8_bin', blank=True, null=True)
    telephone_responsable = models.TextField(db_collation='utf8_bin', blank=True, null=True)
    id_carte_fidelite = models.BigIntegerField(blank=True, null=True)
    id = models.AutoField(primary_key=True)
    email_contact = models.TextField(db_collation='utf8_bin', blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    adress = models.CharField(max_length=45, blank=True, null=True)
    type=models.CharField(max_length=45, blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'fid_pdv'


class FidRoleAdmin(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    id = models.AutoField(primary_key=True)
    id_admin = models.FloatField(blank=True, null=True)
    id_droit_acces = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fid_role_admin'


class FidSecteurActivite(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    id = models.AutoField(primary_key=True)
    nom = models.TextField(db_collation='utf8_bin', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fid_secteur_activite'


class TokenBlacklistBlacklistedtoken(models.Model):
    id = models.AutoField(primary_key=True)
    blacklisted_at = models.DateTimeField()
    token = models.OneToOneField('TokenBlacklistOutstandingtoken', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'token_blacklist_blacklistedtoken'


class TokenBlacklistOutstandingtoken(models.Model):
    id = models.AutoField(primary_key=True)
    token = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    expires_at = models.DateTimeField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    jti = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'token_blacklist_outstandingtoken'


class FidGeolocalisation(models.Model,):
    id = models.BigAutoField(primary_key=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    fid_pdv = models.CharField(max_length=45, blank=True, null=True)
    visited = models.IntegerField(default = 1)

    class Meta:
        managed = False
        db_table = 'fid_geolocalisation'



