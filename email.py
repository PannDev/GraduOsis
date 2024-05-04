import smtplib
import pandas as pd
from email.message import EmailMessage
from email.mime.text import MIMEText
from helper.getTicket import getTicket
from helper.getDB import getDB
import time

smtp_server = "smtp.gmail.com"
smtp_port = 465
email = ""
password = ""

kelas = [f"XII MIPA {i} Belajar ID" for i in range(1,9)] + [f"XII IPS {i} Belajar ID" for i in range(1, 5)]
server = smtplib.SMTP_SSL(smtp_server, smtp_port)
server.login(email, password)
message = EmailMessage()
message["Subject"] = "E-Ticket Bumandhala SMANSA Univday 2024"
message["From"] = "SMANSA Univday 2024"
for kls in kelas:
    df = getDB(f'assets/csvfile/{kls}.csv', kls)
    try:
        file = getTicket(kls)
        for index, row in df.iterrows():
            # if row.Nama == 'Ade Ayu Elvalina Cristin Manalu':
            #     row.email = 'adeayu826@gmail.com'
                message_to_send = f"""\
                Hi, Sobat Bumandhala 🫅🏻<span style="color:red;"><b>&#8252;</b></span><br>
                {row.Nama}, you are invited to <b>𝑻𝒓𝒚 𝑶𝒖𝒕</b> TOBK SNBT and <b>𝑴𝒂𝒊𝒏 𝑬𝒗𝒆𝒏𝒕</b> 'Bumandhala' Smansa Univday 2024.<br><br>

                E-Ticket ini bisa sobat gunakan saat pengerjaan Try Out yang akan dilaksanakan pada hari <b>𝐒𝐚𝐛𝐭𝐮</b>, 20 <b>𝐉𝐚𝐧𝐮𝐚𝐫𝐢</b> 2024. Selain itu, e-ticket juga akan digunakan saat Main Event yang akan diselenggarakan pada hari <b>𝐒𝐚𝐛𝐭𝐮</b>, 27 𝐉𝐚𝐧𝐮𝐚𝐫𝐢 2024. <br>

                Nantinya, Sobat Bumandhala wajib menunjukkan e-ticket kepada Panitia Smansa Univday 2024 sebagai bukti kehadiran saat Try Out dan Main Event. <br>
                Tentunya tidak lupa, setelah penukaran e-ticket ini, Sobat Bumandhala akan mendapatkan konsumsi dari Panitia Smansa Univday 2024.<br><br>

                So, keep it safely and enjoy the event :) !<br>
                See you, Sobat Bumandhala! 👋🏻<br><br>

                ———————————<br>
                Narahubung <br>
                👤: 082218709191 (Nilam Selapandan) <br>
                👤: 0895392152737 (Muhammad Fathur Rizky) <br>
                👤: 088218098425 (Putri Fanisha) <br><br>

                #SmansaUnivday2024<br>
                #BumandhalaSmansaUnivday2024<br>
                @smansa.univday<br>
                <a href='{file.get(str(index + 1)+'.png')}'>E-Ticket SMANSA Univday 2024 {row.Nama}</a>
                """
                message["To"] = row.email
                print(f"{row.Nama}[{index+1}] -> {row.email} ", end="")
                msg = MIMEText(message_to_send, 'html')
                message.set_content(msg)
                # print(f"{row.Nama}[{index+1}] -> {file.get(str(index + 1)+'.png')}")
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