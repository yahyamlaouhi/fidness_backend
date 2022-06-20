from django.shortcuts import render
from rest_framework import generics
from .models import FidPdv,FidGeolocalisation
from .serializer import  FidGeolocalisationSerializer,FidPdvSerializer,geolocationInformationSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
import geopy.distance
import googlemaps
import spacy
from spacy.matcher import Matcher
from strsimpy.jaro_winkler import JaroWinkler
from difflib import SequenceMatcher
from rest_framework.response import Response
from .forms import distanceForm
from django.db.models import Func, F








# Create your views here.
# this function to know if the place is coffee,supermarket....
def key_words_matching_places(keywords):

    nlp = spacy.load('en_core_web_sm')
    keywords1=[
            "tourist_attraction",
            "travel_agency",
            "restaurant",
            "food",
            "point_of_interest",
            "establishment",
          ]
    keywords2=["bar", "restaurant", "food", "point_of_interest", "establishment"]

    string=' '.join(keywords2)


    pattern = [[{"TEXT": "restaurant"}],
    [{"TEXT": "bar"}],
    [{"LEMMA": "agency"}],
    [{"TEXT":"travel"}],
    [{"TEXT": "food"}],
    [{"TEXT": "store"}],
    [{"TEXT": "supermarket"}]]



    doc=nlp(string)
    matcher = Matcher(nlp.vocab)
    matcher.add("restaurant pattern",pattern)

    matches= matcher(doc)
    for match_id,start,end in matches:
        matched_span=doc[start:end]
        if matched_span=="bar":
            return 'bar'
        elif matched_span=="clothes":
            return "clothes_store"
        elif matched_span=="supermarket":
            return matched_span
        elif matched_span=="store":
            return matched_span
        elif matched_span=="agency":
            return "agency"
        elif matched_span=="restaurant":
            return "restaurant"


        
    


# this function to see the similarity between the places in the databases and places visited by the user
def string_similarity(first_place,second_place):
    jarowinkler = JaroWinkler()
    result=jarowinkler.similarity(first_place, second_place)
    
    return result


# this function use the geopy package to calculate the difference between two distance using geodisic shape

def distance_between_person_place(coords_1,coords_2):
    distance=geopy.distance.geodesic(coords_1, coords_2).m
    return distance

    
def person_did_stay_or_not(coords_1,coords_2,time,departure_time,keywords,name_of_place):
    # average number of hours spent in cofee
    arrival_time=time
    time_spend=arrival_time-time
    type_of_place=key_words_matching_places(keywords)
    if type_of_place=='coffee':
        if distance_between_person_place(coords_1,coords_2)<20:
            if time_spend>=60:
                return name_of_place
    elif type_of_place=='supermarket':
        if time_spend>=15:
                return name_of_place
    
    elif type_of_place=='store':
        if time_spend>=5:
                return name_of_place

    elif type_of_place=='bar':
        if time_spend>=30:
                return name_of_place

    elif type_of_place=='retaurant':
        if time_spend>=20:
                return name_of_place
    
    elif type_of_place=='clothing_store':
        if time_spend>=10:
                return name_of_place

    elif type_of_place=='agency':
        if time_spend>=10:
                return name_of_place




def find_place_in_database(name):
    pdv_adress = list(FidPdv.objects.only("adresse"))
    for i in pdv_adress:
        if string_similarity(name,i)>0.7:
            num_visited=FidPdv.objects.only("adresse").filter(adress=i).first()
            c=FidPlaces.objects.update_or_create(
                fid_visited=num_visited+1
                )
        else:
            c=FidPlaces(latitude)
            








########################## geolocalisation section  ####################################

# Create your views here.


@api_view(['GET', 'POST'])

