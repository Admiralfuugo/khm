from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.contrib import messages
from django.utils import timezone

from .forms import ApplicationForm
from .models import Application, Vehicles, Inspection, Refuel, FuelType, Add_fuels
from authentication.models import CustomUser

from django.shortcuts import get_object_or_404



@login_required
def dashboard(request):
    context = {}

    return render(request, "dashboard.html", context=context)

@login_required
def showing(request):
    context = {}

    return render(request, "showing.html", context=context)


@login_required
def application(request):
    context = {}

    if request.method == "POST":
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author = request.user
            form.save()

            messages.success(request, "Ariza qabul qilindi")
            return redirect(reverse("applications"))
        else:
            print("Yemadi")

    form = ApplicationForm()
    context["form"] = form
    return render(request, "application.html", context=context)


@login_required
def applications(request):
    context = {}
    context["applications"] = Application.objects.all().order_by("-date_time")
    return render(request, "applications.html", context=context)


@login_required
def headquarters(request, pk):
    context = {}

    if request.method == "POST":
        tags = request.POST.getlist("cars")
        try:
            obj = Application.objects.get(pk=pk)
            obj.vehicles.set(tags)
            obj.status = "inspection"
            obj.save()
            messages.success(request, "Texnika muvafaqqiyatli biriktirildi")
            return redirect(reverse("applications"))
        except Exception as e:
            return HttpResponseNotFound("Bunday obyekt topilmadi")

    # request.method == "GET":
    try:
        obj = Application.objects.get(pk=pk)
        context["application"] = obj

        if obj.status in ["new", "accepted", "inspection"]:
            context["read_only"] = False
            vehicles = Vehicles.objects.all()
            context["vehicles"] = vehicles
        else:
            context["read_only"] = True

        return render(request, "headquarters.html", context=context)
    except Application.DoesNotExist:
        return HttpResponseNotFound("Bunday obyekt topilmadi")


@login_required
def inspection(request):
    context = {}
    context["applications"] = Application.objects.filter(status="inspection").order_by(
        "-date_time"
    )
    return render(request, "inspection.html", context=context)


@login_required
def sub_inspection(request, pk):
    context = {}
    main = get_object_or_404(applications, pk=pk)

    if request.method == "POST":
        try:
            obj = Application.objects.get(pk=pk)
            vehicles = obj.vehicles.all()
            print(vehicles)
            for ve in vehicles:
                status = request.POST.get(str(ve.id), "")
                ins, created = Inspection.objects.get_or_create(
                    application=obj, vehicles=ve
                )
                print("created:", created)
                ins.status = status
                ins.save()

            obj.status = "petrol_station"
            obj.save()
            messages.success(request, "Texnik ko'rik muvafaqqiyatli saqlandi")
            return redirect(reverse("inspection"))
        except Exception as e:
            return HttpResponseNotFound("Bunday obyekt topilmadi")

    # request.method == "GET":
    try:
        obj = Application.objects.get(pk=pk)
        context["application"] = obj

        if obj.status not in ["new", "accepted", "inspection"]:
            context["read_only"] = True
        else:
            context["read_only"] = False

        return render(request, "sub_inspection.html", context=context)
    except Application.DoesNotExist:
        return HttpResponseNotFound("Bunday obyekt topilmadi")


@login_required
def petrol(request):
    context = {}
    context["applications"] = Application.objects.filter(
        status="petrol_station"
    ).order_by("-date_time")
    return render(request, "petrol.html", context=context)


@login_required
def sub_petrol(request, pk):
    context = {}

    if request.method == "POST":
        try:
            obj = Application.objects.get(pk=pk)
            vehicles = obj.vehicles.all()
            for ve in vehicles:
                type = request.POST.get("select" + str(ve.pk))
                valume = request.POST.get(str(ve.pk), "")

                ins, created = Refuel.objects.get_or_create(
                    application=obj, vehicles=ve, type=FuelType.objects.get(pk=type)
                )
                # print("created:", created)

                ins.valume = valume
                ins.save()

            obj.status = "ready"
            obj.save()
            messages.success(request, "Muvafaqqiyatli saqlandi")
            return redirect(reverse("petrol"))
        except Exception as e:
            return HttpResponseNotFound("Bunday obyekt topilmadi")

    # request.method == "GET":
    try:
        obj = Application.objects.get(pk=pk)
        context["application"] = obj

        if obj.status not in ["new", "accepted", "inspection", "petrol_station"]:
            context["read_only"] = True
        else:
            context["read_only"] = False

        return render(request, "sub_petrol.html", context=context)
    except Application.DoesNotExist:
        return HttpResponseNotFound("Bunday obyekt topilmadi")


@login_required
def driver(request):
    context = {}
    context["applications"] = Application.objects.filter(
        vehicles__driver=request.user
    ).order_by("-date_time")
    return render(request, "driver.html", context=context)


@login_required
def parking(request):
    context = {}

    if request.method == "POST":
        try:
            id = request.POST.get("id", "")
            status = request.POST.get("status", "")

            obj = Application.objects.get(pk=id)
            obj.status = status
            obj.save()
            messages.success(request, "Muvafaqqiyatli saqlandi")
            return redirect(reverse("parking"))
        except Exception as e:
            return HttpResponseNotFound("Bunday obyekt topilmadi")

    today = timezone.now().date()
    context["applications"] = Application.objects.filter(
        status="ready", date_time__contains=today
    ).order_by("date_time")
    print(context["applications"])
    context["in_progress"] = Application.objects.filter(
        status="in_progress",
    ).order_by("date_time")

    return render(request, "parking.html", context=context)





