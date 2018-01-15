#coding=utf-8

"""
@varsion: ??
@author: 张帅男
@file: send_mail1.py    以html形式发送
@time: 2018/1/15 16:37
"""

# coding: utf-8
import sys, traceback

reload(sys)
sys.setdefaultencoding('utf-8')

import time
import smtplib
from email.mime.text import MIMEText

mailto_list = [
    'zhangshuainan@tbkt.cn',
]

mail_host = 'smtp.163.com'  # 设置网易163服务器
mail_user = '15294627382@163.com'  # 用户名
mail_pass = 'ZSN1993zsn'  # 口令
sender = '15294627382@163.com'

content_title = '''<table width="100%%" border="1" cellspacing="0"  >
  <tr>
    <td align="center">项目编号</td>
    <td align="center">项目名称</td>
    <td align="center">参考值</td>
    <td align="center">当前值</td>
    <td align="center">症状</td>
  </tr>
'''
content_title_user_format = '''<table width="100%%" border="1" cellspacing="0"  >
  <tr>
    <td align="center">%s</td>
    <td align="center">%s</td>

  </tr>
'''


# ----------------------------------------------------------------------
def send_email(data_list):
    """"""
    data_format = '''  <tr>
    <td align="center">%s</td>
    <td align="center">%s</td>
    <td align="center">%s</td>
    <td align="center">%s</td>
    <td align="center"><font color='red'>%s</font></td>
    </tr>'''

    data_format_user = '''  <tr>
    <td align="center"><font color='blue'>%s</font></td>
    <td align="center"><font color='blue'>%s</font></td>
    </tr>'''

    content = content_title
    for each_data in data_list:

        content_title_user = ""
        if each_data[0] != 18:
            content += data_format % each_data
        else:
            each_data_status = each_data[4]
            # print "email 18:",each_data_status

            each_data_status = str(each_data_status).strip().split("\n")
            content += data_format % (each_data[0], each_data[1], each_data[2], each_data[3], each_data_status[0])
            # -------------------------->生成用户报表<-------------------------------
            each_data_status.pop(0)

            each_data_status.pop(0)
            # -------------------------->用户名----前12小时测试IP总量<-------------------------------
            title = each_data_status.pop(0)
            title = title.strip().split("----")

            content_title_user = content_title_user_format % tuple(title)

            for i in each_data_status:
                i = i.strip().split("----")
                content_title_user += data_format_user % tuple(i)
            content_title_user += "</table>"

    content += "</table><br/><br/>"
    content += content_title_user

    msg = MIMEText(content, _subtype='html', _charset='utf8')
    msg['Subject'] = u'Geo监控预警'
    msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')  # 定义发送时间（不定义的可能有的邮件客户端会不显示发送时间）
    msg['To'] = ",".join(mailto_list)

    try:
        server = smtplib.SMTP()
        server.connect(mail_host)
        ##server = smtplib.SMTP(mail_host)
        # server = smtplib.SMTP_SSL(mail_host, 25)
        server.login(mail_user, mail_pass)
        server.sendmail(sender, mailto_list, msg.as_string())  # mail to list recipient
    except Exception, e:  # try中有异常则执行
        print 'Mail passed unsuccessfully!\n'
        traceback.print_exc()
    else:  # try中没有异常则执行
        print 'Mail passed successfully!'
    finally:  # try中有无异常都执行
        server.close()


if __name__ == '__main__':
    data_list = [(18L, u'HeNan API', u'\u6b63\u5e38', u'\u6b63\u5e38',
                  u'\u6b63\u5e38\n\u5728\u7ebf\u7528\u6237\u7edf\u8ba1:\n\u7528\u6237\u540d----\u524d12\u5c0f\u65f6\u6d4b\u8bd5IP\u603b\u91cf\nINFO HeNan----44\nTEST Yong----29\nWorkface----13\nNeustar TEST----19')]

    send_email(data_list)
