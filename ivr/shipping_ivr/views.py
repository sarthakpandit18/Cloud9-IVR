import imp
import json

import boto3 as boto3
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from shipping_ivr.scheduling_services import get_city, get_branch, get_days, confirmedPickup
from twilio.twiml.voice_response import VoiceResponse
from .ivr_options import ivr_options
from .shipment_tracking import shipment_tracking
from .quotation_rates import quotation_rates
from shipping_ivr.download_invoice import get_shipment_details

from .utils.ngrok_update import update_ngrok_url
from decouple import config
import random, string

cities = get_city()
branches = get_branch()
days = get_days()
city = ''
branch = ''
day = ''
list = []
language = ""



# Create your views here.
@csrf_exempt
def welcome(request: HttpRequest) -> HttpResponse:
    vr = VoiceResponse()
    # update_ngrok_url()
    vr.say('Welcome to cloud-9!')
    vr.redirect(reverse('choose_language'))
    return HttpResponse(str(vr), content_type='text/xml')


@csrf_exempt
def choose_language(request: HttpRequest) -> HttpResponse:
    vr = VoiceResponse()
    with vr.gather(
            action=reverse('set_language'),
            num_digits=1,
            timeout=2000,
    ) as gather:
        gather.say("Please choose an option")
        gather.say("For English press 1")
        gather.say("For French press 2")
        
    vr.say('We did not receive your selection', voice=language)
    vr.redirect('')
    return HttpResponse(str(vr), content_type='text/xml')


@csrf_exempt
def set_language(request: HttpRequest) -> HttpResponse:
    vr = VoiceResponse()
    digits = request.POST.get('Digits')
    if digits == "1":
        global language
        language = "Polly.Joanna"
        vr.say("Your language is set to English")
    if digits == "2":
        language = "Polly.Lea"
        vr.say("Your language is set to French")
    vr.redirect(reverse('menu'))
    return HttpResponse(str(vr), content_type='text/xml')


@csrf_exempt
def menu(request: HttpRequest) -> HttpResponse:
    vr = VoiceResponse()
    ivr = ivr_options()
    data = json.loads(ivr)
    ivr = sorted(data, key=lambda d: d['id'])
    with vr.gather(
            action=reverse('options'),
            num_digits=1,
            timeout=2000,
    ) as gather:
        gather.say('Main Menu. Please choose an option', voice=language)
        for i in ivr:
            gather.say(f'For {i["name"]}  press {i["id"]}', voice=language)
        gather.say('Press 9 to disconnect the call')
    vr.say('We did not receive your selection', voice=language)
    vr.redirect('')

    return HttpResponse(str(vr), content_type='text/xml')


@csrf_exempt
def options(request: HttpRequest) -> HttpResponse:
    vr = VoiceResponse()
    digits = request.POST.get('Digits')
    if digits == "1":
        vr.say("Redirecting to shipment", voice=language)
        vr.redirect(reverse('track_shipment'))
    elif digits == "2":
        vr.say("Redirecting to scheduling", voice=language)
        vr.redirect(reverse('schedule_services'))
    elif digits == "3":
        vr.say("Redirecting to quotation", voice=language)
        vr.redirect(reverse('get_weight'))
    elif digits == "4":
        vr.say("Redirecting to invoice", voice=language)
        vr.redirect(reverse('invoice_input'))
    elif digits == '9':
        vr.say("Thank you for choosing cloud 9", voice=language)
        vr.hangup()

    return HttpResponse(str(vr), content_type='text/xml')


@csrf_exempt
def track_shipment(request: HttpRequest) -> HttpResponse:
    vr = VoiceResponse()
    with vr.gather(
            action=reverse('get_shipment_status'),
            finish_on_key='#'
    ) as gather:
        gather.say('Enter your tracking number and press #', voice=language)

    return HttpResponse(str(vr), content_type='text/xml')


@csrf_exempt
def get_shipment_status(request: HttpRequest) -> HttpResponse:
    vr = VoiceResponse()
    digits = request.POST.get('Digits')
    status = shipment_tracking(digits)
    item = json.loads(status)
    vr.say(f'Your shipment status is {item["status"]}  at {item["location"]}', voice=language)
    vr.redirect('menu')
    return HttpResponse(str(vr), content_type='text/xml')


@csrf_exempt
def schedule_services(request: HttpRequest) -> HttpResponse:
    vr = VoiceResponse()
    vr.say('Select from the following cities', voice=language)
    vr.redirect(reverse('get_cities'))
    return HttpResponse(str(vr), content_type='text/xml')


