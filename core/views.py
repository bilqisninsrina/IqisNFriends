from allauth.socialaccount.models import SocialApp
from django.conf import settings
from django.contrib.auth import logout
from django.db.utils import DatabaseError, OperationalError
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods


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


def google_oauth_ready() -> bool:
    if settings.GOOGLE_OAUTH_CONFIGURED:
        return True

    try:
        return SocialApp.objects.filter(provider="google", sites__id=settings.SITE_ID).exists()
    except (OperationalError, DatabaseError):
        return False


@require_http_methods(["GET", "POST"])
def home(request: HttpRequest) -> HttpResponse:
    if request.method == "POST" and request.user.is_authenticated:
        theme_color = request.POST.get("theme_color", DEFAULT_THEME)
        request.session["theme_color"] = theme_color
        return redirect("home")

    return render(
        request,
        "core/home.html",
        {
            "biodata_list": BIODATA_LIST,
            "theme_color": request.session.get("theme_color", DEFAULT_THEME),
            "google_oauth_ready": google_oauth_ready(),
        },
    )


def logout_view(request: HttpRequest) -> HttpResponse:
    logout(request)
    request.session.pop("theme_color", None)
    return redirect("home")
