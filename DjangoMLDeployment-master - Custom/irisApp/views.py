from django.shortcuts import render

from joblib import load
model = load('./savedModels/Random_forest80.joblib')

def predictor(request):
    if request.method == 'POST':
        age = float(request.POST['age'])
        trestbps = float(request.POST['trestbps'])
        chol = float(request.POST['chol'])
        thalach= float(request.POST['thalach'])
        oldpeak= float(request.POST['oldpeak'])
        sex_0= request.POST['sex_0']
        sex_1= request.POST['sex_1']
        cp_0= request.POST['cp_0']
        cp_1= request.POST['cp_1']
        cp_2= request.POST['cp_2']
        cp_3= request.POST['cp_3']
        fbs_0= int(request.POST['fbs_0'])
        fbs_1= request.POST['fbs_1']
        restecg_0= request.POST['restecg_0']
        restecg_1= request.POST['restecg_1']
        restecg_2= request.POST['restecg_2']
        exang_0= request.POST['exang_0']
        exang_1= request.POST['exang_1']
        slope_0= request.POST['slope_0']
        slope_1= request.POST['slope_1']
        slope_2= request.POST['slope_2']
        ca_0= request.POST['ca_0']
        ca_1= request.POST['ca_1']
        ca_2= request.POST['ca_2']
        ca_3= request.POST['ca_3']
        ca_4= request.POST['ca_4']
        thal_0= request.POST['thal_0']
        thal_1= request.POST['thal_1']
        thal_2= request.POST['thal_2']
        thal_3= request.POST['thal_3']
        pred = model.predict([[age,trestbps,chol,thalach,oldpeak,sex_0,sex_1,cp_0,cp_1,cp_2,cp_3,fbs_0,fbs_1,restecg_0,restecg_1,restecg_2,exang_0,exang_1,slope_0,slope_1,slope_2,ca_0,ca_1,ca_2,ca_3,ca_4,thal_0,thal_1,thal_2,thal_3]])
        if pred[0] == 0:
            pred = 'Healthy'
        elif pred[0] == 1:
            pred = 'Diseased'
        return render(request, 'main.html', {'result' : pred})
    return render(request, 'main.html')
