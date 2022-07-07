# smtp 서버 (= 우체국)
import smtplib
# mime : 메일에 대한 메시지 데이터
from email.mime.text import MIMEText  # MIMEText :편지지 느낌


sendEmail = "구글ID@gmail.com"
recvEmail = "받는 이메일"
password = "구글 비밀번호"

# 발신 메일 서버
smtpName = "smtp.gmail.com" # smtp 서버 주소
smtpPort = 587 # smtp TLS 포트 번호

text = "메일 내용"
msg = MIMEText(text) # 정석 코드 : MIMEText(text , _charset = "utf8")

msg['Subject'] ="이것은 메일제목"
msg['From'] = sendEmail
msg['To'] = recvEmail
print(msg.as_string()) # 문자열로 변환

s=smtplib.SMTP(smtpName, smtpPort) # 메일 서버 연결 (서버명, 포트명)
s.starttls() #TLS 보안 처리
s.login(sendEmail, password) #로그인
s.sendmail(sendEmail, recvEmail, msg.as_string()) # (발신자, 수신자, 메일정보)
                        # 메일 전송, 문자열로 변환해야 합니다.
s.close() # smtp 서버 연결을 종료합니다.
