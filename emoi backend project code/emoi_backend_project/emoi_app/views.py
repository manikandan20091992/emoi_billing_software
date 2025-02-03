from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime
import pytz
from emoi_app.models import *
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.db.models import Sum
import pandas as pd
# Create your views here.
from django.template.loader import render_to_string
from weasyprint import HTML
def indiantime():
    ist = pytz.timezone('Asia/Kolkata')
    utc_now = datetime.utcnow().replace(tzinfo=pytz.utc)
    ist_now = utc_now.astimezone(ist)
    return ist_now
#Get all getallBillingAgent
@api_view(['GET'])
def getallBillingAgent(request):
    billingAgentRegisterdata = billingAgentRegister.objects.all().values()
    return Response({"code":201,"message":billingAgentRegisterdata})
#Final output excel
@api_view(['POST'])
def outputExcel(request):
    FunctionInformationPrimaryKey=request.data['FunctionInformationPrimaryKey']
    filtered_queryset = MoiDetails.objects.filter(FunctionInformationPrimaryKey=FunctionInformationPrimaryKey).values()
    df = pd.DataFrame(list(filtered_queryset))
    df['Moidetails_Datetime'] = pd.to_datetime(df['Moidetails_Datetime']).dt.strftime('%d-%m-%Y %H:%M')
    df_dict = df.to_dict(orient='records')
    total_amount = filtered_queryset.aggregate(total=Sum('Moi_user_amount'))['total']
    return render(request, 'outputexcel.html', {'data': df_dict,'total':total_amount})
#To get total paid amount 
@api_view(['POST'])
def sumAmountCaluculations(request):
    FunctionInformationPrimaryKey=request.data['FunctionInformationPrimaryKey']
    filtered_queryset = MoiDetails.objects.filter(FunctionInformationPrimaryKey=FunctionInformationPrimaryKey).values('Moi_user_amount')
    functiondetails = FunctioninformationRegistertable.objects.filter(id=FunctionInformationPrimaryKey).values('ManaMaganName','ManaMagalName','FucntionDate','FucntionLocationAddress')
    total_amount = filtered_queryset.aggregate(total=Sum('Moi_user_amount'))['total']
    return Response({"code":"201","total_Moi_amount":total_amount,'functiondetails':functiondetails})
#To get moi details
@api_view(['GET'])
def MoiDetailsGetApi(request):
    FunctionInformationPrimaryKey= request.GET.get('FunctionInformationPrimaryKey')
    MoiDetailsdata = MoiDetails.objects.filter(FunctionInformationPrimaryKey=FunctionInformationPrimaryKey).values()
    return Response({"code":200,"message":MoiDetailsdata})
