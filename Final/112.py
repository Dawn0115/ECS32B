import requests
from TableViewer import *

# Initial code written by Derya Akbaba, University of Utah.
# Author of final code:

######################################
# Data Retrieval & Data Printing
######################################

# You will be using three datasets for this project from opendata.utah.gov.
# We will show you how to import one dataset using an API and you will be
# responsible for the other two.

# Here, we are importing COVID case numbers from the following url
# https://opendata.utah.gov/Health/Utah-COVID-Cases-by-County-Map/y4r8-7n5m
covid = "https://opendata.utah.gov/resource/y4r8-7n5m.json"
covid_api_response = requests.get(covid)

covid_data = covid_api_response.json()

# You can use the view_table function to see the first 5 rows
# of the data that you just loaded.

print("Preview of downloaded COVID data:")
print(view_table(covid_data), "\n")

# This is where you will start loading your data.
# We have provided the name of the dataset and the URl to find the API endpoint.

# Data retrieval Step 1.
# Utah Hospital Characteristics
# https://opendata.utah.gov/Health/Utah-Hospital-Characteristics/ierb-h3t5
# Store the data from this data set in a variable called hospital_data.

# todo Put code here for data retrieval Step 1.
hospital = 'https://opendata.utah.gov/resource/ierb-h3t5.json'
hospital_api_response = requests.get(hospital)
hospital_data = hospital_api_response.json()
print("Preview of downloaded HOSPITAL data:")
print(view_table(hospital_data), "\n")


# Data retrieval Step 2.
# Average Home Price By County In Utah 1996-2015
# https://opendata.utah.gov/Social-Services/Average-Home-Price-By-County-In-Utah-1996-2015/sma7-tpu2
# Store the data from this data set in a variable called housing_data.

# todo Put code here for data retrieval Step 2.
housing = 'https://opendata.utah.gov/resource/sma7-tpu2.json'
housing_api_response = requests.get(housing)
housing_data = housing_api_response.json()
print("Preview of downloaded HOUSING data:")
print(view_table(housing_data), "\n")

######################################
# Dictionary Creation
# Make a dictionary using county name as the key.
# From the hospital dataset you will want to add all of the total_licensed_beds in a county.
# From the COVID dataset you will want to add active cases.
# From the Housing dataset you will want the difference between the housing prices (2015 - 1996).
# Your data structure will look like this:
# {'county1': {'beds': [1], 'cases': [2], 'housing': [3]}, 'county2': {'beds': [1], 'cases': [2], 'housing': [3]}}
######################################

complete_dict = {}
for item in hospital_data:
    county = item['county'].upper()
    beds = int(item['total_licensed_beds'])
    if county in complete_dict:
        if 'beds' in complete_dict[county]:
            complete_dict[county]['beds'] += beds
        else:
            complete_dict[county]['beds'] = beds
    else:
        complete_dict[county] = {'beds': beds}

# Finally, you will find how much the housing prices have changed in each county.
# You can get this number by finding the difference between the average home price
# in April 1996 and the average home price in April 2015.
# The values should mostly be positive since home prices have increased since 1996.
# We are expecting to see float values.

# Get the housing price change per county
for item in housing_data:
    county = item['county'].upper()
    price_1996 = float(item['april_1996_average_price'])
    price_2015 = float(item['april_2015_average_price'])
    price_change = price_2015 - price_1996
    if county in complete_dict:
        if 'housing' in complete_dict[county]:
            complete_dict[county]['housing'] = price_change
        else:
            complete_dict[county]['housing'] = price_change
    else:
        complete_dict[county] = {'housing': price_change}

# You can print the dictionary to see all your data in one place.
print("Nested Dictionary:")
print(complete_dict)