@csrf_exempt
def get_cities(request: HttpRequest) -> HttpResponse:
    vr = VoiceResponse()
    x = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    # print(x)
    # create_schedule('id',x)
    print(cities)
    with vr.gather(
            action=reverse('get_branches'),
            num_digits=1,
            timeout=2000
    ) as gather:
        data = json.loads(cities)
        item = sorted(data, key=lambda d: d['id'])
        for i in item:
            gather.say(f'Press {i["id"]}  for {i["city"]}', voice=language)
    return HttpResponse(str(vr), content_type='text/xml')


@csrf_exempt
def get_branches(request: HttpRequest) -> HttpResponse:
    vr = VoiceResponse()
    digits = request.POST.get('Digits')
    item = json.loads(cities)
    for c in item:
        if c["id"] == int(digits):
            list.append(c["city"])
            # print("City ", c['city'])
    with vr.gather(
            action=reverse('schedule_days'),
            num_digits=1,
            timeout=2000
    ) as gather:
        data = json.loads(branches)
        item = sorted(data, key=lambda d: d['id'])
        print("item: "+str(item))
        for i in item:
            if i["city_id"] == int(digits):
                gather.say(f'Press {i["id"]}  for {i["branch"]}', voice=language)
    return HttpResponse(str(vr), content_type='text/xml')


@csrf_exempt
def schedule_days(request: HttpRequest) -> HttpResponse:
    vr = VoiceResponse()
    digits = request.POST.get('Digits')
    item = json.loads(branches)
    print("days: "+str(item))
    for b in item:
        if b["id"] == int(digits):
            list.append(b["branch"])
            print("Branch ", branch)
    with vr.gather(
            action=reverse('confirmation'),
            num_digits=1,
            timeout=2000
    ) as gather:
        data = json.loads(days)
        print("schedule days: "+days)
        item = sorted(data, key=lambda d: d['id'])
        for i in item:
            gather.say(f'Press {i["id"]}  for {i["day"]}', voice=language)
    vr.redirect(reverse('confirmation'))
    return HttpResponse(str(vr), content_type='text/xml')


@csrf_exempt
def confirmation(request: HttpRequest) -> HttpResponse:
    vr = VoiceResponse()
    digits = request.POST.get('Digits')
    phoneNumber = request.POST.get('Caller')
    item = json.loads(days)
    for d in item:
        if d["id"] == int(digits):
            list.append(d["day"])
            # print("Day ", d['day'])
    for i in range(len(list)):
        if i < 1:
            city = list[i]
            branch = list[i + 1]
            day = list[i + 2]

    print(city, " ", branch, " ", day)
    response = confirmedPickup(city, branch, day, phoneNumber)
    vr.say(f'Your appointment is scheduled for next {day} at {branch} branch in {city}', voice=language)
    vr.redirect('menu')
    return HttpResponse(str(vr), content_type='text/xml')


@csrf_exempt
def get_weight(request: HttpRequest) -> HttpResponse:
    vr = VoiceResponse()
    with vr.gather(
            action=reverse('get_quotation'),
            num_digits=1,
            timeout=2000
    ) as gather:
        gather.say('Enter the weight of the package', voice=language)
    return HttpResponse(str(vr), content_type='text/xml')


@csrf_exempt
def get_quotation(request: HttpRequest) -> HttpResponse:
    vr = VoiceResponse()
    digits = request.POST.get('Digits')
    # total = int(digits)*10
    total = quotation_rates(int(digits))
    # total = total.decode(encoding="utf-8")
    total_money = str(total).split(".")
    dollars = int(total_money[0])
    cents = int(total_money[1])
    vr.say(f'Your entered weight is {digits} and you have to pay {dollars} dollars and {cents} cents', voice=language)
    vr.redirect('menu')
    return HttpResponse(str(vr), content_type='text/xml')


@csrf_exempt
def invoice_input(request: HttpRequest) -> HttpResponse:
    vr = VoiceResponse()
    with vr.gather(
            action=reverse('download_invoice'),
            finish_on_key='#',
            timeout=2000
    ) as gather:
        gather.say('Enter your tracking number and press #', voice=language)

    return HttpResponse(str(vr), content_type='text/xml')


@csrf_exempt
def download_invoice(request: HttpRequest) -> HttpResponse:
    vr = VoiceResponse()
    tracking_id = request.POST.get('Digits')

    res = get_shipment_details(tracking_id)
    print(res)
    vr.say('The invoice link has been sent to your registered mobile number.', voice=language)
    vr.redirect('menu')

    return HttpResponse(str(vr), content_type='text/xml')
