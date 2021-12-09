#練習二
#程式
#變化考題：變化考題：(1)請加入轉速資料的收集，假若轉速 >= 標準轉速的時候，要輸出警訊，提醒駕駛注意。
#變化考題：變化考題：(2)油箱只剩0.5格的時候，怎麼辦??
import streamlit as st
st.write('我們的是第八組，組名是vamos')
car_simulation = {'gas_warning':1, 'speed_limit':100, 'temp_warning':30, '轉速':12000}
gas = st.number_input('油量的資料收集:油箱滿是10格 =>')
speed= st.number_input('車速的資料收集:限速100 =>')
temp = st.number_input('溫度的資料收集:限溫30 =>')
轉速=st.number_input('轉速資料的收集:限轉12000 =>')
confirm_input=st.button('輸入確認')
if confirm_input:

    if gas <= car_simulation.get('gas_warning'):
      st.write('油箱只剩', gas, '格! 準備加油!!')
    else:
      st.write('油箱還剩', gas, '格。')
    if speed>=car_simulation.get('speed_limit'):
      st.write('即將超速')
    else:
      st.write('安全')
    if temp>=car_simulation.get('temp_warning'):
      st.write('過熱')
    else:
      st.write('正常')
    if 轉速>=car_simulation.get('轉速'):
      st.write('即將超過轉速')
    else:
      st.write('正常')

#輸出的參考：
#油量的資料收集:油箱滿是10格 =>10
#車速的資料收集:限速100 =>100
#溫度的資料收集:限溫30 =>30
#轉速資料的收集:限轉12000 =>12000

#油箱還剩 10 格。
#即將超速
#過熱
#即將超過轉速
