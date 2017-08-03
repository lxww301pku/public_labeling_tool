### 环境  

- Python 3.4及以后
- Django 1.11.3及以后
- MySQL 5.5.24及以后

### 功能

实现了一个帮助用户进行语义标注的服务，从mysql中读取需要标注的语句，标注结果保存回mysql中

### 用法

1. 准备数据 先按照django教程安装MySQL API dirver，在MySQL上新建一个待使用的数据库`create database db_name character set utf8`，并把数据库信息（用户名，密码，host，port，数据库名)填入`settings.py`的DATABASES中，然后运行`python manage.py migrate`将`models.py`中定义的数据结构导入数据库，最后把excel中待标注的文本导入到该数据库的`sent_text`列``load data infile 'path_to_file' into table classification_sentence terminated by '\n' (`sent_text`)``
2. 启动服务 `python manage.py runserver`
3. domain/intent标注 浏览器地址栏输入`http://127.0.0.1:8000/classification/`进行标注 建议使用空格键确认，左右键选择，tab键跳转，回车键提交，完全脱离鼠标
4. slots标注 地址栏输入`http://127.0.0.1:8000/slots/`左键选择文本，按键选择tag，点击go按钮使标注数据进入文本框，每行可标注0次或多次，也可直接在文本框内修改，点击submit按钮提交
5. 结果查看 最后的结果可以在`http://127.0.0.1:8000/admin/` 查看，也可以在MySQL命令行查看，每条数据有5个属性值，`id`也是主键，每条数据都不同，自动生成；`sent_text`待标注的句子，从excel或其他数据库导入；`domain`/`intent`来自classification的标注，用数字来代表类别；`slots`来自slots的标注，一句话有多个属性时用`\t`连接

### 注意

1. domain/intent如果有漏标的情况，会跳回原页面并提示漏标，全部标注完成会提示成功。但slots并不检查是否漏标，因为有些句子确实没有属性标注
2. domain/intent中数据库中存储的数字与类别的关系，slots中按键与属性标签的关系，分别在`semantic_labeling/classification/template/classification/sentence_list.html`和`semantic_labeling/classification/static/slots/fillup.js`中修改
