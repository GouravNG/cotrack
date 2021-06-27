import requests  # for the url request
update_id=25538692 #main update id

def data_fetcher(pincode, date, n_date, nn_date):
    url = f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={pincode}&date={date}'
    print(url)  # remove this
    data = requests.get(url)
    if data.status_code == 200:  # which means connection is established
        center = data.json()[
            'centers']  # loaded the ceneters to the center variable
        if (center):    # TO check centers are available or not if no send else
            for num in center:
                for session in num['sessions']:
                    if (session['available_capacity_dose1']
                            or session['available_capacity_dose2']):
                        if (session['date'] == date
                            or session['date'] == n_date
                            or session['date'] == nn_date):
                            #created the output msg which would be send to bot
                            msg = '\nDATE: ' + session['date'] + '\nHOSTIPAL NAME: ' + num['name'] + '\nADDRESS: ' + num['address'] + '\nAGE LIMIT: ' + str(session['min_age_limit']) + '\nPRICE: ' + num['fee_type'] + '\nNAME OF THE VACCINE: ' + session['vaccine'] + '\nDOSE 1 COUNTS: ' + str(session['available_capacity_dose1']) + '\nDOSE 2 COUNTS: ' + str(session['available_capacity_dose2'])
                            print(msg)

        else:
            print('RIGHT NOW NO CENTERS ARE AVAILABLE TO SHOW')

def telegram_recieve():
    global update_id
    timeout=100
    url=f'https://api.telegram.org/bot1644992322:AAEyVpjqwDRY46RniG9degjeoEn5H45y_8Y/getupdates?offset={update_id}&timeout={timeout}'
    print(url) #remove this
    recieved_msg=requests.get(url)
    if recieved_msg.status_code==200:
        data=recieved_msg.json()['result']
        for nums in data:
            msg = (nums['message']['text'])
            unix_tf = (nums['message']['date'])
            chat_id = (nums['message']['from']['id'])
            update_id = (nums['update_id'])
            update_id +=1
            return msg,unix_tf,chat_id,update_id
        
    else:
        print('Problem from telelgram api')

pincode = 574201
date = '27-06-2021'
n_date = '28-06-2021'
nn_date = '29-06-2021'
# data_fetcher(pincode, date, n_date, nn_date)
msg,unix_tf,chat_id,update_id= telegram_recieve()
print(msg,unix_tf,chat_id,update_id)
