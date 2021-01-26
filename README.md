# cjeReportingTool
![example](./img/image.png "サンプル")


This Tool made for CJE(Chishiki Joho Enshu 3) class at Univ. Tsukuba, klis.  
This package converts source code comment to markdown text using split words.  

>ja: 筑波大学 KLISのCJE3のマークダウン形式の小レポート用ライブラリです。特定の文字列`##`や`#$`等をコメントに用いると，その記号を用いたコード行末に書いたコメントのみを行番号と合わせて出力します。

# Usage

## Require
This package does not require on other any packages.


## Installation
This package runs on Python 3.6 or higher version. You can install it from PyPI via pip:  
> pipからインストールすることができます。インストールするには以下のコマンドを使用します。
```
pip install cjeReportingTool
```

to install.

## Documentation
To use the package, load as a function.

```
cjeReportingTool(path, outpath, split_str, prefix)
```
### Args
- `path` Read file path
- `outpaht` Export file path
- `split_str` A symbol or string that separates comments from source code
- `prefix` Prefixes to be written out

### Example
- File
```
.
├── sample.py
├── out.md
└── main.py
```
- Read file `./sample.py`
```
1   # num
2   i = 1 ##number
3   n = i * 2 
4   # output
5   print(n) ##2
```
- Main program `./main.py`
```
1   cjeReportingTool('sample.py', 'out.md', '##', '>')
```

- Output file  `./out.md`
```
1   > 2: number
2   
3   > 5: 2
```
![example](./img/preview_ex.png "サンプル")

### Note
`split_str` uses a string other than the spelling of the symbols used your python code.
- Good: `##`, `#&`, `#$`, `#%`　　
- Bad: `#` No difference from other comments　`$` That's not comment