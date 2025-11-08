import streamlit as st
from utils import generate_script

st.title('视频脚本生成器')

with st.sidebar:
    deepseek_api_key=st.text_input('请输入deepseek API密钥:',type="password")
    st.markdown('[获取deepseek API密钥](https://platform.deepseek.com/api_keys)')

subject=st.text_input('请输入生成的主题:')
video_lenth=st.number_input('请输入想要生成的时间:(单位:分钟)',min_value=0.0,step=0.1)
creativity=st.slider('请输入视频脚本的创造力(数字小说明更严谨,数字大说明更多样)',min_value=0.1,max_value=1.0,step=0.1,value=0.2)
submit=st.button('生成脚本')
if submit and not deepseek_api_key:
    st.info('请输入deepseek API密钥')
    st.stop()
if submit and not subject:
    st.info('请输入视频主题')
    st.stop()
if submit and not video_lenth>=0.1:
    st.info('视频时长需要大于0.1分钟')
    st.stop()
if submit:
    with st.spinner(('AI正在思考中,请稍等...')):
        title,search_result,script=generate_script(subject,video_lenth,creativity,deepseek_api_key)
    st.success('脚本成功生成!')
    st.subheader('标题:')
    st.write(title)
    st.subheader('视频脚本:')
    st.write(script)
    with st.expander('互联网搜索结果'):
        st.info(search_result)