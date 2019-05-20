# Prep 사용법

### 설치
```
$ python -m venv venv # 가상환경 만듬
$ source venv/bin/activate # 가상환경 활성화
$ ./build.sh # build스크립트 실행
$ ls dist # build 확인
prep-0.0.1-py3-none-any.whl
$ pip install dist/prep-0.0.1-py3-none-any.whl # 설치

```
설치하고 나면, prep이라는 커맨드를 사용하여 P-rep을 등록 또는 삭제할 수 있다.
제공하는 명령어는 register, unregister 두가지이며 사용법은 다음과 같다.

## 명령어 사용법
## Prep 등록 : 
```
$ prep register -k [키스토어경로] -p [키스토어 비밀번호(옵셔널)] -j [참조할 json경로] -u [노드url(기본값: http:localhost:9000/api/v3)]
```

- register 명령 예
```bash
$ prep register -k keystore_file.json -p password123 -j prep.json -u http://nodeurl
```

Prep register 명령어를 실행하기 위해선 keystore파일과 json파일이 추가적으로 필요하다(prep 정보가 있는 json파일, prep의 public-key는 keystore file로 추출하기 때문에 생략한다.)
- json file example
```
{
	"url": "target://123.123.123.123:9000",
	"name": "ABCD"
	...
}
```

## Prep 사퇴 : 
```
$ prep unregister -k [키스토어경로] -p [키스토어 비밀번호(옵셔널)]  -u [노드url(기본값: http:localhost:9000/api/v3)]
```

- unregister 명령 예
```bash
$ prep unregister -k keystore_file.json -p password123
```

Prep unregister 명령어를 실행하기 위해선 키스토어 파일만 있으면 된다.
