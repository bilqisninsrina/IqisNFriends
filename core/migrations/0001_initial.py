from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SiteAppearance",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("theme_color", models.CharField(default="#f3f4f6", max_length=7)),
                ("font_choice", models.CharField(default="jakarta", max_length=32)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
