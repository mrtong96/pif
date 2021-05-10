# PIF (politician index fund)

### links

* doc: https://docs.google.com/document/d/1wQMsRnNDKjZF4n9tTS-SjrIXSISYOlHtGk3iBDKqzms/edit

### people

* Michael Tong (mrtong96)
* Amber Yeh
* Katrina Chen

### How to push (to github)

* Disclaimer:
    * If you work in a real job, you do not push directly to master. This is because this is a small project and we value iteration speed over production stability.
    * If your code is broken, please fix it whenever you can. If you look at how we designed this thing, it's meant to be relatively tolerant towards individual notebook failures anyways so it's not really that big of a deal.

* Clone the repo
```
# make some folder somewhere.
$ git clone https://github.com/mrtong96/pif.git
$ cd pif
$ git checkout origin master
```

* Make sure you you have the latest version of the branch
```
$ git checkout origin master
$ git pull origin master
```

* Try pushing your code
```
$ git add *
$ git commit -m 'your important git message here, definitely never use sarcasm in these messages. I definitely never use sarcasm here'
$ git push
```

* If the command fails for whatever reason:
    * Read the error message. git is nice because it not only tells you why it's failing but it also tells you a recommended command to fix it.
```
# usually merging works
$ git merge
$ git push
```
* If you really can't get it to work, ask Michael Tong
