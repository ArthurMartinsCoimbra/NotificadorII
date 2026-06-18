from time import sleep
from bs4 import BeautifulSoup
import requests, phpserialize, json, re

cookies = {
    'PHPSESSID': 'daba0e1be39bb71a9a78c861036778ac',
    '_ga': 'GA1.1.2083834248.1781280005',
    '_ga_KQTSMYDQKY': 'GS2.1.s1781466345$o1$g0$t1781466345$j60$l0$h0',
    '9489d206329ssdb0bd437e1a7541': '530809dfbc11c15eb820b6949fbfc2375049e03c16002ad70ff76f5649029726d2ddb4f1d31607dfbc11c15eb820b6949fbfc2375049e03c16002ad70ff76f5649029726d2ddb4f1d31607',
    '_ga_7D5FCHK8QD': 'GS2.1.s1781806543$o17$g1$t1781807906$j60$l0$h0',
    'token_name': '73f68ff58c91ac9d13f97c212ab74dd38c0d848c241a3163de0bdc6d0292f5bf228aeda973f68ff58c91ac9d13f97c212ab74dd38c0d848c241a3163de0bdc6d0292f5bf228aeda9',
    'token_value': '6eb04967b8dae3851f97f2776aeb1e4e6fc4cc9e217c5827eb49ee30f2fd782961cbfb306eb04967b8dae3851f97f2776aeb1e4e6fc4cc9e217c5827eb49ee30f2fd782961cbfb30',
    '1989d206329b0bd437e1a7531': '3254c45685895ae8f43877a82297c5a81d81619e827624f6cdaf7a3af3ebd2a41d157ad5f011c45685895ae8f43877a82297c5a81d81619e827624f6cdaf7a3af3ebd2a41d157ad5f011',
}

headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,zh;q=0.5',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://adm.zukk.in',
    'priority': 'u=1, i',
    'referer': 'https://adm.zukk.in/agenda-zgo',
    'sec-ch-ua': '"Chromium";v="148", "Google Chrome";v="148", "Not/A)Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    # 'cookie': 'PHPSESSID=daba0e1be39bb71a9a78c861036778ac; _ga=GA1.1.2083834248.1781280005; _ga_KQTSMYDQKY=GS2.1.s1781466345$o1$g0$t1781466345$j60$l0$h0; token_name=8a01b168887bbd844d4f655efaf4a0766754afd6ea88c547bd5b16e9979a9dbaa423bdcb8a01b168887bbd844d4f655efaf4a0766754afd6ea88c547bd5b16e9979a9dbaa423bdcb; token_value=8157fed74d786cee30c420d983919aa470e107266770c7aefa13e39345bd7f97447bf0a78157fed74d786cee30c420d983919aa470e107266770c7aefa13e39345bd7f97447bf0a7; 1989d206329b0bd437e1a7531=325482079f40b328d835b5724e2668d5e3fec2c0e8281860ab52520ef7e1e9bc2f73a7eff1bc82079f40b328d835b5724e2668d5e3fec2c0e8281860ab52520ef7e1e9bc2f73a7eff1bc; _ga_7D5FCHK8QD=GS2.1.s1781471151$o4$g0$t1781471151$j60$l0$h0',
}


payload = {
    'DT_POST': 'a:7:{s:7:"periodo";a:5:{s:8:"criterio";s:1:"1";s:6:"exibir";s:1:"2";s:7:"ultimos";s:1:"7";s:3:"ini";s:10:"DATA_INI";s:3:"fim";s:10:"DATA_FIM";}s:8:"clientes";a:2:{s:4:"view";CLIENTESs:3:"sql";CLIENTES}s:12:"responsaveis";a:2:{s:3:"sql";RESPONSAVEIS_PHPs:4:"view";a:0:{}}s:9:"auditores";a:2:{s:3:"sql";AUDITORES_PHPs:4:"view";a:0:{}}s:12:"listas_tipos";a:2:{s:4:"view";LISTAs:3:"sql";LISTA}s:11:"agenda_tipo";AGENDA_TIPOs:6:"status";STATUS}',
}

def serializar_php_inteiros(ids):

    itens = []

    for indice, valor in enumerate(ids):

        itens.append(
            f"i:{indice};i:{valor};"
        )

    return f'a:{len(ids)}:{{' + ''.join(itens) + '}'

def serializar_php_strings(ids):
    partes = []

    for i, valor in enumerate(ids):
        valor = str(valor)

        partes.append(
            f'i:{i};s:{len(valor)}:"{valor}";'
        )

    return f'a:{len(ids)}:{{' + ''.join(partes) + '}'




html = requests.get(
    "https://adm.zukk.in/agenda-zgo",
    headers=headers,
    cookies=cookies
).text

soup = BeautifulSoup(html, "html.parser")


responsaveis_lista = []

for inp in soup.select('input[id^="responsavel-"]'):
    responsaveis_lista.append(inp["value"])

#print(responsaveis_lista)



responsaveis_dict = {}

for inp in soup.select('input[id^="responsavel-"]'):

    id_resp = inp["value"]

    label = soup.find("label", {"for": inp["id"]})

    if label:
        responsaveis_dict[label.text.strip()] = id_resp

#print(responsaveis_dict)


ids_responsaveis = list(responsaveis_dict.values())

