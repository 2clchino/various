# Utility
面倒な作業の自動化のために書かれた雑多なソースコード達<br>
ディレクトリ内のいたるところに散乱しているのでテキトーにまとめてgit管理する<br>
いつか誰かの役に立つかも...？

# Feature
- calc_ams.py
    - 改行区切りの数列ファイルを読み込んで、ave, med, std を出力
    - これは計算用excelシート作った方が楽だったかも..
- gnp_to_xlsx.py
    - gnuplot用に出力した文字ファイル(.dat)をexcel, numbers にコピペ→グラフ化できるよう整形
- mat_clr.py
    - Unityのmaterialファイルを一括で書き換える用のスクリプト
    - Shaderを変更するとmaterialの設定が初期化されるが、内部データが読み込まれないparameterで残っていたのでrenameして読み込めるようにしている