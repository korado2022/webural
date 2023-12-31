from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class MainPageView(TemplateView):
    template_name = "mainapp/index.html"


class CatalogPageView(TemplateView):
    template_name = "mainapp/catalog.html"


class PortfolioPageView(TemplateView):
    template_name = "mainapp/portfolio.html"


class ContactPageView(TemplateView):
    template_name = "mainapp/contacts.html"

class DetailPageView(TemplateView):
    template_name = "mainapp/detail.html"

class SensorStandsPageView(TemplateView):
    template_name = "mainapp/stendy-datchikov.html"


class CommissioningWorksPageView(TemplateView):
    template_name = "mainapp/puskonaladochnye-raboty.html"

class ElectricalInstallationWorksPageView(TemplateView):
    template_name = "mainapp/elektromontazhnye-raboty.html"

class DesignKipPageView(TemplateView):
    template_name = "mainapp/proektirovanie-kip.html"

class PrivacyPageView(TemplateView):
    template_name = "mainapp/privacy.html"

class KipaPageView(TemplateView):
    template_name = "mainapp/kipa.html"

class DetailexamPageView(TemplateView):
    template_name = "mainapp/detail_exam.html"

class CatalogCardPageView(TemplateView):
    template_name = "mainapp/catalog-card.html"

class CatalogDetailPageView(TemplateView):
    template_name = "mainapp/catalog-detail.html"

class CatalogCardBobyshkiPageView(TemplateView):
    template_name = "mainapp/catalog-card-bobyshki.html"


class BobyshkiTablePageView(TemplateView):
    template_name = "mainapp/bobyshki-table.html"


class ProductDetailPageView(TemplateView):
    template_name = "mainapp/product-detail.html"


class CatalogDescriptPageView(TemplateView):
    template_name = "mainapp/catalog-descript.html"



