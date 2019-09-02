# 1. docopt

출처: docopt.org

## 1.1. 명칭

- program's name: `naval_fate`
- sub commands: `ship`, `new`, `move`
- options: `-h`, `--help`, `--speed=<kn>`
- positional arguments: `<name>`, `<x>`, `<y>`
- brackets: `[ ]` : optional
- parent: `( )` : required
- pipes: `|` : mutually exclusive
- ellipsis: `...` : repeating

## 1.2. 예시
```
Usage: my_program
```
```
Usage:
    my_program command --option <argument>
    my_program [<optional-argument>]
    my program --another-option=<with-argument>
    my program (--either-that-option | <or-this-argument>)
    my_program <repeating-argument> <repeating-argument>...
```
- `Usage:` 다음의 첫 단어는 프로그램 이름

## 1.3. options

- short option은 스택이 가능 `-abc` 은 `-a -b -c` 과 같다
- short option과 argument 사이의 `space`는 optional 이다
    - `-f FILE`
    - `-fFILE`
        - 스택 short option과 헷갈림
        - option에 대한 description 이 있을 경우에만 option argument으로 해석
- long option의 argument 넣는 방법은 `=` 이랑 `space` 가 같다
    - `--input=ARG`
    - `--input ARG`
        - 하지만 ARG 가 option argument 인지 positional argument 인지 헷갈림
        - option에 대한 description이 있을 경우에만 option argument으로 해석

## 1.4. brackets

- optional elements

```
Usage: my_program [command --option <argument>]
```
is equivalent to
```
Usage: my_program [command] [--option] [<argument>]
```

- required elements

```
Usage: my_program (--either-this <and-that> | <or-this>)
```

`either-this <and-that>`을 하나로 묶음

둘 중 하나는 required

```
Usage: my_program [(<one-argument> <another-argument>)]
```

0 or 2 arguments

만약 하나의 argument 가 있으면 다른 하나는 required

## 1.5. 개행
```
Usage: my_program run [--fast]
       my_program jump [--high]
```
is equivalent to
```
Usage: my_program (run [--fast] | jump [--high])
```

## 1.6. ellipsis "..."

argument 혹은 group of arguments 가 한번 이상 반복 가능

```
Usage: my_program open <file>...
       my_program move (<from> <to>)...
```

```
Usage: my_program [<file>]...
```

0 개 이상

```
Usage: my_program <file>...
```

1개 이상

```
Usage: my_program <file> <file>...
```

2개 이상

## 1.7. [options], option description

정의할 때 모든 옵션을 나열하는 것을 방지함

```
Usage: my_program [options] <path>

--all               List everything.
--long              Long output.
--human-readable    Display in human-readable format.
```

is equivalent to

```
Usage: my_program [--all --long --human-readable] <path>

--all               List everything.
--long              Long output.
--human-readable    Display in human-readable format.
```

short option 도 제공될 경우

```
Usage: my_program [-alh] <path>

-a, --all               List everything.
-l, --long              Long output.
-h, --human-readable    Display in human-readable format.
```

## 1.8. [--]

CONVENTION: 
`[--]` 가 단독으로 쓰이면 options 와 positional argument 구분자 역할

```
Usage: my_program [options] [--] <file>...
```

이런 경우 외에는 `--`를 normal command 로 사용할 수 잇음

- `(--)` : `--`를 필수로 사용

## 1.8. [-]

CONVENTION: `[-]` 가 단독으로 쓰이면 파일이 아닌 *stdin* 프로세스를 해야한다는 의미

그 외에 `-` 를 아무런 의미로 사용 가능

## 1.9. option descriptions

`-` 혹은 `--` 으로 시작하는 줄은 option description 임

`Options:` 태그 하위에 정의해도 됨

### 기능들
- 어떤 short option 과 long option 이 같은 의지인지 정의
- option 이 같고있는 argument 정의
- option 의 dafault 값 정의

```
-o FILE --output=FILE
-i <file>, --input <file>
```
argument는 `UPPER-CASE` 아니면 `<angular-brackets>` 으로 표시

옵션 사이에 comma 는 자유

```
-q          Quit.
-o FILE     Output file.
--stdout    Use stdout.
```
2 개 이상의 공백을 두고 description 표시

```
--coefficient=K     The K coefficient [default: 2.95]
```
디폴트 값은 description 끝에 정의