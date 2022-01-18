import requests
import random
kn = 0
nk = 0

print('  Tool Check user telegram :\n  programmer kabos\n  Have Fun ')
print('- - - - -')
k = '2021068735'
t = '2086501602:AAHWXZ1yNZKXU1DDf7dX6X8RjzbiXZbPAwc'
message = requests.get("https://api.telegram.org/bot"+str(t)+"/sendMessage?chat_id="+str(k)+"&text= ⌔ New Start! ").json()
id_msg = str(message['result']["message_id"])
print('- '*9)
oh = 'qwertyuiopasdfghjklzxcvbnm0987654321'
op = 'qwertyuiopasdfghjklzxcvbnm0987654321'
while True :
    ok = str("".join(random.choice(oh)for i in range(1)))
    on = str("".join(random.choice(op)for i in range(1)))
    os = ok+on+ ok+on+ on
    oa = requests.get(f'https://t.me/{os}').text
    if 'tgme_username_link' in oa:
        print(f'\r [{kn}] : DonE  ')
        kn+=1
        tb = f'https://api.telegram.org/bot{t}/sendMessage?chat_id={k}&text= ⌔ 𝚔𝚎𝚛𝚘𝚘 < @{os} >'
        i = requests.post(tb)
    else:
        print(f'\r [{nk}] : ErooR  ')
        nk+=1
        requests.post(f"""https://api.telegram.org/bot{t}/editmessagetext?chat_id={k}&message_id={id_msg}&text= ⌔ Checking in progress .
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
⌔ user : {os} :
⌔️ available {kn} :
⌔ unavailable {nk} :
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉.""")