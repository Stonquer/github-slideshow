# Generated by Django 3.2.2 on 2021-06-12 16:35

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ante', models.IntegerField()),
                ('betSize', models.IntegerField()),
                ('deckType', models.CharField(max_length=16)),
                ('tableNumber', models.IntegerField()),
                ('currency', models.CharField(choices=[('CHIP', 'Chips'), ('ALGO', 'Algorand'), ('USDC', 'Pot Limit Omaha')], default='CHIP', max_length=4)),
                ('gameselect', models.CharField(choices=[('OCWG', 'One Card Wager'), ('NLHE', 'No Limit Texas Hold Em'), ('PLO', 'Pot Limit Omaha'), ('DOMA', 'Domaha')], default='OCWG', max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('acctNo', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('First_Name', models.CharField(max_length=30)),
                ('Last_Name', models.CharField(max_length=30)),
                ('Screen_Name', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('number', models.IntegerField(primary_key=True, serialize=False)),
                ('maxPlayers', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table', models.IntegerField()),
                ('number', models.IntegerField()),
                ('taken', models.BooleanField()),
                ('occupant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='one_card_wager.player')),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('rank', models.CharField(max_length=1)),
                ('suit', models.CharField(max_length=1)),
                ('name', models.CharField(max_length=2)),
                ('backImage', models.CharField(max_length=100)),
                ('faceImage', models.CharField(max_length=100)),
                ('deck', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='one_card_wager.deck')),
            ],
        ),
    ]
