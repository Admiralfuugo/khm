from django.urls import path, include


from .views import (
    dashboard,
    application,
    applications,
    headquarters,
    inspection,
    sub_inspection,
    petrol,
    sub_petrol,
    driver,
    parking,
    showing,
    add_fuel,
  
    #for_print
    N_avto,
    N_zayafka,
    N3,
    N4,
    N5,
    N6,
    N7,
    N8,
    N9zayafka,
    Nback,
    Ndallot,
    Nmoy,
    Nsorovnoma,
    Nxisobot,
    

)

urlpatterns = [
    path("dashboard/", dashboard, name="dashboard"),
    path("application/", application, name="application"),
    path("applications/", applications, name="applications"),
    path("headquarters/<int:pk>/", headquarters, name="headquarters"),
    path("inspection/", inspection, name="inspection"),
    path("inspection/<int:pk>", sub_inspection, name="sub-inspection"),
    path("petrol", petrol, name="petrol"),
    path("petrol/<int:pk>", sub_petrol, name="sub-petrol"),
    path("parking", parking, name="parking"),
    path("driver", driver, name="driver"),
    path("showing", showing, name="showing"),
    path("add_fuel", add_fuel, name="add_fuel"),
    

    # path("account/", include("django.contrib.auth.urls")),
    #for_print
    path("N_avto", N_avto, name="N_avto"),
    path("N_zayafka", N_zayafka, name="N_zayafka"),
    path("N3", N3, name="N3"),
    path("N4", N4, name="N4"),
    path("N5", N5, name="N5"),
    path("N6", N6, name="N6"),
    path("N7", N7, name="N7"),
    path("N8", N8, name="N8"),
    path("N9zayafka", N9zayafka, name="N9zayafka"),
    path("Nback", Nback, name="Nback"),
    path("Ndallot", Ndallot, name="Ndallot"),
    path("Nmoy", Nmoy, name="Nmoy"),
    path("Nsorovnoma", Nsorovnoma, name="Nsorovnoma"),
    path("Nxisobot", Nxisobot, name="Nxisobot"),


]
