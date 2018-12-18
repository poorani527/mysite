from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .forms import ContactForm
from .models import *
import datetime as dt


def index(request):
    return render(request,'header.html')


def search_form(request):
    if request.method == 'POST':
        var1 = request.POST.get('id')
        var2 = request.POST.get('name')
        var3 = request.POST.get('phone')
        saving = db_user_details(id=var1,name=var2,phone=var3)
        saving.save()
        value = db_user_details.objects.get(id = var1)
        print value.name
        return render(request, 'dates/base.html')
    else:
        return render(request, 'dates/base.html')

def search_form1(request , id):
    value = db_user_details.objects.get(id = id)
    return render(request, 'dates/editVal.html', {'value' : value} )

def delete(request , id):
    d = db_user_details.objects.get(id = id)
    d.delete()
    values = db_user_details.objects.values()
    return render(request, 'dates/showVal.html' , {'values' : values} )


def show(request):
    values = db_user_details.objects.values()
    return render(request, 'dates/showVal.html' , { "values" : values } )

def home(request):
    if request.method == 'POST':
         form = ContactForm(request.POST)
         if form.is_valid():
             pass  # does nothing, just trigger the validation
    else:
         form = ContactForm()
    return render(request, 'dates/date_template.html', {'form': form})        


def datepicker(request):
    return render(request, 'dates/date_tem.html')

def save(request):
    if request.method == 'POST':
        var1 = date_for_scripting(\
        start_Date_Roll = request.POST.get('start_Date_Roll'), \
        end_Date_Roll = request.POST.get('end_Date_Roll'), \
        start_Date_Delta = request.POST.get('start_Date_Delta'), \
        end_Date_Delta = request.POST.get('end_Date_Delta'))

        var1.save()
        var = date_for_scripting.objects.values()
        print var
    return HttpResponse(var)
    
def retreive(request):
    for e in db_user_details.objects.all():
        print(e.name)
    d = db_user_details.objects.all()
    d.delete()
    values = db_user_details.objects.values()
    return render(request, 'dates/showVal.html' , {'values' : values} )

def rrr(request):
    date_data = AppConfig.objects.all()[0]
    CURRENT_MONTH_DATE_RANGE = [date_data.cr_start, date_data.cr_end]
    PREVIOUS_MONTH_DATE_RANGE = [date_data.crd_start, date_data.crd_end] 

    CURRENT_QUARTER = date_data.cr_quarter
    PREVIOUS_QUARTER = date_data.pre_quarter

    CURRENT_FINANCIAL_YEAR_DATE_RANGE = [date_data.ry_start, date_data.ry_end] 
    PAST_UTILIZATION_DATE_RANGE  = [date_data.ryd_start, date_data.ryd_end] 

    LAST_ROLLING_YEAR = [date_data.ry_start, date_data.ry_end]
    DELTA_ROLLING_YEAR = [date_data.ryd_start, date_data.ryd_end]

    print PREVIOUS_MONTH_DATE_RANGE
    return HttpResponse(DELTA_ROLLING_YEAR)

def app_config(request):
	if request.method == 'POST':
		AppConfig.objects.all().delete()

		ry_start = dt.datetime.strptime(request.POST.get('ry_start'), '%d-%m-%Y').strftime('%Y-%m-%d')
		ry_end = dt.datetime.strptime(request.POST.get('ry_end'), '%d-%m-%Y').strftime('%Y-%m-%d')
		ry_d_start = dt.datetime.strptime(request.POST.get('ry_d_start'), '%d-%m-%Y').strftime('%Y-%m-%d')
		ry_d_end = dt.datetime.strptime(request.POST.get('ry_d_end'), '%d-%m-%Y').strftime('%Y-%m-%d')
		cr_start = dt.datetime.strptime(request.POST.get('cr_start'), '%d-%m-%Y').strftime('%Y-%m-%d')
		cr_end = dt.datetime.strptime(request.POST.get('cr_end'), '%d-%m-%Y').strftime('%Y-%m-%d')
		cr_d_start = dt.datetime.strptime(request.POST.get('cr_d_start'), '%d-%m-%Y').strftime('%Y-%m-%d')
		cr_d_end = dt.datetime.strptime(request.POST.get('cr_d_end'), '%d-%m-%Y').strftime('%Y-%m-%d')
		cr_quarter = request.POST.get('cr_quarter')
		pre_quarter = request.POST.get('pre_quarter')

		var1 = AppConfig( \
			ry_start = ry_start, ry_end = ry_end, \
			ryd_start = ry_d_start, ryd_end = ry_d_end, \
			cr_start = cr_start, cr_end = cr_end, \
			crd_start = cr_d_start, crd_end = cr_d_end, \
			cr_quarter = cr_quarter, pre_quarter = pre_quarter)
		var1.save()

		return render(request, 'dates/setup_config.html', {'values' : AppConfig.objects.values()})
	else:
		return render(request, 'dates/setup_config.html', {'values' : AppConfig.objects.values()}) 
