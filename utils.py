from langchain_core.prompts import ChatPromptTemplate
from langchain_deepseek.chat_models import ChatDeepSeek
# from langchain_community.utilities.wikipedia import WikipediaAPIWrapper
from langchain_community.tools import DuckDuckGoSearchRun
import os


def generate_script(subject,video_lenth,creativity,api_key):
    title_template=ChatPromptTemplate.from_messages(
        [
            ('human',"请为'{subject}'这个主题的视频想一个吸引人的标题")
        ]
     )
    script_template = ChatPromptTemplate.from_messages(
        [
            ("human",
             """你是一位短视频频道的博主。根据以下标题和相关信息，为短视频频道写一个视频脚本。
             视频标题：{title}，视频时长：{duration}分钟，生成的脚本的长度尽量遵循视频时长的要求。
             要求开头抓住限球，中间提供干货内容，结尾有惊喜，脚本格式也请按照【开头、中间，结尾】分隔。
             整体内容的表达方式要尽量轻松有趣，吸引年轻人。
             脚本内容可以结合以下维基百科搜索出的信息，但仅作为参考，只结合相关的即可，对不相关的进行忽略：
             ```{wikipedia_search}```""")
        ]
    )

    model = ChatDeepSeek(model="deepseek-chat", temperature=creativity,api_key=api_key)
    title_chain=title_template | model
    script_chain=script_template | model

    title=title_chain.invoke({'subject':subject}).content


    search = DuckDuckGoSearchRun()
    search_result=search.run(subject)
    script=script_chain.invoke({'title':title,'duration':video_lenth,'wikipedia_search':search_result}).content

    return title,search_result,script
# print(generate_script('sora模型',1,0.7,os.getenv('DEEPSEEK_API_KEY')))
