from . import logger
from .par import *
import execjs, json
import urllib.request, urllib.parse

"""to get translation and tts from google"""

class Tokener():

    """to get token to call translate"""

    def __init__(self):  
        """compile a js"""
        self.ctx = execjs.compile(""" 
            function TL(a) {
                var k = "";
                var b = 406644;
                var b1 = 3293161072;

                var jd = ".";
                var $b = "+-a^+6";
                var Zb = "+-3^+b+-f";

                for (var e = [], f = 0, g = 0; g < a.length; g++) {
                    var m = a.charCodeAt(g);
                    128 > m ? e[f++] = m: (2048 > m ? e[f++] = m >> 6 | 192 : (55296 == (m & 64512) && g + 1 < a.length && 56320 == (a.charCodeAt(g + 1) & 64512) ? (m = 65536 + ((m & 1023) << 10) + (a.charCodeAt(++g) & 1023), e[f++] = m >> 18 | 240, e[f++] = m >> 12 & 63 | 128) : e[f++] = m >> 12 | 224, e[f++] = m >> 6 & 63 | 128), e[f++] = m & 63 | 128)
                }
                a = b;
                for (f = 0; f < e.length; f++) a += e[f],
                a = RL(a, $b);
                a = RL(a, Zb);
                a ^= b1 || 0;
                0 > a && (a = (a & 2147483647) + 2147483648);
                a %= 1E6;
                return a.toString() + jd + (a ^ b)
            };

            function RL(a, b) {
                var t = "a";
                var Yb = "+";
                for (var c = 0; c < b.length - 2; c += 3) {
                    var d = b.charAt(c + 2),
                    d = d >= t ? d.charCodeAt(0) - 87 : Number(d),
                    d = b.charAt(c + 1) == Yb ? a >>> d: a << d;
                    a = b.charAt(c) == Yb ? a + d & 4294967295 : a ^ d
                }
                return a
            }
        """)  

    def getToken(self,text):  
        
        """initialize a Tokener and call getToken each time"""
        
        return self.ctx.call("TL",text)

def open_url(url, tmout=0):
    
    """construct a request and return respense in uft-8"""
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = urllib.request.Request(url=url, headers=headers)
    if tmout:
        response = urllib.request.urlopen(req, timeout=tmout)
    else:
        response = urllib.request.urlopen(req)
    data = response.read()
    try:
        data = data.decode('utf-8')
    except:
        pass
    return data

def buildUrlofTranslation(tar, sl, tk, tl):
    
    """build a url with token and target-language to get translation from any language to target language"""
    
    Url = "https://" + defaultAddress + "/translate_a/single" + "?client=t&" \
    + "sl=" + sl + "&tl=" + tl \
    + "&hl=zh-CN&" + "dt=at&" + "dt=bd&" + "dt=ex&" + "dt=ld&" + "dt=md&" + "dt=qca&" + "dt=rw&" + "dt=rm&" + "dt=ss&" + "dt=t&" \
    + "ie=UTF-8&" + "oe=UTF-8&" \
    + "clearbtn=1&" + "otf=1&" + "pc=1&" + "srcrom=0&" + "ssel=0&" + "tsel=0&" + "kc=2&" \
    + "tk=" + tk + "&" \
    + "q=" + tar
    return Url

def buildUrlofTTS(tar, tk, tl):    

    """build a url with token and target-language to get tts in target language"""
    
    Url = "https://" + defaultAddress + "/translate_tts?ie=UTF-8&q=" \
    + tar \
    + "&tl=" + tl \
    + "&total=1&idx=0&textlen=" + str(len(tar)) \
    + "&tk=" + tk \
    + "&client=webapp"
    return Url

def getTranslate(tar, sl, tk, tl):

    """return translated text with token and target-language"""
    
    tar = urllib.parse.quote(tar)
    url = buildUrlofTranslation(tar, sl, tk, tl)
    result = open_url(url)
    translatedText = "".join(tuple(x[0] if isinstance(x[0], str) else "" for x in json.loads(result)[0]))
    logger.log("Success", tar, sl, tl)
    return translatedText

def getTTS(tar, tk, tl):

    """return tts audio with token and target-language"""
    
    tar = urllib.parse.quote(tar)
    url = buildUrlofTTS(tar, tk, tl)
    result = open_url(url, tmout=3000)
    logger.log("Success", tar, tl)
    return result