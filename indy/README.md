Notes about Indy Project
================
목차
- [Indy-SDK](#I-Indy-SDK)
 - [1. ]
# Indy-SDK

## 1. 환경 구성

Ubuntu 18.04.3 LTS 버젼에서 실행하였다

### 1.1. Rust 설치
 
1. `~/.cargo/bin` 디렉토리에 `rustc`, `rustup`, `cargo` 설치
- ```
  curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
  ```

2. 환경변수 설정
- ```
  source ~/.cargo/env
  ```

### 1.2. 네이티브 library 및 utitily 설치

1. [optional] 미러 사이트 변경
- ```
  sudo vi /etc/apt/sources.list
  ```
- 모든 `deb` 사이트를 `http://mirror.kakao.com/ubuntu/` 로 변경 후 저장
- ```
  sudo apt-get update
  ```
2. `apt-get install` 이용한 설치
- ```
  sudo apt-get install -y \
  build-essential \
  pkg-config \
  cmake \
  libssl-dev \
  libsqlite3-dev \
  libzmq3-dev \
  libncursesw5-dev
  ```
3. `libindy` 는 `1.0.14` 버젼의 `libsodium`을 요구하지만, Ubuntu 16.04 는 `apt` 레포에서 이를 지원하지 않는다. Ubuntu 18.04는 모르겟지만, 다음과 같이 따로 설치한다. 권한 문제로 `sudo` 를 추가해줬다.
- ```
  cd /tmp && \
  curl https://download.libsodium.org/libsodium/releases/old/unsupported/libsodium-1.0.14.tar.gz | tar -xz && \
  cd /tmp/libsodium-1.0.14 && \
  ./configure --disable-shared && \
  make && \
  sudo make install && \
  rm -rf /tmp/libsodium-1.0.14
  ```

- 설치 완료한것 같아서 `apt list --installed | grep libso` 해본 결과 .. 1.0.16-2 가 발견된다.

### 1.3. `libindy` 빌드

- ```
  cd ~/github.com
  git clone https://github.com/hyperledger/indy-sdk.git
  cd ./indy-sdk/libindy
  cargo build
  cd ..
  ```

### 1.4. test
- ```
  cd libindy
  RUST_TEST_THREADS=1 cargo test
  ```
- 엄청 오래 걸리고, `test high_cases::` 부터 쭉 실패한다. 중도 포기

### 1.5. APT 를 이용한 설치
- 사실 여기까지는 source 를 이용한 설치라고 한다. 다음과 같이 apt 를 받을 수 있다. (Ubuntu 16.04 and 18.04)
- ```
  sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys CE7709D068DB5E88
  sudo add-apt-repository "deb https://repo.sovrin.org/sdk/deb (xenial|bionic) {release channel}"
  sudo apt-get update
  sudo apt-get install -y {library}
  ```
    - {library} 는 `libindy`, `libnullpay`, `libvcx`, `indy-cli` 중 선택
    - (xenial|bionic) Ubuntu 16.04 아니면 18.04
    - {release channel} `master`, `rc` release candidates `stable` 중 선택
- 이런 방식으로 설치하니, 기존에 `apt list --installed | grep indy` 로 찾지 못했던 `libindy` 패키지가 발견된다.

 ## 2. 실행

 ### 2.1. indy-sdk/docs/getting-started

 - ```
   docker-compose up
   ```
- 온갖 설치를 하면서 메시지를 몇개 던진다. `pip upgrade` 해야하는 문구와 `apt-utils`를 설치해야하는 문구가 눈에 띈다.
 

- `docker-compose.yml` 를 살펴보면, 2개의 컨테이너가 뜬다.
    1. indy-pool -> getting start 말고 직접 띄워볼 수 있겠다.
    2. jupyter -> python 코드로 대체할 수 있겠다.
