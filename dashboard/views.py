from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import FidClientSerialiser,PartnerSerializer, PaysSerializer,SuperAdminSerializer,ClientSerializer
import pickle
import pandas as pd
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import FidCarteFidelite,FidAdmin,FidClient, FidGouvernorat
from rest_framework import viewsets







# Create your views here.

@api_view(['GET', 'POST'])
def churn_prediction(request):
    a=0

    if request.method == 'POST':

        serializer = FidCarteFideliteSerialiser(data=request.data)
        if serializer.is_valid(raise_exception=True):
                print(serializer.data)
                ohe=pickle.load(open(r'C:\projects\dash\Fidness backend\fidness_backend\models\OHE.pickle', 'rb'))

            
                df=pd.DataFrame(serializer.data,index=[0])
                df=pd.get_dummies(df, columns = ["pays", "sexe"], drop_first = True)


           

        return Response(df)

        
        
    return Response("hello")



def pipeline(data):
    ohe=pickle.load(open(r'C:\projects\dash\fidness_backend\models\OHE.pickle', 'rb'))
    scale=pickle.load(open(r'C:\projects\dashfidness_backend\models\scaling.pickle', 'rb'))
    best_model=pickle.load(open(r'C:\projects\dash\fidness_backend\models\best_model.pickle', 'rb'))

@api_view(['GET',"POST"])
def prediction(request,pk):
    fc = get_object_or_404(FidClient,pk=pk)
    if request.method == 'GET':
        serializer = FidClientSerialiser(fc)
        civilite=serializer.data["civilite"]
        id_gouvernorat=serializer.data["id_gouvernorat"]
        a_une_carte=serializer.data["a_une_carte"]
        nombre_annees=serializer.data["nombre_annees"]
        quitte=serializer.data["quitte"]
        pays='pays_'+serializer.data["pays"]
        age=serializer.data["age"]
        sexe=serializer.data["sexe"]
        NewAGT=age-nombre_annees
        NewAgeScore=nombre_annees/age
        nbre_total_tampon=serializer.data["nbre_total_tampon"]
        
        NewTamponScore=nbre_total_tampon
        def pays_score(pay_name):
            if pay_name==pays:
                return 1
            else:
                return 0
        def gender_score(sexe):
            if sexe=='homme':
                return 0
            else:
                return 1



        dic={'civilite':civilite, 'id_gouvernorat':id_gouvernorat, 'a_une_carte':a_une_carte, 'nombre_annees':nombre_annees,
       'NewAGT':NewAGT, 'NewAgeScore':NewAgeScore, 'NewTamponScore':NewTamponScore, 'pays_ariana':pays_score('pays_ariana'),
       'pays_ben arous':pays_score('pays_ben arous'), 'pays_bizerte':pays_score('pays_bizerte'), 'pays_béja':pays_score('pays_béja'), 'pays_gabès':pays_score('pays_gabès'),
       'pays_gafsa':pays_score('pays_gafsa'), 'pays_jendouba':pays_score('pays_jendouba'), 'pays_kairouan':pays_score('pays_kairouan'), 'pays_kasserine':pays_score('pays_kasserine'),
       'pays_kebili':pays_score('pays_kebili'), 'pays_le kef':pays_score('pays_le kef'), 'pays_mahdia':pays_score('pays_mahdia'), 'pays_manouba':pays_score('pays_manouba'),
       'pays_monastir':pays_score('pays_monastir'), 'pays_nabeul':pays_score('pays_nabeul'), 'pays_sfax':pays_score('pays_sfax'), 'pays_sidi bouzid':pays_score('pays_sidi bouzid'),
       'pays_siliana':pays_score('pays_sousse'), 'pays_sousse':pays_score('pays_sousse'), 'pays_tataouine':pays_score('pays_tataouine'), 'pays_tozeur':pays_score('pays_tozeur'),
       'pays_tunis':pays_score('pays_tunis'), 'sexe_homme':gender_score(sexe)}



        df=pd.DataFrame(dic,index=[0])


        cat_df = df[["pays_ariana", "pays_ben arous","pays_bizerte"
                 ,"pays_béja","pays_gabès","pays_gafsa","pays_monastir",
                 "pays_nabeul","pays_sfax","pays_sidi bouzid","pays_siliana","pays_sousse",
                 "pays_tataouine","pays_tozeur","pays_tunis","sexe_homme","a_une_carte"]]
        X = df.drop(["pays_ariana", "pays_ben arous","pays_bizerte"
                 ,"pays_béja","pays_gabès","pays_gafsa","pays_monastir",
                 "pays_nabeul","pays_sfax","pays_sidi bouzid","pays_siliana","pays_sousse",
                 "pays_tataouine","pays_tozeur","pays_tunis","sexe_homme","a_une_carte"], axis = 1)
        cols = X.columns
        index = X.index

        scaler=pickle.load(open(r'C:\projects\dash\fidness_backend\models\scaling.pickle', 'rb'))
        df_scaler=scaler.transform(X)

        X = pd.concat([X, cat_df], axis = 1)
        print(X)



       


       
        best_model=pickle.load(open(r'C:\projects\dash\fidness_backend\models\best_model.pickle', 'rb'))


        prediction=best_model.predict(X)
        ["he is staying in Fidness","he is not staying in fidness"]
        


        ['civilite', 'id_gouvernorat', 'a_une_carte', 'nombre_annees', 'quitte',
       'NewAGT', 'NewAgeScore', 'NewTamponScore', 'pays_ariana',
       'pays_ben arous', 'pays_bizerte', 'pays_béja', 'pays_gabès',
       'pays_gafsa', 'pays_jendouba', 'pays_kairouan', 'pays_kasserine',
       'pays_kebili', 'pays_le kef', 'pays_mahdia', 'pays_manouba',
       'pays_monastir', 'pays_nabeul', 'pays_sfax', 'pays_sidi bouzid',
       'pays_siliana', 'pays_sousse', 'pays_tataouine', 'pays_tozeur',
       'pays_tunis', 'sexe_homme']


        return Response(prediction)
    



class PartnerViewSet(viewsets.ModelViewSet):
    serializer_class = PartnerSerializer
    queryset = FidCarteFidelite.objects.all()



# Create your views here.
class SuperAdminViewSet(viewsets.ModelViewSet):
    serializer_class = SuperAdminSerializer
    queryset = FidAdmin.objects.all()


class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = FidClient.objects.all()

class PaysViewSet(viewsets.ModelViewSet):
    serializer_class = PaysSerializer
    queryset = FidGouvernorat.objects.all()



    

