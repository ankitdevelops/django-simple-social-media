# Generated by Django 4.2 on 2023-04-12 02:17

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("post", "0003_alter_post_likes_comment"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment",
            old_name="author",
            new_name="user",
        ),
    ]
