import random
import re

def kunkun(text):
    if random.random() < 0.1:
        if len(text) < 150:
            text=text.upper()

    if text.find('by the way') > -1:
        if random.random() < 0.66:
            strinfo = re.compile('by the way')
            if random.random() < 0.2:
                text = strinfo.sub('BTW', text)
            else:
                text = strinfo.sub('btw', text)

    if text.find('By the way') > -1:
        if random.random() < 0.66:
            strinfo = re.compile('By the way')
            if random.random() < 0.1:
                text = strinfo.sub('BTW', text)
            else:
                text = strinfo.sub('btw', text)
        #print(text)

    if text.find('got to go') > -1:
        if random.random() < 0.9:
            strinfo = re.compile('got to go')
            text = strinfo.sub('G2G', text)
        #print(text)

    if text.find('you') > -1:
        if random.random() < 0.33:
            strinfo = re.compile('you')
            text = strinfo.sub('u', text)
        #print(text)

    if text.find('You') > -1:
        if random.random() < 0.33:
            strinfo = re.compile('You')
            text = strinfo.sub('U', text)
        #print(text)

    if text.find('Thanks') > -1:
        if random.random() < 0.8:
            strinfo = re.compile('Thanks')
            text = strinfo.sub('Thx', text)
        #print(text)

    if text.find('thanks') > -1:
        if random.random() < 0.8:
            strinfo = re.compile('thanks')
            text = strinfo.sub('thx', text)
        #print(text)

    if text.find('to ') > -1:
        if random.random() < 0.2:
            strinfo = re.compile('to ')
            text = strinfo.sub('2 ', text)
        #print(text)

    if text.find('to') > -1:
        if random.random() < 0.1:
            strinfo = re.compile('to')
            text = strinfo.sub('2', text)
        #print(text)

    if text.find('for ') > -1:
        if random.random() < 0.2:
            strinfo = re.compile('for ')
            text = strinfo.sub('4 ', text)
        #print(text)

    if text.find('be ') > -1:
        if random.random() < 0.2:
            strinfo = re.compile('be ')
            text = strinfo.sub('B ', text)
        #print(text)

    if text.find('sorry') > -1:
        if random.random() < 0.66:
            strinfo = re.compile('sorry')
            text = strinfo.sub('sry', text)
        #print(text)

    if text.find('Sorry') > -1:
        if random.random() < 0.66:
            strinfo = re.compile('Sorry')
            text = strinfo.sub('sry', text)
        #print(text)

    if text.find('please') > -1:
        if random.random() < 0.66:
            strinfo = re.compile('please')
            text = strinfo.sub('plz', text)
        #print(text)

    if text.find('Please') > -1:
        if random.random() < 0.66:
            strinfo = re.compile('Please')
            text = strinfo.sub('PLZ', text)
        #print(text)

    if text.find("don't know") > -1:
        if random.random() < 0.9:
            strinfo = re.compile("don't know")
            text = strinfo.sub('dunno', text)
        #print(text)

    if text.find('though') > -1:
        if random.random() < 0.5:
            strinfo = re.compile('though')
            text = strinfo.sub('tho', text)
        #print(text)

    if text.find('cheat') > -1:
        if random.random() < 0.66:
            strinfo = re.compile('cheat')
            text = strinfo.sub('hax', text)
        #print(text)

    if text.find('Cheat') > -1:
        if random.random() < 0.66:
            strinfo = re.compile('Cheat')
            text = strinfo.sub('Hax', text)
        #print(text)

    if text.find('because') > -1:
        if random.random() < 0.3:
            strinfo = re.compile('because')
            text = strinfo.sub('b/c', text)
        else:
            if random.random() < 0.3:
                strinfo = re.compile('because')
                text = strinfo.sub('coz', text)
        #print(text)

    if text.find('Because') > -1:
        if random.random() < 0.33:
            strinfo = re.compile('Because')
            text = strinfo.sub('B/C', text)
        #print(text)

    if text.find('see') > -1:
        if random.random() < 0.33:
            strinfo = re.compile('see')
            text = strinfo.sub('C', text)
        #print(text)

    if text.find('See') > -1:
        if random.random() < 0.33:
            strinfo = re.compile('See')
            text = strinfo.sub('C', text)
        #print(text)

    if text.find("that's") > -1:
        if random.random() < 0.2:
            strinfo = re.compile("that's")
            text = strinfo.sub('thz', text)
        #print(text)

    if text.find("are not") > -1:
        if random.random() < 0.75:
            strinfo = re.compile("are not")
            text = strinfo.sub("aren't", text)
        #print(text)

    if text.find("will not") > -1:
        if random.random() < 0.75:
            strinfo = re.compile("will not")
            text = strinfo.sub("won't", text)
        #print(text)

    if text.find("can not") > -1:
        if random.random() < 0.75:
            strinfo = re.compile("can not")
            text = strinfo.sub("can't", text)
        #print(text)

    if text.find("could not") > -1:
        if random.random() < 0.75:
            strinfo = re.compile("could not")
            text = strinfo.sub("couldn't", text)
        #print(text)

    if text.find("did not") > -1:
        if random.random() < 0.75:
            strinfo = re.compile("did not")
            text = strinfo.sub("didn't", text)
        #print(text)

    if text.find("does not") > -1:
        if random.random() < 0.75:
            strinfo = re.compile("does not")
            text = strinfo.sub("doesn't", text)
        #print(text)

    if text.find("had not") > -1:
        if random.random() < 0.75:
            strinfo = re.compile("had not")
            text = strinfo.sub("hadn't", text)
        #print(text)

    if text.find("has not") > -1:
        if random.random() < 0.75:
            strinfo = re.compile("has not")
            text = strinfo.sub("hasn't", text)
        #print(text)

    if text.find("have not") > -1:
        if random.random() < 0.75:
            strinfo = re.compile("have not")
            text = strinfo.sub("haven't", text)
        #print(text)

    if text.find("he would ") > -1:
        if random.random() < 0.75:
            strinfo = re.compile("he would ")
            text = strinfo.sub("he'd ", text)
        #print(text)

    if text.find("he will ") > -1:
        if random.random() < 0.75:
            strinfo = re.compile("he will ")
            text = strinfo.sub("he'll ", text)
        #print(text)

    if text.find("he is ") > -1:
        if random.random() < 0.75:
            strinfo = re.compile("he is ")
            text = strinfo.sub("he's ", text)
        #print(text)

    if text.find("trying") > -1:
        if random.random() < 0.75:
            strinfo = re.compile("tring")
            text = strinfo.sub("tryin", text)
        #print(text)

    if text.find("they are") > -1:
        if random.random() < 0.75:
            strinfo = re.compile("they are")
            text = strinfo.sub("they're", text)
        #print(text)

    if text.find("They are") > -1:
        if random.random() < 0.75:
            strinfo = re.compile("They are")
            text = strinfo.sub("They're", text)
        #print(text)

    if text.find("I am") > -1:
        if random.random() < 0.75:
            strinfo = re.compile("I am")
            text = strinfo.sub("I'm", text)
        #print(text)

    if text.find("I have") > -1:
        if random.random() < 0.75:
            strinfo = re.compile("I have")
            text = strinfo.sub("I've", text)
        #print(text)

    if text.find("they have") > -1:
        if random.random() < 0.75:
            strinfo = re.compile("they have")
            text = strinfo.sub("they've", text)
        #print(text)

    if text.find("They have") > -1:
        if random.random() < 0.75:
            strinfo = re.compile("They have")
            text = strinfo.sub("They've", text)
        #print(text)
    
    if text.find("she has") > -1:
        if random.random() < 0.75:
            strinfo = re.compile("she has")
            text = strinfo.sub("she's", text)
        #print(text)

    if text.find("he has") > -1:
        if random.random() < 0.75:
            strinfo = re.compile("he has")
            text = strinfo.sub("he's", text)
        #print(text)

    if text.find("let us") > -1:
        if random.random() < 0.75:
            strinfo = re.compile("let us")
            text = strinfo.sub("let's", text)
        #print(text)

    if text.find("Let us") > -1:
        if random.random() < 0.75:
            strinfo = re.compile("Let us")
            text = strinfo.sub("Let's", text)
        #print(text)

    if text.find("Lie") > -1:
        if random.random() < 1:
            strinfo = re.compile("Lie")
            text = strinfo.sub("LIE", text)
        #print(text)

    if text.find("lie") > -1:
        if random.random() < 1:
            strinfo = re.compile("lie")
            text = strinfo.sub("LIE", text)

    return text
