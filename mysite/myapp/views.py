from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import numpy as np
from os.path import join
from django.conf import settings
# Create your views here.

def index(request):
    return HttpResponse("Hello!")


def query(request):
    county = join(settings.STATIC_ROOT, 'myapp/merged.csv' )
    df = pd.read_csv(county,index_col=0)
    state = request.GET.get('state')
    year = request.GET.get('year')
    poverty_percent = 0
    crime_rate = 0
    if state and year:
        x =  df.loc[df["State"] == state]
        y = x.loc[x['Year']==int(year)]
        poverty_percent = float(y['Poverty Percent'])
        crime_rate = float(y['Crime Rate'])
    path = join(settings.STATIC_ROOT, 'myapp/regression.png' )
    params={'poverty_percent':poverty_percent,'crime_rate':crime_rate}
    return render(request,"form.html",params)
