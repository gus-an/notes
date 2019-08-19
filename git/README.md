
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

## COMMIT
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

## ADD
stages modifications and deletions, without new files
```
git add -u
```
stages new files and modifications, without deletions
```
git add .
```
new/modified/deleted files in the current directory

stages all changes

git add .; git add -u 와 동일
```
git add -A
```


## file-glob 패턴
```
git rm log/\*.log
```

## git mv
`git mv README.txt README`는 아래 코드와 완전히 같음
```
mv RED README.txt README
git rm README.txt
git add README
```
