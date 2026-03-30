from django.contrib.auth import logout
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods


BIODATA_LIST = [
    {
        "nama_panjang": "Iqis Nur Aini Putri",
        "nama_panggilan": "Iqis",
        "ttl": "Bandung, 15 Mei 2000",
        "domisili": "Bandung",
    },
    {
        "nama_panjang": "Rizki Maulana Pratama",
        "nama_panggilan": "Rizki",
        "ttl": "Jakarta, 2 Februari 1999",
        "domisili": "Jakarta",
    },
    {
        "nama_panjang": "Nadia Salsabila Ramadhani",
        "nama_panggilan": "Nadia",
        "ttl": "Surabaya, 28 Juli 2001",
        "domisili": "Surabaya",
    },
    {
        "nama_panjang": "Fajar Aditya Nugraha",
        "nama_panggilan": "Fajar",
        "ttl": "Yogyakarta, 10 Oktober 1998",
        "domisili": "Yogyakarta",
    },
]

DEFAULT_THEME = "#f3f4f6"


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
        },
    )


def logout_view(request: HttpRequest) -> HttpResponse:
    logout(request)
    request.session.pop("theme_color", None)
    return redirect("home")
