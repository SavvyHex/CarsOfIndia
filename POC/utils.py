import requests
import json

MAIN_URL = "https://vpic.nhtsa.dot.gov/api/"

# Gets car model names based on the manufacturer
def models_for_make(make:str="", modelyear:str="", vehicletype:str="") -> dict:
    try:
        if modelyear or vehicletype:
            url = MAIN_URL + f"/vehicles/GetModelsForMakeYear/{make}{f"/modelyear/{modelyear}" if modelyear else ""}{f"/vehicletype/{vehicletype}" if vehicletype else ""}?format=json"
        else:
            url = MAIN_URL + f"/vehicles/GetModelsForMake/{make}?format=json"
        r = requests.get(url)
        return json.loads(r.text)["Results"]
    except Exception as e:
        raise e

# Gets information about the manufacturer
def manufacturer_details(manufacturer:str="") -> dict:
    try:
        if not manufacturer:
            manufacturer = input("Enter the manufacturer for which you want the details of : ").lower().replace(" ", "%20")
        url = MAIN_URL + f"/vehicles/GetManufacturerDetails/{manufacturer}?format=json"
        r = requests.get(url)
        return json.loads(r.text)["Results"]
    except Exception as e:
        raise e

# Returns the list of variables related to vehicles
def vehicle_variables()-> dict:
    return json.loads(requests.get(MAIN_URL+"/vehicles/GetVehicleVariableList?format=json").text)["Results"]

# Returns possible values for each variable related to the vehicle
def vehicle_variable_values(variable:str=""):
    try:
        if not variable:
            variable = input("Enter the variable for which you want the possible values of : ").lower().replace(" ", "%20")
        url = MAIN_URL + f"/vehicles/GetVehicleVariableValuesList/{variable}?format=json"
        r = requests.get(url)
        return json.loads(r.text)["Results"]
    except Exception as e:
        raise e
 
