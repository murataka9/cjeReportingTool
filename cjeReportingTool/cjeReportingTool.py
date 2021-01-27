# ==========================================#
# Project Name    : cjeReportingTool
# File Name       : cjeReportingTool.py
# Encoding        : utf-8
# Creation Date   : 26-Jun-2021
# Copyright © 2021 kami; Takahito Murakami. All rights reserved.
# This source code or any portion licensed by MIT
# ===========================================#

def cjeReportingTool(path, outpath, split_str, prefix):

    # 文字列へ強制変換
    path = str(path)
    outpath = str(outpath)
    split_str = str(split_str)
    prefix = str(prefix)

    # シークエンスバー
    seq, sequence_per, sequence_con = 0, 0, 0
    seq = sum(1 for line in open(path))

    # 指定ファイルを開く
    f = open(path, 'r')
    f2 = open(outpath, 'w')

    line_cout = 1  # lineのカウントの初期化
    linenum_explanation = {}  # 行番号:説明文対辞書

    # 1行づつ処理して指定語があったらsplitしてsplit_line[1]を辞書に登録
    for line in f:
        line = line.rstrip()
        sequence_con += 1
        sequence_per = (sequence_con / seq) * 100
        if split_str in line:
            split_line = line.split(split_str)
            line_cout_str = str(line_cout)
            linenum_explanation[line_cout_str] = str(split_line[1])
            line_cout += 1
        else:
            line_cout += 1

    print('■', str(round(sequence_per, 2)), '%', end='')

    for line_num in linenum_explanation:
        f2 = open(outpath, 'a')
        f2.write('{}\t{}:\t{}\t\t\n\n'.format(
            prefix, line_num, linenum_explanation[line_num]))
    f.close()
    f2.close()
