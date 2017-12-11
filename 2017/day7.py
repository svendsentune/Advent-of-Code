import re
from operator import itemgetter
from collections import Counter

"""
http://adventofcode.com/2017/day/7
"""


tops = r' \(\d+\).*'

top_weights = r'\d+'

def createDictionaries(t):
  d_weights = {}
  d_subtrees = {}
  for l in t.split("\n"):
    parent = re.sub(tops,"",l)
    weight = int(re.findall(top_weights,l)[0])
    d_weights[parent]=weight
    try:
      children = [c for c in l.split("-> ")[1].split(', ')]
      d_subtrees[parent] = children
    except IndexError:
      continue
  return d_weights,d_subtrees

def getBottomTower(t):
  parents = []
  children = []
  for l in t.split("\n"):
    parents.append(re.sub(tops,"",l))
    try:
      for c in l.split("-> ")[1].split(', '):
        children.append(c)
    except IndexError:
      continue
  for p in parents:
    if p not in children:
      return p

def getSum(node,st_dict,w_dict):
  w_self = w_dict[node]
  w_children = []
  children = []
  if node in st_dict:
    for n in st_dict[node]:
      w_children.append(getSum(n,st_dict,w_dict))
      children.append(n)
    if len(set(w_children)) != 1:
      for i,n in enumerate(st_dict[node]):
        if w_children.count(w_children[i]) == 1:
          wrong_w = w_children[i]
          wrong_node = n
        else:
          right_w = w_children[i]
      print(right_w-wrong_w)
      print(w_dict[wrong_node]+(right_w-wrong_w))

      print(node,w_self,children,w_children)
    return w_self+sum(w_children)
  else:
    return w_self

def recursiveCircus(t):
  start = getBottomTower(t)
  weights, subtree = createDictionaries(t)
  getSum(start,subtree,weights)