def distance(request):
    fidgeo=0


    if request.method == 'POST':


        serializer = geolocationInformationSerializer(data=request.data)


        serializer.is_valid(raise_exception=True)
        # lat_db = FidPdv.objects.annotate(abs_diff=Func(F('latitude') - serializer.data["latitude"], function='ABS')).order_by('abs_diff').first()
        l_lower = FidPdv.objects.filter(latitude__lte=serializer.data["latitude"]).order_by('-latitude').first()
        l_higher = FidPdv.objects.filter(latitude__gte=serializer.data["latitude"]).order_by('latitude').first()
        if (l_higher.latitude - serializer.data["latitude"]) < abs(l_lower.latitude - serializer.data["latitude"]):
            latitude = l_higher
        else:
            latitude = l_lower

        lon_lower = FidPdv.objects.filter(longitude__lte=serializer.data["longitude"]).order_by('-longitude').first()
        lon_higher = FidPdv.objects.filter(longitude__gte=serializer.data["longitude"]).order_by('longitude').first()
        if (lon_higher.longitude - serializer.data["longitude"]) < abs(l_lower.longitude - serializer.data["longitude"]):
            longitude = lon_higher
        else:
            longitude = lon_lower

        if abs((serializer.data["longitude"]+serializer.data["latitude"])-(latitude.latitude+latitude.longitude))<abs((serializer.data["longitude"]+serializer.data["latitude"])-(longitude.longitude+longitude.latitude)):
            closest_coordinate=(latitude.latitude,latitude.longitude)
            fid_pdv=latitude
        else:
            closest_coordinate=(longitude.latitude,longitude.longitude)
            fid_pdv=longitude

        distance=distance_between_person_place((serializer.data["latitude"],serializer.data["longitude"]),closest_coordinate)

        places=['magasin','bar','store']

        print(latitude.type)

       

        if string_similarity(latitude.type,places[0])>0.7 and distance<30:
            fidgeo=FidGeolocalisation(latitude=closest_coordinate[0],longitude=closest_coordinate[1],fid_pdv=fid_pdv.adress,visited=1)
            fidgeo.save()
            
        
        elif  string_similarity(latitude.type,places[1])>0.7 and distance<20:
            fidgeo=FidGeolocalisation(latitude=closest_coordinate[0],longitude=closest_coordinate[1],fid_pdv=fid_pdv.adress,visited=1)
            fidgeo.save()
        

        elif string_similarity(latitude.type,places[2])>0.7 and distance<10:
            fidgeo=FidGeolocalisation(latitude=closest_coordinate[0],longitude=closest_coordinate[1],fid_pdv=fid_pdv.adress,visited=1)
            fidgeo.save()
        

        serializer1 = FidGeolocalisationSerializer(fidgeo)

        print(fid_pdv.adress)

        
       
            


        
        # lon_db = FidPdv.objects.annotate(abs_diff=Func(F('longitude') - serializer.data["latitude"], function='ABS')).order_by('abs_diff').first()
        # coords_1=(serializer.data["destinationA_lat"],serializer.data["destinationA_lon"])
        # coords_2=(serializer.data["destinationB_lat"],serializer.data["destinationB_lon"])
        # distance=distance_between_person_place(coords_1,coords_2)

        return Response(serializer1.data)
    return Response(0)


# @api_view([ 'POST'])
# def register(request):
    

#     if request.method == 'POST':

#         serializer = (data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

        
        
#     return Response(serializer.data)




{"latitude" :61.385, 
    "longitude" :-152.268}





@api_view(['GET', 'PUT', 'DELETE'])
def geolocalisation_api(request):
    


    # if request.method == 'GET':
    #     serializer = ProductSerializer(product)
    #     return Response(serializer.data)
    # elif request.method == 'PUT':
    #     serializer = ProductSerializer(product, data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)
    # elif request.method == 'DELETE':
    #     if product.orderitems.count() > 0:
    #         return Response({'error': 'Product cannot be deleted because it is associated with an order item.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    #     product.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)





#    API_KEY="AIzaSyDmKT6uy-iS4gjywnHhS0NJik95Hpw9oHU"
#    map_client=googlemaps.Client(API_KEY)
#    dir()
#    print(API_KEY)
#    location=(52.2296756, 21.0122287)
#    search_string='coffe'
#    distance=17
#    buisness_list=[]

#    response=map_client.places_nearby(
#        location=location,
#        keyword=search_string,
#        name="shop",
#        radius = distance
#    )

   

  
   with open('C:\\Users\\USERTEST\\Desktop\\stage2\\Fidness backend\\fidness_backend\\geocalisation\\data.json',"r") as read_file:
       data1 = json.load(read_file)
    
   with open('C:\\Users\\USERTEST\\Desktop\\stage2\\Fidness backend\\fidness_backend\\geocalisation\\persondata.json',"r") as read_file:
       data2 = json.load(read_file)

   coords_1 = (52.2296756, 21.0122287)
   coords_2 = (52.406374, 16.9251681)
#    print(response.get('results'))
   c=geopy.distance.geodesic(coords_1, coords_2).m
   return Response(data2)



