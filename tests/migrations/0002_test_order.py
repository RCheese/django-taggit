import uuid

import django.utils.timezone
from django.db import migrations, models

import taggit.managers


class Migration(migrations.Migration):
    dependencies = [
        ("taggit", "0003_taggeditem_add_unique_index"),
        ("contenttypes", "0002_remove_content_type_name"),
        ("tests", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="UUIDPet",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={"ordering": ["created_at"]},
        ),
        migrations.AlterModelOptions(
            name="uuidfood", options={"ordering": ["created_at"]},
        ),
        migrations.AddField(
            model_name="blanktagmodel",
            name="tags",
            field=taggit.managers.TaggableManager(
                blank=True,
                help_text="A comma-separated list of tags.",
                through="taggit.TaggedItem",
                to="taggit.Tag",
                verbose_name="Tags",
            ),
        ),
        migrations.AddField(
            model_name="uuidfood",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="taggedtrackedfood",
            name="tag",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="taggedtrackedfood_items",
                to="tests.TrackedTag",
            ),
        ),
        migrations.AlterField(
            model_name="taggedtrackedpet",
            name="tag",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="taggedtrackedpet_items",
                to="tests.TrackedTag",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="uuidtaggeditem",
            unique_together={("content_type", "object_id", "tag")},
        ),
        migrations.CreateModel(
            name="UUIDHousePet",
            fields=[
                (
                    "uuidpet_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="tests.UUIDPet",
                    ),
                ),
                ("trained", models.BooleanField(default=False)),
            ],
            bases=("tests.uuidpet",),
        ),
        migrations.AddField(
            model_name="uuidpet",
            name="tags",
            field=taggit.managers.TaggableManager(
                help_text="A comma-separated list of tags.",
                through="tests.UUIDTaggedItem",
                to="tests.UUIDTag",
                verbose_name="Tags",
            ),
        ),
    ]
