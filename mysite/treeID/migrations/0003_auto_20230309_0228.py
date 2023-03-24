# Generated by Django 3.2 on 2023-03-09 02:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treeID', '0002_auto_20210921_0152'),
    ]

    operations = [
        migrations.CreateModel(
            name='TreeDataFinal',
            fields=[
                ('waypoint', models.IntegerField(blank=True, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('altitude', models.FloatField(blank=True, null=True)),
                ('id', models.TextField(blank=True, primary_key=True, serialize=False)),
                ('zone', models.TextField(blank=True, null=True)),
                ('number', models.IntegerField(blank=True, null=True)),
                ('group_field', models.TextField(blank=True, db_column='group_', null=True)),
                ('leaf_fall', models.TextField(blank=True, choices=[('Deciduous', 'Evergreen'), ('Evergreen', 'Deciduous')], null=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('genus', models.TextField(blank=True, null=True)),
                ('species_name', models.TextField(blank=True, null=True)),
                ('family', models.TextField(blank=True, null=True)),
                ('origin', models.TextField(blank=True, null=True)),
                ('age_min', models.IntegerField(blank=True, null=True)),
                ('age_max', models.IntegerField(blank=True, null=True)),
                ('cbh', models.FloatField(blank=True, null=True)),
                ('dbh', models.FloatField(blank=True, null=True)),
                ('height_min', models.FloatField(blank=True, null=True)),
                ('height_max', models.FloatField(blank=True, null=True)),
                ('canopy_radius', models.FloatField(blank=True, null=True)),
                ('root_zone_infringement', models.FloatField(blank=True, null=True)),
                ('condition', models.TextField(blank=True, null=True)),
                ('priority', models.TextField(blank=True, null=True)),
                ('interest_house', models.TextField(blank=True, null=True)),
                ('trust_property', models.TextField(blank=True, null=True)),
                ('trust_property_address', models.TextField(blank=True, null=True)),
                ('is_champion', models.BooleanField(blank=True, null=True)),
                ('is_memorial', models.BooleanField(blank=True, null=True)),
                ('is_blue_mtn_native', models.BooleanField(blank=True, null=True)),
                ('is_pacific_slope_native', models.BooleanField(blank=True, null=True)),
                ('staked', models.TextField(blank=True, choices=[('yes', 'Yes'), ('no', 'No'), ('next', 'Next')], null=True)),
                ('memorial_person', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Tree Data',
                'verbose_name_plural': 'Tree Data',
            },
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_at'], 'verbose_name': 'Comment', 'verbose_name_plural': 'Comments'},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='ID',
            new_name='treeID',
        ),
        migrations.AddField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 9, 2, 28, 27, 818025)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='approval',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_text',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='contact_info',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='comment',
            name='photo',
            field=models.ImageField(blank=True, upload_to='tree_photos'),
        ),
    ]
