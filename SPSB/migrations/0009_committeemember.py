# Generated migration for CommitteeMember model

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('SPSB', '0008_rename_spsb_volun_volunte_idx_spsb_volunt_volunte_c949d8_idx_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommitteeMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='committee/')),
                ('bio', models.TextField(blank=True, default='', help_text='Public bio/role description')),
                ('department', models.CharField(blank=True, default='', help_text='Department/Area they manage (e.g., Marketing, Operations)', max_length=150)),
                ('institution', models.CharField(blank=True, default='', help_text='School/College/University Name', max_length=255)),
                ('qualification', models.CharField(blank=True, default='', help_text='e.g., B.Tech CSE, MBA', max_length=150)),
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
                ('committee_year', models.IntegerField(db_index=True, help_text='Year of committee tenure (e.g., 2024)')),
                ('position', models.CharField(choices=[('president', 'President'), ('vice_president', 'Vice President'), ('secretary', 'Secretary'), ('treasurer', 'Treasurer'), ('coordinator', 'Coordinator'), ('lead', 'Team Lead'), ('member', 'Member')], default='member', help_text='Committee position/role', max_length=30)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('past', 'Past Member')], db_index=True, default='active', max_length=20)),
                ('joining_date', models.DateField(auto_now_add=True)),
                ('tenure_start', models.DateField(blank=True, help_text='Actual tenure start date', null=True)),
                ('tenure_end', models.DateField(blank=True, help_text='Tenure end date for past members', null=True)),
                ('is_public', models.BooleanField(default=True, help_text="Check to display this member's public profile")),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('added_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='added_committee_members', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Committee Member',
                'verbose_name_plural': 'Committee Members',
                'ordering': ['-committee_year', 'position', 'first_name'],
            },
        ),
        migrations.AddIndex(
            model_name='committeemember',
            index=models.Index(fields=['committee_year', 'status'], name='SPSB_commit_committe_idx'),
        ),
        migrations.AddIndex(
            model_name='committeemember',
            index=models.Index(fields=['is_public', 'committee_year'], name='SPSB_commit_is_publ_idx'),
        ),
        migrations.AddIndex(
            model_name='committeemember',
            index=models.Index(fields=['position', 'committee_year'], name='SPSB_commit_position_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='committeemember',
            unique_together={('email', 'committee_year')},
        ),
    ]
