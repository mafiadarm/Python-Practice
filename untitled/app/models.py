from django.db import models
from django import forms

# Create your models here.

"""
设计一个产生数据库的类
在terminal里面创建一个包，用于迁移 python manage.py makemigrations --name initial app
    python manage.py showmigrations app 显示需要迁移的包有哪些
    python manage.py sqlmigrate app 0001_initial 显示将会对数据库使用什么样的命令
        如果有修改，重新运行python manage.py makemigrations --name initial app对包进行修改
    第一次迁移需要使用 python manage.py migrate 进行迁移，同时建立跟踪，之后改变数据库结构不需要重新删除和创建表
        当对类有修改、新的迁移的时候，用python manage.py makemigrations --name initial app创建一个新的包
ORM会自动调用SQL语言进行操作
当修改了setting.py的数据库[新建的]连接信息，需要重新迁移的时候，也使用python manage.py migrate
    因为是新建的，所以调取的数据是空的
    如果这个数据库本身是有数据的，则调取[操作]已有的数据
"""


class Artist(models.Model):
    name = models.CharField("artist", max_length=50)
    year_formed = models.PositiveIntegerField()  # 使用下划线的时候，窗口会处理成标签


class Album(models.Model):
    name = models.CharField("album", max_length=50)
    # 主键key 可以直接指向 class Artist，让两者连接, on_delete必须加
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)


"""
对类进行修改的时候，不用构建save方法，直接从models里面继承过来
在console里面输入
    from app.models import Artist 因为这里还是空的，所以要先引导
    newArtist = Artist(name="Great Big Sea", year_formed=1985) 新增这个类
    newArtist.save() 保存
"""

"""
在执行update的时候，属性要对应
在console里面输入
    newArtist.year_formed = 1986
    newArtist.save()
"""

"""
console：
查询数据的时候，可以使用all方法
allArtists = Artist.objects.all()
for artist in allArtists:  如果想要看内容，可以遍历
    print(artist.name)  获取某个列的内容
单个记录的获取 firstArtist = Artist.objects.get(id=1); print(firstArtist)
    如果一个条件会返回多条记录，使用Artist.objects.filter()方法获取
filter的查询条件可以用name__startswith=xxx% “%”作为匹配任意值
    注意name__startswith中间是两条下划线
如果需要不区分大小写 name__istartswith
如果需要精确匹配 name__exact 或者加上 i 来不区分大小写
如果有多个条件，可以用 Artist.objects.filter(year_formed=1986).filter(id=1)这样来实现
    或者排除语句 Artist.objects.filter(year_formed=1986).exclude(id=1)...
"""

"""
console：
插入几条记录,实现外键查询 在Album查询在Artist中的name 
[引用之前的 newArtist = Artist(name="Great Big Sea", year_formed=1985)]
    from app.models import Album
    Album(name="Up", artist=newArtist).save()
    Album(name="Sea of no cares", artist=newArtist).save()
当我们在去查询 albums = Album.objects.filter(artist__name="Great Big Sea")
    for album in albums:
        print(i.name)  获取结果
"""


class ArtistForm(forms.ModelForm):
    """
    构建一个在网页新增数据的类,并且自动验证
    """
    class Meta:
        model = Artist  # 继承Artist类，同时也拥有了models.Model里面的save方法
        fields = "__all__"
        fileds = ["name", "year_formed"]

