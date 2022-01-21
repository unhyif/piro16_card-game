# Generated by Django 4.0.1 on 2022-01-21 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardgame', '0005_alter_game_attacker_num_alter_game_defender_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='attacker_num',
            field=models.IntegerField(blank=True, choices=[(3, 3), (4, 4), (5, 5), (8, 8), (9, 9)], verbose_name='공격자 선택'),
        ),
        migrations.AlterField(
            model_name='game',
            name='defender_num',
            field=models.IntegerField(blank=True, choices=[(1, 1), (3, 3), (5, 5), (7, 7), (8, 8)], null=True, verbose_name='수비자 선택'),
        ),
    ]
