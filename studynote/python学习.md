# python学习

## 第二章

1. title()以首字母大写的方式显示每个单词
2. 变量.upper()全部大写
3. BIANLIANG.lower() 全部小写
4. +号合并字符串

```python
first_name = "ada"
 last_name = "lovelace"
 full_name = first_name + " " + last_name
❶ print("Hello, " + full_name.title() + "!")

```

```python
 >>> favorite_language = 'python '
❷ >>> favorite_language
 'python '
❸ >>> favorite_language.rstrip()
 'python'
❹ >>> favorite_language
 'python '

```

l r strip  去除空白

5. 乘方 **

```python
>>> 3 ** 2
9
>>> 3 ** 3
27
>>> 10 ** 6
1000000

```

6. ```python
   age = 23
   message = "Happy " + str(age) + "rd Birthday!"
   print(message)
   
   ```

​    str()将非字符串表示为字符串

## 第三章 :修改添加删除插入

### 3.2

1. 列表 由一系列按特定顺序排列的元素组成。你可以创建包含字母表中所有字母、数字0~9或所有家庭成员姓名的列表；也可以将任何东西加入列表中，其中的元素之间可以没有 任何关系。鉴于列表通常包含多个元素，给列表指定一个表示复数的名称（如letters 、digits 或names ）是个不错的主意。 在Python中，用方括号（[] ）来表示列表，并用逗号来分隔其中的元素。

```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title()
```

==在Python中，第一个列表元素的索引为0，而不是1。在大多数编程语言中都是如此，这与列表操作的底层实现相关==

通过将索引指定为-1 ，可让Python返回最后一个列表元素：

```python
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
❶ motorcycles.append('ducati')
print(motorcycles)
在列表中添加和删除元素
```

==方法append() 将元素'ducati' 添加到了列表末尾（见❶ ），而不影响列表中的其他所有元素：==

==使用方法insert() 可在列表的任何位置添加新元素。为此，你需要指定新元素的索引和值。==

```python
motorcycles = ['honda', 'yamaha', 'suzuki']
❶ motorcycles.insert(0, 'ducati')
print(motorcycles)
```

删除：del

```python
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[1]
print(motorcycles)
```

 

弹出并加入：pop()

```python
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
❷ popped_motorcycle = motorcycles.pop() ❸ print(motorcycles) ❹ print(popped_motorcy
                                                                     
                                                                     
                                                                     ['honda', 'yamaha', 'suzuki']
['honda', 'yamaha']
suzuki
```

根据值来删除元素：

```python
#方法remove() 只删除第一个指定的值。如果要删除的值可能在列表中出现多次，就需要使用循环来判断是否删除了所有这样的值
❶ motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
❷ too_expensive = 'ducati' ❸ motorcycles.remove(too_expensive)
print(motorcycles) ❹ print("\nA " + too_expensive.title() + " is too expensive for me.")


['honda', 'yamaha', 'suzuki', 'ducati']
['honda', 'yamaha', 'suzuki']
A Ducati is too expensive for me.

```

### 3.3组织列表

1. sort（）

2. ```python
   cars = ['bmw', 'audi', 'toyota', 'subaru']
   cars.sort(reverse=True)
   print(cars)
   
   ['toyota', 'subaru', 'bmw', 'audi']
   #你还可以按与字母顺序相反的顺序排列列表元素，为此，只需向sort() 方法传递参数reverse=True 
   ```

以上是永久性排列

3. 使用函数sorted() 对列表进行临时排序

    ```python
    cars = ['bmw', 'audi', 'toyota', 'subaru']
    ❶ print("Here is the original list:")
    print(cars)
    ❷ print("\nHere is the sorted list:")
    print(sorted(cars))
    
    
    Here is the original list:
    ['bmw', 'audi', 'toyota', 'subaru']
    Here is the sorted list:
    ['audi', 'bmw', 'subaru', 'toyota']
    
    ```

   

