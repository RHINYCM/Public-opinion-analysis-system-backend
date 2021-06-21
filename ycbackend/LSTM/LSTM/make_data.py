import emoji
import re
import collections
import random
import csv

def make_data(file):
    f = open(file, 'r', encoding='utf-8')
    words = f.readlines()[1:]
    segs = []
    for line in words:
        segs.append(','.join(line.split(',')[1:]).strip('\n').strip('"'))
    return segs

def make_data_out(list ,filename):
    '''f = open(filename, 'w', encoding='utf-8')
    for line in list:
        f.write(line + '\n')'''
    with open(filename, 'w', encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['abstract', 'categories'])
        for line in list:
            writer.writerow(line)  # 这里要以list形式写入，writer会在新建的csv文件中，一行一行写入

def make_data_single(lines, filename):
    global lable_high, lable_num
    prog = re.compile(r':.*?:')
    new_lines = []
    for i in range(len(lines)):
        print(i)
        temp = emoji.demojize(lines[i], use_aliases=True)
        # print(temp)
        word = prog.search(temp)
        words = []
        if word is not None:
            while (word is not None and word.group() != '::' and word.group() != ': :' and len(word.group()) < 20):
                words.append(word.group())
                temp = temp.replace(words[-1], '')
                word = prog.search(temp)
            # 去除重复元素
            if words == []:
                continue
            words = list(collections.Counter(words))
            #words = [('__label__'+i) for i in words]
            new_words = []
            for i in words:
                if i in lable_high:
                    new_words.append(i)
            if new_words == []:
                continue
            #new_words = [i for i in lable_high if i in new_words]
            new_new_words = []
            for i in lable_high:
                if i in new_words:
                    new_new_words.append(i)
            for i in new_new_words:
                if lable_num[i] < 400:
                    new_lines.append([temp, i])
                    lable_num[i] += 1
                    break
            #new_lines.append([temp, ','.join(new_words)])
            #new_lines.append([temp, ','.join(words)])
            '''for j in words:
                new_lines.append([temp, j])'''
    make_data_out(new_lines, filename)

if __name__ == '__main__':
    global lable_high, lable_num
    lable_high = [':joy:', ':thinking_face:', ':point_down:', ':flag_for_China:', ':thumbsup:', ':heart:', ':sweat_smile:', ':pray:', ':arrow_down:', ':clown_face:', ':sob:', ':point_right:', ':rage:', ':fire:', ':eyes:', ':wink:', ':grin:', ':clap:', ':smile:', ':rotating_light:', ':blush:', ':zany_face:', ':satisfied:', ':grinning:', ':cry:', ':smirk:', ':shit:', ':upside__down_face:', ':sunglasses:', ':face_with_monocle:', ':innocent:', ':scream:', ':man_shrugging:', ':sparkles:', ':grimacing:', ':heart_eyes:', ':arrow_right:', ':smiley:', ':thumbsdown:', ':man_facepalming:', ':flushed:', ':face_vomiting:', ':zzz:', ':zap:', ':purple_heart:', ':green_heart:', ':pig_face:', ':arrow_forward:', ':airplane:', ':dizzy:', ':snowflake:', ':japanese_goblin:', ':robot_face:', ':red_car:', ':skull:', ':grapes:', ':black_heart:', ':muscle:', ':star-struck:', ':unamused:', ':nail_care:', ':volcano:', ':lying_face:', ':warning:', ':yum:', ':rooster:', ':hamster:', ':cupid:', ':pineapple:', ':ice_cream:', ':carousel_horse:', ':person_juggling:', ':rhinoceros:', ':angel:', ':red_circle:', ':broken_heart:', ':kissing_heart:', ':relieved:', ':hugging_face:', ':basketball:', ':exploding_head:', ':neutral_face:', ':fist:', ':pensive:', ':link:', ':earth_americas:', ':relaxed:', ':person_shrugging:', ':question:', ':woman_shrugging:', ':rose:', ':100:', ':moneybag:', ':loudspeaker:', ':angry:', ':boom:', ':shushing_face:', ':stuck_out_tongue:', ':pushpin:', ':expressionless:']
    lable_high = lable_high[:43]
    lable_high.reverse()
    lable_num = {}
    for lable in lable_high:
        lable_num[lable] = 0
    lines = make_data('emoji_tweets1.csv')
    #打乱语句顺序
    random.shuffle(lines)
    make_data_single(lines, 'data/all.csv')

    label_dict = {}
    label_high = []
    csv_reader = csv.reader(open('data/all.csv', encoding='utf-8'))
    for row in csv_reader:
        temp = row[1].split(',')
        for i in temp:
            if i not in label_dict:
                label_dict[i] = 1
            else:
                label_dict[i] += 1

    label_dict = sorted(label_dict.items(), key=lambda x: x[1], reverse=True)
    f = open('data/highwords_new.txt', 'w', encoding='utf-8')
    for i in range(len(label_dict)):
        print(label_dict[i])
        f.write(str(label_dict[i]) + '\n')
        label_high.append(label_dict[i][0])
    print(label_high)

    f.write(str(label_high))
    # taxi.csv最好放在同一目录下
