# --------------------------------------------------
# MRAv2 Pick out Questions.
# --------------------------------------------------

# FN_INは、jsonのファイル名を指定します
FN_IN = './template-MRA2-V3.4.json'
# FN_OUTは、出力先のファイル名を指定します
FN_OUT = './tmp/mra-Database.txt'
# 抜き出したい部分のjsonラベルを指定する
QA_CATEGORY = 'optionalDatabase'
# --------------------------------------------------
import json
import boto3
print('--- Start picking out Questions ---')

# 　辞書型でデータをインポート
# 　ソースのjsonファイル名をFN_INで取る
with open(FN_IN) as fd:
    dic = json.load(fd)
fd_out = open(FN_OUT, 'w')
fd_out.write('--- MRAv2 質問一覧　該当箇所：{} ---\n\n'.format(QA_CATEGORY))

# idが QA_CATEGORY の部分を探す
for n in dic["section"]["perspectives"]:    # ここは辞書型
    print('--- Searching target point ---')

    if n['id'] == QA_CATEGORY:   # Target point.
        m = n['categories']
        # categoriesの中に、questions が複数あり、各questions の中にも複数のquestionがリスト型で含まれている
        for tmp in m: 
            qlist = tmp['questions']  # Get question list in questions section.
            for i in qlist:
                # QUESTION : Get question data.
                if 'question' in i and len( i['question'] ) != 0:  # question key is not exist, or "" blank case.
                    # print('{} = {}'.format(QA_CATEGORY, i['question']))
                    fd_out.write('- ' + i['question'])
                    fd_out.write('\n')
                # Ommit processing json label HINT, CONTEXT, RATING 1-5

fd_out.close()
print("--- End, output file name = {} ---".format(FN_OUT))