4. 要反转列表元素的排列顺序，可使用方法reverse() 。==永久性且只是反转列表中排序元素==

```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

```

5. len()

## 第四章：操作列表

#### 4.1 遍历

```python
magicians=['alice','david','carolina']
for magician in magicians:
	print(magician)

```

#### 4.2创建数值列表

1. for value in range(1,5,2):         

   ​		print(value)     #这样会输出1,3，到达5后停止不输出

2. list()    将数字转换为列表

3. min() max() sum()

4. 列表解析

```python
squares = [value**2 for value in range(1,11)]
print(squares)
注意，这里的for 语句末尾没有冒号。
```

#### 4.3使用列表的一部分

1. 切片

   ```python
   players = ['charles', 'martina', 'michael', 'florence', 'eli']
   print(players[1:4])
   
   
   ['martina', 'michael', 'florence']
   
   ```

   ==如果你没有指定第一个索引，Python将自动从列表开头开始：==

2. 复制

​    方法是同时省略起始索引和终止索引（[:] 

```python
 my_foods = ['pizza', 'falafel', 'carrot cake']
 ❷ friend_foods = my_foods[:]   #不能写成赋值形式，否则都指向同一列表
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

```

#### 4.4元组  数据不可改变

1. 使用圆括号
2. 给元祖变量赋值

#### 4.5设置代码格式

## 第五章if

1. 在Python中检查是否相等时区分大小写，例如，两个大小写不同的值会被视为不相等：

## 第六章 字典

### 6.2对字典进行遍历

```python
favorite_languages = {
    'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
    'phil': 'python',
}
❶ for name, language in favorite_languages.items():
    ❷ print(name.title() + "'s favorite language is " +
		language.title() + ".")

```

items的作用是遍历输出字典

```py
Jen's favorite language is Python.
Sarah's favorite language is C.
Phil's favorite language is Python.
Edward's favorite language is Ruby.
结果
```

### 6.3

```python
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
❶ for name in favorite_languages.keys():
print(name.title())
不需要使用字典中的值  keys()
```

### 6.4可遍历字典的中的键或值

```python
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
print("The following languages have been mentioned:")
for language in favorite_languages.values():
	print(language.title())
  

values的使用 包含重复值
```

```python
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
print("The following languages have been mentioned:")
❶ for language in set(favorite_languages.values()):
	print(language.title())
    
    
set()是一个集合
```

### 6.5嵌套

```python
# 创建一个用于存储外星人的空列表
aliens = []
# 创建30个绿色的外星人
for alien_number in range (0,30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)
for alien in aliens[0:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10
# 显示前五个外星人
for alien in aliens[0:5]:
	print(alien)
	print("...")
```

### 6.6在字典中储存列表





```python
❶ pizza = {
'crust': 'thick',
'toppings': ['mushrooms', 'extra cheese'],
}
```

### 6.7字典中存储字典

```python
users = {
	'aeinstein': {
		'first': 'albert',
		'last': 'einstein',
		'location': 'princeton',
		},
	'mcurie': {
		'first': 'marie',
		'last': 'curie',
		'location': 'paris',
		},
	}
❶ for username, user_info in users.items():
    ❷ print("\nUsername: " + username) ❸
    full_name = user_info['first'] + " " + user_info['last']
	location = user_info['location']
❹ 	print("\tFull name: " + full_name.title())
	print("\tLocation: " + location.title())
```

## 第八章

### 8.1文件导入

import()

```python
import pizza
❶ pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

```

使用as 给函数指定别名

### 8.6.5 

导入模块中的所有函数 使用星号（* ）运算符可让Python导入模块中的所有函数：



```
from module_name import *
   文件名
```

## 第九章 类

### 9.3继承

super()

## 第十章 类和对象

类：属性和方法

面向对象特点：封装，继承，多肽

property（fget=（），fset=（），fdel=（），doc=（））
