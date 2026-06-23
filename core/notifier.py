import requests

def Notificador(x):

    mensagem = x

    url = "https://defaulta2b115a46fbc44a0a77e5f54840466.06.environment.api.powerplatform.com:443/powerautomate/automations/direct/workflows/8af55b6fc0154ab18f270af6c04d16c4/triggers/manual/paths/invoke?api-version=1&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=U9TtCkAZSQ-PGm-CZCb0_VjS7It-KM4JOX9ZmHdE-Q4"

    payload = {
        "text": mensagem
    }

    r = requests.post(
        url,
        json=payload,
        timeout=30
    )

    print(r.status_code)
    print(r.text)