#  MRAv2 json parse for translate en -> jp.

print('--- start mra-json-trans ---')

import json
import boto3
# FNAMEは、jsonのフルパス元ファイル名を指定します
FNAME = './template-MRA2-V3.4.json'
# JANAMEは、出力先のフルパスファイル名を指定します
JANAME = './result.json'

translate = boto3.client(service_name='translate', region_name='ap-northeast-1', use_ssl=True)

# 　辞書型でデータをインポート
# 　ソースのjsonファイル名をFNAMEで取る
with open(FNAME) as fd:
    dic = json.load(fd)

# idが optionalAS400 の部分を探す 該当部分行番号は jsonファイル内のL3566 - 4727
for n in dic["section"]["perspectives"]:    # ここは辞書型
    print('--- Searching target point ---')
    if n['id'] == 'optionalAS400':   # Target point.
        # print('id : optionalAS400 = {} \n----------'.format(n['id']))
        m = n['categories']

        # print("abbreviation = {}".format(m[0]['abbreviation']))
        # print("questions[0] = {}\n".format(m[0]['questions'][0]['question']))
        # print("questions[1] = {}\n".format(m[0]['questions'][1]['question']))
        # print("questions[2] = {}\n".format(m[0]['questions'][2]['question']))

        # categoriesの中に、questions が複数あり、各questions の中にも複数のquestionがリスト型で含まれている
        for tmp in m: 
            qlist = tmp['questions']    # Get question list in questions section.
            print("|", end=" ")

            for i in qlist:
                print("-", end=" ")
               # 以下で、翻訳する各部分に対してAmazon Translate で処理する。 
               # questionのリスト内にキーワードがない、またはブランク””文字列（サイズが０）の場合は何もせずに次に進む
            
               # QUESTION : Get question data & translate & replace it.
                if 'question' in i and len( i['question'] ) != 0:    # question key is not, or "" blank case.
                    rc = translate.translate_text(Text = i['question'], SourceLanguageCode="en", TargetLanguageCode="ja")
                    i['question']  = rc.get('TranslatedText')
                
                # HINT : Get question data & translate & replace it.                
                if  'hint' in i and len( i['hint'] ) != 0:
                    rc = translate.translate_text(Text = i['hint'], SourceLanguageCode="en", TargetLanguageCode="ja")
                    i['hint'] = rc.get('TranslatedText')
                
                # CONTEXT : Get question data & translate & replace it.
                if  'context' in i and len( i['context'] ) != 0:
                    # print("-- context = {}".format(i['context']))
                    rc = translate.translate_text(Text = i['context'], SourceLanguageCode="en", TargetLanguageCode="ja")
                    i['context'] = rc.get('TranslatedText')        # Replace en sentence to ja.
                    
                # RATING 1-5 : insert same logic.
                if  'rating1' in i and len( i['rating1'] ) != 0:
                    rc = translate.translate_text(Text = i['rating1'], SourceLanguageCode="en", TargetLanguageCode="ja")
                    i['rating1'] = rc.get('TranslatedText')
                if  'rating2' in i and len( i['rating2'] ) != 0:
                    rc = translate.translate_text(Text = i['rating2'], SourceLanguageCode="en", TargetLanguageCode="ja")
                    i['rating2'] = rc.get('TranslatedText')
                if  'rating3' in i and len( i['rating3'] ) != 0:
                    rc = translate.translate_text(Text = i['rating3'], SourceLanguageCode="en", TargetLanguageCode="ja")
                    i['rating3'] = rc.get('TranslatedText')
                if  'rating4' in i and len( i['rating4'] ) != 0:
                    rc = translate.translate_text(Text = i['rating4'], SourceLanguageCode="en", TargetLanguageCode="ja")
                    i['rating4'] = rc.get('TranslatedText')
                if  'rating5' in i and len( i['rating5'] ) != 0:
                    rc = translate.translate_text(Text = i['rating5'], SourceLanguageCode="en", TargetLanguageCode="ja")
                    i['rating5'] = rc.get('TranslatedText')

#  出力ファイルJANAMEへのjson形式での書出し
with open(JANAME, 'w') as fd:
    json.dump(dic, fd, indent=2, ensure_ascii=False)

print("--- End, output file name = {} ---".format(JANAME))


