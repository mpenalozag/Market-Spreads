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