"""Count anime series."""
import re

count1 = 0  # 不分季统计
count2 = 0  # 分季统计
star1, star2, star3 = [], [], []
d = {'*': star1, '**': star2, '***': star3}
star12 = []
pat1 = re.compile(r'\S .*? ×(\d)', re.VERBOSE)  # 系列数检测
pat2 = re.compile(r'(\S .*?) \s{2} .*? (\*+) .*? ', re.VERBOSE)  # 单星级检测
pat3 = re.compile(r'(\S .*?) \s{2} .*? (\*+) .{2,}? (\*+) .*?', re.VERBOSE)  # 双星级检测

with open('anime_list.txt') as f:
    for line in f.readlines():
        count1 += 1
        m1 = pat1.match(line)
        m2 = pat2.match(line)
        m3 = pat3.match(line)
        count2 += int(m1.group(1)) if m1 else 1
        if m3:
            star12.append(m3.group(1))
        elif m2:
            d[m2.group(2)].append(m2.group(1))

print('不分季统计番数：' + str(count1))
print('分季统计番数：' + str(count2))
print(f'1星作品（共{len(star1)}部）：' + '；'.join(star1) + '。')
print(f'1,2星混合作品（共{len(star12)}部）：' + '；'.join(star12) + '。')
print(f'2星作品（共{len(star2)}部）：' + '；'.join(star2) + '。')
print(f'3星作品（共{len(star3)}部）：' + '；'.join(star3) + '。')