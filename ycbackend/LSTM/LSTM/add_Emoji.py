import random
import emoji


thankful = [':smile:', ':laughing:', ':blush:', ':smiley:', ':joy:', ':)', ':kissing_heart:',
                ':kissing_closed_eyes:', ':heart:', ':two_hearts:', ':sparkling_heart:', ':+1:']
happy = [':smile:', ':laughing:', ':blush:', ':smiley:', ':joy:', ':)', ':heart_eyes:', ':kissing_heart:',
             ':kissing_closed_eyes:', ':heart:', ':two_hearts:']
complaining = [':smirk:', ':sweat_smile:', ':grinning_face_with_sweat:']
angry = [':rage:', ':triumph:', ':anger:', ':punch:']
like = [':heart_eyes:', ':kissing_heart:', ':kissing_closed_eyes:', ':heart:', ':two_hearts:']
sad = [':cry:', ':sob:', ':broken_heart:', ':unamused:', ':confounded:', ':face_with_head-bandage:']
disgusting = [':fearful:', ':cold_sweat:', ':scream:']
fearful = [':fearful:', ':cold_sweat:', ':scream:', ':eyes:']
# country = [':cn:', ':us:']
yygq = [':zany_face:', ':confused:', ':face_with_rolling_eyes:', ':face_with_raised_eyebrow:', ':sweat_smile:', ':sleeping:']

all_emoji = thankful + happy + complaining + angry + like + sad + disgusting + fearful + yygq



def add_emoji(str):
    n = random.randint(0, len(all_emoji) - 1)
    emoji_chosen = all_emoji[n]
    emj = emoji.emojize('{}'.format(emoji_chosen), use_aliases=True)
    print(str + emj)
    return str + emj

def main():
    argv1 = "ababababa"
    with_emoji = add_emoji(argv1)

if __name__ == '__main__':
    main();