# Problem Statement

- Build APIs for a social media platform in either NodeJS or Python
- The API should support features like getting a user profile, follow a user, upload a post, delete a post, like a post, unlike a liked post, and comment on a post
- Design the database schema and implement in PostgreSQL or MongoDB

### **API Endpoints**
BASE_URL = https://dj-social-api.onrender.com
- **POST** /api/authenticate/
- **GET** /api/user/
- **POST** /api/follow/{userId}/
- **POST** /api/unfollow/{userId}/
- **GET** /api/posts/{id}/
- **GET** /api/all_posts/
- **DELETE** /api/posts/{postId}/
- **POST** /api/posts/
- **POST** /api/like/{postId}/
- **POST** /api/unlike/{postId}/
- **POST** /api/comment/{postId}/

### Installation

 Clone the repo
   ```sh
   git clone https://github.com/ankitdevelops/django-simple-social-media.git
   ```

   ```sh
   cd django-simple-social-media
   ```
Create a virtual environment and install the dependencies

```sh
virtualenv env
pip install -r requirements.txt

# or only if using pipenv

pipenv shell
pipenv install
```
### setting  up the database
- create a db in postgres
- create a `.env` file in the project root director and add the following url.
```
ALLOWED_HOSTS = *
DEBUG=1
PYTHON_VERSION=3.10.9
DB_NAME=<your_db_name>
DB_PASSWORD=<your_db_password>
DB_USER=<your_db_user>
```
### Run the following command
```sh
python manage.py collectstatic #only if needed
python manage.py makemigrations #only if needed
python manage.py migrate #only if needed
python manage.py runserver
```

### Credentials

```
Email:- ankit@gmail.com
Password:-testing321

Email:- mohit@gmail.com
Password:-testing321

Email:- manish@gmail.com
Password:-testing321

Email:- john@gmail.com
Password:-testing321
```