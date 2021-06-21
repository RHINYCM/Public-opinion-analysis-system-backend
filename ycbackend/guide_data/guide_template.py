import random

username = ["@realTrump","@yyyyycm","@mzhou","@HuangXvdong","@jIEBAO","@LiHua"]
sentiment = random.randint(0, 1)
subtheme = [
    "cotton", "genocide", "camps", "olympics", "sterilizations", "human right",
    "muslim", "faith", "language"
]

statement1 = [
    [
        "china did not do this at xinjiang",
        "china has open its door,welcome you come to  visit xinjiang",
        "people in xinjiang live a good life, they are the same as other people in china",
        "all you said did not happen in xinjiang, those are all made up",
        "my friends in xinjiang said they has not go through that sort of thing",
        "i live in xinjiang, what you said is  actually not existent"
    ],
    [
        "xinjiang is a nice place, and welcome you come to visit",
        "it would be nice if everyone thought the same as you",
        "everyone in xinjiang is living a happy and fulfilling life",
        "i am from Xinjiang, thank you for what you said",
        "there are too many rumors about Xinjiang, making it difficult to find the truth",
        "i hope more and more people like you can support the truth"
    ]
]
statement2 = [
    [
        "your can see it at this",
        "you can read this for more information about xinjiang",
        "there are some envidence for what i say",
        "this will help you to clarify some facts",
        "if you do not believe, you can look at this",
        "pleaase click here to learn more about xinjiang"
    ],
    [
        "your can see it at this",
        "you can read this for more information about xinjiang",
        "Here's more on what's really going on in Xinjiang",
        "If you could forward this link to your friends, we would appreciate it!",
        "I hope you will also be interested in this",
        "Thank you for your support, you can read this"
    ]
]
link = [
    [
        "https://t.co/yINOiwxpEZ", "https://t.co/Wflv2fDp7Y",
        "https://t.co/XOg7lZUsuw", "https://t.co/i6CocgGd3l",
        "https://t.co/G7GiuQy6qy", "https://t.co/w1cxfmpC3O"
    ],
    [
        "https://t.co/yINOiwxpEZ", "https://t.co/Wflv2fDp7Y",
        "https://t.co/XOg7lZUsuw", "https://t.co/i6CocgGd3l",
        "https://t.co/G7GiuQy6qy", "https://t.co/w1cxfmpC3O"
    ],
]

replytemplate = [
    [
        "{username} i think your have a wrong opinion about {subtheme} in xinjing, {statement1}, {statement2} {link}",
        "{username} i think your opinon about {subtheme} in xinjing is false, {statement1}, {statement2} {link}",
        "{username} your is totally wrong on  {subtheme} in xinjing, {statement1}, {statement2} {link}",
        "{username} you made a mistake about  {subtheme} in xinjing , {statement1}, {statement2} {link}",
        "{username} your viewpoint about {subtheme} in xinjing is not true, {statement1}, {statement2} {link}",
        "{username} what you say about  {subtheme} in xinjing is fake, {statement1}, {statement2} {link}"
    ],
    [
        "{username} what you said for {subtheme} in xinjing is very good , {statement1}, {statement2} {link}",
        "{username} it's very nice of you to think so about {subtheme} in xinjing, {statement1}, {statement2} {link}",
        "{username} you are one of the few without prejudice  to {subtheme} in xinjiang, {statement1}, {statement2} {link}",
        "{username} as a Chinese, I agree with your opinion about {subtheme} in xinjiang, {statement1}, {statement2} {link}",
        "{username} your viewpoint about {subtheme} in xinjiang is totally right, {statement1}, {statement2} {link}",
        "{username} What you said about {subtheme} in xinjiang is quite reasonable , {statement1}, {statement2} {link}"
    ]
]

def makereply(theme):
    replydict = {}
    replydict["username"] = random.choice(username[sentiment])
    print(replydict["username"])
    replydict["subtheme"] = theme
    print("===========================")
    print(theme)
    print(replydict["subtheme"])
    replydict["statement1"] = random.choice(statement1[sentiment])
    replydict["statement2"] = random.choice(statement2[sentiment])
    replydict["link"] = random.choice(link[sentiment])

    reply = random.choice(replytemplate[sentiment])
    print(reply.format(**replydict))
    replytext=reply.format(**replydict)
    return replytext
