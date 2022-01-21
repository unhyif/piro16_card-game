<<<<<<< HEAD
# Generated by Django 4.0.1 on 2022-01-21 11:29
=======
# Generated by Django 4.0.1 on 2022-01-21 14:38
>>>>>>> feature/Jihyun

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
<<<<<<< HEAD
                ('attacker_num', models.IntegerField(blank=True, choices=[(1, 1), (3, 3), (7, 7), (8, 8), (10, 10)], verbose_name='공격자 선택')),
                ('defender_num', models.IntegerField(blank=True, choices=[(4, 4), (5, 5), (5, 5), (6, 6), (9, 9)], null=True, verbose_name='수비자 선택')),
                ('rule', models.CharField(blank=True, choices=[('BIG', 'BIG'), ('SMALL', 'SMALL')], max_length=5, verbose_name='승리 룰')),
                ('attacker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attack', to='cardgame.userlist', verbose_name='공격자')),
                ('defender', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='defend', to='cardgame.userlist', verbose_name='수비자')),
                ('winner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cardgame.userlist', verbose_name='승자')),
=======
                ('attacker_num', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (7, 7), (8, 8)], verbose_name='공격자 선택')),
                ('defender_num', models.IntegerField(blank=True, choices=[(2, 2), (3, 3), (5, 5), (6, 6), (9, 9)], null=True, verbose_name='수비자 선택')),
                ('rule', models.CharField(blank=True, choices=[('BIG', 'BIG'), ('SMALL', 'SMALL')], max_length=5, verbose_name='승리 룰')),
                ('attacker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attack', to='cardgame.profile', verbose_name='공격자')),
                ('defender', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='defend', to='cardgame.profile', verbose_name='수비자')),
                ('winner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cardgame.profile', verbose_name='승자')),
>>>>>>> feature/Jihyun
            ],
        ),
    ]
