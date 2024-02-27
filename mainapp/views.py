from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm
from django.urls import reverse_lazy, reverse
from config.settings import DEFAULT_FROM_EMAIL, RECIPIENTS_EMAIL
import logging
from mainapp.models import Category, Group, Subgroup, Product
from django.shortcuts import get_object_or_404, redirect

logger = logging.getLogger(__name__)

# Create your views here.

class MainPageView(TemplateView):
    template_name = "mainapp/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu_name"] = "index"
        context["categories"] = Category.objects.all()
        return context


class CatalogPageView(TemplateView):
    template_name = "mainapp/catalog.html"

    def get_context_data(self, slug=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu_name"] = "catalog"
        context["categories"] = Category.objects.all()
        context["category"] = get_object_or_404(Category, slug=slug)
        pk = context["category"].id
        context["groups_category"] = Group.objects.all().filter(category=pk)
        return context

class GroupPageView(TemplateView):
    template_name = "mainapp/catalog-card.html"

    def get_context_data(self, slug=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu_name"] = "catalog"
        context["group_a"] = get_object_or_404(Group, slug=slug)
        pk = context["group_a"].category.id
        context["groups"] = Group.objects.all().filter(category=pk)
        ps = context["group_a"].id
        context["subgroups"] = Subgroup.objects.all().filter(group=ps)
        # print(context["subgroups"])
        return context

class SubgroupPageView(TemplateView):
    template_name = "mainapp/catalog-table.html"

    def get_context_data(self, slug=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu_name"] = "catalog"
        context["subgroup_a"] = get_object_or_404(Subgroup, slug=slug)
        pk = context["subgroup_a"].group.id
        context["subgroups"] = Subgroup.objects.all().filter(group=pk)
        ps = context["subgroup_a"].id
        context["products"] = Product.objects.all().filter(subgroup=ps)
        # print(context["subgroups"])
        return context




class WorkingPageView(TemplateView):
    template_name = "mainapp/working.html"

class ContactPageView(TemplateView):
    template_name = "mainapp/contacts.html"


# остальное



class PortfolioPageView(TemplateView):
    template_name = "mainapp/portfolio.html"



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


class SuccessPageView(TemplateView):
    template_name = "mainapp/success-template.html"
    form_class = ContactForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # извлекаем данные из формы
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            company = form.cleaned_data['company']
            message = form.cleaned_data['message']



            # отправляем сообщение
            send_mail(
                'Новая заявка от {}'.format(name),
                f'''
                Имя: {name}
                Email: {email}
                Телефон: {phone}
                Компания: {company}
                Сообщение: {message}
                ''',
                DEFAULT_FROM_EMAIL,  # Укажите ваш адрес электронной почты
                RECIPIENTS_EMAIL,  # Укажите адрес, на который нужно отправить письмо
                fail_silently=False,
            )
            context = self.get_context_data(**kwargs)
            context['text'] = "Ваша заявка отправлена. Мы свяжемся с Вами в ближайшее время"
            return self.render_to_response(context)
        else:
            logger.error('Form validation failed: %s', form.errors)
            return render(request, 'mainapp/success-template.html', {'form': form})

        # Если форма не валидна возвращаем ее с ошибками
        context = self.get_context_data(**kwargs)
        context['text'] = "Ой, что-то не так"
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = "Это get_context_data функция"
        return context

