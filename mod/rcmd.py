from . import logger
from .par import *
import os, sys

"""to resolve command lines"""

def printHelp():
    
    """imitated from the manual of python (:XD"""
    
    content = """
NAME
    Gragle Planter - or Grassy Google Planter : to make your text grassy (Plant grass (Chinglish) / 生草)

SYNOPSIS
    1. if run with source code:
    python ggp.py [-h | -?]
    python ggp.py InputFile [-c [separator]] [-i language] [-o language] [-t times | -l languages]
    2. if run with compiled executable file:
    ggp.exe ......

DESCRIPTION
    See readme file
    if run with source code, PyExecJS and pydub is required

COMMAND LINE OPTIONS
    -h, -? or nothing
        Show this help text
    -c [separator]
        Plant grass for each sentence separately, otherwise plant grass whole passage in one time by default.
        THE WHOLE PASSAGE OR SINGLE SENTENCE SHOULD NOT CONTAIN MORE THAN 5000 CHARACTER (a Chinese character only counts once)
        Set separator for sentence, otherwise '。' (Chinese dot) is used by default
        e.g. 
            python ggp.py InputFile -c      # Use '。' 
            python ggp.py InputFile -c '.'  # Use '.'
            python ggp.py InputFile -c '$'  # Use '$'
    -i language
        Set input language, otherwise auto-detect('auto') by default
        please use language code(available in translation) in the end of the help text
        (Reminder: specify a separator if the text is not in Chinese and you want to plant grass separately)
    -o language
        Set output language, otherwise zh-CN by default
        if the output language is not available in tts, only translation will be output
        "ran" is allowed (see description in -l), but only generate tts available language 
    -t times
        Set iteration times, 0 for just tts(), 
        1 for one iteration time(e.g. zh-CN -> en -> zh-CN) and so on,
        the language used in iteration is generated randomly, 
        otherwise 0 by default
    -l languages
        (if -t is used and the argument is above zero, -l will be ignored)
        Set iteration chain, input language codes separated by ',', no space is allowed.
        if you want to have a random language somewhere, just use 'ran'
        e.g.
            "python ggp.py InputFile -l en,ja,ran" will iterate like:
                auto -> en -> ha -> (random) -> zh-CN
    -m
        Merge mp3 files, require pydub and something related to be installed first
        txt files will always be merged into 0.txt no matter -m exists

LANGUAGE CODE
    available language in translation: ('auto' can only be input in -i)
    {'hi': '印地语', 'ps': '普什图语', 'pt': '葡萄牙语', 'hmn': '苗语'
    'hr': '克罗地亚语', 'ht': '海地克里奥尔语', 'hu': '匈牙利语', 'yi': '意第绪语', 'hy': '亚美尼亚语'
    'yo': '约鲁巴语', 'id': '印尼语', 'ig': '伊博语', 'af': '布尔语(南非荷兰语)', 'is': '冰岛语',
    'it': '意大利语', 'am': '阿姆哈拉语', 'iw': '希伯来语', 'ar': '阿拉伯语', 'ja': '日语',
    'az': '阿塞拜疆语', 'zu': '南非祖鲁语', 'ro': '罗马尼亚语', 'ceb': '宿务语', 'be': '白俄罗斯语',
    'ru': '俄语', 'bg': '保加利亚语', 'rw': '卢旺达语', 'bn': '孟加拉语', 'jw': '印尼爪哇语',
    'bs': '波斯尼亚语', 'sd': '信德语', 'ka': '格鲁吉亚语', 'si': '僧伽罗语', 'sk': '斯洛伐克语',
    'sl': '斯洛文尼亚语', 'sm': '萨摩亚语', 'sn': '修纳语', 'so': '索马里语', 'sq': '阿尔巴尼亚语',
    'ca': '加泰罗尼亚语', 'sr': '塞尔维亚语', 'kk': '哈萨克语', 'st': '塞索托语', 'km': '高棉语',
    'su': '印尼巽他语', 'kn': '卡纳达语', 'sv': '瑞典语', 'ko': '韩语', 'sw': '斯瓦希里语',
    'ku': '库尔德语', 'co': '科西嘉语', 'ta': '泰米尔语', 'ky': '吉尔吉斯语', 'cs': '捷克语',
    'te': '泰卢固语', 'tg': '塔吉克语', 'th': '泰语', 'la': '拉丁语', 'lb': '卢森堡语', 'cy': '威尔士语',
    'tk': '土库曼语', 'tl': '菲律宾语', 'da': '丹麦语', 'tr': '土耳其语', 'tt': '鞑靼语', 'de': '德语',
    'lo': '老挝语', 'lt': '立陶宛语', 'lv': '拉脱维亚语', 'zh-CN': '中文', 'ug': '维吾尔语',
    'uk': '乌克兰语', 'mg': '马尔加什语', 'mi': '毛利语', 'ur': '乌尔都语', 'mk': '马其顿语',
    'ml': '马拉雅拉姆语', 'haw': '夏威夷语', 'mn': '蒙古语', 'mr': '马拉地语', 'uz': '乌兹别克语',
    'ms': '马来语', 'mt': '马耳他语', 'el': '希腊语', 'en': '英语', 'eo': '世界语', 'my': '缅甸语',
    'es': '西班牙语', 'et': '爱沙尼亚语', 'eu': '巴斯克语', 'vi': '越南语', 'ne': '尼泊尔语',
    'fa': '波斯语', 'nl': '荷兰语', 'no': '挪威语', 'fi': '芬兰语', 'ny': '齐切瓦语', 'fr': '法语',
    'fy': '弗里西语', 'ga': '爱尔兰语', 'gd': '苏格兰盖尔语', 'or': '奥利亚语', 'gl': '加利西亚语',
    'gu': '古吉拉特语', 'xh': '南非科萨语', 'pa': '旁遮普语', 'ha': '豪萨语', 'pl': '波兰语'} 

    available language in tts:
    ("sq", "ar", "et", "is", "pl", "bs", "af"
    "da", "de", "ru", "fr", "tl", "fi", "km", "ko", "nl", "ca",
    "cs", "hr", "la", "lv", "ro", "mr", "ml", "mk", "bn", "my",
    "ne", "no", "pt", "ja", "sv", "sr", "si", "eo", "sk", "sw",
    "te", "ta", "th", "tr", "cy", "uk", "es", "el", "hu", "hy",
    "it", "hi", "su", "id", "jw", "en", "vi", "zh-CN")


AUTHOR
    CreeperLKF on Github
LICENSE
    GPLv3 Licensed(https://www.gnu.org/licenses/gpl-3.0.html)
    """
    print(content)