#Moi amount details store
@api_view(['POST'])
def MoiDetailsApi(request):
    Moi_user_Name = request.data['Moi_user_Name']
    Moi_user_address= request.data['Moi_user_address']
    Moi_user_occupation= request.data['Moi_user_occupation']
    Moi_user_amount= request.data['Moi_user_amount']
    FunctionInformationPrimaryKey = request.data['FunctionInformationPrimaryKey']
    indiantimestring = indiantime()
    moi_details = MoiDetails.objects.create(Moi_user_Name=Moi_user_Name,Moi_user_address=Moi_user_address,Moi_user_occupation=Moi_user_occupation,Moi_user_amount=Moi_user_amount,FunctionInformationPrimaryKey=FunctionInformationPrimaryKey,Moidetails_Datetime=indiantimestring)
    #To get a function information
    functiondetails = FunctioninformationRegistertable.objects.filter(id=FunctionInformationPrimaryKey).values('ManaMaganName','ManaMagalName','FucntionDate','FucntionLocationAddress','billingAgentPrimarykey')
    result = list(functiondetails.values())
    finaldict = result[0]
    finaldict['Moi_user_Name']=Moi_user_Name
    finaldict['Moi_user_address']=Moi_user_address
    finaldict['Moi_user_occupation']=Moi_user_occupation
    finaldict['Moi_user_amount']=Moi_user_amount
    billingAgentName = billingAgentRegister.objects.get(id=finaldict['billingAgentPrimarykey']).name
    finaldict['billingAgentName']=billingAgentName
    data=finaldict
    # response_data = {
    #     "code": 200,
    #     "message": "Details stored",
    #     "data": finaldict
    # }
    # response = HttpResponse(content_type='application/pdf')
    # response['Content-Disposition'] = 'attachment; filename="bill.pdf"'

    # p = canvas.Canvas(response, pagesize=letter)
    # p.drawString(100, 750, f"ID: {data['id']}")
    # p.drawString(100, 730, f"Mana Magan Name: {data['ManaMaganName']}")
    # p.drawString(100, 710, f"Mana Magal Name: {data['ManaMagalName']}")
    # p.drawString(100, 690, f"Function Date: {data['FucntionDate']}")
    # p.drawString(100, 670, f"Function Location: {data['FucntionLocationAddress']}")
    # p.drawString(100, 650, f"Billing Agent PK: {data['billingAgentPrimarykey']}")
    # p.drawString(100, 630, f"Moi User Name: {data['Moi_user_Name']}")
    # p.drawString(100, 610, f"Moi User Address: {data['Moi_user_address']}")
    # p.drawString(100, 590, f"Moi User Occupation: {data['Moi_user_occupation']}")
    # p.drawString(100, 570, f"Moi User Amount: {data['Moi_user_amount']}")
    # p.drawString(100, 550, f"Billing Agent Name: {data['billingAgentName']}")

    # p.showPage()
    # p.save()
    return render(request, 'bill_template.html', {'data': data})
    # return Response(response_data)
#All function get
@api_view(['GET'])
def functionDetailsGetAll(request):
    data = FunctioninformationRegistertable.objects.all().values()
    return Response({"code":200,"message":data})
#Function details store
@api_view(['POST'])
def functionInformationStore(request):
    ManaMaganName = request.data['ManaMaganName']
    ManaMagalName = request.data['ManaMagalName']
    FucntionDate = request.data['FucntionDate']
    FucntionLocationAddress = request.data['FucntionLocationAddress']
    billingAgentPrimarykey = request.data['billingAgentPrimarykey']
    FunctioninformationRegistertable.objects.create(ManaMaganName=ManaMaganName,ManaMagalName=ManaMagalName,FucntionDate=FucntionDate,FucntionLocationAddress=FucntionLocationAddress,billingAgentPrimarykey=billingAgentPrimarykey)

    return Response({"code":201,"message":"created"})
#Billing agent register
@api_view(['POST'])
def billingagentRegisterapi(request):
    username = request.data['username']
    password = request.data['password']
    name = request.data['name']
    email = request.data['email']
    rollid = 2
    indiantimestring = indiantime()
    billingAgentRegister.objects.create(username=username,password=password,name=name,email=email,rollid=rollid,datetime=str(indiantimestring))

    return Response({"code":201,"message":"created"})
#Billing agent login
@api_view(['POST'])
def billingAgentlogin(request):
    username = request.data['username']
    password = request.data['password']
    if billingAgentRegister.objects.filter(username=username,password=password).exists() == True:
        return Response({"code":201,"message":"Login successfully"})
    else:
        return Response({"code":404,"message":"Login Failed"})
#Super admin login  
@api_view(['POST'])
def superadminlogin(request):
    username = request.data['username']
    password = request.data['password']
    if superadminRegister.objects.filter(username=username,password=password).exists() == True:
        return Response({"code":201,"message":"Login successfully"})
    else:
        return Response({"code":"404","message":"Login Failed"})
#To store the super admin details
@api_view(['POST'])
def superadminRegisterapi(request):
    username = request.data['username']
    password = request.data['password']
    name = request.data['name']
    email = request.data['email']
    rollid = 1
    indiantimestring = indiantime()
    superadminRegister.objects.create(username=username,password=password,name=name,email=email,rollid=rollid,datetime=str(indiantimestring))

    return Response({"code":201,"message":"created"})