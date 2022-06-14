from django.db import models
from sqlalchemy import false

# Create your models here.


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
    id_marque = models.IntegerField(blank=True, null=True)
    id_pdv = models.IntegerField(blank=True, null=True)
    nom = models.CharField(max_length=250, blank=True, null=True)
    prenom = models.CharField(max_length=250, blank=True, null=True)
    email = models.CharField(max_length=250, blank=True, null=True)
    login = models.CharField(max_length=250, blank=True, null=True)
    mot_passe = models.CharField(max_length=250, blank=True, null=True)
    derniere_activite = models.DateTimeField(blank=True, null=True)
    connecte = models.IntegerField(blank=True, null=True)
    demande_reinitialisation = models.IntegerField(blank=True, null=True)
    date_demande_reinitialisation = models.DateTimeField(blank=True, null=True)
    token_reinitialisation = models.CharField(max_length=250, blank=True, null=True)
    type = models.CharField(max_length=45, blank=True, null=True)
    etat = models.IntegerField(blank=True, null=True)
    id_createur = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fid_admin'


class FidAdminDroitAcces(models.Model):
    id = models.IntegerField(blank=True, null=True)
    id_admin = models.OneToOneField(FidAdmin, models.DO_NOTHING, db_column='id_admin', primary_key=True)
    id_droit_acces = models.ForeignKey('FidDroitAcces', models.DO_NOTHING, db_column='id_droit_acces')

    class Meta:
        managed = False
        db_table = 'fid_admin_droit_acces'
        unique_together = (('id_admin', 'id_droit_acces'),)


class FidBu(models.Model):
    id = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=45, blank=True, null=True)
    slug = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fid_bu'


