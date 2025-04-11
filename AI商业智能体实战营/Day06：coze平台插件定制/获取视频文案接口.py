import re
import json
from urllib.parse import urlparse, parse_qs
import requests
import dashscope
from dashscope.audio.asr import Transcription
from runtime import Args
from typings.get_video_info.get_video_info import Input, Output

"""
Each file needs to export a function named `handler`. This function is the entrance to the Tool.

Parameters:
args: parameters of the entry function.
args.input - input parameters, you can get test input value by args.input.xxx.
args.logger - logger instance used to print logs, injected by runtime.

Remember to fill in input/output in Metadata, it helps LLM to recognize and use tool.

Return:
The return data of the function, which should match the declared output parameters.
"""

def get_video_id(text_or_url):
    try:

        # 1.提取视频地址
        #    格式1：4.66 B@t.EH 08/24 VYM:/ 有些私活真裁员降薪  https://v.douyin.com/i5WJFJWv/ 复制
        #    格式2：https://www.douyin.com/user/self?from_tab_name=main&modal_id=7452662497322077490
        #    格式3：https://www.douyin.com/video/7452662497322077490?modeFrom=userPost&secUid=MS4wLjABAAAACdnpzvOcEtvmZ8h9
        match_list = re.findall(r'https://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
                                text_or_url)
        if not match_list:
            return False, "短视频地址格式错误"
        video_url = match_list[0]

        # 2.处理 短连接
        if video_url.startswith("https://v.douyin.com"):
            res = requests.get(video_url, allow_redirects=False)
            video_url = res.headers["Location"]

        parsed_url = urlparse(video_url)
        query_params = parse_qs(parsed_url.query)

        # 3.地址GET参数处的modal_id读取
        modal_id_list = query_params.get("modal_id")
        if modal_id_list:
            video_id = modal_id_list[0]
        else:
            path_list = parsed_url.path.strip("/").split("/")
            video_id = path_list[-1]

        return True, video_id
    except Exception as e:
        return False, "短视频ID提取失败"


def get_video_info(video_id):
    try:
        # 拼接生成m端地址
        res = requests.get(
            url=f"https://m.douyin.com/share/video/{video_id}",
            headers={
                "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1"
            }
        )

        # 正则提取 视频字典信息
        match_list = re.findall("window._ROUTER_DATA = (.*)</script>", res.text)
        data_dict = json.loads(match_list[0])
        video_info = data_dict['loaderData']["video_(id)/page"]["videoInfoRes"]['item_list'][0]
        # 视频信息
        nickname = video_info["author"]['nickname']
        digg_count = video_info["statistics"]['digg_count']
        comment_count = video_info["statistics"]['comment_count']
        desc = video_info["desc"]
        video_url = video_info["video"]['play_addr']["url_list"][0]

        return True, (nickname, desc, video_url, digg_count, comment_count)
    except Exception as e:
        return False, "视频信息提取失败"


def get_text_by_ali(api_key, video_url):
    try:
        # 1.阿里云百炼账号，创建并获取api_key
        dashscope.api_key = api_key

        # 2.调用模型提取文案
        # 文档：https://help.aliyun.com/zh/model-studio/developer-reference/paraformer-recorded-speech-recognition-python-api?spm=a2c4g.11186623.help-menu-2400256.d_3_3_7_3_3_1.7ebf7f01D3wF0M
        #       https://help.aliyun.com/zh/model-studio/developer-reference/paraformer-recorded-speech-recognition-python-api?spm=0.0.0.i1
        response = Transcription.call(
            model='paraformer-v1',
            file_urls=[video_url],
            language_hints=['zh', 'en']  # “language_hints”只支持paraformer-v2和paraformer-realtime-v2模型
        )

        # 3.读取结果  {"transcription_url":"提取文案结果的URL地址",...}
        status_code = response.get('status_code')
        if status_code != 200:
            return False, response.get('message', "通义千问提取失败")
        res_dict = response["output"]["results"][0]

        transcription_url = res_dict["transcription_url"]

        # 4.获取文案
        res = requests.get(transcription_url)
        res_dict = res.json()
        text = res_dict["transcripts"][0]["text"]

        return True, text
    except Exception as e:
        return False, "文案提取异常" + str(e)


def handler(args: Args[Input])->Output:
    douyin_url = args.input.url
    ali_bailian_api_key = args.input.ali_bailian_api_key

    if not douyin_url.startswith("http"):
        douyin_url = re.search("https?://[^\\s]+", douyin_url).group()
    # 1.获取短视频ID
    status, video_id = get_video_id(douyin_url)
    # args.logger.info(video_id)
    if not status:
        return {"status": False, "error": video_id}

    # 2.获取视频信息（标题、作者、视频地址）
    status, video_info = get_video_info(video_id)
    if not status:
        return {"status": False, "error": str(video_info)}
    nickname, desc, video_url, digg_count, comment_count = video_info

    # 3.视频地址转换
    #   https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0300f
    #   https://aweme.snssdk.com/aweme/v1/play/?video_id=v0300f
    video_url = video_url.replace("playwm", "play")

    # 4.调用 阿里云模型，提取视频文案
    # args.logger.info(video_url)
    status, text = get_text_by_ali(ali_bailian_api_key, video_url)
    if not status:
        return {"status": False, "error": text}

    return {"status": True, "data": {"nickname": nickname, "desc": desc, "text": text, "digg_count": digg_count,
                                  "comment_count": comment_count}}
