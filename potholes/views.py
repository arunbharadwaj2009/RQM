from django.shortcuts import render
from .forms import JsonFileForm
from .models import Pothole
from django.contrib.gis.geos import fromstr
import json

# Create your views here.

JSON_FILE_EXTENSION = ["json"]


def parseJson(request):
    form = JsonFileForm()
    if(request.method == "POST"):
        form = JsonFileForm(request.POST, request.FILES)
        if(form.is_valid()):
            jsonFile = form.save(commit=False)
            jsonFile.jsonfile = request.FILES['jsonfile']
            file_type = jsonFile.jsonfile.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in JSON_FILE_EXTENSION:
                return render(request, 'jsonfile/error.html')
            jsonFile.save()
            with open(jsonFile.jsonfile.url) as r:
                datastore = json.load(r)
                for index in datastore["elements"]:
                    name = index["tags"]["name"]
                    imageNames = index["tags"]["imageName"]
                    address = "india"
                    city = "test"
                    longitude = index["lon"]
                    latitude = index["lat"]
                    location = fromstr(
                        f'POINT({longitude} {latitude})', srid=4326)
                    pothole = Pothole(
                        name=name, imageNames=imageNames, location=location, address=address, city=city)
                    pothole.save()
                    print(index)
            return render(request, 'jsonfile/success.html')
    context = {"form": form}
    return render(request, 'jsonfile/create.html', context)
