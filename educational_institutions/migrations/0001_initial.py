# Generated by Django 4.2.7 on 2023-11-11 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EducationalInstitution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_ru', models.CharField(max_length=128, verbose_name='Название на русском языке')),
                ('name_kz', models.CharField(max_length=128, verbose_name='Название на казахском языке')),
                ('type', models.IntegerField(choices=[(1, 'school'), (2, 'college'), (3, 'university')], default=None, verbose_name='Тип образовательного учреждения')),
                ('address', models.CharField(max_length=125, verbose_name='Адрес')),
                ('work_time', models.CharField(max_length=125, verbose_name='Рабочее время')),
            ],
            options={
                'verbose_name_plural': 'Образовательные учреждения',
                'db_table': 'educational_institutions',
            },
        ),
    ]
