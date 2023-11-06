---

layout: post

title: 댓글 기능 추가 과정

---
# 1. Utterances 설치
[Utterances](https://github.com/apps/utterances)
## Github 앱에서 Utterances를 설치해줍니다.
## 저장소는 본인의 블로그 레포지토리로 설정해주면 됩니다.

# 2. 설정
![](https://github.com/outstanding1301/outstanding1301.github.io/blob/master/imgs/git/2021-01-07-utterances/config-1.png?raw=true)
## 이후 repo는 본인의 레포지토리 주소를 적어주면 됩니다. 저같은 경우 jwnamid/jwnamid.github.io로 설정했습니다.
![](https://github.com/outstanding1301/outstanding1301.github.io/blob/master/imgs/git/2021-01-07-utterances/config-2.png?raw=true)
## 여기선 가장 위에 블로그 글 경로를 이슈의 제목으로 선택해주시면 됩니다.
## 바로 밑에 이슈 라벨과 테마 선택은 본인이 원하는 것으로 선택하시면 됩니다.

```
<!-- Add the Utterances comment section below -->

<div  id="comments">

<script  src="https://utteranc.es/client.js"

repo="jwnamid/jwnamid.github.io"

issue-term="pathname"

label="Comments"

theme="github-light"

crossorigin="anonymous"

async>

</script>

</div>
```
## 마지막으로 해당 코드를 _layout/post.html 경로로 추가해주면 됩니다. 주의할 점은 기본으로 사용하고 있는 disqus와 관련된 코드를 전부 주석으로 처리하고 위의 스크립트를 붙여넣어주시면 됩니다.