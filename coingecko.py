from pycoingecko import CoinGeckoAPI
from telegram import tel_send_message
from pprint import pprint

cg = CoinGeckoAPI()


def get_prices(coin_ids: str, vs_currencies: str):
    prices = cg.get_price(
        ids=coin_ids,
        vs_currencies=vs_currencies
    )

    text = ''
    for k, v in prices.items():
        price = v.get('usd')
        text += f'Symbol: {k} - Price(usd): {price}'
        text += f'\n'

    tel_send_message(text)
    return prices


def get_coin_list():
    return cg.get_coins_list()


def get_coins_markets(vs_currency: str):
    return cg.get_coins_markets(vs_currency)


def get_coin_by_id(id: str):
    return cg.get_coin_by_id(id)

def get_coin_ohlc_by_id(id: str, vs_curreny: str, days:str):
    """
        Example response:
        	
        successful operation

        [
            1594382400000 (time),
            1.1 (open),
            2.2 (high),
            3.3 (low),
            4.4 (close)
        ]
    """
    return cg.get_coin_ohlc_by_id(id, vs_curreny, days)


def get_global_data(descentralized=False):

    if descentralized:
        return cg.get_global_decentralized_finance_defi()
    
    return cg.get_global()

if __name__ == '__main__':

    # Agrega todas las llamadas que consideres necesarias.
    get_prices('bitcoin,ethereum', 'usd')

    # print(get_coin_list())
    #pprint(get_coins_markets('usd'))
    pprint(get_coin_by_id('bitcoin'))

    # Global data
    print('##########################')
    print('No DeFi Data:')
    pprint(get_global_data())

    print('##########################')
    print('DeFi Data')
    pprint(get_global_data(True))

    pprint(get_coin_ohlc_by_id('bitcoin', 'usd', '1'))