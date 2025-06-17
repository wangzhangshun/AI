## Streamlit

### 简介

#### 什么是streamlit

Streamlit是一个免费的开源框架，用于快速构建和共享漂亮的数据科学Web应用程序。它是一个基于Python的库，专为机器学习工程师设计。数据分析工程师不是网络开发人员，他们对花几周时间学习使用这些框架来构建网络应用程序不感兴趣。相反，他们需要一个更容易学习和使用的工具，只要它可以显示数据并收集分析/建模所需的参数。Streamlit允许您仅用几行代码创建一个外观惊艳的应用程序。

参考文档：http://cw.hubwiz.com/card/c/streamlit-manual/

#### 数据科学家为何要使用Streamlit？

Streamlit最大的好处是，您甚至不需要了解Web开发的基础知识就可以开始或创建您的第一个Web应用程序。因此，如果你是一个对数据科学感兴趣的人，你想轻松、快速地部署你的模型，并且只需要几行代码，Streamlit是一个很好的选择。

**优势：**

- 不需要具备前端知识即可应用streamlit。
- 学习成本极低
  - 你不需要花费几天或几个月的时间来创建一个Web应用，你可以在几个小时甚至几分钟内创建一个非常漂亮的机器学习或数据科学应用。
- 它兼容大多数Python库
  - 例如panda、matplotlib、seaborn、plotly、Keras、PyTorch等。

#### 环境安装

```python
pip install streamlit

#测试安装是否正常：
streamlit hello
```

#### 程序运行

```python
streamlit run xxx.py
```

### 具体操作

#### 1.write()函数

可以通过该函数向看板上输出显示指定内容

```python
import streamlit as st
import pandas as pd #用户进行表格创建和表格数据分析的一个模块
st.write("这是我的第一个页面")
#使用pandas创建一个表格，将表格显示在streamlit页面中
table = pd.DataFrame({"第一列":[1,2,3,4,5],"第二列":[6,7,8,9,10]})
st.write(table)
```

#### 2.滑块组件slider

"slider"的中文意思是"滑块"。它是一种用户界面元素，通常用于选择一个数值范围或从给定选项中选择一个值。滑块的外观通常是一个可拖动的滑块，用户可以通过移动滑块来选择所需的值。滑块可以在许多应用程序和网页中使用，例如调整音量、选择年龄范围或设置某个参数的值。

```python
import streamlit as st

st.write("st.slider()滑块")
#slider参数为滑块自定义名称，返回值为滑动到的数值
num = st.slider("num")
st.write(num, "squred is", num*num)
```

#### 3.文本框操作text_input

```python
import streamlit as st

st.write("文本框操作")
#文本框输入，回车结束
st.text_input("your name", key="name")
st.text_input("your age", key="age")

# 显示输入的值
st.write(st.session_state.name,st.session_state.age)
```

密码框：

```python
import streamlit as st

# 创建一个文本输入框，并将其类型设置为密码
password = st.text_input("请输入密码", type="password")

# 检查密码是否正确（这里假设正确密码是"123456"）
if st.button("登录"):
    if password == "123456":
        st.success("登录成功！")
    else:
        st.error("密码错误，请重试。")
```



#### 4.多选框checkbox

```python
import streamlit as st
import pandas as pd

st.write("checkbox()多选框")
# 点击checkbox后返回True，未点击为False
ex1 = st.checkbox('显示/不显示 表格')
if ex1:
    table = pd.DataFrame({"第一列":[1,2,3,4,5],"第二列":[6,7,8,9,10]})
	st.write(table)

ex2 = st.checkbox('显示/不显示 滑块')
if ex2:
    x = st.slider('x')
```

#### 5.下拉框selectbox

```python
import streamlit as st

#返回值为选中的内容信息
option = st.selectbox(
    label='请选择省份信息：',
    options=['河北','山东','河南','吉林']
)

st.write("您选择的是: ", option)
```

