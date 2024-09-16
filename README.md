# Secret Santa

This is a Secret Santa implementation. The app is developed using Django and
Vuejs3. The data are stored on a postgresql database. 

## Backend

### Database

Start the database using docker compose

```shell
docker compose up -d
```

### Dependencies

Install uv for python to speed up dependencies installation

```shell
pip install --user uv
```

Create a virtual env

```shell
uv venv venv
```

Install production and development dependencies

```shell
uv pip sync requirements.txt dev-requirements.txt
```

### Run Django server 

```shell
cd secret_santa
```

Create a .env file with database connection information (python settings use
`python_dotenv` to handle env var for a file).

```shell
cat > .env <<EOF
DB_HOST=localhost
DB_USER=ssanta
DB_PASSWORD=secret
DB_PORT=7777
DB_NAME=ssanta
EOF
```

Execute migrations and start the server.

```shell
./manage.py migrate
./manage.py runserver
```

Django is listening to port 8000.

### Tests

py.test unit test are provided. Tests are run with command `py.test`.


## Frontend

Open another shell and go to js app dir

```shell
cd secret_santa/static/js/secret-santa
```

### Install node dependencies

```shell
npm install
```

### Run development server

```shell
npm run dev
```

Open `http://localhost:5173` in a web browser

## Approach

I start by building a walking skeleton with the database, django and vue3 and
I ensure that all the pieces work together.

Then I code the participants and draw behaviour guided by tests as they are the
important part of the application. 

The implementation of the service is kept as simple as possible : only one
participant list is handled, there is no user management. Changing the
participant list delete existing draw. Cohesion is enfored in database using
foreign keys, enforcing data integrity.


## Deployment

I did not have time to deal with deployment. I would package the app in a multi
stage Dockerfile with following actions:

* adapt API base url in VueJS app
* build the app
* copy the asset to tehe django app
* add and configure a nginx server

DB connection information can be passed to running container using environment
variables (`DB_HOST, DB_USER, DB_PASSWORD, DB_PORT and DB_NAME`).
