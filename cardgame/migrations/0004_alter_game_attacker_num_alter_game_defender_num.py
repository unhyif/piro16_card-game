# Generated by Django 4.0.1 on 2022-01-21 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardgame', '0003_alter_game_attacker_num_alter_game_defender_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='attacker_num',
            field=models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (7, 7), (8, 8), (9, 9)], verbose_name='공격자 선택'),
        ),
        migrations.AlterField(
            model_name='game',
            name='defender_num',
            field=models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (4, 4), (7, 7), (9, 9)], null=True, verbose_name='수비자 선택'),
        ),
    ]
