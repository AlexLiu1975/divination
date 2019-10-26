# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 01:37:10 2019

@author: Alex
"""

# print('易經卜筮--先天易數....')
# 2019/10/27  第一版


print('一、先天盤')
print('--------------------------------------------------')
print('1: 乾宮(進學、命運、讀書、晴雨、取討、科舉、求醫、招婿)')
print('2: 兌宮(移居、病症、房屋、會事、父病、天花、分家、謀事)')
print('3: 離宮(借財、求財、買畜、賭博、放帳、開店、回鄉、墳墓)')
print('4: 震宮(口舌、出行、入贅、捕魚、秋收、尋館、求子、夜夢)')
print('5: 巽宮(見貴、生意、訴狀、起造、春蠶、文憑、解糧、脫貨)')
print('6: 坎宮(納監、婚姻、尋人、陞遷、和事、六甲、取妾、交易)')
print('7: 艮宮(家信、田產、買貨、討僕、納吏、告狀、求官、跟官)')
print('8: 坤宮(合夥、家宅、壽元、失物、行人、手藝、解人、走失)')
print('--------------------------------------------------')
 
firstInt = int(input('請由下選擇欲占卜之事數字1~8: '))
firstDic = {'乾卦':1, '兌卦':2, '離卦':3, '震卦':4, '巽卦':5, '坎卦':6, '艮卦':7, '坤卦':8}
#print(firstDic.values(firstInt))
print('上卦: %d' %firstInt)
 
print('二、後天盤')
print('--------------------------------------------------')
print('1: 乾宮(移居、求財、壽元、晴雨、陞遷、脫貨、田產、秋收)')
print('2: 兌宮(尋人、進學、家信、會事、尋館、見貴、家宅、借財)')
print('3: 離宮(求子、讀書、合夥、春蠶、買畜、謀事、納監、納吏)')
print('4: 震宮(出行、開店、失物、告狀、解糧、和事、取討、父病)')
print('5: 巽宮(房屋、婚姻、走失、買貨、起造、招婿、回鄉、捕魚)')
print('6: 坎宮(求官、命運、生意、夜夢、行人、分家、放帳、六甲)')
print('7: 艮宮(交易、病症、入贅、手藝、跟官、求醫、文憑、墳墓)')
print('8: 坤宮(科舉、口舌、取妾、賭博、討僕、訴狀、解人、天花)')
print('--------------------------------------------------')
 
secondInt = int(input('請由下選擇欲占卜之事數字1~8: '))
print('下卦: %d' %secondInt) 
#挨星盤
thirdInt = int(input('請由1~8之中選1個數字...'))
print('上數: ', thirdInt)
 
#判斷先天盤
if firstInt == 1:  #乾一
    if thirdInt == 1:
        firstFinal = 1
        print('中數:  %d, 乾一' %firstFinal)
    elif thirdInt == 2:
        firstFinal = 6
        print('中數:  %d, 坎六' %firstFinal)
    elif thirdInt == 3:
        firstFinal = 7
        print('中數:  %d, 艮七' %firstFinal)
    elif thirdInt == 4:
        firstFinal = 4
        print('中數:  %d, 震四' %firstFinal)
    elif thirdInt == 5:
        firstFinal = 5
        print('中數:  %d, 巽五' %firstFinal)
    elif thirdInt == 6:
        firstFinal = 3
        print('中數:  %d, 離三' %firstFinal)
    elif thirdInt == 7:
        firstFinal = 8
        print('中數:  %d, 坤八' %firstFinal)
    elif thirdInt == 8:
        firstFinal = 2
        print('中數:  %d, 兌二' %firstFinal)
elif firstInt == 2:  #兌二
    if thirdInt == 1:
        firstFinal = 2
        print('中數:  %d, 兌二' %firstFinal)
    elif thirdInt == 2:
        firstFinal = 1
        print('中數:  %d, 乾一' %firstFinal)
    elif thirdInt == 3:
        firstFinal = 6
        print('中數:  %d, 坎六' %firstFinal)
    elif thirdInt == 4:
        firstFinal = 7
        print('中數:  %d, 艮七' %firstFinal)
    elif thirdInt == 5:
        firstFinal = 4
        print('中數:  %d, 震四' %firstFinal)
    elif thirdInt == 6:
        firstFinal = 5
        print('中數:  %d, 巽五' %firstFinal)
    elif thirdInt == 7:
        firstFinal = 3
        print('中數:  %d, 離三' %firstFinal)
    elif thirdInt == 8:
        firstFinal = 8
        print('中數:  %d, 坤八' %firstFinal)
elif firstInt == 3:  #離三
    if thirdInt == 1:
        firstFinal = 3
        print('中數:  %d, 離三' %firstFinal)
    elif thirdInt == 2:
        firstFinal = 8
        print('中數:  %d, 坤八' %firstFinal)
    elif thirdInt == 3:
        firstFinal = 2
        print('中數:  %d, 兌二' %firstFinal)
    elif thirdInt == 4:
        firstFinal = 1
        print('中數:  %d, 乾一' %firstFinal)
    elif thirdInt == 5:
        firstFinal = 6
        print('中數:  %d, 坎六' %firstFinal)
    elif thirdInt == 6:
        firstFinal = 7
        print('中數:  %d, 艮七' %firstFinal)
    elif thirdInt == 7:
        firstFinal = 4
        print('中數:  %d, 震四' %firstFinal)
    elif thirdInt == 8:
        firstFinal = 5
        print('中數:  %d, 巽五' %firstFinal)
elif firstInt == 4:  #震四
    if thirdInt == 1:
        firstFinal = 4
        print('中數:  %d, 震四' %firstFinal)
    elif thirdInt == 2:
        firstFinal = 5
        print('中數:  %d, 巽五' %firstFinal)
    elif thirdInt == 3:
        firstFinal = 3
        print('中數:  %d, 離三' %firstFinal)
    elif thirdInt == 4:
        firstFinal = 8
        print('中數:  %d, 坤八' %firstFinal)
    elif thirdInt == 5:
        firstFinal = 2
        print('中數:  %d, 兌二' %firstFinal)
    elif thirdInt == 6:
        firstFinal = 1
        print('中數:  %d, 乾一' %firstFinal)
    elif thirdInt == 7:
        firstFinal = 6
        print('中數:  %d, 坎六' %firstFinal)
    elif thirdInt == 8:
        firstFinal = 7
        print('中數:  %d, 艮七' %firstFinal)
elif firstInt == 5:  #巽五
    if thirdInt == 1:
        firstFinal = 5
        print('中數:  %d, 巽五' %firstFinal)
    elif thirdInt == 2:
        firstFinal = 3
        print('中數:  %d, 離三' %firstFinal)
    elif thirdInt == 3:
        firstFinal = 8
        print('中數:  %d, 坤八' %firstFinal)
    elif thirdInt == 4:
        firstFinal = 2
        print('中數:  %d, 兌二' %firstFinal)
    elif thirdInt == 5:
        firstFinal = 1
        print('中數:  %d, 乾一' %firstFinal)
    elif thirdInt == 6:
        firstFinal = 6
        print('中數:  %d, 坎六' %firstFinal)
    elif thirdInt == 7:
        firstFinal = 7
        print('中數:  %d, 艮七' %firstFinal)
    elif thirdInt == 8:
        firstFinal = 4
        print('中數:  %d, 震四' %firstFinal)        
elif firstInt == 6:  #坎六
    if thirdInt == 1:
        firstFinal = 1
        print('中數:  %d, 坎六' %firstFinal)
    elif thirdInt == 2:
        firstFinal = 7
        print('中數:  %d, 艮七' %firstFinal)
    elif thirdInt == 3:
        firstFinal = 4
        print('中數:  %d, 震四' %firstFinal)
    elif thirdInt == 4:
        firstFinal = 5
        print('中數:  %d, 巽五' %firstFinal)
    elif thirdInt == 5:
        firstFinal = 3
        print('中數:  %d, 離三' %firstFinal)
    elif thirdInt == 6:
        firstFinal = 8
        print('中數:  %d, 坤八' %firstFinal)
    elif thirdInt == 7:
        firstFinal = 2
        print('中數:  %d, 兌二' %firstFinal)
    elif thirdInt == 8:
        firstFinal = 1
        print('中數:  %d, 乾一' %firstFinal)
elif firstInt == 7:  #艮七
    if thirdInt == 1:
        firstFinal = 7
        print('中數:  %d, 艮七' %firstFinal)
    elif thirdInt == 2:
        firstFinal = 4
        print('中數:  %d, 震四' %firstFinal)
    elif thirdInt == 3:
        firstFinal = 5
        print('中數:  %d, 巽五' %firstFinal)
    elif thirdInt == 4:
        firstFinal = 3
        print('中數:  %d, 離三' %firstFinal)
    elif thirdInt == 5:
        firstFinal = 8
        print('中數:  %d, 坤八' %firstFinal)
    elif thirdInt == 6:
        firstFinal = 2
        print('中數:  %d, 兌二' %firstFinal)
    elif thirdInt == 7:
        firstFinal = 1
        print('中數:  %d, 乾一' %firstFinal)
    elif thirdInt == 8:
        firstFinal = 6
        print('中數:  %d, 坎六' %firstFinal)
elif firstInt == 8:  #坤八
    if thirdInt == 1:
        firstFinal = 8
        print('中數:  %d, 坤八' %firstFinal)
    elif thirdInt == 2:
        firstFinal = 2
        print('中數:  %d, 兌二' %firstFinal)
    elif thirdInt == 3:
        firstFinal = 1
        print('中數:  %d, 乾一' %firstFinal)
    elif thirdInt == 4:
        firstFinal = 6
        print('中數:  %d, 坎六' %firstFinal)
    elif thirdInt == 5:
        firstFinal = 7
        print('中數:  %d, 艮七' %firstFinal)
    elif thirdInt == 6:
        firstFinal = 4
        print('中數:  %d, 震四' %firstFinal)
    elif thirdInt == 7:
        firstFinal = 5
        print('中數:  %d, 巽五' %firstFinal)
    elif thirdInt == 8:
        firstFinal = 3
        print('中數:  %d, 離三' %firstFinal)

        
#判斷後天盤
if secondInt == 1:  #乾一
    if thirdInt == 1:
        secondFinal = 1
        print('中數:  %d, 乾一' %secondFinal)
    elif thirdInt == 2:
        secondFinal = 6
        print('中數:  %d, 坎六' %secondFinal)
    elif thirdInt == 3:
        secondFinal = 7
        print('中數:  %d, 艮七' %secondFinal)
    elif thirdInt == 4:
        secondFinal = 4
        print('中數:  %d, 震四' %secondFinal)
    elif thirdInt == 5:
        secondFinal = 5
        print('中數:  %d, 巽五' %secondFinal)
    elif thirdInt == 6:
        secondFinal = 3
        print('中數:  %d, 離三' %secondFinal)
    elif thirdInt == 7:
        secondFinal = 8
        print('中數:  %d, 坤八' %secondFinal)
    elif thirdInt == 8:
        secondFinal = 2
        print('中數:  %d, 兌二' %secondFinal)
elif secondInt == 2:  #兌二
    if thirdInt == 1:
        secondFinal = 2
        print('中數:  %d, 兌二' %secondFinal)
    elif thirdInt == 2:
        secondFinal = 1
        print('中數:  %d, 乾一' %secondFinal)
    elif thirdInt == 3:
        secondFinal = 6
        print('中數:  %d, 坎六' %secondFinal)
    elif thirdInt == 4:
        secondFinal = 7
        print('中數:  %d, 艮七' %secondFinal)
    elif thirdInt == 5:
        secondFinal = 4
        print('中數:  %d, 震四' %secondFinal)
    elif thirdInt == 6:
        secondFinal = 5
        print('中數:  %d, 巽五' %secondFinal)
    elif thirdInt == 7:
        secondFinal = 3
        print('中數:  %d, 離三' %secondFinal)
    elif thirdInt == 8:
        secondFinal = 8
        print('中數:  %d, 坤八' %secondFinal)
elif secondInt == 3:  #離三
    if thirdInt == 1:
        secondFinal = 3
        print('中數:  %d, 離三' %secondFinal)
    elif thirdInt == 2:
        secondFinal = 8
        print('中數:  %d, 坤八' %secondFinal)
    elif thirdInt == 3:
        secondFinal = 2
        print('中數:  %d, 兌二' %secondFinal)
    elif thirdInt == 4:
        secondFinal = 1
        print('中數:  %d, 乾一' %secondFinal)
    elif thirdInt == 5:
        secondFinal = 6
        print('中數:  %d, 坎六' %secondFinal)
    elif thirdInt == 6:
        secondFinal = 7
        print('中數:  %d, 艮七' %secondFinal)
    elif thirdInt == 7:
        secondFinal = 4
        print('中數:  %d, 震四' %secondFinal)
    elif thirdInt == 8:
        secondFinal = 5
        print('中數:  %d, 巽五' %secondFinal)
elif secondInt == 4:  #震四
    if thirdInt == 1:
        secondFinal = 4
        print('中數:  %d, 震四' %secondFinal)
    elif thirdInt == 2:
        secondFinal = 5
        print('中數:  %d, 巽五' %secondFinal)
    elif thirdInt == 3:
        secondFinal = 3
        print('中數:  %d, 離三' %secondFinal)
    elif thirdInt == 4:
        secondFinal = 8
        print('中數:  %d, 坤八' %secondFinal)
    elif thirdInt == 5:
        secondFinal = 2
        print('中數:  %d, 兌二' %secondFinal)
    elif thirdInt == 6:
        secondFinal = 1
        print('中數:  %d, 乾一' %secondFinal)
    elif thirdInt == 7:
        secondFinal = 6
        print('中數:  %d, 坎六' %secondFinal)
    elif thirdInt == 8:
        secondFinal = 7
        print('中數:  %d, 艮七' %secondFinal)
elif secondInt == 5:  #巽五
    if thirdInt == 1:
        secondFinal = 5
        print('中數:  %d, 巽五' %secondFinal)
    elif thirdInt == 2:
        secondFinal = 3
        print('中數:  %d, 離三' %secondFinal)
    elif thirdInt == 3:
        secondFinal = 8
        print('中數:  %d, 坤八' %secondFinal)
    elif thirdInt == 4:
        secondFinal = 2
        print('中數:  %d, 兌二' %secondFinal)
    elif thirdInt == 5:
        secondFinal = 1
        print('中數:  %d, 乾一' %secondFinal)
    elif thirdInt == 6:
        secondFinal = 6
        print('中數:  %d, 坎六' %secondFinal)
    elif thirdInt == 7:
        secondFinal = 7
        print('中數:  %d, 艮七' %secondFinal)
    elif thirdInt == 8:
        secondFinal = 4
        print('中數:  %d, 震四' %secondFinal)        
elif secondInt == 6:  #坎六
    if thirdInt == 1:
        secondFinal = 1
        print('中數:  %d, 坎六' %secondFinal)
    elif thirdInt == 2:
        secondFinal = 7
        print('中數:  %d, 艮七' %secondFinal)
    elif thirdInt == 3:
        secondFinal = 4
        print('中數:  %d, 震四' %secondFinal)
    elif thirdInt == 4:
        secondFinal = 5
        print('中數:  %d, 巽五' %secondFinal)
    elif thirdInt == 5:
        secondFinal = 3
        print('中數:  %d, 離三' %secondFinal)
    elif thirdInt == 6:
        secondFinal = 8
        print('中數:  %d, 坤八' %secondFinal)
    elif thirdInt == 7:
        secondFinal = 2
        print('中數:  %d, 兌二' %secondFinal)
    elif thirdInt == 8:
        secondFinal = 1
        print('中數:  %d, 乾一' %secondFinal)
elif secondInt == 7:  #艮七
    if thirdInt == 1:
        secondFinal = 7
        print('中數:  %d, 艮七' %secondFinal)
    elif thirdInt == 2:
        secondFinal = 4
        print('中數:  %d, 震四' %secondFinal)
    elif thirdInt == 3:
        secondFinal = 5
        print('中數:  %d, 巽五' %secondFinal)
    elif thirdInt == 4:
        secondFinal = 3
        print('中數:  %d, 離三' %secondFinal)
    elif thirdInt == 5:
        secondFinal = 8
        print('中數:  %d, 坤八' %secondFinal)
    elif thirdInt == 6:
        secondFinal = 2
        print('中數:  %d, 兌二' %secondFinal)
    elif thirdInt == 7:
        secondFinal = 1
        print('中數:  %d, 乾一' %secondFinal)
    elif thirdInt == 8:
        secondFinal = 6
        print('中數:  %d, 坎六' %secondFinal)
elif secondInt == 8:  #坤八
    if thirdInt == 1:
        secondFinal = 8
        print('中數:  %d, 坤八' %secondFinal)
    elif thirdInt == 2:
        secondFinal = 2
        print('中數:  %d, 兌二' %secondFinal)
    elif thirdInt == 3:
        secondFinal = 1
        print('中數:  %d, 乾一' %secondFinal)
    elif thirdInt == 4:
        secondFinal = 6
        print('中數:  %d, 坎六' %secondFinal)
    elif thirdInt == 5:
        secondFinal = 7
        print('中數:  %d, 艮七' %secondFinal)
    elif thirdInt == 6:
        secondFinal = 4
        print('中數:  %d, 震四' %secondFinal)
    elif thirdInt == 7:
        secondFinal = 5
        print('中數:  %d, 巽五' %secondFinal)
    elif thirdInt == 8:
        secondFinal = 3
        print('中數:  %d, 離三' %secondFinal)

total = str(thirdInt)+str(firstFinal)+str(secondFinal)
print(type(int(total)))

#卦辭
#1.晴雨─問天氣好壞
if int(total) == 111:
    print('乾卦  天雨問晴天必雨,天晴問雨主天晴,若要雨零看亥子,晴多雨少數分明.')
elif int(total) == 266:
    print('坎卦  若問天晴天必晴,若詢不予雨來霖,坎逢壬癸亥陰雨,要晴但看戌申庚.')
elif int(total) == 377:
    print('艮卦  問卜天晴難許晴,庚辛卯午更傾盆,久晴問雨難求雨,久雨問晴未必晴.')
elif int(total) == 444:
    print('震卦  人間終日雨淋漓,天道陰陽沒定期,到底雨多晴日少,時逢三七九可除.')
elif int(total) == 555:
    print('巽卦  欲問天晴天不晴,東南方上有青雲,若還問雨寅申見,雨少晴多卦有靈.')
elif int(total) == 633:  
    print('離卦  離宮太旺太陰明,晴雨而今眼見晴,若是久晴還有雨,時逢甲子雨又晴.')
elif int(total) == 788:
    print('坤卦  卦占久雨問晴天,雨怕雲行頃刻間,欲問天晴晴不久,霈然一陣又連纏.')
elif int(total) == 822:
    print('兌卦  金能生水雨淋林,欲問天晴天不晴,若要晴時寅午戌,晴多雨少數分明.')

#2.進學─問升學考試運勢
elif int(total) == 112:
    print('履卦  進學占之履卦爻,文書官鬼兩相交,才名二字成推薦,定主他年在錦標.')
elif int(total) == 261:
    print('需卦  官爻生世好求名,入學占之許遂心,策論經書如勉勵,定教科舉有聲名.')
elif int(total) == 376:
    print('蒙卦  恩成士業已升堂,選入芹宮姓氏香,小試宮廷求薦拔,文書端的射星光.')
elif int(total) == 447:
    print('小過卦  妻財持世必超群,入學占之遂稱心,行遠登高從此起,他年還許步青雲.')
elif int(total) == 554:
    print('益卦  應來生世喜非常,入學占之定有功,上下貴人皆得力,管教拔選入黌宮.')
elif int(total) == 635:
    print('鼎卦  來占進學弟兄興,絕好文章見不明,一任細思空得意,運中不利枉勞心.')
elif int(total) == 783:
    print('明夷卦  鬼爻持世破文書,入學占之恐不如,秋夏二季猶可望,春冬還要再遲遲.')
elif int(total) == 828:   
    print('萃卦  文書有氣卦生憂,世位逢沖是不同,欲問功名芹淑裡,當回窗下且藏修.')

#3.讀書─問再進修前途
elif int(total) == 113:
    print('同人卦  鬼爻持世卦相同,又許讀書望進身,從此功名終可望,須知入泮有鴻名.')
elif int(total) == 268:
    print('比卦  經綸事業聖賢書,讀書事業可堪圖,官臨世位文星旺,選入功名住帝邦.')
elif int(total) == 372:
    print('損卦  讀書又許恩臨身,印綬相生得稱心,選入芹宮蒙作養,年逢水火得揚名.')
elif int(total) == 441:
    print('大壯卦  鬼應文書來應位,讀書成就實無疑,占來定許業成就,木火之年折桂枝.')
elif int(total) == 556:
    print('渙卦  世應重重兄弟存,子孫臨應可施行,讀書修己功夫進,學業才高自顯明.')
elif int(total) == 637:
    print('旅卦  鬼爻無位不為佳,學業占之未足誇,若要讀書需命湊,財源方許擁烏紗.')
elif int(total) == 784:
    print('復卦  君占此卦問功名,隔角重重總不如,雖是文章成錦繡,也還是個白衣儒.')
elif int(total) == 825:
    print('大過卦  占卦知君欲讀書,應來生世世相扶,巳酉丑年前進步,勸君熟讀五車書.')

#4.取討─問債物能否要到
elif int(total) == 114: 
    print('無妄卦  求物求財先覺難,爻中財盡始相還,秋冬初討無財物,夏季春時不耐煩.')
elif int(total) == 265:
    print('井卦  取討資財此卦靈,託中求取事堪成,雖是月前多阻隔,遲遲方許有佳音.')
elif int(total) == 373: 
    print('賁卦  財初上卦最為奇,欲去取討不必疑,即在目下須作速,遲遲又恐不得齊.')
elif int(total) == 448: 
    print('豫卦  取討資財兩見之,只宜急速不宜遲,三分財氣時方許,七分財氣尚遲遲.')
elif int(total) == 552: 
    print('中孚卦  占問取討事遂心,從今財物自然增,求謀遂意無攔阻,申子辰日見祥正.')
elif int(total) == 631: 
    print('大有卦  虛名虛利久沉沉,取討財物未遂心,癡心指望圖前進,待等運動鐵成心.')
elif int(total) == 786: 
    print('師卦  應高父母喜相逢,取討財物目下過,還須托人方可遂,途中休聽小人言.')
elif int(total) == 827: 
    print('咸卦  卦中喜見兩重財,取討之時實美哉,七分財氣重重見,管教庚寅得利來.')

#5.招婿─問未來女婿、媳婦
elif int(total) == 115:
    print('姤卦  招婿未成來問卜,誰知好事多反覆,應來生世得成全,福祿悠然終分宿.')
elif int(total) == 263:
    print('既濟卦  卦占招婿最為良,財喜重重福祿強,夫婦相諧多福壽,興家立業好呈祥.')
elif int(total) == 378:
    print('剝卦  招婿占之事更佳,妻財子祿實堪誇,將來得此成家計,數卜先天定不差.')
elif int(total) == 442:
    print('歸妹卦  卦占歸妹未堪誇,欲占招婿有參差,若是今日圖容易,久後方知有怨嗟.')
elif int(total) == 551:
    print('小畜卦  招婿占之枉費心,子孫受剋已無情,若還應重龍子選,方許成家立太平.')
elif int(total) == 636:
    print('未濟卦  招婿占之得乾爻,福祿妻財兩見交,未濟之中終有濟,晚年有靠此為高.')
elif int(total) == 787:
    print('謙卦  招婿占之卦甚宜,子孫持世有扶持,謙平受益生利祿,親者為媒不必疑.')
elif int(total) == 824:
    print('隨卦  卦中占婿有躊躇,應位高兮世位低,凡事皆因忙裡過,不知別選且相宜.')

#6.命運─問一生運勢
elif int(total) == 116:
    print('訟卦  往來命運固非宜,人旺財興值此時,發福興家多遂意,貴人相遇有扶持.')
elif int(total) == 267:
    print('蹇卦  命運何須問短長,喜君運限莫相商,雖然早運多成敗,時來應知福壽長.')
elif int(total) == 374:
    print('頤卦  榮枯得失皆由命,壽夭窮通總在天,欲卜五行消息事,晚年命運勝中年.')
elif int(total) == 445:
    print('恆卦  君問窮通不必疑,將來造化卻何如,十年好運才行起,家富人康百事為.')
elif int(total) == 553:
    print('家人卦  命運何須說詳細,眼前造化已非常,再能積德行方便,子子孫孫福祿長.')
elif int(total) == 638:
    print('晉卦  一世勞苦皆是命,數年勞困總有天,謀而不遂休生怨,再過三春福祿全.')
elif int(total) == 782:
    print('臨卦  命運占之實美哉,知君否極泰將來,謀為數載多難遂,今歲秋冬財迎來.')
elif int(total) == 821:
    print('夬卦  占卜知君問五行,眼前造化正豐盈,六爻安靜星辰旺,官鬼無傷福壽增.')

#7.請醫─問尋醫求方
elif int(total) == 117:
    print('遯卦  縱有名良醫國手,厭厭未見退災憂,若逢應位來生世,甲寅之日救星臨.')
elif int(total) == 264:
    print('屯卦  醫憑福德可持身,福不來扶藥不靈,服藥無緣多楚楚,再逢扁鵲也難成.')
elif int(total) == 375:
    print('蠱卦  醫藥無蹤且慢醫,鬼臨世位有蹊蹺,厭厭疾病遲遲愈,求去神藥不扶持.')
elif int(total) == 443:
    print('豐卦  醫來剋病病無妨,可有靈丹即便良,始信仙傳醫國手,寅申巳亥保安康.')
elif int(total) == 558:
    print('觀卦  迎醫行事兩利同,柔位平平病不凶,觀我終身君子道,須知不藥自然通.')
elif int(total) == 632:
    print('睽卦  急占忙忙卜請醫,應來生世不需疑,持身福德醫常致,必遇良醫愈有期.')
elif int(total) == 781:
    print('泰卦  求醫治病不愁凶,福德臨醫定有功,只待交冬方可脫,好將禮物謝郎中.')
elif int(total) == 826:
    print('困卦  君欲求醫卦欠靈,應來生世病源深,當初不禱生嗟怨,服藥如何去病根.')

#8.科舉─問參加各類國家考試運勢
elif int(total) == 118:
    print('否卦  文書官鬼問蘭庭,許宴嘉賓見利名,水上流年多有選,今年科舉只平平.')
elif int(total) == 262:
    print('節卦  財破文書難上榜,子孫太旺又傷官,成舉二科端可望,今年科舉且寬心.')
elif int(total) == 371:
    print('大畜卦  財爻持世破文章,官鬼休愁總不如,科舉占之終未穩,營謀斷許步雲梯.')
elif int(total) == 446:
    print('解卦  妻財持世剋文書,科舉占之事不如,雖是入場無阻隔,只因當道有堪虞.')
elif int(total) == 557:
    print('漸卦  子孫宮破文書破,科舉占之恐不如,子午之年始得力,今日休問貴高低.')
elif int(total) == 634:
    print('噬嗑卦  十年寄跡在寒窗,今日文章射斗光,科舉占之多遂意,此番斷許姓名揚.')
elif int(total) == 785:
    print('升卦  科舉成名占此爻,不須疑慮問低高,鹿鳴宴上呼先進,衣紫腰金福祿全.')
elif int(total) == 823:
    print('革卦  文星光耀斗牛虛,科甲爭名在此時,天爵既修人爵至,果然方不負男兒.')

#9.移居─問搬家適宜否
elif int(total) == 121:
    print('夬卦  移居斷許遂君心,福德星強利祿深,若問東南財便旺,家成業就樂昇平.')
elif int(total) == 216:
    print('訟卦  卦問移居許遂心,從今財物自然增,目前口舌須防備,移過方安切莫停.')
elif int(total) == 367:
    print('蹇卦  卦問移居事可為,應爻生世福神齊,目下讒言休要聽,移居之後有皈依.')
elif int(total) == 474:
    print('頤卦  若問移居事可為,六爻無鬼沿之遲,妻財持世財星旺,以後應知利益興.')
elif int(total) == 545:
    print('恆卦  欲問移居許稱心,不移當有是非生,吉星應在東南位,家業田園百事亨.')
elif int(total) == 653:
    print('家人卦  欲問移居不可疑,移時不見有高低,還應安舊休勞碌,待到秋來得便宜.')
elif int(total) == 738:
    print('晉卦  來占家宅欲移居,擇取良辰吉日時,安富增榮多吉利,丁壬福祿定為宜.')
elif int(total) == 882:
    print('臨卦  移居枉自費心機,世位逢官不必疑,守舊安心方是美,若還勉強有災危.')

#10.會事─問開會、商業談判吉凶
elif int(total) == 122:
    print('兌卦  君占會事恐無成,意氣相投事可通,若在秋冬方可望,如逢春夏事多憂.')
elif int(total) == 211:
    print('乾卦  會事占之卦最宜,朋友重重兄弟齊,作速去邀保全美,庚申辛酉得全財.')
elif int(total) == 366:
    print('坎卦  君來問會卦無妨,事未相投不要忙,再忌土煞來剋動,寅申巳亥百世昌.')
elif int(total) == 477:
    print('艮卦  會事來占不用憂,福神拱照必無愁,日逢巳午方成就,戊戌寅申可遇頭.')
elif int(total) == 544:
    print('震卦  福神不遂事難全,同會不安事有然,但是目前難就急,可交同氣共相連.')
elif int(total) == 655:
    print('巽卦  君占會事可如何,官鬼星明印位多,雖是綿綿難成聚,如逢子午得周全.')
elif int(total) == 733:
    print('離卦  君來問會事纏綿,無奈星辰信不然,莫被小人將事算,破費財物又熬煎.')
elif int(total) == 888:
    print('坤卦   君占會事莫憂心,要成須向好友朋,財旺重重無欠缺,七分財喜自然成.')

#11.謀事─問求職、工作機運
elif int(total) == 123:
    print('革卦  鬼爻持世福神祥,謀事占之百事昌,春季冬時方可就,夏秋占此不相當.')
elif int(total) == 218:
    print('否卦  財爻持世進妻財,謀事無妨慢慢來,最喜星辰應在意,更遇高人百事宜.')
elif int(total) == 362:
    print('節卦  若問謀事都作難,意氣相投方可忝,夏秋二季休提起,直到冬春方可全.')
elif int(total) == 471:
    print('大畜卦  謀事占之大吉昌,鬼爻持世小人防,時逢春夏多剝雜,定在秋冬財見高.')
elif int(total) == 546:
    print('解卦  卦占謀事甚蹊蹺,意氣相投財可交,若能遂意臨門戶,管教財利日日招.')
elif int(total) == 657:
    print('漸卦  君占訴事問如何,官鬼重重受折磨,卦內妻財全不見,時來方唱樂欣歌.')
elif int(total) == 734:
    print('噬嗑卦  君問謀事掛心懷,西北星辰作禍災,只請親友驅逐去,貴人得喜不為難.')
elif int(total) == 685:
    print('升卦  謀事無妨勿罣心,只因損氣費精神,自有好友來助力,成全之後得遂心.')

#12.親病─問父母親病情
elif int(total) == 124:
    print('隨卦 財來生鬼病難醫,父母家星要護持,夙願如今還應早,一旬半月總評論.')
elif int(total) == 215: 
    print('姤卦 父母無端疾病占,卦中財動鬼官連,子未占卜無應事,若把心頭莫罣牽.')
elif int(total) == 363: 
    print('既濟卦疾病纏綿父母身,鬼爻相應有精神,庚辛戊己災星退,作福祈神保安寧.')
elif int(total) == 478: 
    print('剝卦 子占親病事如何,病到臨危又復生,日逢巳午痊癒好,從此無災過有秋.')
elif int(total) == 542: 
    print('歸妹卦 父母得病把卦占,許福求神或可延,年逢七九休歡喜,兼收妙計始無尤.')
elif int(total) == 651:
    print('小畜卦 六爻無鬼病難安,父母占之自不安,待到庚辛方漸減,也須調理才安痊.')
elif int(total) == 736: 
    print('未濟卦 子占父母病纏綿,只為星辰降瓦紀,還要破財並保佑,請醫服藥自然安.')
elif int(total) == 887:
    print('謙卦  父母災殃定不妨,應透官位壽綿長,好藥調和三五劑,限度無沖何必忙.')

#13.買屋─問購屋可行否
elif int(total) == 125:
    print('大過卦  應來生世事宜成,買屋占之許稱心,富貴榮華從此得,家成業就永康寧.')
elif int(total) ==213: 
    print('同人卦  財不生世卦未安,君占買屋慢心歡,中人多欲難成就,捨此不如別路看.')
elif int(total) == 368:
    print('比卦  此卦多凶不順宜,須知買屋有差池,安心守舊休輕舉,切莫胡為惹事非.')
elif int(total) == 472:
    print('損卦  久積青蚨買屋居,知君占宅數為宜,成家立業多財利,旺發壬丁百世居.')
elif int(total) == 541:
    print('大壯卦  買屋占之事可依,只宜速置不宜遲,春秋恐被旁人奪,夏季占之必定宜.')
elif int(total) == 656:
    print('渙卦置產占之無不妥,文書官鬼兩相和,移家之後財源旺,二十餘年積聚多.')
elif int(total) == 737:
    print('旅卦  君占買屋是佳房,移家之後事吉昌,選擇良辰並吉日,親鄰樽酒賀新房.')
elif int(total) == 884:
    print('復卦:  知君買屋來占卦,買時增價頻多話,隔角重重卦未安,只宜退步還須罷.')


#14.分家─問兄弟分家時機
elif int(total) == 126:
    print('困卦  分家君占欲上疑,管教日後不差池,春秋財旺無煩惱,任意為來總得宜.')
elif int(total) == 217:
    print('遯卦  分家何患不稱心,子孫持世益千金,官臨應位總無忌,老實親族信可憑.')
elif int(total) == 364:
    print('屯卦  此卦分家有是非,豈知守舊得便宜,應高世下多煩惱,且自忍耐免被欺.')
elif int(total) == 475:
    print('蠱卦  分家占逢此卦爻,鬼爻持世莫徒勞,經營些小應收利,若是分家有禍招.')
elif int(total) == 543:
    print('豐卦  應識分家後有收,自然得利不須愁,福神旺相臨門戶,財利滔滔無怨尤.')
elif int(total) == 658:
    print('觀卦  子孫持世廣財源,分家占之事可全,財利重重方信算,四季財源利如泉.')
elif int(total) == 732:
    print('睽卦  此卦占來有不宜,君問分家有是非,待到來春方起意,方保無虞有和美.')
elif int(total) == 881:
    print('泰卦  占此分家卦不宜,嫌因世位旺文書,若還後悔須防妒,省得奔馳意不如.')

#15.病症─問自己或他人病情
elif int(total) == 127:
    print('咸卦  卦占疾病事無妨,福德天星兩字強,亥子庚辛痊癒好,五行有救壽綿長.')
elif int(total) == 214:
    print('無妄卦  占病星辰命犯之,五行有救免憂慮,時逢卯酉災星退,作福祈神莫待遲.')
elif int(total) == 365:
    print('井卦  君占疾病有何妨,輕重星辰相見傷,作福祈神三煞退,庚申方許見安康.')
elif int(total) == 473:
    print('賁卦  病犯星辰宜保之,傷寒時熱總難期,平安藥餌多多服,全仗神藥有扶持.')
elif int(total) == 548:
    print('豫卦  君占疾病事無妨,福德天醫不順祥,可去求神並作福,遲遲方許得安康.')
elif int(total) == 652:
    print('中孚卦  君因目下病擔憂,世應逢官不必求,寅午戌亥方漸退,神前祈保可無愁.')
elif int(total) == 731:
    print('大有卦  君占疾病問神明,四肢難安節骨疼,家內福神並宅鬼,三牲俱獻定安寧.')
elif int(total) == 886:
    print('師卦  命犯災星福不輕,傷寒吐瀉腹中疼,災星雖犯無難事,速即求神可保寧.')

#16.天花─問嬰兒健康病情
elif int(total) == 128:
    print('萃卦  嬰兒得喜數無妨,福德臨爻不必憂,服藥且看過未午,闔家歡喜把神酬.')
elif int(total) == 212:
    print('履卦  子孫喜至何須慮,不必憂疑且問醫,虎頭蛇尾災星退,待交節氣病才移.')
elif int(total) == 361:
    print('需卦  天花兒郎何日強,子孫持世卻無妨,要逢申酉方除厄,一服仙方便吉昌.')
elif int(total) == 476:
    print('蒙卦  君來占卜問天花,福德隨身定不差,縱有風波無浪起,吉星拱照喜哈哈.')
elif int(total) == 547:
    print('小過卦  君占子息可吉凶,乃是災星臨命宮,非神保佑難為力,猶宜急禱祈神仙.')
elif int(total) == 654:
    print('頤卦  孩兒有喜不須驚,應下援身喜氣臨,良藥能驅夙小症,三頭四日即安寧.')
elif int(total) == 735:
    print('鼎卦  誠心占卜問因由,孩兒喜事不必憂,官勞鬼爻須禱告,身康體健不須愁.')
elif int(total) == 883:
    print('明夷卦  見喜凶荒苦見傷,子孫臨應未為昌,應皆小子災危至,只有求神保安康.')

#17.求財─問針對某機會之財運
elif int(total) == 131:
    print('大有卦  求財宜緩不宜急,允時亦少定無多,甲乙卯寅方有望,卦爻註定斷無訛.')
elif int(total) == 286:
    print('師卦  占問求財是稱心,東西路道正相應,雖然費卻心機力,利息終得須萬金.')
elif int(total) == 327:
    print('咸卦  君占此爻問求財,秋夏來臨不用猜,若是九流並雜術,許君財物兩相諧.')
elif int(total) == 414:
    print('無妄卦  無望求財終有望,世高應下兩重財,若逢三七十數內,自然方遂君心懷.')
elif int(total) == 565:
    print('井卦  求財喜得貴人強,世應相收大吉昌,但是目前防有阻,遲遲方許遂心腸.')
elif int(total) == 673:
    print('賁卦  卦占求財欲解疑,兩人合意自相宜,亥子丑臨方可旺,一人主事有差池.')
elif int(total) == 748:
    print('豫卦  求財卜卦喜生財,任往東西不必猜,若是本微求利益,管教白子得將來.')
elif int(total) == 852:
    print('中孚卦  求財占卦欲中孚,管教經營遂取圖,出入貴人因得力,重重財喜有相扶.')

#18.借財─問借錢順利否
elif int(total) == 132:
    print('睽卦  財銀借取問神明,托保求之亦可成,亥子庚辛財發動,日前不遂莫生嗔.')
elif int(total) == 281:
    print('泰卦  官鬼妻財兩見奇,與人借貸得便宜,幾番財利遲遲有,目下猶未合事機.')
elif int(total) == 326:
    print('困卦  財爻上卦最為宜,欲借錢財不必疑,若在秋冬多不吉,如逢春夏利相依.')
elif int(total) == 417:
    print('遯卦  官鬼妻財兩見之,問人借取得相宜,三分財氣可應許,目下相求事可知.')
elif int(total) == 564:
    print('屯卦  官鬼妻財兩見之,問人借取定相宜,求謀遂意無攔阻,一任施為喜可期.')
elif int(total) == 675:
    print('蠱卦  六爻安靜最吉昌,借取銀錢要著方,春夏占之尚可求,如遇秋冬難濟急.')
elif int(total) == 743:
    print('豐卦  財爻上卦最為高,借取錢財乃必疑,君在秋冬多不足,如逢春夏兩相宜.')
elif int(total) == 858:
    print('觀卦  錢財借取問神明,托保求之事可成,亥子庚辛財發動,眼前不遂莫生嗔.')
    
    