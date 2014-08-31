FontValidate
============

OS/2 info

---

```
python OS2_info.py -i 'Ubuntu-B.ttf Ubuntu-R.ttf'
```
Will generate:

```
[Ubuntu-B]
xAvgCharWidth = 652
usWeightClass = 700
usWidthClass = 5
fsType = 0
ySubscriptXSize = 700
ySubscriptYSize = 650
ySubscriptXOffset = 0
ySubscriptYOffset = 140
ySuperscriptXSize = 700
ySuperscriptYSize = 650
ySuperscriptXOffset = 0
ySuperscriptYOffset = 477
yStrikeoutSize = 120
yStrikeoutPosition = 250
sFamilyClass = 0
ulUnicodeRange1 = 3758107391
ulUnicodeRange2 = 3489701979
ulUnicodeRange3 = 8
ulUnicodeRange4 = 0
achVendID = DAMA
fsSelection = 32
fsFirstCharIndex = 0
fsLastCharIndex = 65276
sTypoAscender = 776
sTypoDescender = -188
sTypoLineGap = 61
usWinAscent = 1274
usWinDescent = 551

[Ubuntu-R]
xAvgCharWidth = 500
usWeightClass = 700
usWidthClass = 5
fsType = 0
ySubscriptXSize = 700
ySubscriptYSize = 650
ySubscriptXOffset = 0
ySubscriptYOffset = 140
ySuperscriptXSize = 700
ySuperscriptYSize = 650
ySuperscriptXOffset = 0
ySuperscriptYOffset = 477
yStrikeoutSize = 50
yStrikeoutPosition = 250
sFamilyClass = 0
ulUnicodeRange1 = 3758097151
ulUnicodeRange2 = 1342208251
ulUnicodeRange3 = 0
ulUnicodeRange4 = 0
achVendID = DAMA
fsSelection = 32
fsFirstCharIndex = 0
fsLastCharIndex = 65533
sTypoAscender = 693
sTypoDescender = -168
sTypoLineGap = 164
usWinAscent = 835
usWinDescent = 259
```
---
```
python OS2_info.py -i 'Ubuntu-B.ttf Ubuntu-R.ttf' --compare
```
Will produce:

```
.
..
...

Respective Comparison
Ubuntu-BI
Ubuntu-R
xAvgCharWidth
['652', '500']
usWeightClass
Values Are Equal

usWidthClass
Values Are Equal

fsType
Values Are Equal

ySubscriptXSize
Values Are Equal

ySubscriptYSize
Values Are Equal

ySubscriptXOffset
Values Are Equal

ySubscriptYOffset
Values Are Equal

ySuperscriptXSize
Values Are Equal

ySuperscriptYSize
Values Are Equal

ySuperscriptXOffset
Values Are Equal

ySuperscriptYOffset
Values Are Equal

yStrikeoutSize
['120', '50']
yStrikeoutPosition
Values Are Equal

sFamilyClass
Values Are Equal

ulUnicodeRange1
['3758107391', '3758097151']
ulUnicodeRange2
['3489701979', '1342208251']
ulUnicodeRange3
['8', '0']
ulUnicodeRange4
Values Are Equal

achVendID
Values Are Equal

fsSelection
Values Are Equal

fsFirstCharIndex
Values Are Equal

fsLastCharIndex
['65276', '65533']
sTypoAscender
['776', '693']
sTypoDescender
['-188', '-168']
sTypoLineGap
['61', '164']
usWinAscent
['1274', '835']
usWinDescent
['551', '259']

```
---
If you want to use `diff`, generate the metrics files one by one.

```
python OS2_info.py -i 'font1.ttf' >> font1.metrics
python OS2_info.py -i 'font2.ttf' >> font2.metrics

```
---

You can also retrieve individual OS/2 properties:

```
python OS2_info.py -p 'font.ttf' fsLastCharIndex
```

---

To alter OS/2 properties:

```
python OS2_info.py -alt font.ttf usWinAscent 1919 output_font.ttf 

```