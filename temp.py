# import requests

# url = "https://api.vapi.ai/assistant/7b3c389e-72c3-45cf-b4fd-2ed132d1b3ab"

# payload = {
#     "backgroundSound": "office",
#     "voice": {
#         "provider": "11labs",
#         "voiceId": "pNInz6obpgDQGcFmaJgB",
#     }
# }
# headers = {
#     "Authorization": "Bearer 4db5a3be-ca43-485a-a0cb-14214d9c130a",
#     "Content-Type": "application/json"
# }

# response = requests.request("PATCH", url, json=payload, headers=headers)

# print(response.text)

from flask import Flask, request, jsonify
import requests
import json
# def fetch_vehicle_details(registration_number: str):
#     """Run this function when you get the Registration number of a car. It returns the Model Year, Brand, Model, Fuel Type And Mileage of a car"""
#     url = f"https://api.synsbasen.dk/v1/vehicles/registration/{registration_number.upper()}"
#     headers = {"Authorization": "Bearer sb_sk_b13b8db016936ca2b5ee09d4020b9bf9"}
#     response = requests.get(url, headers=headers)

#     if response.status_code == 200:
#         vehicle_data = response.json()
#         return json.dumps({"model year": vehicle_data['data']['model_year'],
#                            "Brand":vehicle_data['data']['brand'],
#                            "Model":vehicle_data['data']['model'], 
#                            "Fuel Type": vehicle_data['data']['fuel_type'], 
#                            "Milage":vehicle_data['data']['mileage']})
#     else:
#         return json.dumps({f"Error: {response.status_code}" :"The Car does not exists"})


# Create the app
app = Flask(__name__)

# API route
@app.route('/vehicle-details', methods=['POST'])
def get_vehicle_details():
    registration_number = request.args.get('registration_number')
    print(registration_number)
    return json.dumps({"model year":  registration_number})

    if not registration_number:
        return jsonify({'error': 'Registration number is required'}), 400 

    url = f"https://api.synsbasen.dk/v1/vehicles/registration/{registration_number.upper()}"
    headers = {"Authorization": "Bearer sb_sk_b13b8db016936ca2b5ee09d4020b9bf9"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        vehicle_data = response.json()
        return json.dumps({"model year": vehicle_data['data']['model_year'],
                           "Brand":vehicle_data['data']['brand'],
                           "Model":vehicle_data['data']['model'], 
                           "Fuel Type": vehicle_data['data']['fuel_type'], 
                           "Milage":vehicle_data['data']['mileage']})
    else:
        return json.dumps({f"Error: {response.status_code}" :"The Car does not exists"})


# Run it 
if __name__ == '__main__':
    app.run(debug=True) 