# 原来Git真的能写成一本书啊

### Git的安装
略
### 完整流程

- git init
- git remote add origin git@github.com:ronnie14165/learn_git_with_me.git
- git pull origin master
- 操作ing...
- git status
- git add .
- git commit -am "write something"
- git push origin master

### Git的基础配置
#### 选定一处本地地址，新建一文件夹，文件夹内右键“Git Bash Here”

- mkdir learngit
- cd learngit
- pwd	（pwd中不要出现汉字或乱码）
- git config --global user.name "Ronnie Lee"
- git config --global user.email "1416558969@qq.com"
- git config --global user.name			（验证姓名）
- git config --global user.email			（验证邮箱）
- git config --list  				(验证)
- ssh-keygen -t rsa -C "youremail@example.com"	（通过SSH秘钥将远程仓库与本地仓库连接起来）
- ssh -T git@github.com			（验证连接）

- git status 				查看状态
- git log				查看日志文件
- git log --oneline			简洁日志文件


### Git的远程仓库
- git remote
- git remote add origin git@github.com:ronnie14165/learn_git_with_me.git	(命名origin)
- git remote -v

### 由工作区（本地）推送至暂存区
- git add test.py
- git add .

### 由暂存区推送到远程仓库
- git commit -m "Version1.0"

### 由工作区直接推送到远程仓库
- git commit -am "Version 1.10"

### Git的分支

- git branch
- git branch dev
- git branch -d dev				（删除本地分支）
- git branch src
- git branch -m src cpp
- git branch checkout cpp
- git branch checkout master
- ... ... 
- git push origin --delete [branch_name]	（删除远程分支）
	
### 上传到Github
- git push origin master

### Github同步
- git pull origin master
- git pull origin master --allow-unrelated-histories

### [推荐blog](https://www.jb51.net/article/92247.htm)







