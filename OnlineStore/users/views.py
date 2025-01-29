import asyncio

import telegram
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from OnlineStore.settings import TELEGRAM_CHAT_ID, TELEGRAM_TOKEN
from checkout.models import Order
from .forms import CreationForm, FeedbackForm
from .models import Feedback


@login_required
def user_orders(request):
    """
    Представление списка заказов пользователя.
    """
    orders = Order.objects.filter(user=request.user)
    context = {
        'orders': orders,
    }
    return render(request, 'users/user_orders.html', context)


@login_required
def profile(request):
    """
    Представление профиля пользователя.
    """
    return render(request, 'users/profile.html')


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('store:home')
    template_name = 'users/signup.html'


async def send_telegram_message(message):
    """
    Асинхронная функция для отправки сообщения в ТГ.
    """
    try:
        bot = telegram.Bot(token=TELEGRAM_TOKEN)
        chat_id = TELEGRAM_CHAT_ID
        await bot.send_message(chat_id=chat_id, text=message)
        print(f"✅ Сообщение успешно отправлено: {message}")
    except Exception as e:
        print(f"❌ Ошибка при отправке в Telegram: {e}")




def feedback_processing(request):
    print("🔍 feedback_processing вызван!")  # Отладка

    if request.method == 'POST':
        print("🔍 Это POST-запрос!")  # Отладка

        form = FeedbackForm(request.POST)
        if form.is_valid():
            print("✅ Форма валидна!")  # Отладка



