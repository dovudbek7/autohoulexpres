from functools import wraps
from django.shortcuts import redirect
import requests
from .forms import OrdersForm

TELEGRAM_BOT_TOKEN = '7483825117:AAGMLu95Huk3-u8x5x5fNuj2GgVeNckA_C4'
CHAT_ID = '-4589564113'
CONTACT_CHAT_ID = '-4537347598'


def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {'chat_id': CHAT_ID, 'text': message}
    requests.post(url, data=payload)


def send_contact_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {'chat_id': CONTACT_CHAT_ID, 'text': message}
    requests.post(url, data=payload)


def create_order_message(order):
    return (
        f"New Order by {order.name}\n"
        f"Pick-Up Location: {order.pick_up_location}\n"
        f"Delivery Location: {order.delivery_location}\n"
        f"Vehicle: {order.make.name} {order.model.name} ({order.year.year})\n"
        f"Transport Type: {order.get_open_enclosed_display()}\n"
        f"Email: {order.email}\n"
        f"Phone: {order.phone_number}\n"
        f"Date: {order.date}\n"
        f"Condition: {order.condition}"
    )


def create_contact_message(contact):
    return (
        f"New contact from: {contact.full_name}\n"
        f"Email: {contact.email}\n"
        f"Phone: {contact.phone}\n"
        f"Message: {contact.message}"
    )


def handle_post_request(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.method == 'POST':
            form = OrdersForm(request.POST)
            if form.is_valid():
                order = form.save()
                message = create_order_message(order)
                send_telegram_message(message)
                return redirect('auto:success')
        return view_func(request, *args, **kwargs)

    return wrapper
