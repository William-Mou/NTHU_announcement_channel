import requests


def send_msg(office, title, link):
    # token depends on each user, should get from db
    # since db not implement, token cannot be init
    token = ''
    msg = f"{office}公告：\n{title}\n{link}"

    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    payload = {'message': msg}
    r = requests.post("https://notify-api.line.me/api/notify", headers=headers,
                      params=payload)
    return r.status_code


def get_status(token):
    pass


def auth(request):
    # get access_token
    # send a welcome message
    # get status
    pass
