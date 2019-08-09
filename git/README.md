
# Git 명령어

## DIFF
staged 된것 과 추가 수정된 것과의 차이
```
git diff
```
commit 된것과 staged 된것의 차이
```
git diff --staged
```

## SHOW
staged 된 파일의 내용을 보여줌
```
git show :filename
```

## ADD
`commit` 하기 전에 `add` 명령을 수행해준다
```
git commit -a -m 'added new stuffs'
```

## RM
그냥 `rm` 도 실행하고, staged 상태로 만든다
```
git rm
```
파일을 지우지 않고 staged 상태 제거 
```
git rm -r --cached .
```

