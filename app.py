from flask import Flask, request, render_template
import pandas as pd
import numpy as np
import pickle

import random


app = Flask(__name__,template_folder='templates')
@app.route('/', methods=['GET', 'POST'])
def main():
    
    # If a form is submitted
    if request.method == "POST":
        
        # Unpickle classifier
        model = pickle.load(open("model.pkl", "rb"))
        # le = pickle.load(open("le.pkl", "rb"))
        
        # Get values through input bars
        print("RFORM", request.form)
        age = int(request.form.get("age"))
        gender = request.form.get("gender")
        Cold = request.form.get("Cold")
        Depression = request.form.get("Depression")
        pregnant = request.form.get("pregnant")
        thyroid_surgery = request.form.get("thyroid_surgery")
        puffy_face = request.form.get("puffy_face")
        Dry_skin = request.form.get("Dry_skin")
        Hypopituitary_Disease = request.form.get("Hypopituitary_Disease")
        psych = request.form.get("psych")
        Sudden_weight_gain = request.form.get("Sudden_weight_gain")
        Muscle_weakness_tenderness_stiffness = request.form.get("Muscle_weakness_tenderness_stiffness")
        Enlarged_thyroid_gland = request.form.get("Enlarged_thyroid_gland")
        Sweating = request.form.get("Sweating")
        Nervousness_Anxiety_Irritability = request.form.get("Nervousness_Anxiety_Irritability")
        sudden_weight_loss = request.form.get("sudden_weight_loss")
        Fatigue = request.form.get("Fatigue")
        sleep_issues = request.form.get("sleep_issues")
        swelling = request.form.get("swelling")
        bulging_of_eyes = request.form.get("bulging_of_eyes")
        anemia = request.form.get("anemia")
        confusion = request.form.get("confusion")
        Rapid_heart_beat = request.form.get("Rapid_heart_beat")
        
        

        
        df1 = pd.DataFrame(data=[[gender,Cold,Depression,pregnant,thyroid_surgery,puffy_face,Dry_skin,Hypopituitary_Disease,psych,Sudden_weight_gain,
                          Muscle_weakness_tenderness_stiffness,Enlarged_thyroid_gland,Sweating,
                          Nervousness_Anxiety_Irritability,sudden_weight_loss,Fatigue,sleep_issues,swelling,bulging_of_eyes,anemia,confusion,Rapid_heart_beat,age]],columns=['Sex', 'Cold', 'Depression', 'pregnant', 'thyroid surgery',
                                                                      'puffy face', 'Dry skin', 'Hypopituitary Disease', 'psych', 'Sudden weight gain', 'Muscle weakness/tenderness/stiffness', 
                                                                      'Enlarged thyroid gland', 'Sweating', 'Nervousness/Anxiety/Irritability', 'sudden weight loss', 
                                                                      'Fatigue', 'sleep issues', 'swelling', 'bulging of eyes', 'anemia', 'confusion', 'Rapid heart beat', 'Age'])


        df1 = df1.replace({'no': 0, 'yes': 1, "n": 0, "y": 1, 'false': 0, 'true': 1, "f": 0, "t": 1})
        df1 = df1.replace({'female': 0, 'male': 1, 'f': 0, 'm': 1})
        

        hypo = [Sudden_weight_gain,Cold,puffy_face,Fatigue,Muscle_weakness_tenderness_stiffness,Dry_skin,Depression,anemia,psych]
        hyper = [Sweating,sudden_weight_loss,Nervousness_Anxiety_Irritability,Rapid_heart_beat,sleep_issues,puffy_face,bulging_of_eyes,confusion]

        type1count = 0
        for i in hypo:
            if (i == 'yes') or (i == 'y'):
                type1count = type1count +1
        type2count = 0
        for i in hyper:
            if (i == 'yes') or (i == 'y'):
                type2count = type2count +1

        # print(df1)
        prediction = model.predict(df1)[0]
        if prediction == 1:
            pred = "Positive"
            if type2count >= 3:
                t_type = "Hyperthyroidism"
            else:
                t_type = "Hypothyroidism"
        elif prediction == 0:
            pred = "Negative"
            t_type = "None"
        print("prediction:",pred)
        print("Type:",t_type)
        
        
        
        
        return render_template("website.html", prediction = pred , type = t_type)


    elif request.method == "GET":
        return render_template("website.html")

if __name__ == '__main__':
    app.run(debug = True)