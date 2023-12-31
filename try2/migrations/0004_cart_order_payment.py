# Generated by Django 4.2.5 on 2023-09-14 07:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('try2', '0003_alter_addressbasic_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('details', models.CharField(max_length=12)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='try2.person')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('item_details', models.CharField(max_length=100)),
                ('done_payment', models.BooleanField()),
                ('price', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='try2.cart')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('paid_using', models.CharField(choices=[('cash', 'Cash'), ('online', 'Online'), ('NEFT', 'NEFT'), ('RTGS', 'RTGS')], default='', max_length=10)),
                ('account_no', models.IntegerField(blank=True, null=True)),
                ('bank_name', models.CharField(blank=True, max_length=19, null=True)),
                ('payment_date', models.DateTimeField(auto_now=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('reference_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='try2.order')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
