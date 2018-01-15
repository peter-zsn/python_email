#coding=utf-8

"""
@varsion: ??
@author: 张帅男
@file: send_mail_html1.py
@time: 2018/1/15 17:36
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


content_title = '''<table width="100%%" border="1" cellspacing="0"  >
  <tr>
    <td align="center">名字</td>
    <td align="center">性别</td>
    <td align="center">年龄</td>
  </tr>
'''


data_format = '''  <tr>
<td align="center">%s</td>
<td align="center">%s</td>
<td align="center"><font color='red'>%s</font></td>
</tr>'''



data_list = [('小李', '男', '25'), ('小李1', '男', '25'), ('小李2', '男', '25')]


content = content_title
for obj in data_list:
    content += data_format % obj

content += "</table><br/><br/>"

subject = '孤独者的自白'

print content
msg = MIMEText(content, _subtype='html', _charset='utf-8')
msg['Subject'] = Header(subject, 'utf-8')
msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')  # 定义发送时间（不定义的可能有的邮件客户端会不显示发送时间）
msg['To'] = ",".join(mailto_list)

smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(username, password)
smtp.sendmail(sender, mailto_list, msg.as_string())
smtp.quit()
