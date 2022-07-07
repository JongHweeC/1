# smtp 서버 (= 우체국)
import smtplib
# mime : 메일에 대한 메시지 데이터
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


sendEmail = "구글ID@gmail.com"
recvEmail = "받는 이메일"
password = "구글 비밀번호"

# 발신 메일 서버
smtpName = "smtp.gmail.com" # smtp 서버 주소
smtpPort = 587 # smtp TLS 포트 번호

# 여러 MIME을 넣기위한 MIMEMultipart 객체 생성
msg = MIMEMultipart()

# 본문 추가
text = "이것은 메일 내용"
contentPart = MIMEText(text) #MIMEText(text , _charset = "utf8")
msg.attach(contentPart)
                        # msg 가 택배 상자
                        # contentPart가 편지

# 파일 추가
etcFileName = 'test.txt'  # 파일명 (다른 위치에 있다면 복잡해짐)
with open(etcFileName, 'rb') as etcFD :  # 파일을 바이너리모드로 읽어서
    etcPart = MIMEApplication( etcFD.read() ) # 메일로 보낼 수 있는 마임데이터 생성
    # 첨부파일의 정보를 헤더로 추가
    etcPart.add_header('Content-Disposition','attachment', filename=etcFileName)
    msg.attach(etcPart)

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
