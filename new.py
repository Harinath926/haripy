import sendgrid

from elasticsearch import Elasticsearch

import time

mail = sendgrid.SendGridAPIClient('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')



esconnector = Elasticsearch(

    "http://10.101.60.86:32315/")

   



message = sendgrid.Mail(

                from_email='harinath.kavuri@perigorddata.com',

                to_emails='anandsadhu@perigorddata.com',

                subject='PM Elastic DB Down',

                html_content='<strong>Elastic DB Down</strong>')



#response = client1.send(message)



while True:

    time.sleep(10)

    try:

        esconnector.info()

        print("Connected")

        continue    

    except:

        print("Error an expectional")

        response = mail.send(message)

    break
