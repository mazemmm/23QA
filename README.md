# 项目介绍
    本问答平台构建于FLASK框架之上，为用户提供了一个互动的问答环境。

    在平台的首页，用户能够浏览到过往发布的各类问题及其答案。为了发布新的问答，用户需先进行登录操作。如果尚未登录，系统将自动跳转到邮箱登录。
    
    对于未注册的用户，平台提供了便捷的邮箱验证注册方式，只需简单几步即可完成注册并顺利登录，进而发布提问与回答。
 
# 环境依赖
 
 
# 目录结构描述
    ├── ReadMe.md           // 帮助文档

    ├── blueprints          //实现模块化

    │   ├── __init__.py     
    
    │   ├── auth.py         //实现授权与验证码发送
    
    │   ├── forms.py        //后端注册表单验证器实现
    
    │   └── qa.py           //问答相关
    
    ├── migrations          //实时更新迁移数据库
    
    ├── static             //页面渲染
    
    │   ├── bootstrap

    │   ├── css

    │   ├── images

    │   ├── jguery
    
    │   └── js              //邮箱验证计时

    ├──templates
    
    │   ├── base.html          //注册页面父模板，导航条实现

    │   ├── detail.html

    │   ├── index.html          

    │   ├── login.html          //登录页面

    │   ├── public_question.html//问答页面
    
    │   └── register.html       //注册页面

    ├── app.py              // 合成结果存放的文件夹

    ├── config.py           //用来进行邮箱验证码等配置

    ├── decorators.py       //登录装饰

    ├── exts.py             //存放扩展文件
    
    └── models.py           // 发布问答后端功能实现
 
# 使用说明

![image](https://github.com/mazemmm/23QA/blob/master/h_page.png)

![image](https://github.com/mazemmm/23QA/blob/master/login.png)

![image](https://github.com/mazemmm/23QA/blob/master/qa.png)

![image](https://github.com/mazemmm/23QA/blob/master/register.png)