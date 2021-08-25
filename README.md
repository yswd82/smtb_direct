# smtb_direct

SMTB Directの振り込み機能を操作するseleniumライブラリ

登録済振込先を番号ベースで指定する


# 準備

口座番号、パスワードなどを別ファイル(デフォルトはconfig.ini)で作成して保存する

```ini
[account]
member_num = xxxxxxxx
password = xxxxxxxx

[passcode]
a-1 = xx
a-2 = xx
...
e-4 = xx
e-5 = xx
```
