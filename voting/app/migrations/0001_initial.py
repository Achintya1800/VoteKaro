# Generated by Django 4.2.2 on 2023-07-24 11:36

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone_number', models.CharField(max_length=12)),
                ('is_phone_verified', models.BooleanField(default=False)),
                ('user_type', models.CharField(choices=[('1', 'HOD'), ('2', 'Student')], default=2, max_length=50)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Session_Year',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_start', models.CharField(max_length=100)),
                ('session_end', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='StudentVotes',
            fields=[
                ('student_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('category1', models.BooleanField(default=False)),
                ('category2', models.BooleanField(default=False)),
                ('category3', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('uid', models.IntegerField()),
                ('gender', models.CharField(choices=[('1', 'Male'), ('2', 'Female')], default=None, max_length=50)),
                ('department', models.CharField(choices=[('1', 'Comps'), ('2', 'AIML'), ('3', 'DS'), ('4', 'EXTC'), ('5', 'IT'), ('6', 'ETRX'), ('7', 'MCA')], default=None, max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('uid', models.IntegerField()),
                ('gender', models.CharField(choices=[('1', 'Male'), ('2', 'Female')], default=None, max_length=50)),
                ('department', models.CharField(choices=[('1', 'Comps'), ('2', 'AIML'), ('3', 'DS'), ('4', 'EXTC'), ('5', 'IT'), ('6', 'ETRX'), ('7', 'MCA')], default=None, max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=100)),
                ('encrypted_candidate_id', models.CharField(max_length=200)),
                ('category_id', models.CharField(max_length=200)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'unique_together': {('user_id', 'category_id')},
            },
        ),
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='app.student')),
                ('category', models.CharField(choices=[('1', 'GENSEC'), ('2', 'FINANCESEC'), ('3', 'SPORTSSEC')], default=None, max_length=60)),
                ('votes', models.IntegerField(default=0)),
                ('reason', models.TextField(default=None)),
                ('status', models.CharField(choices=[('1', 'Selected'), ('2', 'Rejected')], default=None, max_length=60)),
            ],
        ),
    ]
