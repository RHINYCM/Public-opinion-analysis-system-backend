import regex as re
# import stanza
import nltk
import re
import random


topic2tags = {"general":["#Xinjiang","#xinjiang","#China", "#canada", "#uyghurs", "#uyghur", "#uighurs", "#genocide", "#muslims", "#tibet", "#hongkong", "#ccp","#communist"],
              "cotton": ["#XinjiangCotton", "#cia", "#wahabism", "#saudidictatorship", "#imperialism", "#ushypocrisy",
                         "#rightwinghypocrisy", "#doublestandards","#ccp", "#myanmar", "#magnitsky", "#hypocrasy", "#enduyghurforcedlabour", "#nike", "#hm", "#supportxinjiangcotton","#boycottnike"],
              "genocide":["#bci", "#uygur", "#abuja", "#eastturkistan","#genocideuyghur"],
              "camps":   ["#separated", "#consentratiekamp", "#genocideuyghur"],
              "olympics":["#GreatWallHero2021", "#Beijing2022", "#BeijingOlympics","#nobeijing2022"],
              "women":["#bci", "#enduyghurforcedlabour", "#china's reaction",
                        "#canadachina","#canadasanctionschina", "#chinahumanrights", "#chinasanctions", "#chinasanctionscanada","#michaelchong","#us-china", "#labourviolations", "#prc", "#uyghurwomenneedhelp"],
              "humanright":["#xinjiangcotton", "#uyghurforcedlabour", "#uyghurgenocide",
                    "#taiwan", "#netizens", "#saveuyghurs", "#uyghurhumanrights", "#uyghurweek", "#humanrights", "#ccp"],
              "muslim":["#uighurmuslim", "#forcedlabour", "#ethniccleansing", "#uighurgenocide","#enduyghurforcedlabour"],
              "faith":["#faithdrivenventurecapital", "#faithdriveninvestors", "#faithdrivenentrepreneurs", "#ccpchina",
                       "#uyghurgenocide","#islam", "#stopuyghurgenocide", "#freeuyghurs"],
              "language":["#uyghurforcedassimilation", "#fascism", "#uighurgenocide","#boycottchina", "#uyghurland"]
            }

def add_tags(sentence, topics, max_tags=3):
    r = "[_.!+-=——,$%^，。？、~@￥%……&*《》<>「」{}【】()/]"
    sen = re.sub(r, ' ', sentence)
    sen = nltk.word_tokenize(sen)
    add = []
    n = 0
    t = "general"
    for w in sen:
        if w[0] == '#':
            n += 1
            add.append(w)
        tag = '#' + w
        if tag in topic2tags[t] and n <= max_tags and tag not in add:
            add.append(tag)
            n += 1
            sentence = re.sub(w, '#'+ w, sentence)
    if n < max_tags:
        t = topics[random.randint(0,len(topics)-1)]
        tag = random.randint(0, len(topic2tags[t])-1)
        if topic2tags[t][tag] not in add:
            add.append(topic2tags[t][tag])
            sentence = sentence + ' ' + topic2tags[t][tag]

    return sentence 

# r = add_tags("we are going to #boycott the cotton from Xinjiang",["cotton"],3)
# print(r)
