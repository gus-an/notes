
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

## PUSH
(다른 가지를 발행하려면 master를 원하는 가지 이름으로 바꿔주세요.) 
```
git push origin master
```

## REMOTE
만약 기존에 있던 원격 저장소를 복제한 것이 아니라면,
원격 서버의 주소를 git에게 알려줘야 해요.
```
git remote add origin <원격 서버 주소>
```

## MERGE
```
git checkout master
git merge submit
```
master 브랜치에서 submit 에 대한 내용들 가져오기

Git Merge 해서 act1 에 있었던 내용들을 가져왔다
```
git push origin master
```
머지해서 remote 에 푸시해도, 애초에 commit 하지 않은 파일들을 remote 에 반영되지 않는다.

## delete branch
수정내용 여부 확인
```
git checkout submit
git status
```
추가할 것 있으면 하기
```
git add -A
git commit -m "added all"
```
다른 브랜치에서 머지
```
git checkout master
git merge submit
```
브랜치 삭제
```
git branch -d submit
```

## delete remote branch
```
git push origin :submit 
```