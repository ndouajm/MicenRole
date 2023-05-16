# Generated by Django 4.2.1 on 2023-05-13 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30, verbose_name='Nom')),
                ('date', models.DateField(verbose_name="Date d'ajout")),
                ('enfants', models.IntegerField(verbose_name="Nombres d'enfants")),
                ('date_conseil', models.DateTimeField()),
                ('etats', models.CharField(choices=[('N/D', ' Nom demarrer'), ('ENCOURS', 'En cours'), ('TERMINER', 'Terminer'), ('ANNULER', 'Annuler')], max_length=20)),
                ('objet', models.CharField(max_length=500, null=True, verbose_name='Objet')),
                ('economie', models.TextField(max_length=2000, null=True, verbose_name='Economie')),
                ('recommandation', models.TextField(max_length=2000, null=True, verbose_name='Recommandation')),
                ('observation_ct', models.TextField(max_length=2000, null=True, verbose_name='Observation')),
                ('order_jour', models.CharField(max_length=100, null=True, verbose_name='Ordre Du Jour')),
                ('document', models.FileField(blank=True, null=True, upload_to='static/img', verbose_name='Document')),
            ],
            options={
                'verbose_name': 'Role',
                'verbose_name_plural': 'Roles',
            },
        ),
    ]
