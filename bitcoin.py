import requests
import matplotlib.pyplot as plt

def get_btc_price():
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    response = requests.get(url)
    data = response.json()
    return data['bpi']['USD']['rate_float']

responseBancoCentral = requests.get('https://api.bcb.gov.br/dados/serie/bcdata.sgs.10813/dados/ultimos/1?formato=json')
dolar_data = responseBancoCentral.json()[0]
dolar_value = dolar_data['valor']

plt.ion() # modo interativo do pyplot
plt.style.use('dark_background') # define o estilo de cor do gráfico
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim([0, 100]) # define o limite máximo no eixo x
xs = [0]
ys = [get_btc_price()*float(dolar_value)] # adiciona o valor inicial

while True:
    price = get_btc_price()
    xs.append(xs[-1]+1) # atualiza o intervalo de tempo
    real_price = float(price) * float(dolar_value)
    ys.append(real_price)

    ax.clear()
    ax.plot(xs, ys, color='red', linestyle='-')
    plt.title('Valor Bitcoin')
    plt.xlabel('Tempo (segundos)')
    plt.ylabel('Preço (R$)')

    # adiciona um texto com o valor exato do Bitcoin em tempo real
    text = f'Bitcoin: R$ {real_price:.2f}'
    ax.text(0.05, 0.95, text, transform=ax.transAxes, fontsize=14, verticalalignment='top')

    plt.draw()
    plt.pause(5) # pausa por 5 segundos