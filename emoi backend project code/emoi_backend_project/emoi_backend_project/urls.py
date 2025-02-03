"""
URL configuration for emoi_backend_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from emoi_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('superadminRegisterapi/',views.superadminRegisterapi),
    path('superadminlogin/',views.superadminlogin),
    path('billingagentRegisterapi/',views.billingagentRegisterapi),
    path('billingAgentlogin/',views.billingAgentlogin),
    path('functionInformationStore/',views.functionInformationStore),
    path('functionDetailsGetAll/',views.functionDetailsGetAll),
    path('MoiDetailsApi/',views.MoiDetailsApi),
    path('MoiDetailsGetApi/',views.MoiDetailsGetApi),
    path('sumAmountCaluculations/',views.sumAmountCaluculations),
    path('outputExcel/',views.outputExcel),
    path('getallBillingAgent/',views.getallBillingAgent),



]
