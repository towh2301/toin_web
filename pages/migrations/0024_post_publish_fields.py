# Generated migration for Post model publishing fields

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0023_cvsubmission"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="is_published",
            field=models.BooleanField(
                default=False,
                help_text="Publish this post to make it visible on the blog",
            ),
        ),
        migrations.AddField(
            model_name="post",
            name="publish_date",
            field=models.DateTimeField(
                blank=True,
                null=True,
                help_text="Date and time when this post was published",
            ),
        ),
    ]
