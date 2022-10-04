import json
import xmltodict
import requests

bus_url = "https://bustracker.muni.org/InfoPoint/XML/stopdepartures.xml"

def lambda_handler(event, context):
    r = requests.get(bus_url)
    o = xmltodict.parse(r.text)

    stops = {}

    for departures in o['departures']['stop']:
        station_name = departures['name']
        if station_name in stops:
            pass
        else:
            stops[station_name] = []

        for departure in departures['departure']:
            if isinstance(departure, dict):
                route_name = departure['route']['name']
                edt = departure['edt']
                sdt = departure['sdt']
                rt = {"name": route_name,
                      "edt": edt,
                      "sdt": sdt}
                stops[station_name].append(rt)

    return {
        'statusCode': 200,
        "Content-Type": "application/json",
        'body': json.dumps(stops)
    }





