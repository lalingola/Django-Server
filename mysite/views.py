from django.shortcuts import render, redirect
import pickle5 as pickle
from sklearn.fearute_extraction.text import CoutVectorizer
from sklearn.neighbors import KNeigborsClassifier

def inicio(request):
    loader_model = pickle.load(open("finalized_model.sav" , 'rb'))
    return render(request,"index.html",loader_model)

def modelo(request):
    loader_model = pickle.load(open("finalized_model.zav" , 'rb'))
    y_pred=loader_model.predict(x_test_bow)
