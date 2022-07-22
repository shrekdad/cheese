
import sys

from pypinyin import pinyin, lazy_pinyin, Style
from pypinyin import load_phrases_dict, load_single_dict

load_phrases_dict({'碰倒': [['pèng'], ['dǎo']]})
load_phrases_dict({'用处': [['yòng'], ['chu']]})
load_phrases_dict({'弓缴': [['gōng'], ['zhuó']]})
load_phrases_dict({'亲戚': [['qīn'], ['qi']]})
load_phrases_dict({'含糊': [['hán'], ['hu']]})
load_phrases_dict({'圈养': [['juàn'], ['yǎng']]})
load_phrases_dict({'咆哮': [['páo'], ['xiào']]})
load_phrases_dict({'耽搁': [['dān'], ['ge']]})
load_phrases_dict({'帐篷': [['zhàng'], ['peng']]})
load_phrases_dict({'抽屉': [['chōu'], ['ti']]})

if len(sys.argv) != 2 :
	print('- usage: python3 p.py p71.txt')
	print('- by: shrekdad@gmail.com')
	quit()

else :

	file = open(sys.argv[1],'r')
	if file :
		a = file.read()
		file.close()
	else : 
		print("* fail to open %s",argv[1])
		quit()

lines = a.split("\n")
linesNotNil = 0
linesDone = 0
linesErr = []
print("---")

for l in lines :
	if len(l) :

		if l[0] == '#' : 
			print(l)
			continue

		linesNotNil += 1

		if "/" in l :
			if l.count("/") == 2 :
				
				sps = l.split("/")
				str = ""
				for s in sps :
					str += s

				if len(str) >= 2 :
					pys = pinyin(str)
					if len(pys) == len(str) :

						left = sps[0]
						target = l.split("/")[1].split("/")[0]
						right = sps[len(sps) - 1]
						pyTarget = ""

						if str.count(target) == 1 :

							idx = str.index(target)
							for i in range(len(target)) : 
								pyTarget += pys[idx + i][0]
								if len(target) > 0 and i != len(target) - 1 : pyTarget += " "

							res = "[P2] " + left + "/" + target + "/" + right + "#" + pyTarget
							print(res)
							linesDone += 1

						else : linesErr.append(l)
					else : linesErr.append(l)
				else : linesErr.append(l)
			else : linesErr.append(l)

		else :

			pys = pinyin(l,heteronym = len(l) == 1)
			if len(pys) == len(l) :

				if len(l) == 1 :

					print("")
					print(l)
					for p in pys[0] :
						print("- " + p)
					print("")

				else :

					res = "[P1] [ "
					for py in pys :
						res += py[0] + " "
					res += "]#" + l
					print(res)
				
				linesDone += 1

			else : linesErr.append(l)

	else : print("")

print("")
for le in linesErr :
	print(le)
print("Done: %d/%d" % (linesDone,linesNotNil))
print("---")