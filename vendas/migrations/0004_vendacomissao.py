# Generated by Django 2.1.2 on 2018-11-02 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0003_auto_20181102_1804'),
    ]

    operations = [
        migrations.CreateModel(
            name='VendaComissao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comissao', models.DecimalField(decimal_places=2, default=100.0, max_digits=6)),
                ('venda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendas.Venda')),
            ],
        ),
    ]
