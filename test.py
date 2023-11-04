import requests
import time

def make_request(stringThing):
    cookies = {
        'b': 'da0bcb444093d1c4fc58ef2174619c0c',
        '_gcl_au': '1.1.1023467609.1692676420',
        '_rdt_uuid': '1692676420544.26a5c1fd-1512-40b7-8393-1a046b09afa3',
        'ssb_instance_id': '5dd3488b-9b2c-4418-9fd3-ca3dcefa5804',
        'shown_ssb_redirect_page': '1',
        '_gid': 'GA1.2.1639687074.1697789375',
        '_cs_c': '0',
        'PageCount': '1',
        'lc': '1697790066',
        'utm': '%7B%22utm_source%22%3A%22in-prod%22%2C%22utm_medium%22%3A%22inprod-customize_link-slack_menu-click%22%7D',
        '_cs_cvars': '%7B%221%22%3A%5B%22Visitor%20ID%22%2C%22da0bcb444093d1c4fc58ef2174619c0c%22%5D%2C%223%22%3A%5B%22URL%20Path%22%2C%22%2Fintl%2Fen-au%2Fhelp%2Farticles%2F360003534892-Browse-people-and-user-groups-in-Slack%22%5D%2C%224%22%3A%5B%22Visitor%20Type%22%2C%22prospect%22%5D%7D',
        '_ga': 'GA1.1.298679714.1692676421',
        'OptanonConsent': 'isGpcEnabled=0&datestamp=Fri+Oct+20+2023+19%3A30%3A32+GMT%2B1100+(Australian+Eastern+Daylight+Time)&version=202211.1.0&isIABGlobal=false&hosts=&consentId=28267c16-99a3-40d2-9db1-c8fe2fca4da0&interactionCount=1&landingPath=NotLandingPage&groups=1%3A1%2C3%3A1%2C2%3A1%2C4%3A0&AwaitingReconsent=false',
        'shown_download_ssb_modal': '1',
        'show_download_ssb_banner': '1',
        'no_download_ssb_banner': '1',
        'tz': '660',
        '_cs_id': 'b8e26233-f5ae-a458-9aa9-ed647ac7528f.1692676420.5.1697792358.1697792358.1.1726840420581',
        '_ga_QTJQME5M5D': 'GS1.1.1697789375.5.1.1697792359.59.0.0',
        'x': 'da0bcb444093d1c4fc58ef2174619c0c.1697796451',
        'd': 'xoxd-O8K96gVgYqhamJxi%2BWLK%2BJ%2BB8By28w9YXYV19k%2BagkjdgXvlTRAhHvT3toS1s2DC1TVh4aKS49ui0%2B1XNM9Yv9a3O9w%2BHkKW0WPiIu%2BMNCOI%2BlxzFatu3n2nWahB6Thm8EZt9dY0gS18UAo2MqbQ0VyWfB%2FXb6XwZvw8CmB6FrvG5e6KFnWmAnrOICkjA1xUYxjR6NU7uGo%3D',
        'd-s': '1697796717',
    }

    headers = {
        'authority': 'ourvoiceproject.slack.com',
        'accept': '*/*',
        'accept-language': 'en-AU,en-US;q=0.9,en-GB;q=0.8,en;q=0.7',
        'content-type': 'multipart/form-data; boundary=----WebKitFormBoundarywn9As4ExQuS51VoA',
        # 'cookie': 'b=da0bcb444093d1c4fc58ef2174619c0c; _gcl_au=1.1.1023467609.1692676420; _rdt_uuid=1692676420544.26a5c1fd-1512-40b7-8393-1a046b09afa3; ssb_instance_id=5dd3488b-9b2c-4418-9fd3-ca3dcefa5804; shown_ssb_redirect_page=1; _gid=GA1.2.1639687074.1697789375; _cs_c=0; PageCount=1; lc=1697790066; utm=%7B%22utm_source%22%3A%22in-prod%22%2C%22utm_medium%22%3A%22inprod-customize_link-slack_menu-click%22%7D; _cs_cvars=%7B%221%22%3A%5B%22Visitor%20ID%22%2C%22da0bcb444093d1c4fc58ef2174619c0c%22%5D%2C%223%22%3A%5B%22URL%20Path%22%2C%22%2Fintl%2Fen-au%2Fhelp%2Farticles%2F360003534892-Browse-people-and-user-groups-in-Slack%22%5D%2C%224%22%3A%5B%22Visitor%20Type%22%2C%22prospect%22%5D%7D; _ga=GA1.1.298679714.1692676421; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Oct+20+2023+19%3A30%3A32+GMT%2B1100+(Australian+Eastern+Daylight+Time)&version=202211.1.0&isIABGlobal=false&hosts=&consentId=28267c16-99a3-40d2-9db1-c8fe2fca4da0&interactionCount=1&landingPath=NotLandingPage&groups=1%3A1%2C3%3A1%2C2%3A1%2C4%3A0&AwaitingReconsent=false; shown_download_ssb_modal=1; show_download_ssb_banner=1; no_download_ssb_banner=1; tz=660; _cs_id=b8e26233-f5ae-a458-9aa9-ed647ac7528f.1692676420.5.1697792358.1697792358.1.1726840420581; _ga_QTJQME5M5D=GS1.1.1697789375.5.1.1697792359.59.0.0; x=da0bcb444093d1c4fc58ef2174619c0c.1697796451; d=xoxd-O8K96gVgYqhamJxi%2BWLK%2BJ%2BB8By28w9YXYV19k%2BagkjdgXvlTRAhHvT3toS1s2DC1TVh4aKS49ui0%2B1XNM9Yv9a3O9w%2BHkKW0WPiIu%2BMNCOI%2BlxzFatu3n2nWahB6Thm8EZt9dY0gS18UAo2MqbQ0VyWfB%2FXb6XwZvw8CmB6FrvG5e6KFnWmAnrOICkjA1xUYxjR6NU7uGo%3D; d-s=1697796717',
        'dnt': '1',
        'origin': 'https://app.slack.com',
        'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    }

    params = {
        '_x_id': '84b4dd5f-1697796722.086',
        '_x_csid': 'FjH_5MiDkDI',
        'slack_route': 'T05LCGLNHLN',
        '_x_version_ts': '1697793447',
        '_x_frontend_build_type': 'current',
        '_x_desktop_ia': '4',
        '_x_gantry': 'true',
        'fp': 'fa',
    }

    data = f'------WebKitFormBoundarywn9As4ExQuS51VoA\r\nContent-Disposition: form-data; name="token"\r\n\r\nxoxc-5692564765702-5722936452144-6063071937366-73cb9a080a995baaa065e0c0328d9f8979618f9570e22b40628faf937bfd95d1\r\n------WebKitFormBoundarywn9As4ExQuS51VoA\r\nContent-Disposition: form-data; name="channel"\r\n\r\nC05LK38783D\r\n------WebKitFormBoundarywn9As4ExQuS51VoA\r\nContent-Disposition: form-data; name="limit"\r\n\r\n28\r\n------WebKitFormBoundarywn9As4ExQuS51VoA\r\nContent-Disposition: form-data; name="ignore_replies"\r\n\r\ntrue\r\n------WebKitFormBoundarywn9As4ExQuS51VoA\r\nContent-Disposition: form-data; name="include_pin_count"\r\n\r\ntrue\r\n------WebKitFormBoundarywn9As4ExQuS51VoA\r\nContent-Disposition: form-data; name="inclusive"\r\n\r\ntrue\r\n------WebKitFormBoundarywn9As4ExQuS51VoA\r\nContent-Disposition: form-data; name="no_user_profile"\r\n\r\ntrue\r\n------WebKitFormBoundarywn9As4ExQuS51VoA\r\nContent-Disposition: form-data; name="include_stories"\r\n\r\ntrue\r\n------WebKitFormBoundarywn9As4ExQuS51VoA\r\nContent-Disposition: form-data; name="oldest"\r\n\r\n{stringThing}\r\n------WebKitFormBoundarywn9As4ExQuS51VoA\r\nContent-Disposition: form-data; name="_x_reason"\r\n\r\nmessage-pane/requestHistory\r\n------WebKitFormBoundarywn9As4ExQuS51VoA\r\nContent-Disposition: form-data; name="_x_mode"\r\n\r\nonline\r\n------WebKitFormBoundarywn9As4ExQuS51VoA\r\nContent-Disposition: form-data; name="_x_sonic"\r\n\r\ntrue\r\n------WebKitFormBoundarywn9As4ExQuS51VoA\r\nContent-Disposition: form-data; name="_x_app_name"\r\n\r\nclient\r\n------WebKitFormBoundarywn9As4ExQuS51VoA--\r\n'

    response = requests.post(
        'https://ourvoiceproject.slack.com/api/conversations.history',
        params=params,
        cookies=cookies,
        headers=headers,
        data=data,
    )
    return response.text,response.status_code

def write_file(string,i):
    with open(f'{i}.txt', 'w') as file:
        file.write(string)

i = 0   
start = 1697777014.764309 
while (True):
    i += 1
    start = start - 50000
    response,status_code = make_request(start)
    time.sleep(1)
    write_file(response,i)
    print(i)
    