#for_print


@login_required
def N_avto(request):
    context = {}

    return render(request, "for_print/N_avto.html", context=context)

@login_required
def N_zayafka(request):
    context = {}

    return render(request, "for_print/N_zayafka.html", context=context)

@login_required
def N3(request):
    context = {}    
    add_fuels = Add_fuels.objects.all()
    total_result = 0
    
      # Umumiy yig'indining boshlanishi

    for fuel in add_fuels:
        
        total_result += fuel.rim1 + fuel.rim2 + fuel.rim3 + fuel.rim4   

    # Context yaratish
    context['add_fuel'] = add_fuels
    context['total_result'] = total_result 
    total_result=0
    return render(request, "for_print/N3.html", context=context)

@login_required
def N4(request):
    context = {}

    return render(request, "for_print/N4.html", context=context)

@login_required
def N5(request):
    context = {}

    return render(request, "for_print/N5.html", context=context)

@login_required
def N6(request):
    context = {}

    return render(request, "for_print/N6.html", context=context)

@login_required
def N7(request):
    context = {}

    return render(request, "for_print/N7.html", context=context)

@login_required
def N8(request):
    context = {}

    return render(request, "for_print/N8.html", context=context)

@login_required
def N9zayafka(request):
    context = {}

    return render(request, "for_print/N9zayafka.html", context=context)

@login_required
def Nback(request):
    context = {}

    return render(request, "for_print/Nback.html", context=context)

@login_required
def Ndallot(request):
    context = {}

    return render(request, "for_print/Ndallot.html", context=context)

@login_required
def Nmoy(request):
    context = {}

    return render(request, "for_print/Nmoy.html", context=context)

@login_required
def Nsorovnoma(request):
    context = {}

    return render(request, "for_print/Nsorovnoma.html", context=context)

@login_required
def Nxisobot(request):
    context = {}

    return render(request, "for_print/Nxisobot.html", context=context)



#for_page
# @login_required
# def add_fuel(request):
#     context = {}
#     result = 0
#     add_fuel = Add_fuels.objects.all() 
#     context = {
#         "add_fuel" :add_fuel      } 


#     #yig'indi
    
#     for fuel in add_fuel:
#         result += fuel.rim1 + fuel.rim2 + fuel.rim3 + fuel.rim4

#     context['result'] = result

#     result = 0
    


#     print("salomat", context)
#     return render(request, "for_print/Nsorovnoma.html", context=context)



@login_required
def add_fuel(request):
    context = {}    
    add_fuels = Add_fuels.objects.all()
  

    obj_with_sum = []
    umrim = 0
    umtrak = 0
    

    for obj in add_fuels:
        total_sum = obj.rim1 + obj.rim2 + obj.rim3 + obj.rim4
        traks_sum = obj.tank + obj.art + obj.bmp + obj.avto + obj.uchuv + obj.trak + obj.maxs + obj.ishab

        umrim += total_sum
        umtrak += traks_sum
       


        obj_with_sum.append([obj, total_sum])
        
    tank_total_sum  = sum(obj.tank for obj in add_fuels)
    art_total_sum  = sum(obj.art for obj in add_fuels)
    bmp_total_sum  = sum(obj.bmp for obj in add_fuels)
    avto_total_sum  = sum(obj.avto for obj in add_fuels)
    uchuv_total_sum  = sum(obj.uchuv for obj in add_fuels)
    trak_total_sum  = sum(obj.trak for obj in add_fuels)
    maxs_total_sum  = sum(obj.maxs for obj in add_fuels)
    ishab_total_sum  = sum(obj.ishab for obj in add_fuels)
    rim1_total_sum  = sum(obj.rim1 for obj in add_fuels)
    rim2_total_sum  = sum(obj.rim2 for obj in add_fuels)
    rim3_total_sum  = sum(obj.rim3 for obj in add_fuels)
    rim4_total_sum  = sum(obj.rim4 for obj in add_fuels)
    


    
    context['obj_with_sum'] = obj_with_sum
    context['tank_total_sum'] = tank_total_sum
    context['art_total_sum'] = art_total_sum
    context['bmp_total_sum'] = bmp_total_sum
    context['avto_total_sum'] = avto_total_sum
    context['uchuv_total_sum'] = uchuv_total_sum
    context['trak_total_sum'] = trak_total_sum
    context['maxs_total_sum'] = maxs_total_sum
    context['ishab_total_sum'] = ishab_total_sum
    context['rim1_total_sum'] = rim1_total_sum
    context['rim2_total_sum'] = rim2_total_sum
    context['rim3_total_sum'] = rim3_total_sum
    context['rim4_total_sum'] = rim4_total_sum

    context['umrim'] = umrim
    context['umtrak'] = umtrak

    
    print(context)

    return render(request, "for_print/Nsorovnoma.html", context=context)



















#extra page

def custom_404(request, exception):
    return render(request, "404.html", status=404)


def server_error_view(request):
    return render(request, '500.html', status=500)




