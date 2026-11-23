# 물품 요청 목록

Python 3.10 이상에서 실행하는 물품 요청 조회 프로그램이다. 추가 패키지는 필요 없다.
이 디렉터리에서 다음 명령을 실행한다.

```console
python app.py list
python app.py search 장갑
python app.py open R-102
python -m unittest discover -s tests -v
```

`open`에는 목록 첫 열에 표시된 요청 번호를 넣는다. 샘플 요청은 메모리에 저장한다.
