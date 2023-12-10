# Generated by Django 4.1.3 on 2023-12-10 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_projects_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='document',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=64)),
                ('doc', models.BinaryField()),
            ],
        ),
        migrations.CreateModel(
            name='link',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=64)),
                ('url', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='note',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=64)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('parent', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('completed', models.BooleanField()),
                ('archived', models.BooleanField()),
                ('lastActivity', models.DateField()),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.status')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.type')),
            ],
        ),
        migrations.CreateModel(
            name='task',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=64)),
                ('task', models.TextField()),
                ('order', models.IntegerField(unique=True)),
                ('ref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.project')),
            ],
        ),
        migrations.CreateModel(
            name='user_role',
            fields=[
                ('userid', models.IntegerField(primary_key=True, serialize=False)),
                ('role', models.TextField(max_length=32)),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.project')),
            ],
        ),
        migrations.RemoveField(
            model_name='links',
            name='ref',
        ),
        migrations.RemoveField(
            model_name='notes',
            name='ref',
        ),
        migrations.RemoveField(
            model_name='projects',
            name='status',
        ),
        migrations.RemoveField(
            model_name='projects',
            name='type',
        ),
        migrations.RemoveField(
            model_name='tasks',
            name='ref',
        ),
        migrations.RemoveField(
            model_name='user_roles',
            name='project_id',
        ),
        migrations.DeleteModel(
            name='documents',
        ),
        migrations.DeleteModel(
            name='links',
        ),
        migrations.DeleteModel(
            name='notes',
        ),
        migrations.DeleteModel(
            name='projects',
        ),
        migrations.DeleteModel(
            name='tasks',
        ),
        migrations.DeleteModel(
            name='user_roles',
        ),
        migrations.AddField(
            model_name='note',
            name='ref',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.project'),
        ),
        migrations.AddField(
            model_name='link',
            name='ref',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.project'),
        ),
        migrations.AddField(
            model_name='document',
            name='ref',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.project'),
        ),
    ]
