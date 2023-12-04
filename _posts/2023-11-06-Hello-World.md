---
layout: post
title: 블로그 제작 과정
categories: posting
---

## 1. Github 저장소 생성
###  본인의 Github 계정에 접속하여 
```sh
 사용자(계정)이름.github.io 
```
### 과 같은 형식으로 저장소를 생성합니다.
### (아래 설명 부터는 편의상 제 사용자이름으로 설명하겠습니다.)


## 2. Jekyll / Visual Studio Code 설치 및 사이트 생성

#### [Visual Studio Code 설치 사이트](https://code.visualstudio.com/)
#### [Ruby 설치 사이트(x86 버전으로 설치)](https://rubyinstaller.org/)
### jekyll을 설치하기 이전에 Ruby와 Visual Studio Code를 먼저 설치 해주고,
### 윈도우 시작 메뉴를 켜보면 있는 Start Command Prompt with Ruby를 실행한 후
``` 
gem install jekyll bundler
```
### 라는 명령어를 입력해 jekyll 과 bundler를 설치해줍니다.
### 이후에 
```
jekyll new jwnamid.github.io
```
### 라는 명령어로 새로운 jekyll 사이트를 생성해주면 됩니다.

## 3. 사이트와 Github 연동
### 위에서 설치한 Visual Studio Code를 실행한 뒤, 
### File -> Open Folder에서 위에서 생성한 jekyll 사이트 디렉토리를 선택해주고
### 터미널을 Git Bash로 설정해줍니다.
### 이후 
```
git init
```
### 을 통해 Git을 초기화 해주고
```
git remote add origin https://github.com/jwnamid/jwnamid.github.io.git
```
### 과 같은 명령어를 입력해서 로컬저장소와 Github를 연동시켜줍니다.
### 이후에 수정사항을 적용할 땐 
```
git add .
git commit -m '(수정 사항 적어주기)'
git push -u origin main
```
### 와 같은 과정으로 통해서 Github로 push 해주면 됩니다.

## 4. 테마 적용
[Jekyll Themes](http://jekyllthemes.org/)
### Jekyll Themes 사이트에 들어가면 다양한 블로그 테마들이 있습니다.
### 그 중 자신의 마음에 드는 테마를 선택하여 적용해주면 됩니다.
### 테마를 가져오는 방법은 2가지가 있습니다.
### 1. Gem으로 제공되는 테마
**Gemfile에 테마 추가**  
    파일 목록 중`Gemfile`에 다음과 같은 명령어를 작성하여 테마를 추가합니다.
    
    gem "테마이름"
    
**Bundler로 테마 설치**  
    이후 터미널에서 다음 명령어를 실행하여 테마를 설치해줍니다.
    
    bundle install
    
**_config.yml에 테마 적용**  
    `_config.yml`  파일에 다음과 같이 명령어를 작성해서 테마를 적용해줍니다.
    
    theme: 테마이름
    
### 2. 직접 다운로드하여 적용
테마의 GitHub 저장소에서 초록색**Code** 버튼을 눌러보면 보이는
 **Download ZIP**을 클릭하여 테마 파일을 다운로드합니다.
 
이후에 압축을 풀고, 폴더 안에 있는 모든 파일을 복사하여 기존 Jekyll 프로젝트 디렉토리로 복사해주면 됩니다.
### 마지막으로 테마마다 조금씩 수정해줘야 하는 사항들이 있습니다.  테마에 있는 설명 문서 또는 README파일을 보면 자세하게 설명이 되어있기 때문에, 그에 맞춰서 수정해주면 됩니다.


## 5. 블로그 꾸미기
### 파일 중 _config.yml 라는 이름의 파일이 있는데 이곳에서 블로그를 수정할 수 있습니다. 제 파일을 예로 들면
```
# Name of your site (displayed in the header)
name: jwnamid
```
### 블로그 상단의 이름을 설정할 수 있고,

```
# Short bio or description (displayed in the header)
description: Study
```
### 블로그에 대한 설명도 추가할 수 있습니다.

```
# URL of your avatar or profile pic (you could use your GitHub profile pic)
avatar: https://raw.githubusercontent.com/barryclark/jekyll-now/master/images/jekyll-logo.png
```
### 본인의 아바타도 원하는 사진으로 변경할 수 있습니다.
```

# Flags below are optional

# Includes an icon in the footer for each username you enter
footer-links:
  dribbble:
  email:
  facebook:
  flickr:
  github: barryclark/jekyll-now
  instagram:
  linkedin:
  pinterest:
  rss: # just type anything here for a working RSS icon
  twitter: jekyllrb
  stackoverflow: # your stackoverflow profile, e.g. "users/50476/bart-kiers"
  youtube: # channel/<your_long_string> or user/<user-name>
  googleplus: # anything in your profile username that comes after plus.google.com/
```
### 이외에도 다음과 같이 본인의 이메일 주소나 SNS 계정 주소, Github주소까지 전부 작성하여 원하는 대로 블로그를 꾸밀 수 있습니다.
