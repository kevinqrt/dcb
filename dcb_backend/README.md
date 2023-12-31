# DCB_Backend

## Setup local environment
1.  Setup python virtual environment:
    - Go to the root directory of the project and run: `python3.11.5 -m venv venv`
    - Open a terminal inside the venv and install requirements.txt run: `pip install -r requirements.txt`
1.  Set .env variables
    - copy the file `.env.example` and rename it to `.env`
    - Get API Token for embedding model
        - For Hugginface setup from https://huggingface.co/settings/tokens
        - For OpenAI setup from https://platform.openai.com/account/api-keys
    - Initialize DB-Parameters for PostgreSQL database
        - For local db setup refer to: https://www.postgresql.org/
2. Migrate database. Run:
    - `python manage.py makemigrations`
    - `python manage.py migrate`
3. Run redis:
    - `docker run -d --name redis-cache -p 6379:6379 redis/redis-stack-server:7.2.0-v6`
4. Run server:
    - `python manage.py runserver`

## API Schema
### Creating the schema:
    ./manage.py spectacular --color --file schema.yml
### Using SWAGGER UI:
    docker run -p 80:8080 -e SWAGGER_JSON=/schema.yml -v ${PWD}/schema.yml:/schema.yml swaggerapi/swagger-ui
    
