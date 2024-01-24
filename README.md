# CP3Y9A6U_store

#### download
```
git clone https://github.com/SergioRyzhov/CP3Y9A6U_store.git
```

#### to run
```
docker-compose -f docker-compose.yaml up -d
```

#### to stop
```
docker-compose -f docker-compose.yaml down -v
```
#### apply migrations
```
docker exec -it app python app/manage.py migrate
```
#### to init data
```
docker exec -it app python app/manage.py loaddata fixtures.json
```
***

## REST usage

### endpoint to retrieve manufacturer IDs
```
GET 0.0.0.0:8000/store/manufacturers/1/
```
### endpoints to add extra data
```
json body
{
    "number": 123
}

POST 0.0.0.0:8000/store/contracts/
```
```
json body
{
    "contract": 1
}

POST 0.0.0.0:8000/store/orders/
```
```
json body
{
    "name": "manufacturer-1"
}

POST 0.0.0.0:8000/store/manufacturers/
```
```
json body
{
    "name": "Product",
    "credit_order": 1,
    "manufacturer": 2
}

0.0.0.0:8000/store/products/
```