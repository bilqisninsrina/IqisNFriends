from allauth.socialaccount.models import SocialApp
from django.conf import settings
from django.contrib.auth import logout
from django.db.utils import DatabaseError, OperationalError
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from .models import SiteAppearance


BIODATA_LIST = [
    {
        "nama_panjang": "Bilqis Nisrina Dzahabiyah Mulyadi",
        "nama_panggilan": "Bili",
        "ttl": "Jakarta, 7 Mei 2006",
        "domisili": "Depok",
    },
    {
        "nama_panjang": "Annisa Fakhira Cendekia",
        "nama_panggilan": "Nisa",
        "ttl": "Jakarta, 2 Februari 1999",
        "domisili": "Depok",
    },
    {
        "nama_panjang": "Nadila Salsabila Fauziyyah",
        "nama_panggilan": "Dila",
        "ttl": "Jakarta, 28 Juli 2001",
        "domisili": "Depok",
    },
    {
        "nama_panjang": "Rindu Aurellia Zahra",
        "nama_panggilan": "Rindu",
        "ttl": "Jakarta, 10 Oktober 1998",
        "domisili": "Depok",
    },
]

DEFAULT_THEME = "#f3f4f6"
DEFAULT_FONT = "jakarta"
FONT_CHOICES = {
    "jakarta": {
        "label": "Plus Jakarta Sans",
        "body": '"Plus Jakarta Sans", sans-serif',
    },
    "manrope": {
        "label": "Manrope",
        "body": '"Manrope", sans-serif',
    },
    "instrument": {
        "label": "Instrument Sans",
        "body": '"Instrument Sans", sans-serif',
    },
}


def google_oauth_ready() -> bool:
    if settings.GOOGLE_OAUTH_CONFIGURED:
        return True

    try:
        return SocialApp.objects.filter(provider="google", sites__id=settings.SITE_ID).exists()
    except (OperationalError, DatabaseError):
        return False


def is_editor(request: HttpRequest) -> bool:
    if not request.user.is_authenticated:
        return False

    user_email = (getattr(request.user, "email", "") or "").strip().lower()
    return user_email in settings.GROUP_EDITOR_EMAILS


@require_http_methods(["GET", "POST"])
def home(request: HttpRequest) -> HttpResponse:
    appearance = SiteAppearance.load()
    can_customize = is_editor(request)

    if request.method == "POST" and can_customize:
        theme_color = request.POST.get("theme_color", DEFAULT_THEME)
        font_choice = request.POST.get("font_choice", DEFAULT_FONT)

        if font_choice not in FONT_CHOICES:
            font_choice = DEFAULT_FONT

        appearance.theme_color = theme_color
        appearance.font_choice = font_choice
        appearance.save(update_fields=["theme_color", "font_choice", "updated_at"])
        return redirect("home")

    return render(
        request,
        "core/home.html",
        {
            "biodata_list": BIODATA_LIST,
            "theme_color": appearance.theme_color,
            "font_choice": appearance.font_choice,
            "font_family": FONT_CHOICES.get(appearance.font_choice, FONT_CHOICES[DEFAULT_FONT])["body"],
            "font_choices": [
                {"value": key, "label": option["label"]}
                for key, option in FONT_CHOICES.items()
            ],
            "google_oauth_ready": google_oauth_ready(),
            "can_customize": can_customize,
            "editor_emails": sorted(settings.GROUP_EDITOR_EMAILS),
        },
    )


def logout_view(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect("home")
