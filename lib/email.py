from email.message import EmailMessage
import smtplib
import ssl

def my_function_email(pass_email,init_hour,process):
    user = "efloran1408@gmail.com"
    remitente = "IRL - Procesos <efloran1408@gmail.com>"
    destinatario = "eflorian@utp.edu.pe"
    mensaje = f""" El proceso  de Migracion apolo13-irl {process} :  {init_hour} . """
   

    email = EmailMessage()
    email["From"] = remitente
    email["To"] = destinatario
    email["Subject"] = "IRL - Proceso 01"
    email.set_content(mensaje)
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as smtp:
        smtp.login(user, "ypwz mnwg qixx mykc")
        smtp.sendmail(remitente, destinatario, email.as_string())
        smtp.quit()
    
    return 0