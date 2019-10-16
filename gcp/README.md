GCP
====================

# 1. SSH 설정

## 1.1. 부팅시 스크립트 파일 실행하여 ssh 키 등록

cron : 자동실행 내장 툴

```
crontab -e
```

```
@reboot /home/jinwoo_gus_an/add_keys.sh
```

add_keys.sh : 스크립트 파일 

```bash
#!/bin/bash
keys_dir="/home/jinwoo_gus_an/.ssh/authorized_keys"
temp_dir="/home/jinwoo_gus_an/.ssh/temp"
touch ${keys_dir}
echo 'ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEA1PHTPoLww83aL5MhvXlnsxdvWudQh++D4Y23nwOfTu2qoBtWvR+B2tzVtYLKDtug1Uupr3WI71fn4ae8T5hBBuy0DeLFJwm4CJLynF3+abwYSpM+4BCYcxhPvFS1SOg1CZOZ5feQL+VHLT0Nt/KliM/0tFg3VeJE20kqKF4Gyx/2DxNAtIUhqGvNPy121jHZ2zWw9z0ad+E+68FDeBt0tz7M1yOkZRpyug7tvRTUdscvMIzH3dfoMYAF++ll/lS/oh7Q+mpkjYQG1M9+qYQUV8SxljJ5spiTV+vqB6h/p8Yoc19JRmfhRBXv0ZV5oWXebOLWxYZ2TZsp0/4Mf+i1ww== rsa-key-20190904' | cat - ${keys_dir} > ${temp_dir} && mv ${temp_dir} ${keys_dir}
echo "ssh keys are added"
```

- 콘솔에서 ssh 창을 키면 활성화 되는것 같음

## 1.2. 정상적인 방법:  GCP 콜솔 이용

- instance 별로 메타데이터 입력도 가능하지만, 
- ssh 키 입력시 마지막 정보에 로그인 아이디 넣는것이 중요
- instance 시작하고 기다리기만 하면 된다

```
ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAtAeUbja/WUo4DWuky6TGFxyrXr5X6V0KTkq7EohipHzMn0cnoJ1F/LGn+vjCPWPM1dZjoIoLyIc0fEPPGzJ7HOCEJVpiddT4xlJ75/T0CpM/1Ula3OVeCtj6obc2qiJqKHsm3PO6bc3Mv/1UlLLGHKNXknSCrOAp47GGMoivhAz8IebAPgWIofWxl2GB4duNRR198f8AR8tiisOCPBJ/WoLa+AUzmRtJ9+U9Ax9DCI6CD1yLW5Q+de6LliRdA/PA+RLMumaQBHN3KJTXNFH2hjFivd2ErV4d93yTcT97dmQhWQ2UcO1wHMy8gwa3qfwqao/ddR2a5BbcXKm25VXoTQ== jinwoo_gus_an
```

