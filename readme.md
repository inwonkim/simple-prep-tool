# Prep 사용법

### 설치
```
$ python -m venv venv # 가상환경 만듬
$ source venv/bin/activate # 가상환경 활성화
$ ./build.sh # build스크립트 실행
$ ls dist # build 확인
prep-0.0.1-py3-none-any.whl	prep-0.0.1.tar.gz
$ pip install dist/prep-0.0.1-py3-none-any.whl # 설치

```
설치하고 나면, prep이라는 커맨드를 사용하여 P-rep을 등록 또는 삭제할 수 있다.
제공하는 명령어는 register, unregister 두가지이며 사용법은 다음과 같다.

## 명령어 사용법
## Prep 등록 : 
```
register -k [키스토어경로] -p [키스토어 비밀번호(옵셔널)] -j [참조할 json경로] -u [노드url(기본값: http:localhost:9000/api/v3)]
```

Prep register 명령어를 실행하기 위해선 keystore파일과 json파일이 추가적으로 필요하다(prep을 등록하기 위해선, publicKey와 url을 입력해야하기 때문)
- example
```
{
	"publicKey": "0x123~~",
	"url": "prep의 url",
	"name"등 다른 옵셔널한 필드들...
}
```

## Prep 사퇴 : 
```
unregister -k [키스토어경로] -p [키스토어 비밀번호(옵셔널)]  -u [노드url(기본값: http:localhost:9000/api/v3)]
```
Prep unregister 명령어를 실행하기 위해선 키스토어 파일만 있으면 된다.
