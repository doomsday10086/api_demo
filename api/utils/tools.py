import random
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

# 发送邮件
class SendMail(object):

    def __init__(self, code=None, to_addr=None):
        # 初始化
        self.code = code
        self.to_addr = to_addr
        self.from_addr = "18573151260@163.com"
        self.password = "spf1994"
        self.smtp_server = 'smtp.163.com'
        self.msg = self.format_data()

    def format_data(self):
        # 数据处理
        msg = MIMEText("<h2>这是以讽刺测试邮件，验证码如下：</h2>/r/n <h1>{}</h1>".format(self.code), 'html', 'utf-8')
        msg['From'] = u'<%s>' % self.from_addr
        msg['To'] = u'<%s>' % self.to_addr
        msg['Subject'] = "python邮件测试"

        return msg

    def send(self):
        # 发送邮件
        smtp = smtplib.SMTP_SSL('smtp.163.com', 465)
        smtp.set_debuglevel(1)
        smtp.ehlo("smtp.163.com")
        smtp.login(self.from_addr, self.password)
        smtp.sendmail(self.from_addr, [self.to_addr], self.msg.as_string())
        smtp.quit()


def get_verify_code():
    """
    生成验证码
    :return:
    """
    str_list = '0123456789'
    verify_code = ''
    for _ in range(6):
        verify_code += random.choice(str_list)
    return verify_code


if __name__ == '__main__':
    print(get_verify_code())
