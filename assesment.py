

import pandas as pd
import json
#importing pandas and json libraries

df = pd.read_json("/content/data.json")


# cm_to_meter , Bmi , Category , Health_risk are using fucntions to apped the json files
try:
  def cm_to_meter (cm):
    Meter = cm / 100.0 

    return Meter
except:
  print("there is a problem in converting cm to meter function")


try:
  def BMI( weight , height ):

    # forumula 1 :- mass(kg) / height(m)
    height = cm_to_meter(height)
    bmi = weight / (height*height)

    return round(bmi , 2)
except:
  print("there is a problem in BMI calcualting fucntion ")


try:

  def Category(bmi):
    
    if bmi < 18.4:
      return "Under Weight"
    elif bmi >= 18.5 and bmi <= 19.5:
      return "Normal Weight"
    elif bmi >= 25 and bmi <= 24.9:
      return "Over Weight"
    elif bmi >= 30 and bmi <= 34.5:
      return "Moderately obese"
    elif bmi >= 35 and bmi <= 39.9:
      return "Severly Obese"
    else:
      return "Very Severely Obese"

except:
  print("there is problem in catergorying bmi types fucnction")



try:

  def Health_risk(bmi):
    if bmi < 18.4:
      return "Malnutrition risk"
    elif bmi >= 18.5 and bmi <= 19.5:
      return "Low Risk"
    elif bmi >= 25 and bmi <= 24.9:
      return "Enhanced risk"
    elif bmi >= 30 and bmi <= 34.5:
      return "Medium risk"
    elif bmi >= 35 and bmi <= 39.9:
      return "High risk"
    else:
      return "Very high risk"
except:
  print("problem in Health in risk function")


new_df = pd.DataFrame()

try:

  new_df['BMI_kg/m2'] = BMI(df['WeightKg'] , df['HeightCm'])
  #applying the bmi fucntion to the data frame and creating a new BMI_kg/m2 column
  new_df['BMI_Category'] = new_df.apply(lambda x: Category(x['BMI_kg/m2']), axis=1)
  #applying Category fucntion to a dataframe and creating new data frame
  new_df['BMI_Health_Risk'] = new_df.apply(lambda x: Health_risk(x['BMI_kg/m2']), axis=1)
  #applying Health_risk fucntion to df and creating a new column

except:
  print("error in applying functions to a data using data frames")



x = json.loads(new_df.to_json(orient='records'))



try:
  with open("/content/data.json", "r+") as file:
    data = json.load(file)
    #loading json file 

    for i in range(0 , len(data)):
      data[i].update(x[i])
    #updating dict objects 

    file.seek(0)
    json.dump(data , file)
    file.truncate()
    #truncating the file
    
except:
  print("error: loading json file or " 
                "wring into json file or " )

