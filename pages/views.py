from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import ContactForm
from django.urls import reverse_lazy
from pycoingecko import CoinGeckoAPI


def index(request):
    cg = CoinGeckoAPI()
    result = cg.get_coins_markets('usd')
    return render(request, 'index.html', context={'coins': result})


def currency(request):
    cg = CoinGeckoAPI()
    result = cg.get_coins_markets('usd')
    return render(request, 'currency.html', context={'coins': result})


class AboutView(TemplateView):
    template_name = 'about.html'


class ContactView(SuccessMessageMixin, FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')
    success_message = 'Your message has been sent successfully'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def search(request):
    cg = CoinGeckoAPI()
    result = cg.search(query=request.GET['query'])
    coin_list = []
    for coin in result['coins']:
        # response = cg.get_coin_by_id(id=coin['id'])
        # market_response = cg.get_price(ids=coin['id'], include_market_cap=True, vs_currencies='usd')
        coin_dict = {
            'image': coin['thumb'],
            'name': coin['name'],
            # 'current_price': response['market_data']['current_price']['usd'],
            # 'market_cap': market_response[coin['id']]['usd_market_cap'],
        }

        coin_list.append(coin_dict)

    return render(request, 'currency.html', context={'coins': coin_list})
