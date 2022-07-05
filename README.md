# mrav2-json-translate

MRAv2のI18N対応の一環として、jsonファイルで書かれた画面表示のテキストを英語から日本語に機械翻訳するコードです。
機械翻訳には、Amazon Translateを利用しています。
jsonファイルをPythonでパースすると、辞書型とリスト型の混在となります。
翻訳したい部分、question, name, Ability, hint, rating-1, .., rating-5 を探して翻訳し、テキストを差し替えます。
当初、Jupyter Notebookで作成しましたが、その後、mra-json-trans.py も作成しました。内容処理は同じです。

