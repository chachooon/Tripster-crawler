
## 도커컴포즈 설정 가이드
> 원본 프로젝트 : https://github.com/raccoonyy/django-sample-for-docker-compose

클론받은 폴더 경로로 가서 실행합니다 

#### 시작하기
```
$ docker-compose up
```
 * docker-compose.yml 내용에 떄라 이미지를 빌드하고 서비스를 실행한다.
 * -d : 서비스 실행 후 콘솔로 빠져 나온다.
 * --force-recreate : 컨테이너를 지우고 새로 만든다.
 * --build : 서비스 시작전 이미지를 새로 만든다.
 
#### 실행중인 서비스 보기
```
$ docker-compose ps 
```
#### 서비스 멈추기/재시작하기
```
$ docker-compose stop/start 
```
#### 서비스 지우기
```
$ docker-compose down
```
* 서비스를 지우면서 컨테이너와 네트워크도 삭제한다.
* --volume : 볼륨까지 삭제한다.
