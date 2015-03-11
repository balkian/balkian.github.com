Sharing dotfiles
################
:date: 2015-04-10 17:47:00 
:tags: github, git, dotfiles

Today's post is half a quick note, half public shaming. In other words, it is a reminder to be very careful with OAuth tokens and passwords.

As part of moving to emacs, I starting using the incredibly useful `gh.el <https://github.com/defunkt/gist.el>`_.
When you first use it, the extension saves either your password or an OAuth token in your .gitconfig file.
This is cool and convenient, unless you `happen to be publishing your .gitconfig file in a public repo <https://github.com/balkian/dotfiles>`_.

So, how can you still share your gitconfig without sharing your password/token with the rest of the world?
Since Git 1.7.0, you can `include other files in your gitconfig <http://stackoverflow.com/questions/1557183/is-it-possible-to-include-a-file-in-your-gitconfig>`_.

.. code-block:: config 
    
    [include]
        path = ~/.gitconfig_secret

And now, in your .gitconfig_secret file, you just have to add this:

.. code-block:: config 
    
    [github]
        user = balkian 
        token = "< Your secret token >" 
