# Generated by Django 4.2.16 on 2024-10-21 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarefas', '0004_rename_usuarios_usuario_delete_atividade'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='funcao',
            field=models.CharField(max_length=50, null=True),
        ),
    ]