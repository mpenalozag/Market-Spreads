from spread import get_all_market_spreads, get_market_spread
from fastapi import FastAPI

app = FastAPI()


@app.get("/all_spreads")
def read_markets_spreads():
    return get_all_market_spreads()

@app.get("/spread/{market_id}")
def read_item(market_id: str):
    return get_market_spread(market_id)