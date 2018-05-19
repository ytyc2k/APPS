#coding=utf-8
import random
wordstr='salad,jammy,pastry,blender,mustard,doughnut,crust,onion,ketchup,pudding,aperitif,caviar,pie,broth,cheese'
hzstr='色拉，涂果酱的，酥皮点心，搅拌机，芥茉，甜甜圈，面包皮，洋葱，番茄酱，布丁，开胃酒，鱼子酱，馅饼，肉汤，乳酪'
wordlst=wordstr.split(',')
hzlst=hzstr.split('，')
print(wordlst)
print(hzlst)
while True:
    # letterNum=random.randint(5,20)
    # letters=[]
    # letterStr=""
    # for x in range(letterNum):
    #   num=random.randint(65,122)
    #   while num>=91 and num<=96:  #屏蔽非字母
    #        num=random.randint(65,122)
    #   letters.append(chr(num))
    # letterStr="".join(letters)#列表转换为字符串

    randomNum=random.randint(0,len(wordlst)-1)
    letterStr=wordlst[randomNum]
    letterNum=len(letterStr)
    print("请输入以下",letterNum,"位的字符串",letterStr)
    user_input=input("请输入：")
    if user_input.strip()=='quit': break
    if len(user_input)>letterNum:
      print("输入数据有误")
    else:
      rightNum=0
      for z in range(len(user_input)):
           if user_input[z]==letterStr[z]:
               rightNum+=1
      if rightNum==letterNum:
          print("完全正确，正确率%.2f%%,翻译:%s"%((rightNum*1.0)/letterNum*100,hzlst[randomNum]))
      else:
          print("正确率%.2f%%"%((rightNum*1.0)/letterNum*100))