# Brioche Food

## Table Of Contents

- [Table Of Contents](#table-of-contents)
- [About The Project](#about-the-project)
  - [What has been implemented so far?](#what-has-been-implemented)
  - [Done With](#done-with)
- [Getting Started](#getting-started)
- [Flow](#flow)
- [Routes](#routes)
- [Run tests](#run-tests)
- [File Structure](#file-structure)
  - [Architecture](#architecture)
  - [Fisrt Level](#first-level)
  - [Second Level](#second-level)

## About The Project

This project is aimed at creating the Back-End of a Bakery Marketplace that connects establishments to people crazy about breads and sweets!

## What has been implemented so far?

We already:

- [x] Created the endpoint of listing and creating bakeries.
- [x] Created the endpoint of listing and creating products.
- [x] Created the endpoint of listing and creating customers.
- [x] Created an endpoint that creates a recipient and bank account for a bakery.
- [x] Create an endpoint that creates a sale for the bakery.
- [x] Integrate with the Pagarme payments API.
- [x] Added split rule.
- [x] Added integration tests to the current codebase.
- [x] Document in Swagger.

### Done With

Below is what was used to create this project:

- [Python] - The chosen language was Python;
- [Django] - For a clean and fast api development;
- [Django Rest Framework] - Apis development kit that implements Django and makes our implementation even more elegant;
- [Pagarme] - Payment intermediary that facilitates transactions carried out;
- [Swagger] - API documentation tool

<!-- GETTING STARTED -->

## Getting Started

1. Get Python
2. register with paying for a test account at this link -> https://dashboard.pagar.me/#/login
3. update your .env with its 'PAGARME_CHAVE_API' and 'PAGARME_RECIPIENT_ID' values
4. go to the source 'cd .\briochefood\src\'
5. run 'pip install -r requirements.txt'
6. run 'python manage.py migrate'
7. run 'python manage.py runserver'
8. Enjoy!

## Flow

The flow to be followed is as follows

1. create customer
2. create bakerie
3. create product
4. create recipient and bank account
5. create sale

## Routes

We have the following routes below, but you can also check them on Swagger at this link 'https://app.swaggerhub.com/apis/Dianna-coder/BriocheFood/1.0.0'

### Creating a customer - POST /api/customers

We expect the input to be a json like this

```bash
{
  "name": "Pirate Customer 2",
  "email": "pirate@customer.com",
  "cpf": "44699109888",
  "phone_number": "11938485966",
  "birthday": "2001-02-02",
  "country": "BR",
  "state": "SP",
  "city": "Taboao da Serra",
  "neighborhood": "Av aaa",
  "street": "Av aaaa",
  "street_number": "10000",
  "zipcode": 6787360
}
```

Our successful creation output will be (201)

```bash
[
    {
        "id": "2fefb2bf-7182-4346-b49c-7de349cbd9c6",
        "name": "Pirate Customer 2",
        "email": "pirate@customer.com",
        "cpf": "44699109888",
        "phone_number": "11938485966",
        "birthday": "2001-02-02",
        "country": "BR",
        "state": "SP",
        "city": "Taboao da Serra",
        "neighborhood": "Av aaa",
        "street": "Av aaaa",
        "street_number": "10000",
        "zipcode": 6787360
    }
]
```

### Creating a bakery - POST /api/bakeries

We expect the input to be a json like this

```bash
{
  "cnpj": "33095101000142",
  "name": "Bread Bakery",
  "address": "Av bakery"
}
```

Our successful creation output will be (201)

```bash
{
    "id": "9575e89d-cb36-4da3-add5-613074795778",
    "cnpj": "33095101000142",
    "name": "Bread Bakery",
    "address": "Av bakery",
    "recipient": null
}
```

### Creating a product - POST /api/bakeries/products

We expect the input to be a json like this

```bash
{
  "title": "Bread",
  "unit_price": "10000",
  "quantity": 1000,
  "bakery": "9575e89d-cb36-4da3-add5-613074795778"
}
```

Our successful creation output will be (201)

```bash
{
    "id": "ffd32a1b-e784-4166-bb0f-5613c55d91c4",
    "title": "Bread",
    "unit_price": "10000",
    "quantity": 1000,
    "bakery": "9575e89d-cb36-4da3-add5-613074795778"
}
```

### Creating a recipient and bank account for a bakery - POST /api/bakeries/<bakery_cnpj>/recipient

We expect the input to be a json like this

```bash
{
  "transfer_day": "5",
  "transfer_interval": "weekly",
  "bank_account": {
    "agencia": "0932",
    "agencia_dv": "5",
    "bank_code": "341",
    "conta": "58054",
    "conta_dv": "1",
    "document_number": "26268738888",
    "legal_name": "HOUSE TARGARYEN"
  }
}
```

Our successful status output will be (200)

```bash
Recebedor e conta bancária criados!
```

### Creating a sale for a bakery - POST /api/bakeries/<bakery_cnpj>/sales

We expect the input to be a json like this

```bash
{
  "amount": "10000",
  "payment_method": "credit_card",
  "card_number": "4111111111111111",
  "card_cvv": "123",
  "card_expiration_date": "0922",
  "card_holder_name": "Morpheus Fishburne",
  "customer": {
    "external_id": "2fefb2bf-7182-4346-b49c-7de349cbd9c6",
    "name": "Arroz de teste",
    "type": "individual",
    "country": "br",
    "email": "mopheus@nabucodonozor.com",
    "documents": [
      {
        "type": "cpf",
        "number": "30621143049"
      }
    ],
    "phone_numbers": ["+5511999998888", "+5511888889999"],
    "birthday": "1965-01-01"
  },
  "billing": {
    "name": "Trinity Moss",
    "address": {
      "country": "br",
      "state": "sp",
      "city": "Cotia",
      "neighborhood": "Rio Cotia",
      "street": "Rua Matrix",
      "street_number": "9999",
      "zipcode": "06714360"
    }
  },
  "shipping": {
    "name": "Arroz de teste",
    "fee": "1000",
    "delivery_date": "2000-12-21",
    "expedited": true,
    "address": {
      "country": "br",
      "state": "sp",
      "city": "Cotia",
      "neighborhood": "Rio Cotia",
      "street": "Rua Matrix",
      "street_number": "9999",
      "zipcode": "06714360"
    }
  },
  "items": [
    {
      "id": "9dd2b3cf-9e1b-4927-9cd7-24aa85a61a83",
      "title": "Red pill",
      "unit_price": "10000",
      "quantity": "1",
      "tangible": true
    },
    {
      "id": "1b989eb3-4ca1-4c9d-97e5-38058984679d",
      "quantity": "1",
      "title": "Blue pill",
      "unit_price": "10000",
      "tangible": true
    }
  ]
}

```

Our successful status output will be (200)

```bash
Compra realizada!
```

### Common 400 and 500 status for all routes

Our validation error output (400)

```bash
{
    "name": [
        "This field is required."
    ]
}
```

Output on server error (500):

```
HTTP 500 INTERNAL SERVER ERROR
```

## Run tests

- run `python manage.py test`

## File Structure

### Architecture

The architecture follows the MVT standard proposed by Django Rest Framework, in addition I separated the project into modules

### First Level

- On the first level we concentrated the project on the src and I shared two major responsibilities which are "bakeries" and "customers".
- We have a global folder of utils where I can put providers or other utilities.
- We have examples of json to make requests.
- And the rest of the level concerns the project's settings and database.

```bash
briochefood
├── src/
│    ├── bakeries/
│    ├── customers/
│    ├── requests_examples/
│    ├── utils/
│    ├── manage.py
│    ├── requirements.txt
│    ├── urls.py
│    └── wsgi.py
└── db.sqlite3
```

### Second Level

- In each module we have the migrations and models to create the SQL tables, we have their tests, serializers, routes and views with the implementation of the endpoints
- In utilities I have the methods and rules related to Pagarme's api

```bash
briochefood
├── src/
│    ├── bakeries/
│    │   ├── migrations/
│    │   ├── tests/
│    │   ├── validators/
│    │   ├── admin.py
│    │   ├── apps.py
│    │   ├── models.py
│    │   ├── serializer.py
│    │   ├── urls.py
│    │   └── view.py
│    ├── customers/
│    │   ├── migrations/
│    │   ├── admin.py
│    │   ├── apps.py
│    │   ├── models.py
│    │   ├── serializer.py
│    │   ├── tests.py
│    │   ├── urls.py
│    │   └── view.py
│    ├── requests_examples/
│    │   ├── bakery_create.json
│    │   ├── customer_create.json
│    │   ├── product_create.json
│    │   ├── recipient_and_bank_create.json
│    │   └── sale_create.json
│    ├── utils/
│    │   ├── pagarme.py
│    │   └── rules.py
│    ├── manage.py
│    ├── requirements.txt
│    ├── urls.py
│    └── wsgi.py
└── db.sqlite3

```
