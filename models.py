# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Citaciones(models.Model):
    id_hotel = models.OneToOneField('Hoteles', models.DO_NOTHING, db_column='Id_Hotel', primary_key=True)  # Field name made lowercase. The composite primary key (Id_Hotel, Id_Noticia) found, that is not supported. The first column is selected.
    id_noticia = models.ForeignKey('Noticias', models.DO_NOTHING, db_column='Id_Noticia')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Citaciones'
        unique_together = (('id_hotel', 'id_noticia'),)


class Consultas(models.Model):
    id_hotel = models.OneToOneField('Hoteles', models.DO_NOTHING, db_column='Id_Hotel', primary_key=True)  # Field name made lowercase. The composite primary key (Id_Hotel, Id_Usuario) found, that is not supported. The first column is selected.
    id_usuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='Id_Usuario')  # Field name made lowercase.
    fecha = models.DateField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Consultas'
        unique_together = (('id_hotel', 'id_usuario'),)


class Fuentes(models.Model):
    url = models.CharField(db_column='URL', primary_key=True, max_length=100)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Fuentes'


class Hoteles(models.Model):
    id_hotel = models.AutoField(db_column='Id_Hotel', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=20)  # Field name made lowercase.
    ciudad = models.CharField(db_column='Ciudad', max_length=30)  # Field name made lowercase.
    pais = models.CharField(db_column='Pais', max_length=30)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Hoteles'


class Multimedia(models.Model):
    id_noticia = models.OneToOneField('Noticias', models.DO_NOTHING, db_column='Id_Noticia', primary_key=True)  # Field name made lowercase. The composite primary key (Id_Noticia, Id_Multimedia) found, that is not supported. The first column is selected.
    id_multimedia = models.IntegerField(db_column='Id_Multimedia')  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=20)  # Field name made lowercase.
    url = models.CharField(db_column='URL', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Multimedia'
        unique_together = (('id_noticia', 'id_multimedia'),)


class Noticias(models.Model):
    id_noticia = models.AutoField(db_column='Id_Noticia', primary_key=True)  # Field name made lowercase.
    tÝtulo = models.CharField(db_column='TÝtulo', max_length=20)  # Field name made lowercase.
    fecha = models.DateField(db_column='Fecha')  # Field name made lowercase.
    contenido = models.TextField(db_column='Contenido')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Noticias'


class Usuarios(models.Model):
    id_usuario = models.CharField(db_column='Id_Usuario', primary_key=True, max_length=50)  # Field name made lowercase.
    nombres = models.CharField(db_column='Nombres', max_length=50)  # Field name made lowercase.
    apellidos = models.CharField(db_column='Apellidos', max_length=50)  # Field name made lowercase.
    tipo_cuenta = models.CharField(db_column='Tipo Cuenta', max_length=15)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rol = models.CharField(db_column='Rol', max_length=15)  # Field name made lowercase.
    contraseña = models.CharField(db_column='Contraseña', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Usuarios'
