import requests  # for the url request


def data_fetcher(pincode, date):
    url = f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={pincode}&date={date}'
    print(url)  # remove this
    data = requests.get(url)
    if data.status_code == 200:  # which means connection is established
        center = data.json()[
            'centers']  # loaded the ceneters to the center variable
        if (center):  # TO check centers are available or not if no send else
            for num in center:
                for session in num['sessions']:
                    if (session['available_capacity_dose1']
                            or session['available_capacity_dose2']):
                        msg = '\nDATE: ' + session['date'] + '\nHOSTIPAL NAME: ' + num[
                            'name'] + '\nADDRESS: ' + num[
                                'address'] + '\nAGE LIMIT: ' + str(
                                    session['min_age_limit']
                                ) + '\nPRICE: ' + num[
                                    'fee_type'] + '\nNAME OF THE VACCINE: ' + session[
                                        'vaccine'] + '\nDOSE 1 COUNTS: ' + str(
                                            session['available_capacity_dose1']
                                        ) + '\nDOSE 2 COUNTS: ' + str(
                                            session['available_capacity_dose2']
                                        )
                        print(msg)

        else:
            print('RIGHT NOW NO CENTERS ARE AVAILABLE TO SHOW')


pincode = 574201
date = '27-06-21'
data_fetcher(pincode, date)
