import requests
import time

while True:
    response = requests.get('https://api.coinbase.com/v2/prices/BTC-USD/spot')
    responseBancoCentral = requests.get(
        'https://api.bcb.gov.br/dados/serie/bcdata.sgs.10813/dados/ultimos/1?formato=json')
    data = response.json()
    price = data['data']['amount']
    dolar_data = responseBancoCentral.json()[0]
    dolar_value = dolar_data['valor']
    real_price = float(price) * float(dolar_value)
    if(real_price < float(108000)):
        print("ALERTA!")
    
    print(f'Preço do Bitcoin: R$ {real_price:.2f}')
    time.sleep(10)
