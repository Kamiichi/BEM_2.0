import requests

def lineNotify(message):
    try:
        line_notify_token = 'Mg6IqP69Z6JZnpsmjgHd6VX1BmrbtgEuKS1w0X5x33f'
        line_notify_api = 'https://notify-api.line.me/api/notify'
        payload = {'message': message}
        headers = {'Authorization': 'Bearer ' + line_notify_token} 
        requests.post(line_notify_api, data=payload, headers=headers)
    except:
        print("Line通知エラー ５秒後に再通信します")
        time.sleep(5)
        lineNotify(message)