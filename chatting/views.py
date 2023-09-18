from django.views.generic import TemplateView
from django.utils import timezone

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class HomePage(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ConfirmSignUpView(TemplateView):
    template_name = 'confirm.html'
