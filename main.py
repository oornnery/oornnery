# pandas
# openpyxl
# twilio

import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC964c1bacff40b3d4c0202a30c55fcd03"
# Your Auth Token from twilio.com/console
auth_token  = "5c9e6aa17db46089ff5b2f832318e0d5"

client = Client(account_sid, auth_token)
# Passo a passo de solução

# Abrir os 6 aquivos de Excel
from twilio.rest.api.v2010.account.message import MessageInstance

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'Nos mês {mes} Alguem bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        message = client.messages.create(
            to="+5511983120625",
            from_="+12182154779",
            body=f'No mês {mes} Alguem bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')

        print(message.sid)

# Verificaar se algum valor na coluna de Vendas daquele arquivo é maior que 55.000

# Se for maior que 55.000 -> enviar um SMS com o Nome, o Mês e as vendas do vendedor

# Caso não seja maior que 55.000 não fazer nada


