# Generated by Django 4.1.3 on 2022-12-11 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shared', '0001_initial'),
        ('uploads', '0002_upload_enable_hls'),
    ]

    operations = [
        migrations.CreateModel(
            name='HlsVideo',
            fields=[
                ('uuidmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shared.uuidmodel')),
                ('hls_video', models.FileField(blank=True, null=True, upload_to='videos/tls/')),
                ('status', models.CharField(choices=[('pend', 'Pending'), ('inpr', 'In Progress'), ('undf', 'Undefined'), ('done', 'Done')], default='undf', max_length=4)),
                ('uploaded_video', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='uploaded_video', to='uploads.upload')),
            ],
            bases=('shared.uuidmodel',),
        ),
    ]
