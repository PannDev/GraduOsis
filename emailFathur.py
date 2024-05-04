import smtplib
import pandas as pd
from email.message import EmailMessage
from email.mime.text import MIMEText
from helper.getTicket import getTicket #custom lib
from helper.getDB import getDB #custom lib
import time

# import helper.getTicket could not be resolved

smtp_server = "smtp.gmail.com"
smtp_port = 465
email = "workergithub@gmail.com"
password = "browncoffee"

kelas = [f"XII MIPA {i} Belajar ID" for i in range(1,9)] + [f"XII IPS {i} Belajar ID" for i in range(1, 5)]
server = smtplib.SMTP_SSL(smtp_server, smtp_port)
server.login(email, password)
message = EmailMessage()
message["Subject"] = "SMANSA Graduation 2023/2024"
message["From"] = "OSIS/MPK x IC81"
for kls in kelas:
    df = getDB(f'assets/csvfile/{kls}.csv', kls)
    try:
        file = getTicket(kls)
        for index, row in df.iterrows():
            # if row.Nama_Siswa == 'Ade Ayu Elvalina Cristin Manalu':
            #     row.belajarid_email = 'adeayu826@gmail.com'
                message_to_send = f"""\
                    
                @panzelv
                    
                <a href='{file.get(str(index + 1)+'.png')}'>E-Ticket SMANSA Univday 2024 {row.Nama_Siswa}</a>
                """
                
                
                message["To"] = row.belajarid_email
                print(f"{row.Nama_Siswa}[{index+1}] -> {row.belajarid_email} ", end="")
                msg = MIMEText(message_to_send, 'html')
                message.set_content(msg)
                # print(f"{row.Nama_Siswa}[{index+1}] -> {file.get(str(index + 1)+'.png')}")
                try:
                    server.send_message(message)
                    print('[Sent]')
                except Exception as e:
                    print(f'[{e}]')
                del message["To"]
                time.sleep(5)
        print(f"{kls} [Success]")
    except Exception as e:
        print(f"{kls} [{e}]")