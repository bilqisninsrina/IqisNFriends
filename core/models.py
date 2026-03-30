from django.db import models


class SiteAppearance(models.Model):
    theme_color = models.CharField(max_length=7, default="#f3f4f6")
    font_choice = models.CharField(max_length=32, default="jakarta")
    updated_at = models.DateTimeField(auto_now=True)

    @classmethod
    def load(cls) -> "SiteAppearance":
        appearance, _ = cls.objects.get_or_create(
            pk=1,
            defaults={
                "theme_color": "#f3f4f6",
                "font_choice": "jakarta",
            },
        )
        return appearance

    def __str__(self) -> str:
        return "Site Appearance"
