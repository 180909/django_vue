# django vue 前后端分离

## 做什么
*使用django vue来实现前后端分离的web项目，以博客的CRUD为例子*

## 技术栈
1. 后端 backend
  * django
  * django rest framework
  * django cors headers
2. 前端 frontend
  * vue
  * bootstrap
  * fontawesome
## 步骤
1. 后端
  * 安装django
  * 创建django项目
  * 添加blog的Model，并添加一些初始数据
  * 使用restframework来添加serializer、viewset、set
  * 设置跨域 cors headers
2. 前端
  * 安装node、vue
  * vue-cli创建项目
  * 修改index.html主页 添加bootstrap css框架和fontawsome字体依赖
  * 修改App.vue和核心组件
  * 添加axios http请求组件
  * 添加请求后端代码
## 启动
1. 后端
  * 定位到backend文件夹下
  * 控制台输入python manage.py runserver
2. 前端
  * 定位到frontend文件夹下
  * 控制台输入npm run serve