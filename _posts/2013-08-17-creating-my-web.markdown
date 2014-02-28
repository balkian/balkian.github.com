---
layout: post
title:  "Creating my web"
date:   2013-08-22 14:14:22
tags: starters javascript ruby github git 
---

Finally, I've decided to finally set up a decent personal page. I have settled for github-pages because I like the idea of keeping my site in a repository and having someone else host it and deploy it for me. The site will be really simple, mostly static files, but [Jekyll](http://jekyllrb.com) creates the static pages for the posts automatically every time I commit anything new to the repository.

Jekyll can be used independently, so if I ever choose to host the site myself, I can do it quite easily. Another thing that I liked about this approach is that the generated html files can be used in the future, and I will not need Jekyll to serve it. Jekyll is really simple and most of the things are written in plain html. Everything could be easily reused if I ever choose to change to another blogging framework.

I hadn't played with HTML and CSS for a while now, so I also wanted to use this site as a playground for the capabilities of HTML5. At some point, I realised I was doing mostly everything in plain HTML and CSS, and decided to keep it like that for as long as possible. As of this writing, I haven't included any Javascript code in the page. Probably I will use some to add my [gists](http://gist.github.com/balkian) and [repositories](http://github.com/balkian), but we will see about that.

I think the code speaks for itself, so you can check out [my repository on Github](http://github.com/balkian/balkian.github.com). You can clone and deploy it easily like this:

{% highlight bash linenos %}
git clone https://github.com/balkian/balkian.github.com
cd balkian.github.com
jekyll serve -w
{% endhighlight %}

I will keep updating this post with information about:
 * Some Jekyll plugins that might be useful
 * What CSS tricks I learnt
 * The webfonts I used
 * The badge on the left side of the page
