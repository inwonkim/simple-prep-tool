# Prep 사용법

## whl파일 설치
pip install prep-0.0.1-py3-none-any.whl

설치하고 나면, t-bears처럼 prep이라는 커맨드를 사용하여 P-rep을 등록 또는 삭제할 수 있다.
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