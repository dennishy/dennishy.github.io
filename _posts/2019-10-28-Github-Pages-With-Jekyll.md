---
layout: post
title: "Github Pages with Jekyll"
date: 2019-10-26 12:00:00 -0000
categories: GITHUB 
---

*This* is a github page. Github offers a free website per account called Github Pages that allows you to host your site within a repository. It's a pretty neat way to deliver content quickly using markdown and templates, especially with Jekyll. In this post I'll be including notes that I've found helpful during my time with Github Pages. 


## Issue: Could not locate Gemfile or .bundle/directory
Unfortunately, Jekyll can be a bit confusing to install thanks to the age-old issue of version conflicts and dependancy issues. The crux of the matter is that [jekyll](https://jekyllrb.com/docs/) has moved on to V4.0.0 while Github-Pages is dependent on V3.8.5 [see dependancies here:](https://pages.github.com/versions/)

A version mismatch will lead to the error: 'Could not locate Gemfile or .bundle/ directory' 

If the correct versions of ruby, jekyll, and bundler have been installed and an error remains, confirm that a jekyll site has been started with 'jekyll new' on the root node of your repo. Note: the repo name must be identical to your github username

Lastly, confirm that the ruby path has been added to your shell config (so for those on zsh be sure to look in .zshrc)

## Issue: Github Pages show images locally but not published
If you've ever had your images work on your editor but fail when you push your changes, it may be due to the tags you're using, your configuration, or both. 

in the _config.yml file, confirm that the value for 'url' is set to your page and note that it is not a quoted value.

{% highlight console %}
url = https://dennishy.github.io
{% endhighlight %}

When you go to add images, use the syntax:
{% highlight console %}
<img src="{{site.url}}/assets/YOURIMAGEHERE" style="display: block; margin: auto;" />
{% endhighlight %}

replacing '/assets/YOURIMAGEHERE' with the filepath to your own images folder. The syntax is case sensitve and this syntax assumes your asset/images folder is at the root level of your repo. 

## Tip: Highlighting Syntax
Jekyll offers a number of highlighting options for different programming languages and environments. The keywords are fairly intuitive and have additional alises, just keep in mind the string must be all lower case. To find the complete list of keywords, look at the documentation for [rouge ruby](https://github.com/rouge-ruby/rouge/wiki/List-of-supported-languages-and-lexers).

A few quick ones: 

1. For python scripts use  'python' alias: 'py' 

2. Terminal sessions use 'console' alias: 'terminal', 'shell_session', 'shell-session'

3. YAML and XML use 'yaml' and 'xml' respectively

## Posts not showing
(Edited 6/11/2020)

Posts need a certain format to be reflected in pages. The typical format is 'YYYY-MM-DD-[post_title]' and the dash between the date and title is critical. Pages won't post any .md files on your github page if there is an underscore '_' instead of the dash '-'. 