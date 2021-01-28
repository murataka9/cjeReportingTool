# ==========================================#
# Project Name    : cjeReportingTool
# File Name       : cjeReportingTool.py
# Encoding        : utf-8
# Creation Date   : 26-Jun-2021
# Copyright © 2021 kami; Takahito Murakami. All rights reserved.
# This source code or any portion licensed by MIT
# ===========================================#


def __lineCount(path: str) -> int:
    return sum(1 for line in open(path))


def cjeReportingTool(
        path: str, outpath: str, split_str: str, prefix: str) -> None:

    # シークエンスバー
    seq, sequence_per, sequence_con = __lineCount(path), 0, 0

    # 指定ファイルを開く
    f = open(path, 'r')
    f2 = open(outpath, 'w')

    linenum_explanation = {}  # 行番号:説明文対辞書

    # 1行ずつ処理して指定語があったらsplitしてsplit_line[1]を辞書に登録
    for line_cout, line in enumerate(f):
        line = line.rstrip()
        sequence_con += 1
        sequence_per = (sequence_con / seq) * 100
        if split_str in line:
            split_line = line.split(split_str)
            line_cout_str = str(line_cout+1)
            linenum_explanation[line_cout_str] = str(split_line[1])

        print('■{}%'.format(str(round(sequence_per, 2))), end='\r')

    print('')

    for line_num in linenum_explanation:
        f2.write('{}\t{}:\t{}\t\t\n\n'.format(
            prefix, line_num, linenum_explanation[line_num]))

    f.close()
    f2.close()
