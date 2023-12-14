from django.urls import path

from mainapp import views
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path("", views.MainPageView.as_view(), name="index"),
    path("catalog/", views.CatalogPageView.as_view(), name="catalog"),
    path("portfolio/", views.PortfolioPageView.as_view(), name="portfolio"),
    path("contacts/", views.ContactPageView.as_view(), name="contacts"),
    path("detail/", views.DetailPageView.as_view(), name="detail"),
    path("stendy-datchikov/", views.SensorStandsPageView.as_view(), name="stendy-datchikov"),
    path("puskonaladochnye-raboty/", views.CommissioningWorksPageView.as_view(), name="puskonaladochnye-raboty"),
    path("elektromontazhnye-raboty/", views.ElectricalInstallationWorksPageView.as_view(), name="elektromontazhnye-raboty"),
    path("proektirovanie-kip/", views.DesignKipPageView.as_view(), name="proektirovanie-kip"),
    path("privacy/", views.PrivacyPageView.as_view(), name="privacy"),
    path("kipa/", views.KipaPageView.as_view(), name="kipa"),
    path("detail_exam/", views.DetailexamPageView.as_view(), name="detail_exam"),
]