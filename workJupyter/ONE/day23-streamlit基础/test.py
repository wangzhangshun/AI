import streamlit as st
import pandas as pd #用户进行表格创建和表格数据分析的一个模块
st.write("这是我的第一个页面")
#使用pandas创建一个表格，将表格显示在streamlit页面中
table = pd.DataFrame({"第一列":[1,2,3,4,5],"第二列":[6,7,8,9,10]})
st.write(table)