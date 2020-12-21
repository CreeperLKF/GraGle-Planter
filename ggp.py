import os, time, random
# from . import mod
import mod

"""Entrance"""

def lsp(tsmax=mod.par.timeSleepMax, tsmin=mod.par.timeSleepMin):
    time.sleep(random.random() * (tsmax - tsmin) + tsmin)

def solve(flName, tar, chain):

    """Solve single sentence"""

    if len(tar) == 0:
        with open(flName + ".txt", "w", encoding='utf-8') as otxt: pass
        with open(flName + ".mp3", "wb") as omp3: pass
        return "No content in this part"
    if len(tar) > 5000:
        return "Too much in one time (Maximum: 5000 characters)"
    mod.logger.log("Processing " + tar, chain, doTellUser=True)

    with open(flName + ".txt", "w", encoding='utf-8') as otxt:
        otxt.write(tar + '\n')
        for i in range(len(chain) - 1):
            if not (chain[i] == chain[i + 1]):
                tar = mod.ctg.getTranslate(tar, chain[i], mod.tokenHolder.getToken(tar), chain[i + 1])
                otxt.write(tar + '\n')
                mod.logger.log("Translated " + tar, str(int(i * 100 / (len(chain) - 1))) + "%", doTellUser=True)
                lsp()

    if chain[-1] in mod.par.availableTTSLanguage:
        with open(flName + ".mp3", "wb") as omp3:
            omp3.write(mod.ctg.getTTS(tar, mod.tokenHolder.getToken(tar), chain[-1]))
            mod.logger.log("TTS " + tar + " OK", doTellUser=True)
            lsp()

    mod.logger.log("Write " + tar + " 100%", doTellUser=True)
    return tar + " 100%"

def buildChain(inp, ch, outp):
    
    """build a translate chain from input language to target language"""
    
    ret = [random.choice(tuple(mod.par.availableTranslationLanguage.keys())) if x == "ran" else x\
        for x in [inp] + ch]
    ret.append(random.choice(mod.par.availableTTSLanguage) if outp == "ran" else outp)
    return ret

def mergeFile(dirName, ltxt, mergeMp3):
    with open(dirName + "/0.txt", "w", encoding='utf-8') as otxt:
        for i in range(ltxt):
            with open(dirName + '/' + str(i + 1) + ".txt", encoding='utf-8') as itxt:
                otxt.write(itxt.readlines()[-1])
    mod.logger.log("Text Merged", doTellUser=True)
    
    if mergeMp3:
        from pydub import AudioSegment
        imp3 = list(AudioSegment.from_mp3(dirName + '/' + str(i + 1) + ".mp3") for i in range(ltxt))
        imp3_tdb = max(imp3, key = lambda x : x.dBFS).dBFS
        for i in range(len(imp3)):
            imp3[i] += imp3_tdb - imp3[i].dBFS
        omp3 = sum(imp3)
        omp3.export(dirName + "/0.mp3", format="mp3")
        mod.logger.log("mp3 Merged", doTellUser=True)
    else:
        mod.logger.log("mp3 not Merged", doTellUser=True)

def work(CMD):

    """recieve resolved arguments and split text and build chain to call solve"""

    txt = open(CMD["filename"], "r", encoding='utf-8').read() # haven't been close
    dirName = CMD["filename"] + "_output"
    if not os.path.exists(dirName):
        os.mkdir(dirName)
    if CMD["cut"]: txt = list(txt.replace('\n', CMD["cut"]).split(CMD["cut"])) 
    else: txt = [txt.replace('\n', '.'), ]
    while True:
        try:
            txt.remove("")
        except:
            break  
    txt = tuple(txt)
    mod.logger.log(txt)

    for i, tar in enumerate(txt):
        flName = dirName + '/' + str(i + 1)
        if os.path.exists(flName + ".txt"):
            mod.logger.log(flName + ".txt Already exists, skipped", doTellUser=True)
            continue
        mod.logger.log(solve(flName, tar, buildChain(CMD["input"], CMD["chain"], CMD["output"])))
        lsp()

    mergeFile(dirName, len(txt), CMD["merge"])

    return str(CMD) + " Success"

def main():

    """Plant Grass here"""

    # print debug text here
    CMD = mod.rcmd.resolveCommandLine()
    mod.logger.log(CMD, doTellUser=True)
    if isinstance(CMD, dict):
        mod.logger.log(work(CMD), doTellUser=True)

if __name__ == "__main__":
    main()