---
layout: default
title: Posts
---

<div class="posts">
  <h1>Posting</h1>
  <ul>
    {% for post in site.posts %}
      {% if post.categories contains 'posting' %}
        <li><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></li>
      {% endif %}
    {% endfor %}
  </ul>
</div>  