import streamlit as st
# import numpy as np
# import pandas as pd
# from PIL import Image
import time

st.title('Streamlit 超入門')

########################################
# ウィジェット
st.write('Interactive Widgets')
########################################
st.write('プレグレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Itemration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.01)

'Done!!!'
########################################
# 2カラム
left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button: # 左ボタンが押されたら
     right_column.write('ここは右カラム')
# expander(折りたたみ)
expan = st.expander("問合せ１")
expan.write('問合せ内容を書く')
########################################
# expander の例
# st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

# expander = st.expander("See explanation")
# expander.write(
#     "The chart above shows some numbers I picked for you."
# )
########################################
#st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})
# with st.expander("See explanation"):
#     st.write(
#         "The chart above shows some numbers I picked for you."
#     )
########################################
# サイドバー(st.sidebar)
# text = st.sidebar.text_input('あなたの趣味を教えてください。')
# condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)
# 'あなたの趣味：', text, 'です。'
# 'コンディション：', condition, 'です。'
########################################
# テキスト入力(st.text)
# text = st.text_input('あなたの趣味を教えてください。')
# 'あなたの趣味：', text, 'です。'
# スライダー(st.slider)
# condition = st.slider('あなたの今の調子は？', 0, 100, 50)
# 'コンディション：', condition, 'です。'
########################################
# セレクトボックス(st.selectbox)
# option = st.selectbox(
#     'あなたが好きな数字を教えてください',
#     list(range(1, 11)) # 1～10の数字
# )

# 'あなたの好きな数字は、', option, 'です。'
########################################
# st.write('Display Image')
#
# チェックボックスによる画像表示
# if st.checkbox('Show Image'):
#     img = Image.open('test.png')
#     st.image(img, caption='cnpj', use_column_width=True)
########################################
# 画像表示
# img = Image.open('test.png')
# st.image(img, caption='cnpj', use_column_width=True)
# ########################################
#st.write('DataFrame')
########################################
# # マッピング(新宿付近)
# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#     # lat:緯度、lon:経度
#     columns=['lat', 'lon']
# )
# st.map(df)
########################################
# # 0から1未満の乱数
# df = pd.DataFrame(
#     np.random.rand(20, 3),
#     columns=['a', 'b', 'c']
# )
# # 折れ線グラフ
# st.line_chart(df)
# # エリアチャート
# st.area_chart(df)
# # 棒グラフ
# st.bar_chart(df)
########################################
# df = pd.DataFrame({
#     '1列目': [1, 2, 3, 4],
#     '2列目': [10, 20, 30, 40]
# })
#
# dataframe: 表
# table: staticなテーブル
# st.table(df.style.highlight_max(axis=0))
########################################
# マークダウン記法
# """
# # 章
# ## 節
# ### 項
# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """
########################################