tower = """bqyqwn (68) -> wscqe, cwxspl, syogw, xnxudsh
ddswb (34)
hnkvw (320)
ibqmynm (252) -> oglcdgs, tkjofj, upurae, oypvhy, bzfkt, hdvcz, cfwxyl
rkerea (87)
lcmlbj (66)
vtccvv (69)
nachvlp (20)
tmkli (66)
exuyuk (82)
ojzogs (79)
egkiqcp (37) -> rxjnad, psetts
xadjes (10)
fivkqxx (121) -> acvzsbe, kkmax, qcmwsvm
krgtrdn (53)
mxemqqb (267) -> iuuouds, qqmvd
iwwqvoa (24)
yyecrv (59)
zjpkoar (40)
ilsgqdw (37)
bmlfd (43)
nxqwag (81)
ubbwvvl (44)
khfzis (48) -> ztxcc, bvejguc
gvtcy (39)
xbxxe (173) -> bzjxil, amklj
qejgaf (25)
uunpyb (82)
dmidur (57)
fklfgd (65)
vcjfe (22)
rkjfx (33)
ioglbe (88)
tymkixg (36)
qbhhtw (90)
afbrhy (79)
nswcez (47)
wzjonl (16)
xviqup (95)
claolm (312) -> ndmkbul, rpjfkh
qhlhfk (387) -> iwwqvoa, rmshk, ftezz
vtokttx (55)
boalcdm (13)
angpy (62) -> fitha, itxgz, pyiexlj, wqshh, rloxobx
gwcdf (32)
jpscxfh (46) -> qsakd, exuyuk, dqdmie, kjwfeoj
qkzpcyy (96)
fifams (415)
yseezd (11)
qcmwsvm (37)
hfnhd (152) -> vdcfh, ufrhi
wfgzr (82)
sjoov (6)
fonrb (7531) -> xohxq, cmsqe, jefsr
pyhof (21)
pplis (9)
fosdh (90)
pjkyydd (15)
wvmtyez (46)
bzfkt (66) -> rauho, xctuhbx
zyqssjb (13) -> olebdv, byahs, xajzwdh
wotus (119) -> dndrnc, tebkmhi, qejgaf
rusndcc (39) -> xcfxvd, kvylxr, vwkegak, oiuztx
stofi (16)
mgqil (66) -> noibcw, nptqxtu
qjzss (31)
hawhqex (71)
kjjee (174) -> lltgjo, gwcdf
gdamb (99)
diqdy (183) -> gackyrq, vcjfe, lcnsf
sfwzqk (54) -> rkuzg, ewvvb
vktjns (45)
urwaex (59)
nyouzhg (17) -> lofybs, baedi
mklqpn (9)
iktget (33)
gxtfu (57)
xkymbld (37) -> mqgbif, ptxfk
qjeuqe (92)
benqzp (92) -> wvmtyez, gmveehb
rkctaq (20)
sbwoye (50)
bujufb (148) -> tduxvx, lxzvkpk, jllqymn, csrpy
cwfydbh (369) -> qcmtgvr, tyvjs
cjjytkr (305) -> trszl, fgzgfc
qsakd (82)
domway (2464) -> kgphv, pjujovx, hrdggo
mrpji (61)
kzrgfb (92)
hocazx (818) -> bmukspb, mgbwxw, gyirkcj, kgxfc
bobvssz (25) -> srvqt, alhghui, wnjaw, qhlhfk, lsbvzaf, qjkfys, nnncfl
rrzyzq (76)
eaufvn (78) -> dtazpb, nlajc
tduix (18)
yzcez (62) -> rlxto, vkaxa
uvpuko (91)
xtnmps (95) -> ptatzl, bujufb, oybbzr, zwopz, phqpwkw
ibeis (54)
ofkvpq (500) -> auvuxv, stqmwk, dptekr
pmolg (166) -> uuunqk, uolqt
byedxex (180) -> gsaqlad, ebwubc
aicjff (67)
vtcxw (860) -> ezlfnhs, aizdt, ylbftp
nzuswm (80) -> ojzogs, qfopwo
hgwbg (89)
sflonq (190) -> gppwsbp, mpvgy
pqiuhyp (52) -> xbtjl, jykseco, aftnyad, xaden, urdgg, ijkpfv, ejekn
ccgjf (99)
devsz (38)
vmmtsr (33)
ebwubc (70)
mgcnohi (69)
klege (92)
jtlqxy (66)
ofbqk (148)
ewluica (22)
mulvwn (290) -> ubbwvvl, jmuqp, dnovxt
trlcj (245)
uezwz (20)
bbtnj (170) -> xvwok, rqyxzn
ndticx (54) -> rbtco, bobvssz, umtxk, domway, wugia, ubvttg, ydpemw
lxwkpqh (325) -> xoigv, fqsjaz
mpvgy (35)
ujgeml (94)
jkoir (6)
kemkz (98)
dtqgdc (90)
girxc (147) -> zylotoh, qtxmjwm
olawkuc (79) -> earmfdp, wnowypb
umrqldb (99)
oyurlfq (57)
flgpg (188) -> jimltsw, xhgza
wawtrk (80)
nlajc (85)
ewqcktv (1364) -> hfnhd, amqvr, ntxcpwl
dmvyuf (35)
vtdbov (50)
xnszvs (65)
mjrktxe (50) -> eoxwp, jgsmitm, isrgei, rnbgz, kymbvpp, ktjdpt, mgzocpe
zicvok (81)
tkmfbk (93) -> ffhsg, kynezb
vlwvot (84)
oybbzr (1007) -> qstlv, nayvvrh, izxpf, habni, ckfefl, fjdlcbh, thhakxn
qiksfr (44)
wowxv (92)
fmdba (44)
zgxbjj (96)
jncjxue (66)
xquhgig (190) -> rqhfxty, maftysp
habni (27) -> xwknab, xukfcd, scvhl, tcbgf
iftcnc (50)
dqdmie (82)
otlvq (40) -> hjsrvj, rtbcch, vpirde
mgzocpe (51) -> zkwajbd, mrpji
fkzxb (89)
jlsmm (32)
igdkn (43) -> dgtxjuj, jxyakll, kptdem
rftuf (43)
uolqt (9)
rtwlo (78) -> wgbvle, npttye, claolm, ydffzgu, mgbgb, jwjuth, mulvwn
nrgzcge (132) -> bywbrk, vazoq, eaufvn
juoaena (94)
wfsaglg (54) -> nlfdps, tdkdiqe
jfsgqq (100) -> crslvc, esized
mcucysr (49)
tcbgf (28)
mlalrpt (166) -> jtbrjm, fyaxzl
srvqt (155) -> jyftx, dtijfqc, phcqntb, uyhrcfl
xohxq (1457) -> czbydf, wgdnyy
lqbmor (230) -> rkjfx, vmmtsr
jjsyexg (38)
ynvesz (88) -> rqaxn, afntec
ibbxb (194) -> imiimt, llikz
ktasnia (49) -> thkjz, cjgtra, tzngdx, cqjsqh, vtjtyp, lyzaead, xrtzs
vsjjq (30)
yjnzgl (67)
mcrhiy (6559) -> mkgafux, gugxitg, tymmo
nlgymop (139) -> tymkixg, crchwpb
ybosi (18)
rhqfb (179) -> okurp, gpwbcg, invqsb
kzjozhi (90)
ixncawy (28)
ooczbeh (36)
ubvttg (796) -> wuuvnlz, donzb, bwgimi, rywtmt, rusndcc, ceagctk
ohcoit (6)
exrud (176) -> hpziqqg, abxglwt, gozhrsf, oqjqu, vhkodl
opvrgh (79)
blyms (46)
vfrylx (10) -> qhkniqm, bmcwbsi
ndmkbul (55)
mohey (86) -> tbmyue, ibeis
wktzh (93)
ystgyng (50)
jclntv (87)
dsjcqpn (133) -> slufzy, gbbpqj, jxawk
fitha (68) -> faqngn, xguqqao, athuly, fmdsfus
xyang (225) -> njxrb, mfwuqb
acjedny (49)
mfwuqb (60)
ayuma (81)
qqmchoq (7)
yzjhmqq (171) -> dinpz, upozls
qfopwo (79)
srypr (64)
tvwmzal (236) -> cpujsn, ewluica
umtxk (2942) -> jyazs, scnhwcs, fmpvv, aahqvqy
gkwyfz (49)
dodrbx (227) -> uhtnl, vxnsova
sfdclf (238)
kksizqf (44)
dfofyir (236) -> ddswb, grxdbx
qakiz (37)
ceagctk (255) -> bwvlnlt, rkazlp, vbejzc, njhlrtm
hnjszii (284) -> zkdwz, bwlit
gbbpqj (34)
bvaoy (114) -> mogwbda, rodntl
vkihn (36)
symdxo (8)
nduildw (30)
nxhfgx (18)
chgfb (16)
gugaaiq (40)
euvrdg (79)
ckzaj (67)
jupzgjm (90)
llalaql (27)
qdnghwn (16)
iffluz (515) -> bbbvmxo, reomle, vspqi
nvrjzg (214) -> nzfko, qqmchoq
xvwok (34)
enmjipp (95)
jtbrjm (18)
rlxto (83)
xpotznx (41)
lslhph (59)
vhkodl (221) -> otlvq, fioegdo, rreidgp, fivkqxx, xahvbm
mncivb (88)
hbhfdlh (89)
mkgafux (688) -> admjq, tqtut, emkgc
tymmo (22) -> uxjaa, nlgymop, dcvfkk, yzjhmqq, iqjqlfq, faopk
vxslvq (37) -> jmvcgo, ioglbe
rxjnad (80)
ejdxula (92) -> kviiza, uqmaluk, nasbs
xvzoy (35)
vukpdsr (162) -> gumncu, mlzmimg, vjobpzv
xoigv (10)
iuehdsr (21)
jzgvab (9)
odxpup (89)
vwkegak (92)
bsvgagj (41)
mxwgu (310) -> yeyxf, qdnghwn
jynmg (1140) -> wotus, mohey, fiynyre
qftwuv (36)
veabcj (67)
zaargo (30) -> ytrsmfx, jtlqxy
xfbfvuu (65)
gpwbcg (5)
elysbb (81)
engpslr (85)
tqbtvqc (31)
faqngn (98)
jykseco (166) -> xawzbz, fsdoohr
nfywcyp (62)
rreidgp (168) -> vfupn, xyvnk
obmcr (89)
spnllx (76)
mbbuqoi (35)
wjxgg (177) -> symdxo, dsptf, yaxeloo, yxrhis
chcjswk (89)
anamgt (346) -> ywwxi, rnbvid
zjwqc (26)
wxgoew (1481) -> hnjszii, ygqxl, xhkwrs
dydcy (76) -> drnki, uxolsws, lrcstqr
npttye (42) -> wkrgvo, jhydv, enmjipp, hnyjyga
yjwvnhl (219)
fykgs (43)
vrmqym (97) -> lrmnb, nvigovl
gkfdg (226) -> ohcoit, jkoir
ictsk (122) -> devsz, jjsyexg
gixezcy (37)
rywtmt (158) -> nevrtrs, sybvdj, qcorw
pwhtvdh (40)
yapfoe (59)
xnnbqju (90) -> xzsmw, petvm, xyxidwf
vxiwms (99)
htaszsq (87)
mgbwxw (52) -> afbrhy, jrsfu
rdzsisf (59)
qvxanzu (262) -> nxhfgx, vvzmdr, inddon, ybosi
ysbhsn (181) -> wleavrv, kmvvxon
tirifqs (6489) -> ofbqk, iqdiez, kspsz, kejph
rnkbli (84)
bjbndbg (169) -> oqsdzpe, sbwoye, yhukqf
dndrnc (25)
oxzhz (86) -> bcbftl, hjzgzoe
ufrhi (68)
gsyeaes (26)
kgbzu (180) -> wzczb, bzqjb
dgtxjuj (97)
xulgx (5)
wleavrv (16)
qnhbmzp (118) -> wktzh, zodwdpq
csrpy (62) -> zmoxc, ccgjf, umrqldb, gdamb
ldqyt (50)
btwmd (54)
volompq (96)
qmshniw (443)
lrmnb (98)
yijwaf (32)
paoxff (98)
ulbute (95)
lyzaead (939) -> jfqddfd, ucpkpfb, sbmwazv
rodntl (60)
tykcvi (9)
aftnyad (188) -> rfqddq, recxxj
zdelqb (155) -> jaasf, snqnh
akwcv (65)
nszqngg (44)
eavas (45) -> ytsmc, mrxdp, prjpkm, nzawh
fqvbdq (96) -> tzimies, jduij
mabcqcb (194) -> itutdol, vtokttx
trvtkqj (49)
ynlzggk (36)
pggjo (19)
jajdx (19)
ackyirz (16)
gtiopzn (49)
idvnxqp (5)
njsjq (273) -> vptdap, eteyvz
qkjdjpe (44)
dzfon (61) -> wksjlix, zicvok, utiwem
nxmhned (166) -> pekohn, xnszvs
pnqycz (43) -> gkkit, khyca, yudzxoa
lvkeqm (192) -> lneyu, uopxjn
qvrvcu (19)
hvwyae (23)
ocgbpez (114) -> gjgrhw, bvtgvu
mehuxr (53)
pmdcajx (7)
ybixf (299) -> xvhgvw, ooczbeh, ksbwlir, pkzwosb
inlft (36)
hshafy (65)
nzfko (7)
vcnael (95)
nxuer (13)
pulql (59) -> akwcv, uijffti, ysxvzdu, xfbfvuu
hlbotz (13)
zhrdezs (28)
aqxaecv (297)
ppjapn (27)
bbbvmxo (21) -> rceksnv, uhnlse, rswnjx, ogcmm
ikvzux (44)
hdvcz (156) -> zisdcf, keurs, bjops
ytsmc (22)
jiwfia (13)
jthpj (44)
dtijfqc (76)
vgfhpwb (99)
sjmhuxn (11) -> aceyee, iohigm, zildb, vrmqym, pxxabj, gjjfx
byahs (65)
qllime (202) -> dspkk, wgtnepi
ksbwlir (36)
hzawlq (16)
kgwftu (87)
qtzelhq (62)
wabzx (209) -> sfazwz, lnndami
dyazidi (219)
resoi (25)
hgwkyu (91)
urdgg (166) -> srypr, fnayjx
hsfhqhe (17)
metif (68)
ifxzdfy (96) -> ssnpxj, ejhojmh
jefsr (477) -> fqvbdq, xsygbj, rcluk, dcero, lfgqgs
oglcdgs (140) -> dmvyuf, xvzoy
jrhzmbj (45)
mlvhqpe (91) -> qsstg, tnrrui, utsnke, gxtfu
iffxdk (87)
xboqv (17)
hppxlu (174) -> lkjhmiq, kntwy, auhnyn
pralyx (191) -> dmkfnm, xcmzg
osnkrr (53)
nhvyso (77)
mogwbda (60)
rqaxn (96)
vxnsova (5)
xsxnizc (50)
hskhxx (36)
ogcmm (57)
drnki (25)
ecjxs (197)
dnniv (16)
wnjaw (369) -> brvxyyg, hsvmept, praagwp
xjcxk (24)
aahqvqy (74)
hpwaux (97)
sadyx (59)
dptekr (112) -> xiqthw, ihtfo
mlmhe (4563) -> uwxjkq, uqals, ofkvpq, pyxdkm
yytmc (66)
hmbuu (16)
ezzpr (94)
zpxgfq (118) -> tqplqn, fysxwmd
hgkmod (75)
earmfdp (83)
mxpgmte (5)
kcfgbv (73) -> fdeowqq, pbzvjg, tzrqwt
jtxjj (120) -> hiuviy, sadyx
dsptf (8)
dsezlbe (54)
onzind (245) -> wayzzn, ystgyng
pjndde (422) -> yseezd, cseckdt
rnbgz (131) -> iuehdsr, xgzluhk
yswonja (195) -> gachtig, bjadb, gtiopzn
piizso (59)
msqxo (47)
jacmj (29)
hjsrvj (64)
prcxksh (20)
aceyee (219) -> gixezcy, zqwqcnq
pkipy (95)
czbydf (75)
bpguivk (32)
utapoe (84)
qjdou (87)
njhlrtm (38)
pkzwosb (36)
wpphwjv (83)
teqej (66)
lneyu (64)
dicalia (44)
opzxu (46)
gasejp (15)
llikz (22)
uhtnl (5)
kntwy (25)
wzbewii (157) -> myetb, dhwakp, vqtalpm
vkaxa (83)
kwnqw (49)
uhnlse (57)
zqamk (37518) -> mflijpx, ikzap, wzimze, agjpn
fnnykbh (91) -> nxqwag, tpcbt, elysbb, xlaqpg
ytrsmfx (66)
pyiexlj (92) -> oozbxqb, kzrgfb, klege, csfjt
yaxeloo (8)
tzbmy (71)
pjecv (56)
gsaqlad (70)
gmzcjo (76)
cuscn (114) -> fmdba, ikvzux
rbzmniw (52959) -> tespoy, tirifqs, exrud
jzoxv (52)
egizyey (78) -> metif, towuup
uxolsws (25)
twyhx (86)
nqjydpi (44) -> rpgzp, nszqngg, jthpj, qiksfr
avecfoq (95)
wltax (21)
xfyqx (20)
tnrrui (57)
gmveehb (46)
kymbvpp (67) -> qzvobt, osnkrr
xbccghy (66)
iqdiez (134) -> wkkmvcn, nkzgse
pmopji (128) -> gpcyq, qsdyww
cfwxyl (210)
khzqqwi (12)
wjrhp (992) -> nyouzhg, ccxff, qmifv, oonpy, vutdji, owukmji
yvlajs (35)
hkltivy (26)
vylzag (33)
mieynp (21)
jppbvbo (929) -> ynvesz, tvwmzal, mbwaxn
yxxgd (296)
utiwem (81)
ihvefep (110) -> ffzzzc, ckzaj, zfyqzi
vfupn (32)
jhydv (95)
vspqi (201) -> wzjonl, dnniv, pdazlob
iohigm (248) -> icxzod, mclqrmw, pjkyydd
hzehjo (43)
kwhgtnk (78)
npxexv (66)
lycfbo (89)
vezhmd (47)
amqvr (274) -> aditjen, xvdmeo
vbqpp (35)
upurae (33) -> rdzsisf, lslhph, urwaex
uvkwg (88)
wapknj (2443) -> xulgx, idvnxqp
mvgmf (105) -> dicalia, qhkhuow, phnuqn
qmifv (163) -> hzawlq, ackyirz
xlacmu (87)
aesiz (86)
jjiikvt (25)
prjpkm (22)
rbtco (1110) -> dfofyir, qnhbmzp, dzfon, zmdkea, valby, mabcqcb, mifwbmm
greav (20)
dmkfnm (30)
ftezz (24)
iuuouds (14)
jwjuth (390) -> hmbuu, oxlzlor
gzwrv (212) -> efqjc, gasejp, qqooh
wgdnyy (75)
rqhfxty (53)
qhpvuzi (75)
cvxqnh (53)
stqmwk (96) -> vcnael, dhobx
wuuvnlz (206) -> pznkdcr, ucfipvi, jfhzgp
nnyws (190)
bbbhx (5)
qdfvw (69) -> hgwkyu, uvpuko, wclnx
inddon (18)
gyirkcj (138) -> inlft, vkihn
lrtzi (53)
pjlxc (62)
slufzy (34)
zkdwz (20)
tigvdj (44217) -> xtnmps, ylnobx, mlmhe
vptdap (23)
aemkbp (35) -> dwrtbo, rkerea, iffxdk
dpngy (17)
nzhbfc (207) -> hvgozl, hsfhqhe
wayzzn (50)
myhnuu (66)
jrsfu (79)
gqeiy (257) -> opvrgh, sibvtz
xgzluhk (21)
fiynyre (156) -> mieqogh, zpaivc
vqtalpm (26)
thkjz (437) -> insleik, ayjse, sgovqnf, wjxgg, euwab
ylbftp (82) -> epcjds, gsyeaes
ndikjqv (22)
tqplqn (36)
aifpxqv (89)
hjbfr (20)
lltgjo (32)
picnycy (33)
kplvk (24)
ptatzl (314) -> sfdclf, ibbxb, slzpby, kjjee, bbtnj, gkfdg, nzuswm
qtxmjwm (7)
ckudisa (78)
opskc (35)
qhkniqm (96)
rqyxzn (34)
vdcfh (68)
hpziqqg (637) -> ypqkl, nmazby, hxswr
vrfme (20)
ozdnanh (34)
qcmtgvr (12)
gvdlvgg (20)
krnbkr (82) -> qladcl, tefdmi, ocdpr
fyxttac (39)
hbbpp (95)
hjzgzoe (38)
hjqsj (85)
asevk (44) -> hpwaux, byojhfr
fgzgfc (44)
ejtdhx (57)
ntxcpwl (36) -> kerjk, nggubzz, utapoe
fqsjaz (10)
hxswr (74) -> bixxpzd, htaszsq
dinpz (20)
yxxdal (44)
wozakri (251) -> mgcpbp, omslcm
dhwakp (26)
kvylxr (92)
lsbvzaf (75) -> ibqrz, cokvree, volompq, zgxbjj
bixxpzd (87)
xbtjl (294)
dyfzj (95)
utsnke (57)
sxjlr (91)
ckfefl (115) -> khzqqwi, fzwzr
ezlfnhs (62) -> qftwuv, ynlzggk
xguqqao (98)
jazqb (7378) -> xadcuw, hocazx, cqvdpy
dsmjo (32)
gpcyq (55)
dhvsrt (7)
jllqymn (110) -> dzwfsix, paeel, jclntv, qjdou
zkgdtp (90)
mjqkaqs (50)
nzcqte (140) -> wkkdc, pwhtvdh, gugaaiq
woypnze (91)
dcriqom (79)
zppujp (34)
aqacmr (18)
rkazlp (38)
fysxwmd (36)
mzutqi (571) -> qdfvw, mxwgu, yswonja
zfyqzi (67)
wqshh (460)
rztur (86)
bdlnohy (584) -> dodrbx, qwotm, cbavt, mvgmf, igcmpn
qqmvd (14)
uwxge (94)
ijkpfv (218) -> rxcgwd, steez
slzpby (136) -> nxxlbnt, ozdnanh, zppujp
dzuqljn (7) -> spnllx, fpeiss, hjzkjuw, pjoqde
dporud (50)
hrdggo (152) -> agztuz, mehuxr
kigyp (65) -> hjqsj, ijtis, engpslr
qcorw (83)
cmsqe (12) -> njsjq, zqpxn, pulql, fkttd, wozakri
keurs (18)
pyxdkm (872) -> xnnbqju, oxzhz, zaargo
pjhpwh (35)
vdlbwyo (24)
ocdpr (44)
gacseeh (89)
xzsmw (24)
liujmc (41)
myetb (26)
xawzbz (64)
qmyfg (114) -> weipv, woypnze
heisrl (36)
mlzmimg (24)
ayjse (75) -> veabcj, aicjff
htitjjt (203) -> nswcez, msqxo
xhkwrs (324)
tdkdiqe (87)
ukgbdva (65)
qmcphv (32)
fmhfnhv (24)
nhjtvk (47)
sbmqxu (25)
ewobo (25)
hvgozl (17)
ysxvzdu (65)
sfazwz (68)
hlwesdc (24)
wgbvle (422)
ugzmeb (77)
hbptt (138) -> uezwz, gbckkh, gvdlvgg
auezw (95)
lkuwf (95)
cneno (190) -> uwjobru, jeadxth
wkrgvo (95)
koxzeku (79)
vehziv (67)
codkti (71) -> tqbtvqc, oausk
kjwfeoj (82)
dcvfkk (111) -> uahcz, xsxnizc
lcnsf (22)
zzwmn (40)
bywbrk (80) -> rnkbli, vlwvot
jpmrs (94)
lfgqgs (187) -> vbjpz, hlbotz, boalcdm
xbnmg (48) -> aesiz, tqelui
pcvfgti (29)
ucpkpfb (181)
blkewbk (64) -> jlsryou, idokb, avecfoq, ozyqew
mbwaxn (240) -> nachvlp, prcxksh
wgsgaj (17)
fzwzr (12)
mgcpbp (34)
jxyakll (97)
fdeowqq (77)
zxmwy (35)
yudzxoa (84)
wwbebbr (95)
wgtnepi (66)
wkkdc (40)
xlccnkv (13)
yxrhis (8)
uwjobru (22)
csfzl (64)
dspkk (66)
xwknab (28)
fmdsfus (98)
vpirde (64)
nulax (10)
ymkgx (23)
psetts (80)
ucfipvi (67)
hsdym (340) -> onjqcrh, eitdb, ycuuwxa, mxemqqb, pnqycz, wexncjl
wqojj (22)
xiiqh (98)
cqjsqh (360) -> bzmqg, jpscxfh, ercxmph
wnowypb (83)
snqnh (95)
mifwbmm (114) -> tfezflv, qxrspl
fcgkmq (68) -> thftfut, svtqdbd
gachtig (49)
qxnvoh (214)
ihtfo (87)
qxrspl (95)
nnciip (95)
ercxmph (318) -> ixncawy, zhrdezs
iqmpc (53)
rnbvid (49)
xukfcd (28)
bjadb (49)
niifkl (90)
kxrbd (20)
lrcstqr (25)
gackyrq (22)
cbavt (161) -> qvrvcu, uhuees, pggjo, jajdx
mahlbe (6)
llpbev (29)
efqjc (15)
efvqwzi (7)
epqowm (45)
fjdlcbh (139)
csfjt (92)
zrnlkl (63) -> dyfzj, xviqup, atrzkqf, ulbute
xsygbj (130) -> vdlbwyo, ciquv, msdcz, kplvk
cdfmatu (80)
xeihyok (81) -> uunpyb, wfgzr
ssnpxj (56)
wclnx (91)
nnncfl (335) -> sgytd, nreuwh
cdjxwb (99) -> buznuv, hkltivy
aditjen (7)
auhnyn (25)
nvigovl (98)
yeyxf (16)
uwxjkq (905) -> jblwph, cdjxwb, dydcy
lkjhmiq (25)
teygd (170) -> llpbev, nrxyk
jaasf (95)
dwrtbo (87)
hwgwzv (57) -> qqqbf, fnslg
alhghui (279) -> qbhhtw, ltytvpb
mjqzvuu (195) -> hvwyae, tmzxl
wzczb (61)
ciquv (24)
gozhrsf (762) -> ifxzdfy, uuxpvxf, zyqssjb
khyca (84)
atrzkqf (95)
psjec (97)
xyxidwf (24)
esized (69)
towuup (68)
trszl (44)
fkttd (141) -> hbhfdlh, hgwbg
olvztw (21)
tebkmhi (25)
ltytvpb (90)
msdcz (24)
csdap (27)
vqinar (2904) -> qhbrmur, nrgxdmx, angpy, gcswiam
yxbaldn (122) -> vxiwms, syvza
swgjx (6)
mflijpx (75) -> oxypy, rtwlo, vwnvlh
pygrhr (144) -> rdorrx, pjecv
alneot (25)
wdbmakv (42933) -> ktasnia, mxnaq, mcrhiy
fjticim (35)
rsfxf (123) -> yjnzgl, glrmew
tyvjs (12)
gbckkh (20)
dgqfrv (35)
oozbxqb (92)
oypvhy (140) -> yvlajs, pjhpwh
fnslg (52)
vhzfut (96) -> obzrtar, qtzelhq
iqjqlfq (59) -> gmzcjo, rrzyzq
amklj (23)
tvbgr (80)
qsrxouy (96)
rauho (72)
tzrqwt (77)
pdazlob (16)
uhuees (19)
qebqgxd (94)
ffhsg (79)
hzuyh (50)
oiuztx (92)
wjdeth (5)
bjops (18)
bwvlnlt (38)
baedi (89)
irokors (39) -> xiiqh, paoxff
zvtfm (41)
aizdt (54) -> zjpkoar, zzwmn
ffzzzc (67)
oxoul (12) -> fkzxb, chcjswk
dcero (34) -> ssvfbfs, nxbec
rloxobx (421) -> jiwfia, nxuer, xfcktep
foznw (146) -> dpngy, wgsgaj, xboqv
buznuv (26)
tduxvx (326) -> iktget, vylzag, picnycy, lfdery
hiuviy (59)
dtazpb (85)
oxlzlor (16)
bvejguc (68)
uwjkolt (52) -> tvxvtce, igdkn, rteyxil, qvxanzu, qllime
rvqopbu (67)
owukmji (195)
pbzvjg (77)
agztuz (53)
zpaivc (19)
nofpmh (290) -> efvqwzi, pmdcajx
mhnnmp (8) -> qbaosu, pjndde, anamgt, bcesxba, blkewbk
zfqmic (67) -> lkuwf, pkipy
tespoy (5) -> bdlnohy, jppbvbo, fgsmzi, sjmhuxn
qhbrmur (1450) -> kcfgbv, dyomhm, nofpmh
lkdyq (57)
fuaio (16)
ccxff (53) -> cgveph, tzbmy
fioegdo (140) -> opzxu, blyms
bgnfpcr (75)
bmukspb (106) -> jzoxv, gqvmeg
sbmwazv (39) -> arrvxtj, hawhqex
xqwfgy (1496) -> cywvxf, bjbndbg, mlvhqpe
jfqddfd (64) -> ewgadin, fyxttac, gvtcy
empixc (142) -> hlwesdc, xjcxk, fmhfnhv
zmdkea (154) -> bgnfpcr, hgkmod
jeadxth (22)
ucilvib (40) -> ddgnyfo, koxzeku
rteyxil (334)
clqfbvi (66)
lfdery (33)
ijtis (85)
rmshk (24)
kptdem (97)
ropdc (226) -> usevjww, agthzo
talptwp (77)
bzqjb (61)
idokb (95)
kynezb (79)
tvxvtce (52) -> ujgeml, jpmrs, lpsaav
athuly (98)
vazoq (248)
rxcgwd (38)
tfezflv (95)
cywvxf (279) -> greav, kybtla
lfliwg (65)
qjkfys (353) -> bjhxuqc, cvxqnh
vvzmdr (18)
gwuixj (31)
svtqdbd (61)
nqfqgj (22) -> niifkl, fosdh
lxzvkpk (458)
gewpohj (16410) -> cvqbwem, uzljl, zlhpt, vtcxw, iffluz
bggovyb (144) -> supjxi, mieynp, wltax, pyhof
pbdafpz (236) -> wjdeth, zacwh, mxpgmte, wjgjhc
pqrpkmd (34)
maftysp (53)
qqqbf (52)
fpeiss (76)
qsstg (57)
oqeam (128) -> qjzss, gwuixj
brvxyyg (30)
oqmxlu (39)
tlpfhx (147) -> heisrl, hskhxx
icush (877) -> rsfxf, zfqmic, axzszf, gzwrv, cujuai
jagajrh (93)
kejph (98) -> alneot, jjiikvt
acvzsbe (37)
gqvmeg (52)
olebdv (65)
tqtut (74) -> ykitsi, wxvjyn
tzngdx (486) -> pvyrkg, hppxlu, eovobtl, diqdy
vmsoc (61) -> euvrdg, dcriqom
qiznqk (77)
kspsz (112) -> tduix, aqacmr
kybtla (20)
ktjdpt (23) -> tdmirp, qhpvuzi
jmvcgo (88)
hjzkjuw (76)
qinne (35)
ypqkl (64) -> qjeuqe, wowxv
epcjds (26)
mrxdp (22)
pznkdcr (67)
kmvvxon (16)
xlaqpg (81)
nhtfal (23)
bxqqvue (5668) -> zqbpucs, mhnnmp, ewqcktv
ipnvjje (80)
noibcw (95)
pywtg (16)
omslcm (34)
sxdngcn (6)
insleik (209)
wxvjyn (63)
ntezb (25)
klkwsa (57)
figvamv (32)
phqpwkw (1192) -> egkiqcp, ecjxs, foznw, tokyi
onjqcrh (67) -> lkdyq, tptqtpq, dmidur, klkwsa
igytdcp (160) -> vtdbov, dporud
vrtgae (66)
bwgimi (242) -> eohjrft, ankrgg, kvvkbhi
bzjxil (23)
ankrgg (55)
okurp (5)
rndvcf (39)
rkgoovn (104) -> qyfsc, lytrpo
thftfut (61)
jduij (65)
invra (180) -> sxdngcn, mahlbe, swgjx
wkkmvcn (7)
igcmpn (55) -> bcadp, sxjlr
pgaiut (90) -> vtccvv, mgcnohi
iytvm (15) -> juoaena, qebqgxd, uwxge
glrmew (67)
uqmaluk (70)
qstlv (75) -> qmcphv, bpguivk
gtbgp (234) -> ilsgqdw, qakiz, zesfmu
rziopi (57) -> flgpg, nqjydpi, xbnmg, xxdcgas, vhzfut, sfwzqk, kirnt
rdorrx (56)
oxypy (1992) -> sflonq, igytdcp, nzcqte, sjbfmfa
pekohn (65)
praagwp (30)
qqooh (15)
nzawh (22)
ywwxi (49)
phnuqn (44)
ylnobx (5204) -> rziopi, mzutqi, lcitl
gumncu (24)
cjgtra (900) -> nfkfex, rhqfb, oyyctv
gjgrhw (94)
paeel (87)
xiqthw (87)
ogowst (176) -> pdzooh, xlccnkv
mevujmj (83)
tlqjsb (994) -> odxpup, znagag, obmcr
ejoxsy (38) -> lxwkpqh, zdelqb, xyang, gtbgp, onzind, wabzx, kzjtb
agthzo (15)
xyvnk (32)
crchwpb (36)
pjoqde (76)
fgcajp (50)
tefdmi (44)
xctuhbx (72)
tokyi (79) -> yapfoe, yyecrv
njxrb (60)
qotyaq (7)
dnbejx (70)
uhrdeol (171) -> qinne, opskc, zxmwy, dgqfrv
cwxspl (12) -> nnciip, hbbpp
nggubzz (84)
uuunqk (9)
lxttas (133)
xvdmeo (7)
gkkit (84)
wexncjl (295)
jgsmitm (173)
pxxabj (33) -> wgupfl, lpdhdvy, lfliwg, fklfgd
ruedk (146) -> kgwftu, xlacmu
ydpemw (3192) -> ymkgx, nhtfal
ibqrz (96)
oyyctv (34) -> ipnvjje, tvbgr
xfcktep (13)
jblwph (81) -> lxexhp, vbqpp
steez (38)
xnxudsh (78) -> pjlxc, nfywcyp
rxjly (133) -> rftuf, hzehjo
eteyvz (23)
eohjrft (55)
wqilo (32)
tbmyue (54)
nkwwia (1405) -> dsjcqpn, irokors, wzbewii
oausk (31)
rpjfkh (55)
mxnaq (3937) -> glcsinj, icush, wjrhp
kviiza (70)
anggtqq (86)
uuxpvxf (114) -> nhjtvk, vezhmd
yrolq (64)
tkjofj (60) -> mjqkaqs, lnfjj, nakli
nasbs (70)
usevjww (15)
valby (106) -> vgfhpwb, xtnvc
zxygmaq (10)
tdmirp (75)
zodwdpq (93)
uyhrcfl (76)
mqgbif (73)
oqjqu (67) -> xbxxe, yjwvnhl, vmsoc, tlpfhx, rxjly, dyazidi
euwab (49) -> cdfmatu, wawtrk
admjq (40) -> qvaayfl, uqynzy
petvm (24)
zqpxn (196) -> himyt, zvtfm, xpotznx
nxxlbnt (34)
kpbawoe (26)
zlhpt (74) -> zvbqni, iytvm, htitjjt, aqxaecv
kkmax (37)
recxxj (53)
ejhojmh (56)
dnovxt (44)
crslvc (69)
fnayjx (64)
lytrpo (47)
auvuxv (242) -> wqojj, ndikjqv
zesfmu (37)
cnffplo (166) -> fuaio, pywtg
dfmjy (399) -> isxysg, dxlpr
xcfxvd (92)
xznhz (54)
mclqrmw (15)
cqvdpy (62) -> yzcez, nvrjzg, sebvkw, pgaiut, bggovyb, wfsaglg, teygd
fewgct (90)
xaden (108) -> jagajrh, fucxhz
xvhgvw (36)
ejekn (98) -> kemkz, souqntk
hsvmept (30)
zwopz (60) -> byedxex, yxbaldn, hnkvw, lvkeqm, kigyp, ruedk
uqynzy (80)
axzszf (167) -> iiuqtqw, vktjns
gugxitg (553) -> trlcj, olawkuc, xeihyok
wugia (2689) -> temju, xkymbld, ntlrkw
lxexhp (35)
scnhwcs (74)
yhukqf (50)
upozls (20)
qladcl (44)
wjgjhc (5)
fucxhz (93)
nayvvrh (25) -> ejtdhx, oyurlfq
oonpy (15) -> wyryqvy, zkgdtp
xowkw (41)
zildb (116) -> umjcr, pinqp, piizso
hrrld (1802) -> pqiuhyp, nkwwia, exsmez, rarkt, hsdym
lzojty (214)
uzljl (710) -> pmolg, benqzp, khfzis
vyinb (154) -> fzyim, vrfme, hjbfr
syogw (36) -> mevujmj, wpphwjv
qyfsc (47)
wvvivob (6)
wksjlix (81)
reomle (191) -> jacmj, amcixd
fzyim (20)
zfipnh (21)
uopxjn (64)
gaxdd (25)
dzwfsix (87)
nrxyk (29)
vbjpz (13)
kgxfc (30) -> kzjozhi, dtqgdc
nfkfex (134) -> vsjjq, nduildw
cpujsn (22)
weipv (91)
wjceo (184) -> resoi, gaxdd
unkkoph (119) -> myhnuu, lcmlbj
lnfjj (50)
bmmzqxb (81)
gzocw (110) -> qkjdjpe, yxxdal
uxjaa (131) -> coapfqs, kxrbd, rkctaq, xfyqx
jimltsw (16)
nptqxtu (95)
rpwdig (10)
xflhoc (20092) -> bqyqwn, hycgb, nrgzcge
jfofam (6042) -> gewpohj, ndticx, xflhoc
syvza (99)
whrinsh (34)
coapfqs (20)
souqntk (98)
rpgzp (44)
wgupfl (65)
jxawk (34)
zeolg (214)
qzvobt (53)
nmazby (120) -> yijwaf, idmqvse, dsmjo, wqilo
yuiyjpc (862) -> eavas, lxttas, codkti
rkuzg (83)
gdvuw (179) -> vrtgae, teqej
pinqp (59)
xtnvc (99)
gppwsbp (35)
exsmez (1357) -> pralyx, tkmfbk, unkkoph
ewvvb (83)
nlfdps (87)
jmuqp (44)
mieuhe (97)
donzb (407)
igbzlxl (27)
invqsb (5)
xxdcgas (30) -> auezw, wwbebbr
qhkhuow (44)
sgytd (62)
ikzap (5388) -> mjrktxe, tlqjsb, yuiyjpc
kvvkbhi (55)
xahvbm (222) -> udgssh, bbbhx
iiuqtqw (45)
isrgei (173)
ntlrkw (36) -> gkwyfz, acjedny, mcucysr
qxugs (31) -> iqmpc, lrtzi, krgtrdn
sebvkw (214) -> qotyaq, dhvsrt
gcswiam (1183) -> vahmn, cwfydbh, cjjytkr
ncuzpin (39)
sybvdj (83)
obzrtar (62)
thhakxn (103) -> pplis, tykcvi, mklqpn, jzgvab
vtjtyp (152) -> dhisacj, zpxgfq, oqeam, fcgkmq, nnyws, qxugs, oxoul
icxzod (15)
nakli (50)
bzmqg (374)
dhisacj (73) -> rndvcf, oqmxlu, ncuzpin
pdzooh (13)
pvyrkg (51) -> yytmc, clqfbvi, tmkli
scvhl (28)
qwotm (169) -> pqrpkmd, whrinsh
dcpzwz (87) -> wxgoew, xqwfgy, hrjlzxr, wapknj, ejoxsy
qsdyww (55)
puvmdie (41)
umjcr (59)
himyt (41)
tptqtpq (57)
zkwajbd (61)
vutdji (31) -> bsvgagj, puvmdie, liujmc, xowkw
lpsaav (94)
bmcwbsi (96)
rtbcch (64)
nadbegy (66)
jyazs (74)
xcmzg (30)
abxglwt (191) -> pmopji, jtxjj, asevk, yznmd, jfsgqq
tzimies (65)
jfhzgp (67)
wyryqvy (90)
kirnt (134) -> bmlfd, fykgs
xhgza (16)
xajzwdh (65)
tpcbt (81)
zmoxc (99)
bcbftl (38)
arrvxtj (71)
imiimt (22)
tqelui (86)
sibvtz (79)
pchfpqp (86)
faopk (147) -> figvamv, jlsmm
wscqe (14) -> ezzpr, chyun
emkgc (142) -> lcrbt, pcvfgti
nreuwh (62)
vahmn (49) -> twyhx, rztur, pchfpqp, anggtqq
eourjv (204) -> kpbawoe, zjwqc
ssvfbfs (96)
dxlpr (8)
sgovqnf (69) -> kzsoasg, dnbejx
eoxwp (133) -> zxygmaq, xadjes, nulax, rpwdig
ydffzgu (380) -> olvztw, zfipnh
byojhfr (97)
nlwakg (161)
ztxcc (68)
zisdcf (18)
itutdol (55)
cseckdt (11)
zqwqcnq (37)
fhqhu (188) -> igbzlxl, llalaql, ppjapn, csdap
kzsoasg (70)
cvqbwem (92) -> wjceo, gqqsfsr, vukpdsr, cneno, bvaoy
pjujovx (96) -> ayuma, bmmzqxb
vjobpzv (24)
kerjk (84)
qvaayfl (80)
bcesxba (444)
hnyjyga (95)
gjjfx (131) -> btwmd, xznhz, dsezlbe
idmqvse (32)
ygqxl (16) -> nhvyso, talptwp, qiznqk, ugzmeb
ozyqew (95)
itxgz (370) -> epqowm, jrhzmbj
afntec (96)
cgveph (71)
isxysg (8)
cqlvkj (65)
ykitsi (63)
bjhxuqc (53)
uahcz (50)
vbejzc (38)
cujuai (157) -> ldqyt, fgcajp
kgphv (246) -> wvvivob, sjoov
gqqsfsr (78) -> ckudisa, kwhgtnk
dofou (44)
uijffti (65)
nkzgse (7)
xrtzs (96) -> ictsk, invra, rkgoovn, gzocw, hbptt, ucilvib, cnffplo
zvbqni (105) -> qkzpcyy, qsrxouy
zqbpucs (568) -> dfmjy, fnnykbh, gqeiy, fifams
lnndami (68)
rcluk (156) -> fjticim, mbbuqoi
zylotoh (7)
phcqntb (76)
amcixd (29)
jlsryou (95)
rceksnv (57)
vwnvlh (1534) -> krnbkr, egizyey, empixc, lzojty, vyinb, zeolg, qxnvoh
chyun (94)
hrjlzxr (1124) -> ybixf, qmshniw, zrnlkl
bwlit (20)
grxdbx (34)
eqgvf (9) -> wdbmakv, zqamk, hvecp, rbzmniw, jfofam, tigvdj
uqals (78) -> ropdc, pbdafpz, mgqil, pygrhr, eourjv
veuzidj (49) -> kmhug, yrolq, csfzl
eovobtl (149) -> hzuyh, iftcnc
udgssh (5)
nxbec (96)
dyomhm (40) -> npxexv, xbccghy, jncjxue, nadbegy
fsdoohr (64)
lcrbt (29)
rarkt (1387) -> mjqzvuu, nzhbfc, veuzidj
temju (53) -> qpzszp, cqlvkj
nrgxdmx (1352) -> mlalrpt, nqfqgj, cuscn, ogowst, vfrylx
tlpfggk (25)
wzimze (4005) -> uwjkolt, jynmg, ibqmynm
ddgnyfo (79)
fyaxzl (18)
qpzszp (65)
eitdb (197) -> trvtkqj, kwnqw
fgsmzi (525) -> dzuqljn, ihvefep, uhrdeol, gdvuw
nevrtrs (83)
jyftx (76)
lcitl (1114) -> nlwakg, hwgwzv, girxc
kzjtb (78) -> gacseeh, lycfbo, aifpxqv
zacwh (5)
glcsinj (90) -> aemkbp, yxxgd, fhqhu, xquhgig, nxmhned, lqbmor, qmyfg
rswnjx (57)
cokvree (96)
ewgadin (39)
oqsdzpe (50)
yznmd (62) -> uvkwg, mncivb
lpdhdvy (65)
kmhug (64)
bvtgvu (94)
hycgb (237) -> zmciyk, ysbhsn, vxslvq
ycuuwxa (161) -> vehziv, rvqopbu
mieqogh (19)
xadcuw (1626) -> chgfb, stofi
supjxi (21)
rfqddq (53)
qbaosu (314) -> hshafy, ukgbdva
ptxfk (73)
lofybs (89)
agjpn (8265) -> ocgbpez, ejdxula, kgbzu
mgbgb (334) -> kksizqf, dofou
izxpf (39) -> ewobo, ntezb, sbmqxu, tlpfggk
znagag (89)
zmciyk (19) -> mieuhe, psjec
dhobx (95)
hvecp (90) -> hrrld, jazqb, fonrb, dcpzwz, vqinar, bxqqvue
sjbfmfa (80) -> fewgct, jupzgjm
fmpvv (74)
bcadp (91)
tmzxl (23)"""

test = """pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)"""

#print(createDictionaries(test))
#print(getBottomTower(tower))
print(recursiveCircus(tower))
