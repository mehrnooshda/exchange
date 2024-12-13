

# Crypto Purchase Platform

This project provides an API to allow users to purchase cryptocurrencies using their account balance. The platform 
supports the purchase of several cryptocurrencies like BTC, ETH, ADA, and more. The backend is built using Django and 
Django Rest Framework, and the project can be easily deployed using Docker. 

## Features

- **User Management**:
Users can create accounts and manage their balance.
- **Purchase Cryptocurrencies**: Users can buy supported cryptocurrencies (BTC, ETH, etc.) if they have sufficient balance.
- **Error Handling**: Includes error messages for unsupported coins, insufficient balance, and invalid user IDs.
- **Testing**: The project is tested using DRF’s test framework.

## Tech Stack

- Django: Web framework for building the application.
- Django Rest Framework (DRF): For building the RESTful API.
- Docker: Containerization for the application, making it easy to deploy across environments.
- In Memory Queue: which can easily be replaced with Redis queue to store pending purchase requests.
## Setup
### Prerequisites

Before running the project, make sure you have the following installed:

- Python 3.12+
- Docker (For containerization)


### Installation

1. **Clone the Repository:**

```bash
git clone https://github.com/mehrnooshda/exchange
cd exchange
```

2. **Create a Virtual Environment** (Optional, if you don't use Docker):

```bash
python3 -m venv .venv
source .venv/bin/activate 
```
3. **Install Dependencies:**

```bash
pip install -r requirements.txt
```
4. **Migrate Database:** Run the following command to set up your database:

```bash 
python manage.py migrate
```

5. **Create Superuser:** To create an admin user for the Django admin panel:

```bash
python manage.py createsuperuser
```
6. **Create user for buy currencies:** Go to http://127.0.0.1:8000/admin in create a user with currency in order to be
able to buy currencies. This user is going to have the user_id of 1.

7. **Run the Development Server:**
```bash
python manage.py runserver
```
The application should now be accessible at http://127.0.0.1:8000/.

## Dockerization

To run the application inside Docker containers, follow these steps:

Build the Docker Image:
```bash
docker build -t crypto_purchase_platform .
```
Run the Docker Container:
```bash
docker run -p 8000:8000 crypto_purchase_platform
```
The application should now be accessible at http://127.0.0.1:8000/.

The instructions in readme are complete for building the docker image and run it on a preinstalled ubuntu server (and I suggest to use them to build docker image)
But in case of any issue you can also pull the image via Docker-hub:
```bash
docker pull mehrnooshda/app
```


## API Endpoints

- **POST** `/buy-crypto/`: Allows users to purchase cryptocurrencies.
- **Request body Example**:
```json
{
  "user_id": 1,
  "coin_name": "BTC",
  "quantity": 2
}
```

- **Response**:

  
  + Success: `{ "message": "Purchase successful" }`
  + User not found: `{ "message": "User does not exist" }`
  + Insufficient balance: `{ "message": "Insufficient balance to complete this transaction." }`
  + Unsupported coin: `{ "message": "Coin <coin_name> is not available. Please choose from: BTC, ETH, XRP, ADA, LTC" }`

## Tests

The project includes a set of unit tests to verify the behavior of the application. To run the tests:

Run Tests with Django:

```BASH
python manage.py test
```
