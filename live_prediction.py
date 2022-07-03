import pandas as pd
import numpy as np
import pickle

model = pickle.load(open("model.pkl", "rb"))


gender = input("Enter Gender of the Participant - M/F").lower()
Cold = input("Does the participant have Cold? - false/ true").lower()
Depression = input("Does the participant have Depression? - false/ true").lower()
pregnant = input("is the participant pregnant? - false/ true").lower()
thyroid_surgery = input("has the participant undergone thyroid surgery? - false/ true").lower()
puffy_face = input("Does the participant have a puffy face? - false/ true").lower()
Dry_skin = input("Does the participant have Dry skin? - false/ true").lower()
Hypopituitary_Disease = input("Does the participant have Hypopituitary Disease? - false/ true").lower()
psych = input("Does the participant have any records of psychological issues? - false/ true").lower()
Sudden_weight_gain = input("has the participant undergone Sudden weight gain? - false/ true").lower()
Muscle_weakness_tenderness_stiffness = input("Does the participant have any Muscle weakness/tenderness/stiffness? - false/ true").lower()
Enlarged_thyroid_gland = input("Does the participant have an Enlarged thyroid gland? - false/ true").lower()
Sweating = input("Does the participant experience excessive Sweating? - false/ true").lower()
Nervousness_Anxiety_Irritability = input("Does the participant have Nervousness/Anxiety/Irritability? -  false/ true").lower()
sudden_weight_loss = input("Has the participant experienced sudden weight loss? - Yes/ No").lower()
Fatigue = input("Does the participant experience Fatigue? - Yes/ No").lower()
sleep_issues = input("Does the participant experience sleep issues? - Yes/ No").lower()
swelling = input("Does the participant have swelling? - Yes/ No").lower()
bulging_of_eyes = input("Does the participant have bulging of eyes? - Yes/ No").lower()
anemia = input("Does the participant have anemia? - Yes/ No").lower()
confusion = input("Does the participant experience confusion? - Yes/ No").lower()
Rapid_heart_beat = input("Does the participant have Rapid heart beat? - Yes/ No").lower()
age = int(input("Enter Age of Participant as a number"))



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
