# import os
# import smtplib
# import ssl
# from email import encoders
# from email.mime.base import MIMEBase
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from dataConfig import config
#
#
# def send_mail():
#     #
#     subject = "Daily Report"
#     body = "This is report with attachment sent from QATeam"
#     sender_email = config.sender_email
#     password = config.sender_password
#     receiver_email = config.receiver_email
#
#     # Create a multipart message and set headers
#     message = MIMEMultipart()
#     message["From"] = sender_email
#     message["To"] = receiver_email  # 寄給單人
#     message["Subject"] = subject
#     # message["To"] = ','.join(receiver_email) #寄給多人
#     # message["Bcc"] = ','.join(receiver_email)  # Recommended for mass emails
#
#     # Add body to email
#     message.attach(MIMEText(body, "plain"))
#
#     # filename = r"D:\GM Automation\gpk.api.test\test_reports"  # In same directory as script
#     filename = r"./test_reports"
#
#     lists = os.listdir(filename)  # 获得文件夹内所有文件
#     lists.sort(key=lambda fn: os.path.getmtime(filename + '\\' + fn))  # 排序
#     # print('new file is : ' + lists[-1])  # 最新的文件名
#
#     filename = os.path.join(filename, lists[-1])
#
#     # Open PDF file in binary mode
#     with open(filename, "rb") as attachment:
#         # Add file as application/octet-stream
#         # Email client can usually download this automatically as attachment
#         part = MIMEBase("application", "octet-stream")
#         part.set_payload(attachment.read())
#
#     # Encode file in ASCII characters to send by email
#     encoders.encode_base64(part)
#
#     # Add header as key/value pair to attachment part
#     part.add_header(
#         "Content-Disposition",
#         f"attachment; filename= {lists[-1]}",
#     )
#
#     # Add attachment to message and convert message to string
#     message.attach(part)
#     text = message.as_string()
#
#     # Log in to server using secure context and send email
#     context = ssl.create_default_context()
#     with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
#         server.login(sender_email, password)
#         server.sendmail(sender_email, receiver_email, text)
