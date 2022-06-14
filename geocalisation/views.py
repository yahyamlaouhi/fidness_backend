from django.shortcuts import render
from rest_framework import generics
from .models import FidPdv,FidKeyWordsMarque,FidPlaces
from .serializer import FidPdvSerializer, distanceSerializer
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
    first_place=jarowinkler.similarity(first_place, second_place)
    second_place= SequenceMatcher(None, first_place, second_place).ratio()
    result=(first_place+second_place)/2
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
    print("llllllllllllllllllllllllllllllllllllllllll",pdv_adress)
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
    distance=0

    if request.method == 'POST':

        serializer = distanceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.data)
        coords_1=(serializer.data["destinationA_lat"],serializer.data["destinationA_lon"])
        coords_2=(serializer.data["destinationB_lat"],serializer.data["destinationB_lon"])
        distance=distance_between_person_place(coords_1,coords_2)

        return Response(distance)
    return Response(distance)




{    "destinationA_lat" :52.2296756, 
    "destinationA_lon" :21.0122287,
   "destinationB_lat" :52.406374, 
    "destinationB_lon" :16.9251681
}




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



