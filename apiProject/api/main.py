from fastapi import FastAPI
from teamWeb import getFantasyName, getPlayerNews

app = FastAPI()

@app.get('/test')
async def root():
    return {'example': 'this is an example', 'data': 0}

@app.get('/{sport}')
async def team(sport):
    result = getFantasyName(sport)
    return {'sport-name': result}

@app.get('/{sport}/player-news')
async def playerNews(sport):
    result = getPlayerNews(sport)
    return {'player-data': result}