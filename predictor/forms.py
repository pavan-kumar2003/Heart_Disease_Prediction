# heart_disease/forms.py
from django import forms

class HeartDiseaseForm(forms.Form):
    age = forms.IntegerField(label='Age', min_value=0)
    sex = forms.ChoiceField(label='Sex', choices=[(0, 'Female'), (1, 'Male')])
    cp = forms.ChoiceField(label='Chest Pain Type', choices=[(0, 'Typical Angina'), (1, 'Atypical Angina'), (2, 'Non-Anginal Pain'), (3, 'Asymptomatic')])
    trestbps = forms.IntegerField(label='Resting Blood Pressure', min_value=0)
    chol = forms.IntegerField(label='Cholesterol', min_value=0)
    fbs = forms.ChoiceField(label='Fasting Blood Sugar > 120 mg/dl', choices=[(0, 'False'), (1, 'True')])
    restecg = forms.ChoiceField(label='Resting Electrocardiographic Results', choices=[(0, 'Normal'), (1, 'Having ST-T wave abnormality'), (2, 'Showing probable or definite left ventricular hypertrophy')])
    thalach = forms.IntegerField(label='Maximum Heart Rate Achieved', min_value=0)
    exang = forms.ChoiceField(label='Exercise Induced Angina', choices=[(0, 'No'), (1, 'Yes')])
    oldpeak = forms.FloatField(label='Oldpeak', min_value=0.0)
    slope = forms.ChoiceField(label='Slope of the Peak Exercise ST Segment', choices=[(0, 'Upsloping'), (1, 'Flat'), (2, 'Downsloping')])
    ca = forms.ChoiceField(label='Number of Major Vessels (0-3) Colored by Fluoroscopy', choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3')])
    thal = forms.ChoiceField(label='Thalassemia', choices=[(0, 'Normal'), (1, 'Fixed Defect'), (2, 'Reversible Defect')])


from django import forms

class HealthIndicatorForm(forms.Form):
    HighBP = forms.ChoiceField(label='High Blood Pressure', choices=[(0, 'No'), (1, 'Yes')])
    HighChol = forms.ChoiceField(label='High Cholesterol', choices=[(0, 'No'), (1, 'Yes')])
    CholCheck = forms.ChoiceField(label='Cholesterol Check', choices=[(0, 'No'), (1, 'Yes')])
    BMI = forms.FloatField(label='BMI')
    Smoker = forms.ChoiceField(label='Smoker', choices=[(0, 'No'), (1, 'Yes')])
    Stroke = forms.ChoiceField(label='Stroke', choices=[(0, 'No'), (1, 'Yes')])
    Diabetes = forms.ChoiceField(label='Diabetes', choices=[(0, 'No'), (1, 'Yes')])
    PhysActivity = forms.ChoiceField(label='Physical Activity', choices=[(0, 'No'), (1, 'Yes')])
    HvyAlcoholConsump = forms.ChoiceField(label='Heavy Alcohol Consumption', choices=[(0, 'No'), (1, 'Yes')])
    AnyHealthcare = forms.ChoiceField(label='Any Healthcare', choices=[(0, 'No'), (1, 'Yes')])
    NoDocbcCost = forms.ChoiceField(label='No Doctor due to Cost', choices=[(0, 'No'), (1, 'Yes')])
    GenHlth = forms.ChoiceField(label='General Health', choices=[(i, str(i)) for i in range(1, 6)])
    MentHlth = forms.IntegerField(label='Mental Health', initial=0)
    PhysHlth = forms.IntegerField(label='Physical Health', initial=0)
    DiffWalk = forms.ChoiceField(label='Difficulty Walking', choices=[(0, 'No'), (1, 'Yes')])
    sex = forms.ChoiceField(label='Sex', choices=[(0, 'Female'), (1, 'Male')])
    age = forms.IntegerField(label='Age', min_value=0)

class BMICalculatorForm(forms.Form):
    height = forms.FloatField(label='Height (cm)', min_value=1, widget=forms.NumberInput(attrs={'placeholder': 'Enter height in cm'}))
    weight = forms.FloatField(label='Weight (kg)', min_value=1, widget=forms.NumberInput(attrs={'placeholder': 'Enter weight in kg'}))