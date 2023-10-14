* 数据模型其实是对python框架的描述，他规范了这门语言自身构建模型的接口，这些模块包括但不限于序列、迭代器、函数、类和上下文管理器

### magic方法/dunder方法
  特殊方法能让你自己的对象实现和支持以下的语言框架，并与之交互

  迭代
  集合类
  属性访问
  运算符重载
  函数与方法的调用
  对象的创建和销毁
  字符串表示形式和格式化
  管理上下文(with)

#### 特殊方法一览
1. 与运算符无关的特殊方法
* 字符串/字节列表: __repr__ __str__ __format__ __byte__
* 数值转换：__abs__ __bool__ __complex__ __int__ __float__ __hash__ __index__
* 集合模拟： __len__ __getitem__ __delitem__ __contains__
* 迭代枚举： __iter__ __reversed__ __next__
* 可调用模拟： __call__
* 上下文管理： __enter__ __exit__
* 实例创建和销毁： __init__ __new__ __del__
* 属性管理： __getattr__ __getattribute__ __setter__ __delattr__ __dir__
* 属性描述符：__get__ __set__ __delete__
* 跟类相关的服务：__prepare__ __instancecheck__ __subclasscheck__
2. 与运算符相关的特殊方法
* 
