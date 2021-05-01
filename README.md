# Fleet management

## How to run locally
- create a virtual environment based on requirements.txt file
- run `python3 manage.py migrate`
- run `python3 manage.py runsslserver`

## API

1. Downloading single entity:
GET, https://api_address/car:retrieve?id={id}
2. Downloading a list of entities and filter on query params:
GET, https://api_address/car:list?query_params
query params available : ['model', 'brand', 'production_year', 'registration_number', 'max_passenger_capacity', 'id', 'car_class', 'low_emission']
- If you want to display additional data, like 'car_class' or 'low_emission':
GET, https://api_address/car:list?info=car_class,low_emission
3. Creating an entity:
POST, https://api_address/car:create, Body: JSON 
4. Updating an entity:
POST, https://api_address/car:update/id, Body: JSON 
5. Deleting an entity:
DELETE, https://api_address/car:delete/id

