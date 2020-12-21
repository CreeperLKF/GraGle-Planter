# This is the readme file for project 'Gragle Planter'.

## Something...

I have little experience of releasing a project so the readme file maybe ugly, QWQ. Since some of the code was written years ago, it also seems ugly. It may also contain many bugs, but I will try to fix them.

The part calculating token comes from a blog in baidu. However, since the original code was finished years ago, I can't find the original article or the original writer right now. I'm sorry for that, but I guess the original code might comes from "https://github.com/cocoa520/Google_TK".

## What is Gragle Planter

Gragle Planter is a tool to make your text grassy("生草").

Why Google? Fly me to the moon!

This is a program originally written to produce 'Autotune Remix' years ago, which originally can automatically translate a sentence into many languages and collect corresponding tts.

Given that it is more and more popular to produce 'Autotune Remix', I add some functions to the program and now it can `Get the tts in different languages` with several additional functions(see help).

## How to use

### InputFile

The text you want to plant grass (on)

### OutputFile(s)

The Grass-Planter will first create InputFile_output if it does not exist yet

The it will cut the passage into sentences if you choose '-c' and plant grass in order. If the output language support tts, you will get x.mp3(tts result) and x.txt(translated text), otherwise x.txt only. x represents the order of the sentence.

**Important:**`Please note that the Grass-Planter will not recreate txts, which means if x.txt exists, the Grass-Planter will not plant grass again. So you stopped the Grass-Planter forcely last time, I recommend you check the integrity of the lastest txt file in case of incomplete output file`

**If you use the python source code, PyExecJS is required.**
**pydub is only required when -m is on**

Use `python ggp.py -h` or `ggp.exe` to get help text or read text below(Assuming ggp.py or ggp.exe is the Grass-Planter and you want to plant grass for InputFile)

```
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
                zh-CN -> en -> ha -> (random) -> zh-CN
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
```