responsaveis_php = serializar_php_inteiros(ids_responsaveis)

#relacao id - clientes
'''
r = requests.get(
    "https://adm.zukk.in/get-clientes",
    headers=headers,
    cookies=cookies
)

clientes_json = r.json()

#relacao cliente - id

clientes_dict = {
    item["text"]: int(item["id"])
    for item in clientes_json["results"]
}

print(clientes_dict)'''


'''clientes_ids = [
    cliente["id"]
    for cliente in clientes_json["results"]
]'''

#ids de clientes serializados
#print(serializar_php_strings(clientes_ids))


def serializar_lista_php(lista):
    itens = []

    for i, valor in enumerate(lista):
        valor = str(valor)
        itens.append(f'i:{i};s:{len(valor)}:"{valor}";')

    return f'a:{len(lista)}:{{' + ''.join(itens) + '}'




dic_agenda_tipo = {"ZGO":1, "ZRobot":2}

lista_de_status = [5]
lista_de_clientes = [268]
lista_de_listas = [7]
lista_de_agenda_tipo = [1]
data_ini = "15/06/2026"
data_fim = "19/06/2026"
clientes_php = serializar_lista_php(lista_de_clientes)
status_php = serializar_lista_php(lista_de_status)
listas_php = serializar_lista_php(lista_de_listas)
agenda_tipo_php = serializar_lista_php(lista_de_agenda_tipo)



payload['DT_POST']=payload['DT_POST'].replace("DATA_INI", data_ini)
payload['DT_POST']=payload['DT_POST'].replace("DATA_FIM", data_fim)
payload['DT_POST']=payload['DT_POST'].replace("CLIENTES", clientes_php)
payload['DT_POST']=payload['DT_POST'].replace("AGENDA_TIPO", agenda_tipo_php)
payload['DT_POST']=payload['DT_POST'].replace("STATUS", status_php)
payload['DT_POST']=payload['DT_POST'].replace("LISTA", listas_php)
payload['DT_POST']=payload['DT_POST'].replace("RESPONSAVEIS_PHP", responsaveis_php)
payload['DT_POST']=payload['DT_POST'].replace("AUDITORES_PHP", responsaveis_php)

#response = requests.post('https://adm.zukk.in/dt-agenda-zgo', cookies=cookies, headers=headers, data=payload)
#resposta = response.json()




dados = phpserialize.loads(
    payload['DT_POST'].encode(),
    decode_strings=True
)



lista_agendas = []


def obter_agendas():
    
    try:
        response = requests.post('https://adm.zukk.in/dt-agenda-zgo', cookies=cookies, headers=headers, data=payload)
        resposta = response.json()

    
        agendas = {}
        for agenda in resposta["data"]:

            agenda_id = agenda["DT_RowId"].replace("row_", "")
            # Dia da semana
            dia_semana = re.search(
                r'<span class="size10">(.*?)</span>',
                agenda["0"]["show"]
            ).group(1)

            # Data
            data_agenda = re.search(
                r'id="data_\d+">(.*?)</span>',
                agenda["0"]["show"]
            ).group(1)

            # Cliente + tipo
            cliente_info = re.search(
                r'badge badge-light">(.*?)</span>',
                agenda["1"]["show"]
            ).group(1)

            # Nome da pesquisa
            pesquisanome = agenda["1"]["sort"]

            # Status
            
            status = re.search(
            r'<button[^>]*>(.*?)</button>',
            agenda["6"]["show"]
            ).group(1)


            '''pesquisa = {
                "dia_semana": dia_semana,
                "data": data_agenda,
                "cliente_info": cliente_info,
                "pesquisa": pesquisanome,
                "status": status
            } ''' 

            agendas[agenda_id] = {
            "data": data_agenda,
            "dia_semana": dia_semana,
            "concorrente" : pesquisanome,
            "cliente(lista)" : cliente_info,
            "status": status
        }
        return agendas
    except Exception as e:
        print("Erro ao obter agendas. Renove os cookies e tente novamente.")
        print(f"Tipo de erro ocorrido: {type(e).__name__}")
        return {}


    

agendas_anteriores = {}

while True:

    agendas_atuais = obter_agendas()

    novas = agendas_atuais.keys() - agendas_anteriores.keys()
    i = 1
    for agenda_id in novas:
        print("Nova agenda:")
        print(agendas_atuais[agenda_id])
        if len(novas) == i:
            print("__________________________________")
        else:
            i += 1

    agendas_anteriores = agendas_atuais.copy()

    sleep(60)






#print(json.dumps(agendas, indent=4, ensure_ascii=False))


'''    if i%2 == 0:
        agendas[agenda_id] = {
            "data": data,
            "dia_semana": dia_semana,
            "pesquisanome" : pesquisanome,
            "nome_pesquisa" : cliente_info,
            "status": status
        }
        i += 1
    else:
        agenda2[agenda_id] = {
            "data": data,
            "dia_semana": dia_semana,
            "pesquisanome" : pesquisanome,
            "nome_pesquisa" : cliente_info,
            "status": status
        }
        i += 1'''





    #lista_agendas.append(pesquisa)  
    


#print(json.dumps(agendas, indent=4, ensure_ascii=False))
    #lista_agendas.append(pesquisa)







#print(json.dumps(lista_agendas, indent=4, ensure_ascii=False))

#print(response.text)


