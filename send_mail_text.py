#coding=utf-8

"""
@varsion: ??
@author: 张帅男
@file: send_mail_text.py    以文件形式发送
@time: 2018/1/15 17:02
"""
import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header

mailto_list = [
    'zhangshuainan@tbkt.cn',
]

smtpserver = 'smtp.exmail.qq.com'  # 设置网易163服务器
username = 'zhangshuainan@tbkt.cn'  # 用户名
password = 'ZSN1993zsn'  # 口令
sender = 'zhangshuainan@tbkt.cn'

subject = '孤独者的自白'

msg_text = '你好！ 没有理想的人不伤心!'

msg = MIMEText(msg_text, _charset='utf-8')
msg['Subject'] = Header(subject, 'utf-8')
msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')  # 定义发送时间（不定义的可能有的邮件客户端会不显示发送时间）
msg['To'] = ",".join(mailto_list)

smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(username, password)
smtp.sendmail(sender, mailto_list, msg.as_string())
smtp.quit()
