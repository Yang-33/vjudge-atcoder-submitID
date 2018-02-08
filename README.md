# vjudge-atcoder-submitID
Help getting atcoder submit IDs for vjudge


### 概要
Vjudgeでatcoderの問題を登録する際、submitIDを調べるのがめんどくさいのでスクリプトを書きました。

beta版URLでも大丈夫です。

#### 使い方
`$ atcid.py [-f [FILE]] `

引数にファイルを指定した際、FILE内にあるURLに対するsubmit IDを出力します。
引数を指定せず実行した場合は標準入力でURLを記述(コピー)し、end of file 的なものを受け取るとそこまでのURLに対するsumbit IDを出力します。
```
$ atcid.py 
  URL 1
  URL 2
  ...
  URL N
  (EOF)
```

#### Example
![result](https://github.com/Yang-33/vjudge-atcoder-submitID/blob/media/capture.gif)

