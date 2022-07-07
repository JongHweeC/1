import os  # os 모듈의 시스템 명령어 사용 가능

# os.system('gdrive list')  # gdrive의 list 명령어 실행
        # 최근 30개의 파일 리스트를 불러옴
        # 토큰 파일 삭제시 연동 삭제됨.

# os.system('gdrive mkdir GDRIVE')
    # 만든 폴더의 ID: 1SUlp_yvp_XGUnq2jVp8JDB04K9PX927R

# 업로드
os.system('gdrive upload --parent 1SUlp_yvp_XGUnq2jVp8JDB04K9PX927R translate.txt')
    # 파일명.확장자