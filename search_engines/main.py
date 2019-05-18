from fastapi import FastAPI


app = FastAPI()


@app.get('/v1/es')
def es(q: str):
    pass


@app.get('/v1/mysql')
def mysql(q: str):
    pass