class FidCarteFidelite(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.CharField(unique=True, max_length=250)
    nom = models.CharField(max_length=250)
    date_debut = models.DateTimeField(blank=True, null=True)
    date_expiration = models.DateTimeField(blank=True, null=True)
    type_palier = models.IntegerField(blank=True, null=True)
    coefficient = models.FloatField(blank=True, null=True)
    nbre_point_fidelite_cummule = models.IntegerField(blank=True, null=True)
    recto_carte = models.CharField(max_length=250, blank=True, null=True)
    verso_carte = models.CharField(max_length=250, blank=True, null=True)
    etat = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fid_carte_fidelite'


class FidCarteMagnetique(models.Model):
    id_secteur_activite = models.ForeignKey('FidSecteurActivite', models.DO_NOTHING, db_column='id_secteur_activite')
    enseigne = models.CharField(max_length=45, blank=True, null=True)
    logo = models.CharField(max_length=45, blank=True, null=True)
    etat = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fid_carte_magnetique'


class FidCarteMagnetiqueClient(models.Model):
    fid_carte_magnetique = models.OneToOneField(FidCarteMagnetique, models.DO_NOTHING, primary_key=True)
    fid_client = models.ForeignKey('FidClient', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'fid_carte_magnetique_client'
        unique_together = (('fid_carte_magnetique', 'fid_client'),)


# class FidCarteMagnetiqueHasFidCarteMagnetique(models.Model):
#     fid_carte_magnetique = models.OneToOneField(FidCarteMagnetique, models.DO_NOTHING, primary_key=True)
#     fid_carte_magnetique_id1 = models.ForeignKey(FidCarteMagnetique, models.DO_NOTHING, db_column='fid_carte_magnetique_id1')

#     class Meta:
#         managed = False
#         db_table = 'fid_carte_magnetique_has_fid_carte_magnetique'
#         unique_together = (('fid_carte_magnetique', 'fid_carte_magnetique_id1'),)


# class FidCarteMagnetiqueHasFidCarteMagnetique1(models.Model):
#     fid_carte_magnetique = models.OneToOneField(FidCarteMagnetique, models.DO_NOTHING, primary_key=True)
#     fid_carte_magnetique_id1 = models.ForeignKey(FidCarteMagnetique, models.DO_NOTHING, db_column='fid_carte_magnetique_id1',related_name='fid_carte_m_id1')

#     class Meta:
#         managed = False
#         db_table = 'fid_carte_magnetique_has_fid_carte_magnetique1'
#         unique_together = (('fid_carte_magnetique', 'fid_carte_magnetique_id1'),)


class FidCategorie(models.Model):
    id_marque = models.ForeignKey('FidMarque', models.DO_NOTHING, db_column='id_marque')
    nom = models.CharField(unique=True, max_length=250, blank=True, null=True)
    slug = models.CharField(max_length=250, blank=True, null=True)
    etat = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fid_categorie'
        unique_together = (('id', 'id_marque'),)


class FidClient(models.Model):
    civilite = models.IntegerField(blank=True, null=True)
    nom = models.CharField(max_length=100, blank=True, null=True)
    prenom = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    telephone = models.CharField(max_length=45, blank=True, null=True)
    date_naissance = models.DateTimeField(blank=True, null=True)
    token = models.CharField(max_length=250, blank=True, null=True)
    rib = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fid_client'


class FidClientCarteMagnetique(models.Model):
    id = models.IntegerField(unique=True)
    id_client = models.OneToOneField(FidClient, models.DO_NOTHING, db_column='id_client', primary_key=True)
    id_carte_magnetique = models.ForeignKey(FidCarteMagnetique, models.DO_NOTHING, db_column='id_carte_magnetique')
    note = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fid_client_carte_magnetique'
        unique_together = (('id_client', 'id_carte_magnetique', 'id'),)


# class FidClientHasFidClient(models.Model):
#     fid_client = models.OneToOneField(FidClient, models.DO_NOTHING, primary_key=True)
#     fid_client_id1 = models.ForeignKey(FidClient, models.DO_NOTHING, db_column='fid_client_id1')

#     class Meta:
#         managed = False
#         db_table = 'fid_client_has_fid_client'
#         unique_together = (('fid_client', 'fid_client_id1'),)


# class FidClientHasFidClient1(models.Model):
#     fid_client = models.OneToOneField(FidClient, models.DO_NOTHING, primary_key=True)
#     fid_client_id1 = models.ForeignKey(FidClient, models.DO_NOTHING, db_column='fid_client_id1')

#     class Meta:
#         managed = False
#         db_table = 'fid_client_has_fid_client1'
#         unique_together = (('fid_client', 'fid_client_id1'),)


class FidClientMarque(models.Model):
    id_client = models.ForeignKey(FidClient, models.DO_NOTHING, db_column='id_client')
    id_marque = models.PositiveIntegerField()
    nbre_produit_achat = models.IntegerField(blank=True, null=True)
    somme_achat = models.FloatField(blank=True, null=True)
    nbre_point_fid_achat = models.FloatField(blank=True, null=True)
    nbre_point_fid_actuel = models.FloatField(blank=True, null=True)
    nbre_point_fid_global = models.FloatField(blank=True, null=True)
    somme_gagne_actuel = models.FloatField(blank=True, null=True)
    somme_gagne_global = models.FloatField(blank=True, null=True)
    date_achat = models.DateTimeField(blank=True, null=True)
    etat_remboursement = models.IntegerField(blank=True, null=True)
    date_remboursemnt = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fid_client_marque'
        unique_together = (('id', 'id_client', 'id_marque'),)


class FidConfiguration(models.Model):
    adresse_mail_contact = models.CharField(db_column='adresse_mail _contact', max_length=250, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    adresse_mail_remarque = models.CharField(max_length=250, blank=True, null=True)
    nbre_points_gagne_partage = models.IntegerField(blank=True, null=True)
    nbre_points_gagne_parrainage = models.IntegerField(blank=True, null=True)
    nbre_points_gagne_checkin = models.IntegerField(blank=True, null=True)
    publicite = models.CharField(max_length=250, blank=True, null=True)
    nbre_points_gagne_publicite = models.IntegerField(blank=True, null=True)
    equivalence_addition_point = models.CharField(db_column='equivalence_addition_ point', max_length=250, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    nbre_additions_etablissemnt = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fid_configuration'


class FidDelegation(models.Model):
    id_gouvernorat = models.ForeignKey('FidGouvernorat', models.DO_NOTHING, db_column='id_gouvernorat')
    nom = models.CharField(max_length=250, blank=True, null=True)
    slug = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fid_delegation'


class FidDroitAcces(models.Model):
    label = models.CharField(max_length=250, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fid_droit_acces'


class FidGouvernorat(models.Model):
    nom = models.CharField(max_length=250, blank=True, null=True)
    slug = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fid_gouvernorat'


class FidKeyWordsMarque(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    fid_marque = models.ForeignKey('FidMarque', models.DO_NOTHING)
    key_word = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fid_key_words_marque'


class FidLocalite(models.Model):
    id_delegation = models.ForeignKey(FidDelegation, models.DO_NOTHING, db_column='id_delegation')
    id_gouvernorat = models.ForeignKey(FidGouvernorat, models.DO_NOTHING, db_column='id_gouvernorat')
    nom = models.CharField(max_length=250, blank=True, null=True)
    slug = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fid_localite'


class FidMarque(models.Model):
    id_pays = models.ForeignKey('FidPays', models.DO_NOTHING, db_column='id_pays')
    id_localite = models.ForeignKey(FidLocalite, models.DO_NOTHING, db_column='id_localite')
    id_secteur_activite = models.ForeignKey('FidSecteurActivite', models.DO_NOTHING, db_column='id_secteur_activite')
    id_nbre_employes = models.ForeignKey('FidNbreEmployes', models.DO_NOTHING, db_column='id_nbre_employes')
    url_google_plus = models.CharField(max_length=250, blank=True, null=True)
    raison_sociale = models.CharField(max_length=250, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    code_postal = models.CharField(max_length=45, blank=True, null=True)
    adresse = models.CharField(max_length=250, blank=True, null=True)
    responsable = models.CharField(max_length=250, blank=True, null=True)
    logo_site = models.CharField(max_length=250, blank=True, null=True)
    logo_app = models.CharField(max_length=250, blank=True, null=True)
    telephone = models.CharField(max_length=250, blank=True, null=True)
    fax = models.CharField(max_length=250, blank=True, null=True)
    email_contact = models.CharField(max_length=250, blank=True, null=True)
    site_web = models.CharField(max_length=250, blank=True, null=True)
    regime = models.CharField(max_length=250, blank=True, null=True)
    pays_participan_etranger = models.CharField(max_length=250, blank=True, null=True)
    url_fcb = models.CharField(max_length=250, blank=True, null=True)
    url_twitter = models.CharField(max_length=250, blank=True, null=True)
    nom_responsable = models.CharField(max_length=250, blank=True, null=True)
    prenom_responsable = models.CharField(max_length=250, blank=True, null=True)
    titre_responsable = models.CharField(max_length=250, blank=True, null=True)
    telephone_responsable = models.CharField(max_length=250, blank=True, null=True)
    email_responsable = models.CharField(max_length=250, blank=True, null=True)
    etat = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fid_marque'


class FidMarqueHasFidClient(models.Model):
    fid_marque = models.OneToOneField(FidMarque, models.DO_NOTHING, primary_key=True)
    fid_marque_fid_client_id = models.PositiveIntegerField()
    fid_client = models.ForeignKey(FidClient, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'fid_marque_has_fid_client'
        unique_together = (('fid_marque', 'fid_marque_fid_client_id', 'fid_client'),)


class FidNbreEmployes(models.Model):
    nom = models.CharField(max_length=250, blank=True, null=True)
    slug = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fid_nbre_employes'


class FidOffre(models.Model):
    id = models.IntegerField(primary_key=True)
    id_marque = models.ForeignKey(FidMarque, models.DO_NOTHING, db_column='id_marque')
    id_pdv = models.IntegerField(blank=True, null=True)
    prospectus = models.CharField(max_length=500, blank=True, null=True)
    nom = models.CharField(max_length=250, blank=True, null=True)
    date_debut = models.DateTimeField(blank=True, null=True)
    date_expiration = models.DateTimeField(blank=True, null=True)
    eat = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fid_offre'


class FidPalierPointFid(models.Model):
    id = models.IntegerField(primary_key=True)
    id_carte_fidelite = models.ForeignKey(FidCarteFidelite, models.DO_NOTHING, db_column='id_carte_fidelite')
    label_produit_achet = models.CharField(max_length=250, blank=True, null=True)
    nbre_points_fid_equivalente = models.CharField(max_length=45, blank=True, null=True)
    etat = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fid_palier_point_fid'


class FidPalierTampon(models.Model):
    id_carte_magnetique = models.ForeignKey(FidCarteMagnetique, models.DO_NOTHING, db_column='id_carte_magnetique')
    nbre_tampon = models.IntegerField(blank=True, null=True)
    equivalence_offre = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fid_palier_tampon'


class FidPays(models.Model):
    nom = models.CharField(max_length=45, blank=True, null=True)
    slug = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fid_pays'


class FidPdv(models.Model):
    id_pays = models.ForeignKey(FidPays, models.DO_NOTHING, db_column='id_pays')
    id_marque = models.ForeignKey(FidMarque, models.DO_NOTHING, db_column='id_marque')
    id_carte_fidelite = models.ForeignKey(FidCarteFidelite, models.DO_NOTHING, db_column='id_carte_fidelite')
    id_localite = models.ForeignKey(FidLocalite, models.DO_NOTHING, db_column='id_localite')
    id_secteur_activite = models.ForeignKey('FidSecteurActivite', models.DO_NOTHING, db_column='id_secteur_activite')
    code_postal = models.CharField(max_length=45, blank=True, null=True)
    adresse = models.CharField(max_length=250, blank=True, null=True)
    telepphone = models.CharField(max_length=45, blank=True, null=True)
    email_contact = models.CharField(max_length=45, blank=True, null=True)
    site_web = models.CharField(max_length=45, blank=True, null=True)
    latitude = models.IntegerField(blank=True, null=True)
    longitude = models.IntegerField(blank=True, null=True)
    nom_responsable = models.CharField(max_length=250, blank=True, null=True)
    prenom_responsable = models.CharField(max_length=250, blank=True, null=True)
    titre_responsable = models.CharField(max_length=250, blank=True, null=True)
    telephone_responsable = models.CharField(max_length=250, blank=True, null=True)
    email_responsable = models.CharField(max_length=250, blank=True, null=True)
    etat = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fid_pdv'


class FidPdvCarteMagnetique(models.Model):
    id = models.IntegerField(primary_key=True)
    id_carte_magnetique = models.ForeignKey(FidCarteMagnetique, models.DO_NOTHING, db_column='id_carte_magnetique')
    adresse = models.CharField(max_length=250, blank=True, null=True)
    longitude = models.CharField(max_length=250, blank=True, null=True)
    latitude = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fid_pdv_carte_magnetique'


class FidProduit(models.Model):
    id = models.IntegerField(primary_key=True)
    id_categorie = models.ForeignKey(FidCategorie, models.DO_NOTHING, db_column='id_categorie')
    code = models.CharField(max_length=250, blank=True, null=True)
    nom = models.CharField(max_length=250, blank=True, null=True)
    code_barre = models.CharField(max_length=250, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    image = models.CharField(max_length=250, blank=True, null=True)
    coefficient_achat_point_fid = models.IntegerField(blank=True, null=True)
    nbre_point_fid = models.IntegerField(blank=True, null=True)
    somme_gagne = models.CharField(max_length=45, blank=True, null=True)
    slug = models.CharField(max_length=250, blank=True, null=True)
    etat = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fid_produit'


class FidProduitHasFidClient(models.Model):
    fid_produit = models.OneToOneField(FidProduit, models.DO_NOTHING, primary_key=True)
    fid_client = models.ForeignKey(FidClient, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'fid_produit_has_fid_client'
        unique_together = (('fid_produit', 'fid_client'),)


class FidProspectus(models.Model):
    id = models.IntegerField(primary_key=True)
    id_marque = models.ForeignKey(FidMarque, models.DO_NOTHING, db_column='id_marque')
    id_pdv = models.IntegerField(blank=True, null=True)
    prospectus = models.CharField(max_length=500, blank=True, null=True)
    nom = models.CharField(max_length=250, blank=True, null=True)
    date_debut = models.DateTimeField(blank=True, null=True)
    date_expiration = models.DateTimeField(blank=True, null=True)
    eat = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fid_prospectus'


class FidRoleAdmin(models.Model):
    q3_role_admin = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fid_role_admin'


class FidSecteurActivite(models.Model):
    id_bu = models.ForeignKey(FidBu, models.DO_NOTHING, db_column='id_bu')
    nom = models.CharField(max_length=250, blank=True, null=True)
    slug = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fid_secteur_activite'

class FidPlaces(models.Model):
    id = models.IntegerField(primary_key=True)
    fid_client = models.ForeignKey(FidClient, models.DO_NOTHING)
    latitude = models.IntegerField(blank=True, null=True)
    longitude = models.IntegerField(blank=True, null=True)
    fid_pdv=models.ForeignKey(FidPdv, models.DO_NOTHING)
    time_consumed=models.DateField()
    fid_visited=models.IntegerField(blank=True, default=0)
    class Meta:
        managed = False
        db_table = 'fid_places'
        unique_together = (('id','fid_client'))



