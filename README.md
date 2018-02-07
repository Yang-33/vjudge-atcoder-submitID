# vjudge-atcoder-submitID
Help getting atcoder submit IDs for vjudge


### 今は適当
Vjudgeでatcoderの問題を登録する際、submitIDを調べるのがめんどくさいのでスクリプトを書きました。


#### 使い方
> atcid.py -f [FILE]

FILE内にあるURLから、atcoderのsubmit IDを持ってきます。

> atcid.py 
>
> URL1
> 
> URL2
> 
>...
>
> 終端

標準入力から終端までのURLから、atcoderのsubmit IDを持ってきます。


#### 実行例
標準入力からのとき
> python3 atcid.py

>(IN) https://arc061.contest.atcoder.jp/tasks/arc061_a

>(IN) https://arc068.contest.atcoder.jp/tasks/arc068_a

>(OUT)2067 https://arc061.contest.atcoder.jp/tasks/arc061_a

>(OUT)2298 https://arc068.contest.atcoder.jp/tasks/arc068_a

ファイルからのとき
> cat today-problems.txt
> 
> https://arc061.contest.atcoder.jp/tasks/arc061_a
> 
> https://arc068.contest.atcoder.jp/tasks/arc068_a
>
> python3 atcid.py -f 
>
>(OUT)2067 https://arc061.contest.atcoder.jp/tasks/arc061_a
>
>(OUT)2298 https://arc068.contest.atcoder.jp/tasks/arc068_a