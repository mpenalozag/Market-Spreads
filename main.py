import markets_requests
from fastapi import FastAPI

app = FastAPI()


@app.get("/all_spreads")
def read_markets_spreads():
    return markets_requests.get_all_market_spreads()

@app.get("/spread/{market_id}")
def read_item(market_id: str):
    return markets_requests.get_market_spread(market_id)