|————————————————————
|/home/用户名 = /~
|    登录用户的主目录，存放用户的个人文件以及配置
|————————————————————
|/etc 
|    系统配置文件
|————————————————————
|/var/log
|    存放日志文件
|————————————————————
|/usr/bin
|    存放用户命令
|————————————————————
|/tmp
|    临时文件
|————————————————————
|/root
|    主用户目录
|————————————————————


绝对路径和相对路径的区别:
    绝对路径:
        是从根目录开始到指定目录为止的完整路径，路径涵盖以/开头，指定目录结尾(包括指定目录)经过的所有目录,支持用户在任意目录下进行绝对路径的目录切换
    相对路径:
        是从当前目录开始到指定目录位置的路径，路径涵盖以当前目录(pwd)开头，指定目录结尾(包括指定目录)经过的目录，支持用户在以当前目录为基准下的目录切换

ls 的 5 个选项各是什么意思:
    -l:显示文件及其详细信息
    -a:显示所有文件(包括隐藏文件)
    -h:搭配-l输出指令为-lh额外显示文件存储大小
    -d:显示文件本身
    -t:显示文件，并以修改时间的新旧逐前向后排列

权限模型报错:
    1.
    cd ~/projects/linkpulse/docs/linux
    echo "这是一个测试文件" > secret.txt
    ls -l secret.txt
        -rw-rw-r-- 1 dev dev 25 Oct  7 20:45 secret.txt
    chmod 000 secret.txt
    cat secret.txt
        cat: secret.txt: Permission denied
    
    2.
    mkdir -p priv
    echo "里面的内容" > priv/a.txt
    chmod 600 priv
    ls priv
        ls: cannot access 'priv/a.txt': Permission denied
        a.txt
    ls -d priv
        priv

    3.
    touch testperm.txt
    chmod 751 testperm.txt
    ls -l testperm.txt
        -rwxr-x--x 1 dev dev 0 Oct  7 21:01 testperm.txt