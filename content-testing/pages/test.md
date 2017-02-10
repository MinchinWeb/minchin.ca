title: Pelican Thoughts
modified: March 31, 2014
copy_date: 2014
slug: test
status: hidden
status: draft

# Links don't work yet

<{filename}/index.md>

<{filename}\index.md>

<{filename}index.md>

<{filename}../index.md>

<{filename}..\index.md>

<../index.md>

these generate links, but none of them work


[1]({filename}/index.md)
[2]({filename}\index.md)
[4]({filename}../index.md)
[5]({filename}..\index.md)
[6](../index.md)
[7]({{SITEURL}})
[11]({filename}../design/www.metrofinancialplanning.com/index.html)

<www.minchin.ca/index.html> - this one is completely missing!

{filename}

{{SITEURL}}

# Links that do work

[To Minchin.ca](http://www.minchin.ca/index.html)
[3]({filename}index.md)
[8]({filename}20projects.md)
[9]({filename}./index.md)
[10]({filename}../images/240_bot.gif)
<http://www.minchin.ca/index.html>

# New Markdown Phraser for Notepad++

Needed...

# LESS Phraser for Notepad++

Needed...

# Documentation Upgrades

- list of available header metadata
- interpage links that work
     - interpage links need to point to the source file, not the output
	 location of the page.
- difference between two `conf` files
