import smtplib
# import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

import os

def setCredentials(email_login: str, email_pass: str):
    global EMAIL_LOGIN, EMAIL_PASS
    EMAIL_LOGIN = email_login
    EMAIL_PASS = email_pass

def sendToSupport(to:str = "", message:str = ""):
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_LOGIN # type: ignore
        msg['To'] = ', '.join(to)
        msg['Subject'] = f"Bot - Resposta Automática" 

        msg.attach(MIMEText(message, 'plain', 'utf-8'))
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(EMAIL_LOGIN, EMAIL_PASS) # type: ignore
            smtp.send_message(msg)
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")

def sendMsg(to:str = "", cc_emails:str = "", message=""):
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_LOGIN # type: ignore
        msg['To'] = to
        msg['Cc'] = cc_emails
        msg['Subject'] = f"Bot - Resposta Automática" 

        msg.attach(MIMEText(message, 'plain', 'utf-8'))
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(EMAIL_LOGIN, EMAIL_PASS) # type: ignore
            smtp.send_message(msg)

    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")

def sendWithFile(to: str, cc_emails: str = "", subject ="Resposta Automatica", file='path', trying:int = 3):
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_LOGIN # type: ignore
        msg['To'] = to
        msg['Cc'] = cc_emails
        msg['Subject'] = subject

        if (trying <= 0):
            return sendMsg(to, cc_emails, "Você atingiu o limite de tentativas para enviar o e-mail. Por favor, tente novamente mais tarde.")

        msg.attach(MIMEText("Segue em anexo os dados solicitados.", 'plain', 'utf-8'))
        if os.path.exists(file):
            filename = os.path.basename(file)
            attachment = open(file, "rb") 

            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())

            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f"attachment; filename= {filename}")

            msg.attach(part)
            attachment.close()
        else:
            sendToSupport(cc_emails, f"Aviso: Arquivo de anexo não encontrado.")
            return
        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.login(EMAIL_LOGIN, EMAIL_PASS) # type: ignore
                smtp.send_message(msg)
        except smtplib.SMTPServerDisconnected as e:
            print(f"Erro ao enviar e-mail: {e}")
            if trying > 0:
                print(f"Tentando novamente... ({trying} tentativas restantes)")
                return sendWithFile(to, cc_emails, subject, file, trying - 1)
            else:
                sendToSupport(cc_emails, "Erro ao enviar e-mail -> Except -> SMTPServerDisconnected \n" + str(e))
                sendMsg(to, cc_emails, "Ocorreu um erro ao enviar o e-mail. Por favor, tente novamente mais tarde.")
        except smtplib.SMTPException as e:
            print(f"Erro ao enviar e-mail: {e}")
            if trying > 0:
                print(f"Tentando novamente... ({trying} tentativas restantes)")
                return sendWithFile(to, cc_emails, subject, file, trying - 1)
            else:
                sendToSupport(cc_emails, "Erro ao enviar e-mail -> Except -> SMTPException \n" + str(e))
                sendMsg(to, cc_emails, "Ocorreu um erro ao enviar o e-mail. Por favor, tente novamente mais tarde.")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")
        sendToSupport(cc_emails, "Erro ao enviar e-mail -> Except -> Exception \n" + str(e))

