# Generated by Django 3.0.5 on 2020-05-31 09:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('username', models.EmailField(blank=True, max_length=254, null=True, verbose_name='username')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('password', models.CharField(blank=True, max_length=100)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('name', models.CharField(max_length=200)),
                ('mobile_number', models.CharField(blank=True, max_length=20)),
                ('primary_number', models.CharField(blank=True, max_length=20)),
                ('mobile_number_verified', models.BooleanField(default=False)),
                ('email_verified', models.BooleanField(default=False)),
                ('account_activation_token', models.CharField(blank=True, max_length=100)),
                ('address', models.TextField(blank=True, max_length=200)),
                ('city', models.CharField(blank=True, max_length=120)),
                ('state', models.CharField(blank=True, choices=[('BW', 'Baden-Württemberg'), ('BY', 'Bayern'), ('BE', 'Berlin'), ('BB', 'Brandenburg'), ('HB', 'Bremen'), ('HH', 'Hamburg'), ('HE', 'Hessen'), ('MV', 'Mecklenburg-Vorpommern'), ('NI', 'Niedersachsen'), ('NW', 'Nordrhein-Westfalen'), ('RP', 'Rheinland-Pfalz'), ('SL', 'Saarland'), ('SN', 'Sachsen'), ('ST', 'Sachsen-Anhalt'), ('SH', 'Schleswig-Holstein'), ('TH', 'Thüringen')], max_length=120)),
                ('country', models.CharField(blank=True, max_length=120)),
                ('postal_code', models.CharField(blank=True, max_length=20)),
                ('total_purchases', models.CharField(blank=True, max_length=20)),
                ('forgot_password_token', models.CharField(blank=True, max_length=100)),
                ('file_sharing_token', models.CharField(blank=True, max_length=100)),
                ('status', models.BooleanField(default=False)),
                ('role', models.CharField(choices=[('user', 'user'), ('toc', 'toc')], default='user', max_length=250)),
                ('tax_number', models.CharField(max_length=250)),
                ('profile_image', models.CharField(max_length=250)),
                ('profile_image_path', models.CharField(max_length=250)),
                ('file_encryption_key', models.CharField(blank=True, max_length=250, null=True)),
                ('users_under_toc', models.TextField(blank=True, max_length=1500, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TOCUser',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('users.user',),
        ),
    ]