#### 6.侧边栏sidebar

```python
import streamlit as st

#侧边栏下拉框
add_selectbox = st.sidebar.selectbox(
    label="通讯方式选项",
    options=('微信','QQ','手机','邮件')
)
#获取下拉选项
st.write("下拉选项: ", add_selectbox)

#侧边栏滑块
add_slider = st.sidebar.slider(
    label="选择一个范围的值",
    min_value=0.0, max_value=100.0, value=(25.0, 75.0)
)
#获取滑块的值
st.write("值的范围: ", add_slider)

```

#### 7.单选按钮radio

```python
import streamlit as st

#columns参数表示列数
left_column, right_column = st.columns(2)
# 左边列设置
with left_column:
    #返回值为选中的选项值
    chosen = st.radio(
        label='电脑品牌',
        options=('苹果','华为','小米')
    )
    st.write(f'你选择的品牌是: {chosen}')
    
# 右边列设置
with right_column:
    # 返回值为选中的选项值
    chosen = st.radio(
        label='手机品牌',
        options=('苹果','华为','小米')
    )
    st.write(f'你选择的品牌是: {chosen}')

```

#### 8.进度条progress

```python
import streamlit as st
import time
st.write("模拟长时间的计算...")

# 创建一个动态显示数据的容器，用于动态显示进度条的进度数值
value = st.empty()
#创建进度条，进度条初始值为0
bar = st.progress(0)
for i in range(100):
    #这是动态显示的数值
    value.text(f'Iteration {i+1}')
    # 更新进度条
    bar.progress(i+1)
    time.sleep(0.1)
st.write('运行结束!')
```



### 布局

#### 1.st.sidebar - 在侧边栏增添交互元素

```python
import streamlit as st

# 方式1：使用对象表示法添加选择框
add_selectbox = st.sidebar.selectbox(
    "您希望如何联系您？",
    ("电子邮件", "家庭电话", "移动电话")
)
# 方式2：使用“with”语法添加单选按钮
with st.sidebar:
    add_radio = st.radio(
        "选择一种运输方式",
        ("标准（5-15天）", "快递（2-5天）")
    )
```

#### 2.st.columns - 并排布局多元素容器

通过调用 st.columns，您可以插入多个多元素容器，并将它们布局为并排的形式。返回的是一个容器对象的列表，每个对象都可以用来添加元素。您可以选择使用“with”语法（更推荐）或者直接在容器对象上调用方法来添加元素。

```python
import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
   st.header("一只猫")
   st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
   st.header("一只狗")
   st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
   st.header("一只猫头鹰")
   st.image("https://static.streamlit.io/examples/owl.jpg")
```

#### 3.st.tabs - 以选项卡形式布局多元素容器

通过调用 st.tabs，您可以插入多个多元素容器作为选项卡。每个选项卡都代表一组相关内容。返回的是一个容器对象的列表，每个对象都可以用来添加元素。与之前一样，您可以选择使用“with”语法或者直接在容器对象上调用方法来添加元素。

需要注意的是，每个选项卡的所有内容都会被一次性发送并渲染在前端。

```python
import streamlit as st

tab1, tab2, tab3 = st.tabs(["猫", "狗", "猫头鹰"])

with tab1:
   st.header("一只猫")
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
   st.header("一只狗")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
   st.header("一只猫头鹰")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

```

#### 4.st.expander - 可展开/折叠的多元素容器

调用 st.expander，您可以插入一个可展开或折叠的容器，用于包含多个元素。容器的初始状态是折叠的，只显示提供的标签。用户可以点击标签来展开容器，查看其中的内容。

```python
import streamlit as st


with st.expander("查看说明"):
    st.write("""
        上面的图表展示了我为您选择的一些数字。
        这些数字是通过真实的骰子摇出来的，所以它们*保证*是随机的。
    """)
    st.image("https://static.streamlit.io/examples/dice.jpg")
```

