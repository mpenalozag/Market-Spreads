import requests

API_BUDA_URL = "https://www.buda.com/api/v2"

def get_all_markets() -> dict:
    """
    Retorna la información de todos los mercados.
    """
    response = requests.get(API_BUDA_URL + "/markets")
    return response.json()
        
def get_market_order_book(market_id: str) -> dict:
    """
    Retorna el libro de ordenes de un mercado.
    """ 
    response = requests.get(API_BUDA_URL + f"/markets/{market_id}/order_book")
    return response.json()

def get_market_spread(market_id: str) -> float:
    """
    Retorna un float, que indica el spread del mercado pedido.
    """
    order_book = get_market_order_book(market_id)["order_book"]
    print(order_book)
    try:
        lowest_ask = float(order_book["asks"][0][0])
        highest_bid = float(order_book["bids"][0][0])
    except Exception as error:
        print(error)
    try:
        return lowest_ask - highest_bid
    except:
        return 0
    
def get_all_market_spreads() -> list:
    """
    Retorna el spread de todos los mercados en una lista de tuplas.
    Cada tupla es un par (market_id, spread). 
    """
    markets_spreads = []
    all_markets = get_all_markets()["markets"]
    for market in all_markets:
        market_id = market["id"]
        market_spread = get_market_spread(market_id)
        markets_spreads.append((market_id, market_spread))
    return markets_spreads