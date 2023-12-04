---
layout: post
title: Google Analytics 적용
categories: posting
---

# 1. Google Analytics 계정 설정

[Google Analytics](http://analytics.google.com/analytics/web/#/)

## 1) Google Analytics 사이트에 들어가 로그인을 해준 뒤, 관리 탭으로 이동해서 계정을 생성해줍니다.

## 2) 새 웹사이트에 대한 속성들을 설정해준 뒤에 추적 코드를 받습니다.

  

# 2. Jekyll 블로그에 추척코드 추가
```
# Enter your Disqus shortname (not your username) to enable commenting on posts
# You can find your shortname on the Settings page of your Disqus account
disqus: 

# Enter your Google Analytics web tracking code (e.g. UA-2110908-2) to activate tracking
google_analytics: G-WFE7QRRYJL

# Your website URL (e.g. http://barryclark.github.io or http://www.barryclark.co)
# Used for Sitemap.xml and your RSS feed
url:
```
## 저 같은 경우는 _config.yml 파일에 추적 코드를 바로 넣을 수 있게 되어있습니다.

## 발급 받은 코드를 복사해서 붙여넣기만 해주면 모든 설정이 완료됩니다.
# 3. Google Analytics 사용
 [Google Analytics 대시보드](Google%20Analytics)
## 사이트에 접속하여 좌측 상단에 보고서 탭을 선택 해줍니다.
## 해당 탭에서 다양한 정보를 직접 확인할 수 있습니다.