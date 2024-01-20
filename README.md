# star-navi
StarNavi test task "Social Network".
##Api
* Install requirements:
```
pip install -r requirements.txt
```
* Update requirements:
```
pip freeze > requirements.txt
```
* Run local:
```
python manage.py runserver
```
* Run docker-compose:
```
docker-compose up --build
```
* Make migrations:
```
docker exec -it <container_id> bash
python manage.py makemigrations
python manage.py migrate
```
### Set environment variables:
**list of environment variables which should be set:**<br>
```
DB_NAME
DB_USER
DB_PASSWORD
DB_HOST
DB_PORT
DJANGO_SECRET_KEY
DEBUG
```
if running with docker: 
DB_HOST should be set as name of container with db<br>

**Windows:**
```
//CMD:
set SOME_VARIABLE=some_value

//Powershell:
$Env:Foo = 'An example'
```
**Linux:**
```
export SOME_VARIABLE=some_value
```

### Endpoints:
* List of all endpoints you can find in Swagger:
```
http://127.0.0.1:8000/star-navi/api/schema/docs/    # Swagger docs
http://127.0.0.1:8000/star-navi/register
http://127.0.0.1:8000/star-navi/api/token/
http://127.0.0.1:8000/star-navi/api/token/refresh/
http://127.0.0.1:8000/star-navi/api/post/
http://127.0.0.1:8000/star-navi/api/post/{post_id}/like/
http://127.0.0.1:8000/star-navi/api/post/{post_id}/unlike/
http://127.0.0.1:8000/star-navi/api/analytics/
http://127.0.0.1:8000/star-navi/api/user/
```
## Bot
**Configure Data**
* Set config data in bot/config.py

**Run bot:**
```
python automated_bot.py 
```
