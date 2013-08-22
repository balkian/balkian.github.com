---
layout: post
title:  "Remove git files with globbing"
date:   2013-08-22 23:14:00
tags: git 
---
A simple trick. If you want to remove all the '.swp' files from a git repository, just use:
{% highlight bash %}
git rm --cached '\*\*.swp'
{% endhighlight %}
