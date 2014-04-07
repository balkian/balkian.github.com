---
layout: post
title:  "Updating EuroLoveMap"
date:   2014-03-27 14:00:00
tags: javascript python heroku
---

As part of the [OpeNER hackathon](http://www.opener-project.org/2013/07/18/opener-hackathon-in-amsterdam/) we decided to build a prototype that would allow us to compare how different countries feel about several topics.
We used the OpeNER pipeline to get the sentiment from a set of newspaper articles we gathered from media in several languages.
Then we aggregated those articles by category and country (using the source of the article or the language it was written in), obtaining the "overall feeling" of each country about each topic.
Then, we used some fancy JavaScript to make sense out of the raw information.

It didn't go too bad, it turns out [we won](http://eurosentiment.eu/wp-content/uploads/2013/07/BOLv9qnCIAAJEek.jpg).

Now, it was time for a face-lift.
I used this opportunity to play with new technologies and improve it:

* Using Flask, this time using python 3.3 and Bootstrap 3.0
* Cool HTML5+JS cards (thanks to [pastetophone](http://pastetophone.com))
* Automatic generation of fake personal data to test the interface
* Obfuscation of personal emails

Publishing a Python 3 app on Heroku
-----------------------------------

[seen here](http://eurolovemap.herokuapp.com/)

``` bash
mkvirtualenv -p /usr/bin/python3.3 eurolovemap
```

Since Heroku uses python 2.7 by default, we have to tell it which version we want, although it supports python 3.4 as well.
I couldn't get python 3.4 working using the [deadsnakes](https://launchpad.net/~fkrull/+archive/deadsnakes) ppa, so I used python 3.3 instead, which works fine but is not officially supported.
Just create a file named *runtime.txt* in your project root, with the python version you want to use:

```
python-3.3.1
```

Don't forget to freeze your dependencies so Heroku can install them:
{% highlight bash %}
pip freze > requirements.txt
{% endhighlight %}

Publishing personal emails
--------------------------
There are really sophisticated and effective ways to obfuscate personal emails so that spammers cannot easily grab yours.
However, this time I needed something really simple to hide our emails from the simplest form of crawlers.
Most of the team are in academia somehow, so in the end all our emails are available in sites like Google Scholar.
Anyway, nobody likes getting spammed so I settled for a custom [Caesar cipher](http://en.wikipedia.org/wiki/Caesar_cipher).
Please, don't use it for any serious application if you are concerned about being spammed.

{% highlight python %}
def blur_email(email):
    return "".join([chr(ord(i)+5) for i in email])
{% endhighlight %}

And this is the client side:

{% highlight javascript %}
window.onload = function(){
     elems = document.getElementsByClassName('profile-email');
     for(var e in elems){
        var blur = elems[e].innerHTML;
        var email = "";
        for(var s in blur){
            var a = blur.charCodeAt(s)
            email = email+String.fromCharCode(a-5);
        }
        elems[e].innerHTML = email;
     }
}
{% endhighlight %}

Unfortunately, this approach does not hide your email from anyone using [PhantomJS](http://phantomjs.org/), [ZombieJS](http://zombie.labnotes.org/) or similar.
For that, other approaches like generating a picture with the address would be necessary.
Nevertheless, it is overkill for a really simple ad-hoc application with custom formatting and just a bunch of emails that would easily be grabbed manually.

Generation of fake data
-----------------------
To test the contact section of the site, I wanted to populate it with fake data.
[Fake-Factory](https://github.com/joke2k/faker) is an amazing library that can generate fake data of almost any kind: emails, association names, acronyms...
It even lets you localise the results (get Spanish names, for instance) and generate factories for certain classes (à la Django).

But I also wanted pictures, enter [Lorem Pixel](http://lorempixel.com/).
With its API you can generate pictures of almost any size, for different topics (e.g. nightlife, people) and with a custom text.
You can even use an index, so it will always show the same picture.

For instance, the picture below is served through Lorem Pixel.

![This picture is generated with LoremIpsum](http://lorempixel.com/400/200/nightlife/)

By the way, if you only want cat pictures, take a look at [Placekitten](http://placekitten.com/).
And for NSFW text, there's the [Samuel L. Jackson Ipsum](http://slipsum.com/)
