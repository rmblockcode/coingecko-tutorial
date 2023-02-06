from pycoingecko import CoinGeckoAPI
from telegram import tel_send_message

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


if __name__ == '__main__':
    get_prices('bitcoin,ethereum', 'usd')

    # print(get_coin_list())