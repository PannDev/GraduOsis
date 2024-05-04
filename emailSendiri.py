import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Pengaturan SMTP
smtp_server = 'smtp.gmail.com'
smtp_port = 465  # Ganti port sesuai kebutuhan (587 untuk TLS, 465 untuk SSL)
smtp_username = 'dryhezelnut@gmail.com'
smtp_password = ''

# Pengaturan email
sender_email = 'dryhezelnut@gmail.com'
subject = 'Hai panzelv'
message = 'panndev'

# Fungsi untuk membaca alamat email dan nama file QR dari file CSV
def read_emails_and_qr_filenames_from_csv(csv_file):
    data = []
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Lewati baris header
        for row in reader:
            # row[1] berisi alamat email, row[2] berisi nama file QR
            data.append((row[1], row[2]))
    return data

# Fungsi untuk mengirim email dengan lampiran
def send_email_with_attachment(receiver_email, qr_filename):
    # Membuat objek pesan
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Menambahkan isi pesan
    msg.attach(MIMEText(message, 'plain'))

    # Melampirkan file QR
    qr_filepath = f'assets/qr_code/{qr_filename}'
    with open(qr_filepath, 'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename= {qr_filename}')
    msg.attach(part)

    try:
        # Inisialisasi koneksi SMTP
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Mengaktifkan mode TLS
        server.login(smtp_username, smtp_password)
        
        # Mengirim email
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        
        print(f'Email berhasil dikirim ke {receiver_email}!')
    except Exception as e:
        print(f'Gagal mengirim email ke {receiver_email}: {e}')
    finally:
        # Menutup koneksi
        server.quit()

# Loop untuk mengirim email ke setiap kelas dan nomor
for kelas in ['IPS', 'MIPA']:
    for i in range(1, 5 if kelas == 'IPS' else 9):
        # Membaca alamat email dan nama file QR dari file CSV
        csv_file = f'assets/csvfile/XII {kelas} {i} Belajar ID.csv'
        data = read_emails_and_qr_filenames_from_csv(csv_file)

        for email, qr_filename in data:
            # Menambahkan "_email" ke alamat email
            receiver_email = f'{email}_email'

            # Mengirim email dengan lampiran
            send_email_with_attachment(receiver_email, qr_filename)