def resolveCommandLine():

    """Resolve command lines inputed"""

    # not been tested under Windows or Linux executable file

    print(sys.argv)

    if len(sys.argv) < 2 or "-h" in sys.argv or "-?" in sys.argv:
        printHelp()
        return "Help Printed"
    if not os.path.isfile(sys.argv[1]):
        return "Grass Maker cannot find the file specified."
    
    ret = {"filename" : sys.argv[1], "cut" : False, "input" : "auto",\
        "output" : "zh-CN", "chain" : [], "merge" : False}

    if "-c" in sys.argv:
        ret["cut"] = '。' if not sys.argv.index("-c") == len(sys.argv)\
            else sys.argv[sys.argv.index("-c") + 1]
    
    if "-i" in sys.argv:
        ret["input"] = sys.argv[sys.argv.index("-i") + 1]
        if not (ret["input"] in availableTranslationLanguage or ret["input"] == 'auto'):
            return "You Choose -i with unsupported language specified"
    
    if "-o" in sys.argv:
        ret["output"] = sys.argv[sys.argv.index("-o") + 1]
        if not (ret["output"] in availableTranslationLanguage or ret["output"] == "ran"):
            return "You Choose -o with unsupported language specified('auto' is not allowed)"
    
    if "-t" in sys.argv:
        ret["times"] = int(sys.argv[sys.argv.index("-t") + 1])
        if ret["times"] < 0:
            return "Is your time lost?"
        elif ret["times"]:
            ret["chain"] = ["ran"] * ret["times"]
    
    if (not ret["chain"]) and "-l" in sys.argv:
        ret["chain"] = eval("['" + sys.argv[sys.argv.index("-l") + 1].replace(",", "','") + "',]")
        for tar in ret["chain"]:
            if not tar in availableTranslationLanguage:
                return "A language in chain is unsupported('auto' is not allowed)"
    
    if "-m" in sys.argv:
        ret["merge"] = True
    
    return ret    

if __name__ == "__main__":
    # This print debug information using return value
    logger.log(resolveCommandLine(), doTellUser=True)