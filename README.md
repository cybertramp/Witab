# Witab
WiFi based multitab with raspberrypi project

라즈베리파이를 이용한 와이파이 기반 멀티탭 프로젝트입니다.

**내용**

- /backup

    - rc.local

        /etc/rc.local의 파일
        부팅시 와이파이 설정과 파이썬 스크립트를 자동으로 실행합니다.

- /webserver

    - static

        정적파일들이 존재하는 폴더

        - menu.css

    - templates

        동적파일들이 존재하는 폴더

        - index.html
        - time.html
        - stat.html

    - witab.py

        flask 파이썬 스크립트 파일



**사용한 재료**

- RaspberryPi 3B
- 4channel Relay
- 6port mulititab
- 0.96 OLED SSD1306



**적용된 기술**

- Python
- Flask
- Linux



**업데이트 내역**

- v1 업데이트