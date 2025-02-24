# Generated by Django 5.0.2 on 2025-02-24 04:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DefectsPortal', '0003_alter_defect_defect_type_alter_defect_priority'),
    ]

    operations = [
        migrations.CreateModel(
            name='Defects_screen_shots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('defect_image', models.ImageField(blank=True, null=True, upload_to='defectsimg/')),
                ('defect', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='defect', to='DefectsPortal.defect')),
            ],
        ),
    ]
