import requests


def get_near_earth_objects(start_date, end_date, api_key):
    query = {'start_date': start_date, 'end_date': end_date, 'api_key': api_key}
    response = requests.get('https://api.nasa.gov/neo/rest/v1/feed', params=query).json()
    return response['near_earth_objects']
