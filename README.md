# vjudge-atcoder-submitID
Help getting atcoder submit IDs for vjudge


### ���͓K��
Vjudge��atcoder�̖���o�^����ہAsubmitID�𒲂ׂ�̂��߂�ǂ������̂ŃX�N���v�g�������܂����B


#### �g����
> atcid.py -f [FILE]

FILE���ɂ���URL����Aatcoder��submit ID�������Ă��܂��B

> atcid.py 
>
> URL1
> 
> URL2
> 
>...
>
> �I�[

�W�����͂���I�[�܂ł�URL����Aatcoder��submit ID�������Ă��܂��B


#### ���s��
�W�����͂���̂Ƃ�
> python3 atcid.py

>(IN) https://arc061.contest.atcoder.jp/tasks/arc061_a

>(IN) https://arc068.contest.atcoder.jp/tasks/arc068_a

>(OUT)2067 https://arc061.contest.atcoder.jp/tasks/arc061_a

>(OUT)2298 https://arc068.contest.atcoder.jp/tasks/arc068_a

�t�@�C������̂Ƃ�
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