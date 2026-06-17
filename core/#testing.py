from time import sleep

import requests, phpserialize, json, re

cookies = {
    'PHPSESSID': 'daba0e1be39bb71a9a78c861036778ac',
    '_ga': 'GA1.1.2083834248.1781280005',
    '_ga_KQTSMYDQKY': 'GS2.1.s1781466345$o1$g0$t1781466345$j60$l0$h0',
    '9489d206329ssdb0bd437e1a7541': '5308103b1733c94d9b0edf715393f4f6ed86aefb9713eff9f9fd127c7e49def21bc437f2c08e2d3b1733c94d9b0edf715393f4f6ed86aefb9713eff9f9fd127c7e49def21bc437f2c08e2d',
    '1989d206329b0bd437e1a7531': '325475aa915eed3c36badde6b290b6188a2f4a73cc7e51092caa4470f638c4eeb461f542409575aa915eed3c36badde6b290b6188a2f4a73cc7e51092caa4470f638c4eeb461f5424095',
    '_ga_7D5FCHK8QD': 'GS2.1.s1781723876$o12$g1$t1781724305$j60$l0$h0',
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
    'DT_POST': 'a:7:{s:7:"periodo";a:5:{s:8:"criterio";s:1:"1";s:6:"exibir";s:1:"2";s:7:"ultimos";s:1:"7";s:3:"ini";s:10:"DATA_INI";s:3:"fim";s:10:"DATA_FIM";}s:8:"clientes";a:2:{s:4:"view";CLIENTESs:3:"sql";CLIENTES}s:12:"responsaveis";a:2:{s:3:"sql";a:94:{i:0;i:309;i:1;i:467;i:2;i:229;i:3;i:405;i:4;i:406;i:5;i:443;i:6;i:448;i:7;i:247;i:8;i:246;i:9;i:435;i:10;i:254;i:11;i:455;i:12;i:194;i:13;i:190;i:14;i:113;i:15;i:221;i:16;i:1;i:17;i:456;i:18;i:446;i:19;i:205;i:20;i:163;i:21;i:480;i:22;i:440;i:23;i:232;i:24;i:322;i:25;i:326;i:26;i:331;i:27;i:428;i:28;i:429;i:29;i:430;i:30;i:432;i:31;i:470;i:32;i:463;i:33;i:415;i:34;i:449;i:35;i:255;i:36;i:311;i:37;i:419;i:38;i:383;i:39;i:394;i:40;i:250;i:41;i:469;i:42;i:438;i:43;i:475;i:44;i:423;i:45;i:45;i:46;i:398;i:47;i:459;i:48;i:358;i:49;i:408;i:50;i:395;i:51;i:417;i:52;i:452;i:53;i:471;i:54;i:206;i:55;i:10;i:56;i:317;i:57;i:379;i:58;i:96;i:59;i:447;i:60;i:388;i:61;i:241;i:62;i:304;i:63;i:233;i:64;i:476;i:65;i:462;i:66;i:479;i:67;i:439;i:68;i:478;i:69;i:412;i:70;i:481;i:71;i:451;i:72;i:425;i:73;i:473;i:74;i:272;i:75;i:464;i:76;i:99;i:77;i:460;i:78;i:67;i:79;i:314;i:80;i:421;i:81;i:2;i:82;i:343;i:83;i:416;i:84;i:387;i:85;i:82;i:86;i:461;i:87;i:413;i:88;i:468;i:89;i:445;i:90;i:420;i:91;i:346;i:92;i:454;i:93;i:466;}s:4:"view";a:0:{}}s:9:"auditores";a:2:{s:3:"sql";a:94:{i:0;i:309;i:1;i:467;i:2;i:229;i:3;i:405;i:4;i:406;i:5;i:443;i:6;i:448;i:7;i:247;i:8;i:246;i:9;i:435;i:10;i:254;i:11;i:455;i:12;i:194;i:13;i:190;i:14;i:113;i:15;i:221;i:16;i:1;i:17;i:456;i:18;i:446;i:19;i:205;i:20;i:163;i:21;i:480;i:22;i:440;i:23;i:232;i:24;i:322;i:25;i:326;i:26;i:331;i:27;i:428;i:28;i:429;i:29;i:430;i:30;i:432;i:31;i:470;i:32;i:463;i:33;i:415;i:34;i:449;i:35;i:255;i:36;i:311;i:37;i:419;i:38;i:383;i:39;i:394;i:40;i:250;i:41;i:469;i:42;i:438;i:43;i:475;i:44;i:423;i:45;i:45;i:46;i:398;i:47;i:459;i:48;i:358;i:49;i:408;i:50;i:395;i:51;i:417;i:52;i:452;i:53;i:471;i:54;i:206;i:55;i:10;i:56;i:317;i:57;i:379;i:58;i:96;i:59;i:447;i:60;i:388;i:61;i:241;i:62;i:304;i:63;i:233;i:64;i:476;i:65;i:462;i:66;i:479;i:67;i:439;i:68;i:478;i:69;i:412;i:70;i:481;i:71;i:451;i:72;i:425;i:73;i:473;i:74;i:272;i:75;i:464;i:76;i:99;i:77;i:460;i:78;i:67;i:79;i:314;i:80;i:421;i:81;i:2;i:82;i:343;i:83;i:416;i:84;i:387;i:85;i:82;i:86;i:461;i:87;i:413;i:88;i:468;i:89;i:445;i:90;i:420;i:91;i:346;i:92;i:454;i:93;i:466;}s:4:"view";a:0:{}}s:12:"listas_tipos";a:2:{s:4:"view";LISTAs:3:"sql";LISTA}s:11:"agenda_tipo";AGENDA_TIPOs:6:"status";STATUS}',
}


def serializar_lista_php(lista):
    itens = []

    for i, valor in enumerate(lista):
        valor = str(valor)
        itens.append(f'i:{i};s:{len(valor)}:"{valor}";')

    return f'a:{len(lista)}:{{' + ''.join(itens) + '}'

lista_de_status = [10]
lista_de_clientes = [83, 268, 328]
lista_de_listas = [2,7]
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


