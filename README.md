# mrav2-json-translate

- MRAv2のI18N対応の一環として、jsonファイルで書かれた画面表示のテキストを英語から日本語に機械翻訳するコードです。
- 機械翻訳には、Amazon Translateを利用しています。
- jsonファイルをPythonでパースすると、辞書型とリスト型の混在となります。
- 翻訳したい部分、question, name, Ability, hint, rating-1, .., rating-5 を探して翻訳し、テキストを差し替えます。
- 当初、Jupyter Notebookで作成しましたが、その後、mra-json-trans.py も作成しました。内容処理は同じです。

## pickout-qa.py
オプションの質問だけを抜き出すツールです。
プログラム冒頭部分で、｛出力ファイル名、質問カテゴリー}を設定すると、指定のファイル名に質問文だけを抜き出したテキストファイルを作成します。
現時点でのオプション質問のjson内ラベルは下記があります。  

 optionalVmc  
 optionalStorage  
 optionalMicrosofot  
 optionalMainframe  
 optionalAS400  
 optionalNetowkrTransformation  
 optionalDatabase  
 optionalOutpost  
 optionalSAP  
 optionalAppModernization  
  

