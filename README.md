# 앤서블 인벤토리 자동 생성
## 목적
- 앤서블 인벤토리 작성 시, 폐쇄망에 위치한 수백개에 달하는 서버를 입력하는데 필요한 공수를 줄이기 위함
- 엑셀 파일에 서버 리스트를 입력하면 해당 파일을 읽어들여 인벤토리에 자동 입력

## Requirements
- Python 2.x 이상
- Pandas
- openpyxl

## 사용법(인터넷망)
```bash
$ git clone https://github.com/dev-kimdoyoung/make_ansible_inventory/
$ python main.py
```

## 사용법(폐쇄망)
```bash
$ git clone https://github.com/dev-kimdoyoung/make_ansible_inventory/
```
#### 1. 인터넷망에서 아래 명령어 입력 (whl 파일로 해당 패키지 다운로드 받아줌)
```bash
$ pip download -d [다운받을 디렉토리] [패키지명]
```
#### 2. 폐쇄망으로 해당 whl 파일 옮기기
#### 3. 폐쇄망에서 아래 명령어로 패키지 설치
```bash
pip install --no-index --find-links=[패키지가 저장된 디렉토리 명] [패키지명]
```
#### 4. 설치된 패키지 리스트 확인
```bash
$ pip list

```
#### 5. 파일 실행
```bash
$ python main.py
```

## 작성자
dev-kimdoyoung@github.com
