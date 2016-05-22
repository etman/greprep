# encoding=utf8
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')
from commons import *
import re

def extractTextInTagClass(tag, className):
    subTag = tag.find(attrs={"class": re.compile(className)})
    #print subTag
    return None if subTag is None else \
        reduce(lambda contents, text: contents + str(text), subTag).strip("\r\n ")

def lookupDictionaryCom(word, getSource=httpGet):
    def collectProperties (items, block):
        def extractDef(defSetTag):
            defNum = extractTextInTagClass(defSetTag, "def-number")
            defContent = extractTextInTagClass(defSetTag, "def-content")
            if defNum is None or defContent is None: return None
            return {"num": defNum, "content": defContent}
            
        speech = extractTextInTagClass(block, "dbox-pg")
        extractBlockDefs = [blockDef for blockDef in 
                            [extractDef(x) for x in block.findAll(attrs={"class": "def-set"})] 
                            if blockDef is not None]
        if speech is None and not extractBlockDefs: return items
        
        items.append({
            "speech": speech,
            "set": extractBlockDefs
        })
        return items

    def collectPronunciations(items, tag):
        items.append(str(tag).strip("\r\n "))
        return items
    
    def collectExamples(items, tag):
        def extractExampleSentences(exampleItemTag):
            return {
                "sentence": extractTextInTagClass(exampleItemTag, "partner-example-text"),
                "source": str(exampleItemTag.find(attrs={"class": "partner-example-credentials"}))
            }
            
        def extractExamples(sourceTag):
            return {
                "title": extractTextInTagClass(sourceTag, "source-subtitle"),
                "sentences": [extractExampleSentences(ex) for ex in sourceTag.findAll("li")]
            }
            
        data = [extractExamples(x) for x in tag.findAll(attrs={"class": re.compile("source-box")})]
        return items + data
    
    def collectExternalSources(items, tag):
        data = {
            "source": extractTextInTagClass(tag, "source-title"),
            "definitions": reduce(collectProperties, 
                           tag.findAll(attrs={"class": re.compile("def-pbk")}), 
                           [])
        }
        return items + [data]
    
    data = getSource("http://www.dictionary.com/browse/%s" % word)
    
    output = {
        "word": word,
        "definitions": parseHtml(data, {"class": re.compile("def-pbk")}, collectProperties, []),
        "pronunciation": parseHtml(data, {"name": "audio"}, collectPronunciations, []),
        "examples": parseHtml(data, {"class": re.compile("source-example-sentences")}, collectExamples, []),
        "externalSources": parseHtml(data, {"class": re.compile("source-ced\d*")}, collectExternalSources, [])
    }
    
    return output

if __name__ == "__main__":
    #=========Add system path==========
    import os, sys
    FILE_PATH = os.path.abspath(__file__)
    FILE_FOLDER = FILE_PATH[:FILE_PATH.rindex(os.sep)]
    #==================================
    print FILE_FOLDER
    def readLocalFile(word):
        with open("../../test/dictcom-talk.html") as f:
            return f.read()
        
    printJson( lookupDictionaryCom("inauguration"))
    #print json.dumps(lookupDictionaryCom())
#     with open("../../test/dictcom-talk.html", "w") as f:
#         f.write(httpGet("http://www.dictionary.com/browse/talk"))
    