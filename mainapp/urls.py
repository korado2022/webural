from django.urls import path
from django.urls import re_path

from mainapp import views
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path("", views.MainPageView.as_view(), name="index"),
    path("catalog/<slug:slug>/", views.CatalogPageView.as_view(), name="catalog"),
    path("service/<int:pk>/", views.ServicePageView.as_view(), name="service"),
    # re_path(r'(?P<slug>.*)/', views.GroupPageView.as_view(), name='group'),
    path("group/<slug:slug>/", views.GroupPageView.as_view(), name="group"),
    path("subgroup/<slug:slug>/", views.SubgroupPageView.as_view(), name="subgroup"),
    # path("catalog-card/bobyshki", views.CatalogCardBobyshkiPageView.as_view(), name="catalog-card-bobyshki"),
    # path("catalog-card/bobyshki/BN01/", views.BobyshkiTablePageView.as_view(), name="bobyshki-table"),
    # path("catalog-card/bobyshki/BN01/product-detail/", views.ProductDetailPageView.as_view(), name="product-detail"),
    # path("catalog-descript", views.CatalogDescriptPageView.as_view(), name="catalog-descript"),
    # path("catalog-detail/", views.CatalogDetailPageView.as_view(), name="catalog-detail"),
    # path("portfolio/", views.PortfolioPageView.as_view(), name="portfolio"),
    path("contacts/", views.ContactPageView.as_view(), name="contacts"),
    # path("detail/", views.DetailPageView.as_view(), name="detail"),
    # path("stendy-datchikov/", views.SensorStandsPageView.as_view(), name="stendy-datchikov"),
    # path("puskonaladochnye-raboty/", views.CommissioningWorksPageView.as_view(), name="puskonaladochnye-raboty"),
    # path("elektromontazhnye-raboty/", views.ElectricalInstallationWorksPageView.as_view(), name="elektromontazhnye-raboty"),
    # path("proektirovanie-kip/", views.DesignKipPageView.as_view(), name="proektirovanie-kip"),
    path("privacy/", views.PrivacyPageView.as_view(), name="privacy"),
    # path("kipa/", views.KipaPageView.as_view(), name="kipa"),
    path("working/", views.WorkingPageView.as_view(), name="working"),
    # path("detail_exam/", views.DetailexamPageView.as_view(), name="detail_exam"),
    path("success/", views.SuccessPageView.as_view(), name="success"),
]