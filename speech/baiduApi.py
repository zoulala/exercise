#!/usr/bin/python3
'''
通过调用百度语音识别API，实现语音识别+语音合成，百度语音识别Api方式一:隐式方式
reference ：http://blog.csdn.net/wolfblood_zzx/article/details/46418635

注意：wav各式的音频要求较严格，其他各式转过来的貌似不行
'''
import urllib.request
import urllib
import json
import base64
class BaiduRest:
    def __init__(self, cu_id, api_key, api_secert):
        # token认证的url
        self.token_url = "https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s"
        # 语音合成的resturl
        self.getvoice_url = "http://tsn.baidu.com/text2audio?tex=%s&lan=zh&cuid=%s&ctp=1&tok=%s"
        # 语音识别的resturl
        self.upvoice_url = 'http://vop.baidu.com/server_api'

        self.cu_id = cu_id
        self.getToken(api_key, api_secert)
        return

    def getToken(self, api_key, api_secert):
        # 1.获取token
        token_url = self.token_url % (api_key,api_secert)

        r_str = urllib.request.urlopen(token_url).read().decode()
        #r_str = {"access_token":"24.c62dd767da27505918aa4149dd318b55.2592000.1499566864.282335-5722325","session_key":"9mzdWEYKkkDMBo02E1Dp\/yLpY714S0wD\/FBR1UsT2utsGh2ycPP86An2jAgRMIs4D44ClaDCEGcnanFcn1rJh7Jq0hti","scope":"public audio_voice_assistant_get audio_tts_post wise_adapt lebo_resource_base lightservice_public hetu_basic lightcms_map_poi kaidian_kaidian wangrantest_test wangrantest_test1 bnstest_test1 bnstest_test2 vis-classify_flower","refresh_token":"25.6a607b491cc83ec967b842c52998d8e6.315360000.1812334864.282335-5722325","session_secret":"2eba0ffeb6959f1449286dc4508dda30","expires_in":2592000}
        token_data = json.loads(r_str)
        self.token_str = "24.c62dd767da27505918aa4149dd318b55.2592000.1499566864.282335-5722325"#token_data['access_token']
        pass

    def getVoice(self, text, filename):
        # 2. 向Rest接口提交数据
        get_url = self.getvoice_url % (urllib.parse.quote(text), self.cu_id, self.token_str)

        voice_data = urllib.request.urlopen(get_url).read()
        # 3.处理返回数据
        voice_fp = open(filename,'wb+')
        voice_fp.write(voice_data)
        voice_fp.close()
        pass

    def getText(self, filename):
        # 2. 向Rest接口提交数据
        data = {}
        # 语音的一些参数
        data['format'] = 'wav'
        data['rate'] = 16000
        data['channel'] = 1
        data['cuid'] = self.cu_id
        data['token'] = self.token_str
        wav_fp = open(filename,'rb')
        voice_data = wav_fp.read()
        data['len'] = len(voice_data)

        data['speech'] = base64.b64encode(voice_data).decode('utf-8')
        post_data = json.dumps(data)
        r_data = urllib.request.urlopen(self.upvoice_url,data=bytes(post_data,encoding="utf-8")).read().decode()

        # 3.处理返回数据
        return json.loads(r_data)['result']

if __name__ == "__main__":
    # 我的api_key,供大家测试用，在实际工程中请换成自己申请的应用的key和secert
    api_key = "SrhYKqzl3SE1URnAEuZ0FKdT"
    api_secert = "hGqeCkaMPb0ELMqtRGc2VjWdmjo7T89d"
    # 初始化
    bdr = BaiduRest("test_python", api_key, api_secert)
    # 将字符串语音合成并保存为out.mp3
    bdr.getVoice("你好", "out.wav")
    # 识别test.wav语音内容并显示
    print(bdr.getText("23.wav"))