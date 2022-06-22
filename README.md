# 유성 피하기

### 아이디어 소개

- 플레이어는 우주선을 타고 유성을 피해 살아남아야한다.
- 미사일을 쏴서 유성을 제거할 수 있다.
- 랜덤하게 등장하는 유성에 맞으면 게임에 패배한다.
- 조이스틱으로 이동하고, 스위치로 미사일을 발사해 살아남자.

### 파일 구조 및 기능

```markdown
main.py
controller.py
```
- `main`: 전역 변수가 선언되어 있으며 gpio와 pygame와 controller 객체를 초기화시킨다.
- `Controller`: 모든 객체를 연결시켜주며 주로 이동을 관리한다.

```markdown
model/
| - joystick.py
|
| - missile.py
| - player.py
| - star.py
|
| - referee.py
```

- `Joystick`: 조이스틱의 입력을 받고 좌표로 변환시켜주는 객체
- `Missile`: 미사일을 생성하고 이동시키는 객체
- `Player`: 플레이어를 생성하고 이동시키는 객체
- `Star`: 유성을 생성하고 이동시키는 객체
- `Referee`: 충돌을 판단하고 게임오버를 판단하는 객체

```markdown
util/
| - factory.py
```
- `Factory`: 팩토리 패턴을 활용
    - 이미지로부터 미사일과 유성을 생성하는 객체
    - 객체의 좌표를 담는 rect객체 역시 생성하는 객체

### 장치 활용

- Joystick: 플레이어를 이동시킬 때 활용한다.
- ADC: Joystick과 Raspberry를 연결시켜준다.
- Switch: 입력할 때 미사일을 쏘는 기능을 한다.

### 기여

- Issue를 생성한다.
- `feature/#{Issue Number}`로 branch를 생성한다.
- 작업 후 `{Tag}: {description} [#{Issue Number}]`의 형식에 맞춰 commit한다.
- `develop` branch로 `Pull request`를 보낸다.

### 시연

- ![시연 영상]()
- [발표 ppt]()

### References

- [References](https://github.com/Cha-Ji/raspberry-term-project/issues/5)
 