import requests, phpserialize, json, re

cookies = {
    'PHPSESSID': 'daba0e1be39bb71a9a78c861036778ac',
    '_ga': 'GA1.1.2083834248.1781280005',
    '_ga_KQTSMYDQKY': 'GS2.1.s1781466345$o1$g0$t1781466345$j60$l0$h0',
    '_ga_7D5FCHK8QD': 'GS2.1.s1781620699$o7$g1$t1781627461$j30$l0$h0',
    'token_name': '21ba8c452eb8ff95cfe2970f7f8250407ed32e88dd5920a5e54669c742c8f4378009fac421ba8c452eb8ff95cfe2970f7f8250407ed32e88dd5920a5e54669c742c8f4378009fac4',
    'token_value': '6b682b4f6f14948c60f5b2dd4f9f6ef07e46f1c1ba3c83cf1318dda45c71f27d3a0243746b682b4f6f14948c60f5b2dd4f9f6ef07e46f1c1ba3c83cf1318dda45c71f27d3a024374',
    '1989d206329b0bd437e1a7531': '3254bc59d58a743ffa470839ff792dccfab29b17110dda09c0c91ed7573a0b0759b4140e383dbc59d58a743ffa470839ff792dccfab29b17110dda09c0c91ed7573a0b0759b4140e383d',
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
cliente = "083"
data_ini = "08/06/2026"
data_fim = "14/06/2026"
agenda_tipon = "1"
statusn = "5"
data = {
    'DT_POST': 'a:7:{s:7:"periodo";a:5:{s:8:"criterio";s:1:"1";s:6:"exibir";s:1:"2";s:7:"ultimos";s:1:"7";s:3:"ini";s:10:"08/06/2026";s:3:"fim";s:10:"14/06/2026";}s:8:"clientes";a:2:{s:4:"view";a:1:{i:0;s:3:"262";}s:3:"sql";a:1:{i:0;s:3:"262";}}s:12:"responsaveis";a:2:{s:3:"sql";a:94:{i:0;i:309;i:1;i:467;i:2;i:229;i:3;i:405;i:4;i:406;i:5;i:443;i:6;i:448;i:7;i:247;i:8;i:246;i:9;i:435;i:10;i:254;i:11;i:455;i:12;i:194;i:13;i:190;i:14;i:113;i:15;i:221;i:16;i:1;i:17;i:456;i:18;i:446;i:19;i:205;i:20;i:163;i:21;i:440;i:22;i:232;i:23;i:322;i:24;i:326;i:25;i:331;i:26;i:428;i:27;i:429;i:28;i:430;i:29;i:432;i:30;i:470;i:31;i:463;i:32;i:415;i:33;i:449;i:34;i:255;i:35;i:311;i:36;i:419;i:37;i:383;i:38;i:394;i:39;i:250;i:40;i:469;i:41;i:438;i:42;i:475;i:43;i:423;i:44;i:45;i:45;i:398;i:46;i:459;i:47;i:358;i:48;i:408;i:49;i:395;i:50;i:417;i:51;i:452;i:52;i:471;i:53;i:206;i:54;i:10;i:55;i:317;i:56;i:379;i:57;i:96;i:58;i:447;i:59;i:388;i:60;i:241;i:61;i:304;i:62;i:233;i:63;i:476;i:64;i:462;i:65;i:479;i:66;i:439;i:67;i:478;i:68;i:412;i:69;i:465;i:70;i:451;i:71;i:425;i:72;i:473;i:73;i:272;i:74;i:464;i:75;i:99;i:76;i:460;i:77;i:67;i:78;i:314;i:79;i:421;i:80;i:2;i:81;i:343;i:82;i:416;i:83;i:387;i:84;i:82;i:85;i:461;i:86;i:413;i:87;i:468;i:88;i:445;i:89;i:320;i:90;i:420;i:91;i:346;i:92;i:454;i:93;i:466;}s:4:"view";a:0:{}}s:9:"auditores";a:2:{s:3:"sql";a:94:{i:0;i:309;i:1;i:467;i:2;i:229;i:3;i:405;i:4;i:406;i:5;i:443;i:6;i:448;i:7;i:247;i:8;i:246;i:9;i:435;i:10;i:254;i:11;i:455;i:12;i:194;i:13;i:190;i:14;i:113;i:15;i:221;i:16;i:1;i:17;i:456;i:18;i:446;i:19;i:205;i:20;i:163;i:21;i:440;i:22;i:232;i:23;i:322;i:24;i:326;i:25;i:331;i:26;i:428;i:27;i:429;i:28;i:430;i:29;i:432;i:30;i:470;i:31;i:463;i:32;i:415;i:33;i:449;i:34;i:255;i:35;i:311;i:36;i:419;i:37;i:383;i:38;i:394;i:39;i:250;i:40;i:469;i:41;i:438;i:42;i:475;i:43;i:423;i:44;i:45;i:45;i:398;i:46;i:459;i:47;i:358;i:48;i:408;i:49;i:395;i:50;i:417;i:51;i:452;i:52;i:471;i:53;i:206;i:54;i:10;i:55;i:317;i:56;i:379;i:57;i:96;i:58;i:447;i:59;i:388;i:60;i:241;i:61;i:304;i:62;i:233;i:63;i:476;i:64;i:462;i:65;i:479;i:66;i:439;i:67;i:478;i:68;i:412;i:69;i:465;i:70;i:451;i:71;i:425;i:72;i:473;i:73;i:272;i:74;i:464;i:75;i:99;i:76;i:460;i:77;i:67;i:78;i:314;i:79;i:421;i:80;i:2;i:81;i:343;i:82;i:416;i:83;i:387;i:84;i:82;i:85;i:461;i:86;i:413;i:87;i:468;i:88;i:445;i:89;i:320;i:90;i:420;i:91;i:346;i:92;i:454;i:93;i:466;}s:4:"view";a:0:{}}s:12:"listas_tipos";a:2:{s:4:"view";a:1:{i:0;s:1:"2";}s:3:"sql";a:1:{i:0;s:1:"2";}}s:11:"agenda_tipo";a:1:{i:0;s:1:"AGENDA_TIPOV";}s:6:"status";a:1:{i:0;s:1:"STATUSV";}}',
}

data['DT_POST']=data['DT_POST'].replace("08/06/2026", data_ini)
data['DT_POST']=data['DT_POST'].replace("14/06/2026", data_fim)
data['DT_POST']=data['DT_POST'].replace('"262"', f'"{cliente}"')
data['DT_POST']=data['DT_POST'].replace('"AGENDA_TIPOV"', f'"{agenda_tipon}"')
data['DT_POST']=data['DT_POST'].replace('"STATUSV"', f'"{statusn}"')


response = requests.post('https://adm.zukk.in/dt-agenda-zgo', cookies=cookies, headers=headers, data=data)

dados = phpserialize.loads(
    data['DT_POST'].encode(),
    decode_strings=True
)

resposta = response.json()



lista_agendas = []
agendas = {}

for agenda in resposta["data"]:

    agenda_id = agenda["DT_RowId"].replace("row_", "")
    # Dia da semana
    dia_semana = re.search(
        r'<span class="size10">(.*?)</span>',
        agenda["0"]["show"]
    ).group(1)

    # Data
    data = re.search(
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
        r'btn btn-success btn-sm size12">(.*?)</button>',
        agenda["6"]["show"]
    ).group(1)

    pesquisa = {
        "dia_semana": dia_semana,
        "data": data,
        "cliente_info": cliente_info,
        "pesquisa": pesquisanome,
        "status": status
    }
    
    agendas[agenda_id] = {
        "data": data,
        "dia_semana": dia_semana,
        "pesquisanome" : pesquisanome,
        "nome_pesquisa" : cliente_info,
        "status": status
    }


    lista_agendas.append(pesquisa)  
    


print(json.dumps(agendas, indent=4, ensure_ascii=False))
    #lista_agendas.append(pesquisa)







#print(json.dumps(lista_agendas, indent=4, ensure_ascii=False))

#print(response.text)


