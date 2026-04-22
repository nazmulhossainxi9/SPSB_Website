# Generated migration for Volunteer model

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('SPSB', '0006_alter_media_file_hash'),
    ]

    operations = [
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='volunteers/')),
                ('bio', models.TextField(blank=True, default='', help_text='Public bio/contribution description')),
                ('institution', models.CharField(blank=True, default='', help_text='School/College/University Name', max_length=255)),
                ('degree', models.CharField(blank=True, default='', help_text='e.g., B.Tech CSE, B.A. English', max_length=150)),
                ('graduation_year', models.IntegerField(blank=True, help_text='Expected/Actual graduation year', null=True)),
                ('instagram_handle', models.CharField(blank=True, default='', max_length=100)),
                ('twitter_handle', models.CharField(blank=True, default='', max_length=100)),
                ('linkedin_url', models.URLField(blank=True, default='')),
                ('facebook_url', models.URLField(blank=True, default='')),
                ('website_url', models.URLField(blank=True, default='')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(blank=True, default='', max_length=20)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('address', models.TextField(blank=True, default='')),
                ('city', models.CharField(blank=True, default='', max_length=100)),
                ('state', models.CharField(blank=True, default='', max_length=100)),
                ('zip_code', models.CharField(blank=True, default='', max_length=20)),
                ('emergency_contact_name', models.CharField(blank=True, default='', max_length=150)),
                ('emergency_contact_phone', models.CharField(blank=True, default='', max_length=20)),
                ('volunteer_year', models.IntegerField(db_index=True, help_text='Year of volunteering (e.g., 2024)')),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('past', 'Past Volunteer')], db_index=True, default='active', max_length=20)),
                ('role', models.CharField(blank=True, default='', help_text='e.g., Event Coordinator, Social Media Manager', max_length=150)),
                ('joining_date', models.DateField(auto_now_add=True)),
                ('contribution_hours', models.IntegerField(default=0)),
                ('is_public', models.BooleanField(default=True, help_text="Check to display this volunteer's public profile")),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('added_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='added_volunteers', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Volunteer',
                'verbose_name_plural': 'Volunteers',
                'ordering': ['-volunteer_year', 'first_name'],
            },
        ),
        migrations.AddIndex(
            model_name='volunteer',
            index=models.Index(fields=['volunteer_year', 'status'], name='SPSB_volun_volunte_idx'),
        ),
        migrations.AddIndex(
            model_name='volunteer',
            index=models.Index(fields=['is_public', 'volunteer_year'], name='SPSB_volun_is_publ_idx'),
        ),
    ]
