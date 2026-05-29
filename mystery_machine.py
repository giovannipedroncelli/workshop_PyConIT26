#!/usr/bin/env python3
"""
Mystery Machine — Workshop Target
===================================
Start this to launch the Mystery Machine on localhost.
Your mission: scan, discover, and explore!

Usage:
    python mystery_machine.py

Press Ctrl+C to stop all services.
"""

import atexit
import io
import base64
import hashlib
import importlib
import logging
import os
import socket
import shutil
import sys
import tempfile
import threading
import time
import zipfile


_BLOB = (
    "#nns#jpuzYQZg6Xd*U_YCiCVV`6@aI(RU2d%pvQ`c|uQ*j&AvNZhS2qamtKh;Tz908atRN72zJQA",
    "2oi=z@gAT@%s?QZrH!%2Q3W83WfvDc=DRSRZD5QFc*2#vpNL>v|CP5!tx36)OM5)BgQka^|muW4a",
    ";q&R-`_gm+E|DnRt>>%ZODd%gA08^8eYDbSV}jt9#K@e?)FBDYbmT1S4b{><_PrU|%2$tmntoPta",
    "04s_`c2(rZilwZ;US!x(3X{^WEh_bsuQocLIK!Jgq}X9)Z}Rz-OW^dltuCI-;R@B`b~B}wj#6oV=",
    "K`J$dMCrD2C`fdZqsjGQS6AnaY;0MO>uxdHN6fynS<Bw3OplH`4Y{-UGK*P17f300tggRkX!qFTg",
    "xdBvCay{gY>nT<l_E;|gbp5&x7rtfJdTe|8e26{%+szK}9V<JFUpc(EccP(PX4$~deCV0sh;A5m@",
    ";t~=DYj+ts}HBhv-P;vf5b}<ue-J`2;?fl+LsgyyN+cnW@T)MI9RQ5H}rb0hEz`#FNwC)c3~;Bu#",
    "o5-O8!HXC3DR;*N6Bbb;MKNah8$3HQTWf^f4zZ<1Yj9<?`D-UX0F_@#uew<JI5Gs|i+TAxa4|f&;",
    "=4S4$yvdenf@ZwsZ!%e^B|6LuE)0SJTG(-HL{oJqgYy7u>7vkiI*K)3wgE3JRseI-c_*+-M+@eiS",
    "z6hq}^9G-&crFxTLR~Nb)I<_);K9F4}@tLk}P$lRe?<Rr_;M3CC?-pe`<9jw$3=C(wEpvJhyLRGg",
    "WQ)$rHoE(T_o_DhcIrDEw<t9sh{=H7{O;j);^z^9tiOF!9bkoY-{opyC7TV<h~M#z4q;o9Q~SsKo",
    "0Mzv4gPrNbgSZrsh7cqs+fsQChKj5u0T~zJ<(bQH8ib(neLH<sE7&y4*j81+sLBb%1iB|%!cO7!`",
    "X#tCi7Wq8wE7N{<Q4cMZC&!lNd_ha$}rVW*mz9id~@Mea=1LYlvZ?f)0?8Nf9r|frdj-;#5|=lE`",
    "3a0L70l&}3?k`x_Z|B@2;2#Y&cAAH(Fm*?_Hey-B4IUKYz5l2g9*&k7LwYQu9SfP!kOCTtbmN6z?",
    "Iy7V|OA(p_bMaf?7%IAv=olYaXR3w4R4`r*jP(Nd$Ko(*MfF!*3zh)+~a*!uK<J|6)@(jM^hE_fR",
    "<?e6=c;F@rbIUzzFHIS7;wc51bRc>Nx>^39x7zakYq|+6;T~qUD@Q-8X#`CqVy1-OQwkbZ-$>cn%",
    "!$Ji;^3=(Mz9WzoMD(`ATq7g{ZT|p8Trd{SsX_xdlun_e#VTu{L%!z8kQK2>0|KZ_A3NU<79D<&5",
    "!{9qUoT|cpYv$k|Uu?VUi5evGsp#!UZ~XKY!$(EyclD%8mI|Ym-M{xs7{Jen`xV{{nj}f@q>hxhb",
    "0ngO&q;Py!-<(%-wqHlTuF+-qr|4YXTkx8klzS!k*o*V{r4K_wG!5UB~LL@a3xk{Rx$h(az6&pZ;",
    "JUo=Pd#{<EI+nigkVfsC+PFFHpHOefbDj>1Z?R|Erz<y56{bUW5q`E-U>C|O@A~tffb4kG%+Z|Wm",
    "rvuf35eU3)5o(Bo?M8g8zd_;+mB8W})G`vvAUhLiHQ!ORS89<V;TK0O#cYS?eC#c@f05?Rfm;`gd",
    "k<X4IG{<hXmEznA@8L1TmrP4ow*iMt(FJFx^GhMo?9<*&6|x|gyJHvh^<fa?U{<+w|g6H4Y+fcKm",
    "rO39#FJm2D8*c$<BuE!BO}%0_mx~_GJN?-F2R5{v82pMYX{BQFEpqgEpujNc#lmPO=+9Fm4&j5?t",
    "y#H^ni2`$d<fY%D*O7$;3qSFBBO-y(&aG<G`PD}+a0R>S}tjXPiAqd4dIh5XFuy{LPOH#}hOJzgq",
    "FcKjgWqTv$i{CM<mrV-k}8-4Tk>1&!QK1SJ!MWsu%vn&u)4)91fo2Mko2zO&d#@N8Bmb1uRG(qo+",
    "53X(R7=-cyf_clVB->nqe#B1XGM_6&_4EUN+J!gce9a1G{tcN}u@ARDxHOJI$<?%v0bR}uFWl3zv",
    "yNfBd}U;JIM453ysO|?)|wH<jA@d_6T|%zzXTHDJohbQ1u454Zd_eG9Zj-AOt4f&DOoJ_6d_ffbA",
    "TK=JWdpH`*}3d5?1XjNQHhh;kge1efFRJS3nJEXa_LRpQlG%kwQ|0Zy;7JT~B223)eNJYiT2!2-8",
    "Z>>)Lx4$b~}HF@WkO?w%HD@(3etux5(<*=)Q%Ma|aA-GvCDU_wEe>=gBkIp_w`v4W|t#KTH*qbBD",
    "941qa$w){MkoxQUYXm>l}8nb?R0^nqTSIk7=<}=^Y$HgGKK~!{ooZ!L+t}x-fZR&C08rZ>9m~f%t",
    "&XTH<=jyYDPhih^R*=(?;n>BM$9n$YjD1i;BV01mEpbUYcR+l=8-;J91qvyGz`qPPr!qjRl~O*?7",
    "*qj>t4-~Q2lMfR`(|EN(^H|~yY7Ezc8FsQbp}`!;W8AXIq+DSm?GBkm*KM{q~jA5El_3c%-Mi4k{",
    "mz_F#s)Kiu#WtkUH<1K6=0Px8scsuG^{Zp>~X)_F>Ll^M$tsUT7e&PV+<V<@#!Wu+5ZfgN)N{g&y",
    "PXi37rD<3}jKQ!xY&SsRzIuRga^v-qT2&r-fmBRVe(%{28|>ZLHD5$@5kag+^Vc2oDE3ZT4cgK!s",
    "O+vwq}kWL3+6x%b2P0WyK3PA)H&b`zd+QM-Jio?EBJfY3~*qT@m(C3zFlL<@=5{f}|J0wvt*${{n",
    "4aoyN9BpEG?WijBE=KP<8hBkesUB0e>i&m&jOuiznoa=^J=ELx8;<yEQqT;pw&Gv=o4F7dyAcGC;",
    "eWH8YW-1yIzqvvR89V8m5Ic!?RBNCf`mom5%lB+M&l`ug5;u7FmWojM2UVO=wVoRi#{1=LX?*mL|",
    "|A~#;a9jK2h84eWo>Z`wsErD_+l+DRgmbRU2na{r7hfB$SJ+ICoP2cc&6;z}S{8dge#Mol$?Y-Ow",
    "^tK|||CyuCi?xn1oj40o>KhIm5Xk)8!hd^oSDS+fdF+4kOXa?b@;FNnigX-#mfcOuuMj_A-w2$I{",
    ">qE&)=ri|^KUIlD3HL`AeI0XUQj&v<AZ_yqI^*n-u+H!I?WDrt+K$9k~F_LfJlO{5KIB|AzDB#)O",
    "ul@*AYaz)2U_BWFL~}1iUa}kTdCxL^@?b)c0N}f2r#|vhz5UVmyno<4W2ag15qI;_gF!MIM+agmT",
    "f=-phwuvP*n$*TJI6tL+st0JZIjPf@O9Y6ti7%=1;&#_Cp;|O!aD^Ny?MojH^)-2(D@`m(;BkKI?",
    "HpMjeX6wGQ&)@^fjf($h8!Tp<JCXeb)tZPnJF*iKFy#$BM<!G1ea=E|M@nxA=jGV^%XMgqgGA%P~",
    "686W3gU3I0n<*o}Yts&oy#?-+oplm}z(^7J~)1s9xbZztO55w~*|7Y&aciSaGRM1_}X>I0wIHAI@",
    "%Ao#;{c5<r+XwN2QuZ9k%Ri{(V_;Yt-WFaLmH>M}lAb__NZ?>fjsj#cK!HHZ4>M+|)G8c8SpDEmt",
    "81fJ51wyd19*Dz03R4a`Sc+XmKLn|kP|e>uCU1r+qK7|dKb%tYVq*wc^Mg--*DC;HJO-b>0DDNB>",
    "vRWQwJKg{;lYCd)=xS)@e{c0p~P|e5WfHSz<m5&4%(GUZN0f~g{x^M(r^WP*(br8J`3HMby1YA^o",
    "yc~Srdm;(gS72N*NI@(E4eYzc7AP&voAyX|b&9TXx$G*6Y6;oS*UY1|n5wIcp4Ie;KLNMwM&Fq%q",
    "35v#x+CQi48n*pSTXh;Y#TYo4BA>+a@0o86Ixe~d5&>&n53T=N#Cr;G@bAq&G`ar6)`Z`qfD6|!{",
    "`BIM-ni@#&WA;Ac_(qd4hq6w0sDIm6K+G`7vsgQx%i$wo?Bw<5+oSxScE+AZu$cxt%8+T2Gw{*S=",
    "s;AO5YupB>bM+_r4~5z0-x#^-AYXmr#5;eVn<YUKf?eUvTSa6li)LEi53kB+7D7nefCFEcta~iW3",
    "26)=r2kZrn430D3LgBH?+8A9O}hIiy`!bJRQVz;bZdmbC@#A+ju5Ue6&BP<>|8Sw%OR8_+z}_nUE",
    "~vSJLl@dIu*wb7;CF^vJ&o26G$rbP6(UTY2Dg0fs#AghjN-Ny4XBjIGxmSC!l0?T=VUXa&C&9Ib5",
    "e5vVOOQ*~cBb6kuX?;r5|*kROKHK+m!#BUN>uHZ=3P>e1T~l0~^$Vg~cO1`-r~W`SDl$?V3G<@_a",
    "FItW~ixU7*HSY6y_1j7Z}VoAD)fPt(YUb}ya32g?ru5Iu{;!6{T8Q7iK`kV=;oAnqO3mRU8>BLJY",
    "HKI-bjc74$oCt?efyH&vS@gTkE#rOfWFOR`BaKACjG>2_9)#>cZnI}v>DWjL@k8=`^H=hTW9ph&X",
    "Zif%KC0%9m{(7Kny7xvQE|||^KhdBk=Ax#B|#dit2=IyA7dE}Thon;g{HHmV&U0KVC7LybzvSMUt",
    "T5EXH4{-gbc8bkFvtF`{y^XE{`-HI2Dx!9`j;zGLW4(arj#;Gi*q7<QlE<f+62iIM0f|rL1>{jRz",
    "v@ktVrpGjv`7wQyKwPtUe&q2jb2hP~Xi7(t9}?z@==J5L@|&;g9HnHVjHBHKAIR5(8JcFRiX7^9e",
    "a4`qIV;K4PUo@YX?r;ZN$vMZOy#X-ovpB=&h?+|G?dz4BI*NF8|6ff2GKv}gsDQhZeczVzeajFe1",
    "??`o-BWrux?Q;y`b6SAer@{ujKGJhb9y5@x(;5N=TCcF6O(Fn>4Vk%DapyzbOcjtf>%konSb+NX)",
    "E#dlNseAl@-$T_uqjML#^5+Cq-gs4VI^=oZX0jb4QtVTZUg<hGg6%2DJsYYVD#$W3Ut`>bErq)v-",
    "s6ai=#=CRxZ18@WGdafqA*pK+{QcIt8axp-->9DP|c7fKW!eZ+Kn1LkwM1DQe>v)UkrKr;U8fUO<",
    "EM->u5D5I!f9as94pj|HQoTDmCE0iwAG*V3MkWdnc98qo9P*jSb4vLRhP<xK~$;Lj-r>DRLjKa{!",
    "Ef|l516IZR5zl(7lVp$cd<y=*<DRGr0BTCrN%CRr^6I=_^2VHC?58L!ThG)||Y!0u(NsfWuW%U0m",
    "h?s!oy))~zl8BQFe^Cz)u#3q&7v_9s?_K2;>g}kHu-UZ#Lb)0z2qDZ5wJ%58smV_LllgT(J-eX{@",
    "6O%8prT$$b+7Z()j!A+DPY;L*MkcY@J*J_X;0GG2dOmNcK`$C#L>gg(L(%)rhpPrdv0y`xLJ<Xge",
    "RHT=<UAH1ujvVamY4v+al}N8g0o30)8EVk$^LdGbvgK+lje{T_Mn}o8f#gj-EQeE$mF+R_-s^`=P",
    "z5oOyj8Xw$dTWE#?Gp=94*@4CRYyKHJq0RyqhA~MJ<@}fbXA<P&drfYYKG$mjRQ%gDGMFZ`H83gk",
    "19&J8M_uXso3M8XEd83g!O3fWIMxoQz2KgDbBz9U<?Sp)EwsR0e*&^I9%sF*etAi?sskAIG?e`S(",
    ";CMamn*nsgWkPZzwm8fUb46)aCpA!|Qg!_hp&ezd%c=J#^tt{m&B4vP{~wjedHP5m^ZbsYekNk=2",
    "qrphnlYyN;`yiVB7gDM>LxB;@9Yz*Fal1m?Kc19lZeF*NPBO!)K$%Ef~(F&>5I{#K;Z4_)i1I6Qs",
    "M;ZinmD)Xe0!wpF1|`iZ7M8Ni?F=*$~JGfMZ2`fqS6D2s~t3JX(&lNyrZHPS6DCePJm851UVOkd3",
    "WP0NrQeM?gco3+SM$7i25klm>V6Akams{!QuL-JcsPgZdud3*`eVKd}O_f*`o?A;if4A^VN<<I07",
    "Q8^CZhvGS||E1A(v_OpR7me~JhGPczGY&L7#GSl4DJXvkUL#(bU<2cS|ndf;hB7w70BM}g$^v7Kf",
    "&$hpzGA|`GE=ExEsKcwZyx~rL*~!Mq&JTuBmI-oF<di>K8?~m4SdwM1{&jU7Vdzz4W^Oq`Qxc<Pv",
    "Tp(RM0>~In;lFPUyUt8-_7YdKl?DJ3>;+ebN_d9N|;HT%W$bdU!+ARn0F3feLQdUAqTq^=Fhu`Mw",
    "1-0q}l1Fn(qdcEpg@GHJS=R)qrk*&ISv=jCC8ktJAks82$jTtmsR4NZPQ%U{A-nb}}vw9#!%$Nj3",
    "f=k<Q1?q>dA#-3>YCC?bZ*HsdNH&?q@Z`Dx6qcrzOu{WcA=?pXs-PHh3U-zJ?m<(}6*d?GfX!iE|",
    "4WV$%dQaK&ZEde}!D_^N+BO~Q972FZm1sd0u>4lsWq@_xqaKf>?iwcEFTGsH;<$NOvdcQ*g7m<wR",
    "KW<ArF^O|<Ai?-ZMeyqT{>bJuT+bUpQH|m+9Z`!-jz!GUkTB!8;xE*?<u=gIQFe>jc^JN#nj&wLr",
    "k6jOi2H)Pdr1lHAuzA~K-@K${UzfH)57JA1QcV-ln>p#Q6TgMjQ#7zH0P8wz=}l=tsXmPP-opOa`",
    "^J>;hu*4^L&{j<=<8n`JQg?=~nU{C)y+zC^qrM7)Cnw)O4|g-F&EMw>C_%u#t<#g{+zcz;Qi7!am",
    "2-sgR&J2rrFFamfV{6kDPfSjFQEb$-L$DaX*+s1n@n&4K5I9lFIbo4ex>+qfsK$_~bk7tNZYg2y%",
    "Zr5~#4lfwH|`(VEH)zaI<cbN;hvjM)qwzSzsWUhd65Il!cx`Zrq2eUe{GtVYI?nM`330r~BmeowE",
    "i)PH2KrDGNdzrum9~|yVVQJ_AF?v$45BYH4_M27ohApq}0!Ylat^PL<IF2KTuDdWX(hOMtsJsGeW",
    "I|L^8eRanu<?Nh`5hsqV?%S+?B1{9opEA#tpVC=gj6<k$J9;wC?mR~&WH)$#eXg=SbphDs*6oJf#",
    "<8C#uRm?$`+g%px{S;sst<RuE(FUt+e4i4N+3x0X31!nQ+$_-G@OFL-V&&Ur!s4Q`b5H1opubR>p",
    "U0E~+uMxJ41tXiQ?$1fgt?Zf3Ji_Vz*U>*izLO(^r;Nb=Zfc^(<9=NsT^Uy@nX&fuz4Y8D^%oRn~",
    "f_my{O`6l`wJM3=H7sYf1D!ET8+Y?(UNZ)LKM*(CwXCPK!SV#`9+Rmd!QW(Toj-*Tn?$$W=s<J{`",
    "621~#Hw4wiVZ5$B!tQ>R=Fha&%ieckrk5JB_AxTnRag(S2Rq||$e7VsF0X<D{oIWYP#Kq!^4;5B6",
    "z3`@jQfNtJ!#@*jwD<kBzXepI*fEGY-v|<S|k$lgx^y;N{%l(x3`?Pd*1%6qZhNr8igFxqIMdC%q",
    "v){{3H;E<=eG4qacX>!1SB-y>1DttPDk~@kI$xxe@RG?rk3MT(3v|>_OOUX_54p>DRf~^_<c!J)O",
    "FM0U|&R?@?~Ug5`CtUI$~X6g@olPWY1c!0lEpAeyHycD)aY{Hb)>sA1hRXp+&BK=fO$D$Mbh!I*e",
    "(hG$M$%DzlqvQr>3pu@qA=El&<=7kfxi`JDIv^)MF)_(;&@&;4}|1W{K%5GR$7@r`?MA7eWsF_k-",
    "kXzA-ABraV;o~g@^&melva?q&L`mW;Juy=vn?BPO3h<V#&skEDKYA-K{y8Na7$>kCFH38XnQEI|2",
    "zTufR<ZvFROT7x^Ok(sq?6eZZvgK(M_ieNf-^L&spEsMkCBgkc!1Tjzjm2g)+jNPvv#IrL)i}B)d",
    "ZF@n=-X%yq~7Z^-x`cUMHilq8)d3Q+hk!LRCL2CoStshLXNO5U=bxEh7bv=d}|Mc-#B)up^?-F7C",
    "eINI2kvkpW55FngC|Ko?LDh01sTy2s8up<So#o119}4Nw0!BcEeiZnxiOl#9=L+$-ML73Uc_SZsc",
    "R$!yMJU+nw#XCs*uZn$7-1lkhJY(Zo>bOKW@ueQ}1&(#0ek$SCl66Qh#@Z=Z5;_xD}HVsk^+q=38",
    "Mn<F?1eGvC#Yf_7KRq@xSEHF7LT!ED6iTm!5?|!9@?oR@<q1=g(Uv663z=;{qI#Jim9(S2YQAOuf",
    "{gZuO8-859IA9LSz=K@0OTp`BO3_wnA*Vd|4r@KNDMT2{>d8&7p*-7yX2StYnHAl+mLgC0P&>-X(",
    "zIkkwp!Y8X~)(AJMOd;6=}n6kGMHi70%TGr}lKAatwNB*<%rxuF$Z;#Z|-BOj_7<B%DXzKbwkeN@",
    "=CwuReJ{IyAixNl==Mu$;f-J#6(8^#Crh>f&|Hd49pa$(bMPXZAPEs}Hn>!fCkDK=;GLg-;0rz*T",
    "y&jY#7d^uaVk!6<|+V)SQBFW7xG{HktkrlFTR0NKhV{Zepjx~b$o~+K|cxARBRysW;z6)I(F-KUg",
    "$s%K=9FQc^(qcr1JoXlc!I6^4gH}x^CmhvDmo=aE=+1n1eayt(BMV*M0E^~J1(N3z`)im+L;nbqz",
    "iVs~*|Nu~jZa!Dj7oMK5b|``;97D}F25WVX{IhUbr&NO8k=rRktkwG5W@yx#IzxGFX*O6b97QQcn",
    "W3Q)x&fDf|k6@l(ouL-q4TVRr#nv>I)=h<~=)`Asz8miIox=tAGsPPqri!e8Nk4CxZtwxv5=dLEp",
    "nwlP(7;L<h1C*U@E%r);6l9(a!I6luqDV5`3;GJf*AkOHQ#iYj2@0Z@iO-itvjq85W1vAm?;&hnl",
    "72cS5)z$XvjNo+-G<=9wk^ZE*I*~YO2tr?CsL_pKzz_RrkyP5Or2GMLy4qjNt&_<*F*;C?rK2*0k",
    "!hxZ=bqy^U&pVimcj&s7y2n8}v+7!^%bk4gN4qMCvqHyoyOefIx~Wnc`^X0W2xRl9d*Sm}PCe{n{",
    "X1*=U=25|S%kDIT(KUQToJ5c1R{$0EhX|VXXSp`rcH<(Vs_uRoC)O4M}_iQO3UC|xB4=vfT*jm{!",
    "9mobbEgj-<}^M0?BPf;fw+l14EnN|9o$>UNg69R2AJ2>B?u@i3`2~()Q+jAAc&xZ>`7mlTLK)^Ab",
    "WN?us?+8X*u{)c@tZ&53Ek&fSwFj)c+BFn{b_o!~uzlKj9=6{Z)*yW|m{n<fb@1flWC<xQ=1k4Wm",
    "``2e&D&V#)aYw>fNZq-BBASuXP@-UZm`tL6!Ya$>eF8(OOhMI&MqkM*>s9mAHodSwd%XofEeN15R",
    "YWK2>_JH~6kkJGbvExBFgP$$Qp2B3z0dDDje;J~nrJP$Td@j*<7L=Pfd+@ZHdCc%@G=ON=f#B=Pc",
    "c=c}9xu*ElsmQr0FPY`j;-4(%+cy5eu^#S_o|fQp~sn$JmHCpv_RA)juI~_p!7=^If$@x0F=Jtu`",
    "za|Xi{D0hXa8tz<??GyzZ^>H|$Q%2UAV;JMnVy$ZlF9@eBOdhvNHxx1JvcrA2X)Ya5xkudQLG&GT",
    "m9e|dho{&dmAwo*YYcMMx}?Pbud2AiY$GT+@he>t(>vcoSu`l1i95`;g=YHpYVF^d%+`lVwbP8X=",
    "yT~`+{E}|AU1ENIoX%;EQmd%1)7DbznkEA^fAjR~Q{2_9dxnvZfE7$~EwIc8>FqN6I003$J=x#LZ",
    "F=D+M1jAAXwQ2P}V@<21jTo>4?8W(B)QucYOgY#<lZKWqaX=)uCXa40@ou%(j3yIIaf1~o8Up8CW",
    "%24??!Uh{P}EPz*G32D$T~38PCAACt`@Ao)~6f-CG(uye}W9vweMe<|FEJvbe&B;*$0B^Q^NM({@",
    "Ba;c47!wdZ)JG*vAotIW8@*$##i*^ycA+!X4Eo9llO3;+r!yWlj&&D;4crb9GwMQMN}bH%rvr$I}",
    "p?Gw|T-Y~j!~ayYh>I|FyJg=(DVQE)Jl&p93=P#-TpS0P<&$~@!QEA6ZFC2KhW^o}M*doj!f-`>U",
    "fQwbU)xp+QMKQ<n2a+{dBa*--WIC5>JdsJoo^j$jX%(e+dc*8PBQeF3y>JA8RZIU4v=hYqmcqpyS",
    "b+!>G&tmCHp}FRQ{e#x8%tM(Ah33^oMuN^3M!(Y&1r69(TvcT*9;|!A?RkX>?Qj^wVg+e1;0nJxa",
    "I9dCvFX;Mv+~ekG-fTZT5&8n6-zi4<nWtlw1YQYyB}#_Qu&CWEN$hsfQzeF__DXy)1*ClI(Z@<)7",
    "+rj$kCR!-^{T?2x<@%(vPmpc7UxG4<<+5afLa^D&(BifrC0FdA7~prVUqXPwIIYWJ?agTfjfg#JS",
    "EH$1$k*K;*!gvo0gHS(I<5Y!%+jhymrFqdpX0mNBIv9qbqzut?V3rjM(tMOtT1-Wx%?NY#m!!2}q",
    "FEmq>UG)+p}JXL`fMG-5f^avqgCR84di8}EQ%+s#oL_m9VfCAyRhtE)?@H&Xy+AjzDbbK{7KjPX=",
    "r)7=kuhheE8j9jmA&LV7{9`6aIo^I3J)OPrMECmbq%WNFyM>N{Oa-DobyKCw&ECtWJM&D_>C_4Ag",
    "3WCew*5XZ@jJ?`RQ>N^=-?%j^!7X{ySd%T;WA?Y5d;1n1|LUDiJT1dy8BbP7-jS<BSB2os8#RAM=",
    "si5d=7>it^`$o$kJ~<%}*bDB8$W`-ci6b!;<Z6@c3Gn3jjxuec0zxD0x3&X?wmDA|H)8e8&_Lpbo",
    "v9b2tVS&(NCyEu6zd>gm6A75`rG{vy)y+uCxjET#aGnkNU>zC5m6Cl+*9u1A9xttk2GydR%lo3M7",
    "wIaqmQW6b(pzm`pU)-fz{{i@t3<#b7%pONuE1X2~m`vAEJG4i_eDi-L)md*-HMIFvZ7OOQ6F?5bx",
    "bjnVkY26sw)>+F^{+q<_7p>SwK*V-umpEuwu*VgL8z*~uU;-;mP;2KgI~1KTrNJ&mzeG^a>O$l-k",
    "(2SWmH_Ts-NVgfYTE3EtLCpppp1O_JW%aEYO_W^t0Z8Vn!-ZD+*Yh|8F#+2E7HcjW?_g1%As5_BJ",
    "fBL!2s?+6E?H_A})1|&sbm%IAe}zru7@q0}5j!lL0`>&Abbm<IM)OAMk(TkFrrCHEb}Q!gIWes2z",
    "*))J=IiOn>@V?6kWH@l4@eA45C@8Ay&o6FFOjN+wY2U9Wif9rG#PCh?KFZGscSMCsB$ZSc}}R>JA",
    "m`_?!^=vMcZo1bKVKZgu!sp@UmE~4Z^MDqB~z{T4Hh}B6~?5eVKN3Lj@GpM^$aZN_yyBVYLPZ3Aw",
    "iw#Vv6;uqZwI6%NokV-Is-X)mY0L@a5M*7VapjU<czk<K=|o*b<u{O1ZzpstEd6W0%86(sO83+ut",
    "GdAZE-LQHQCjtjOUm!+oE1}ON*km=gyN*zPKWZ9*`Xe2g>8<L-DE!%2@P&VkmB|-8llQiPrZ>4IW",
    "YRnLZ#|9RZ8<3ZOskHY6LVSP_7+aM8v^J=4|WWn*uO3Yi37vf5E;J*+}qjwC)s*tNT1gr64Z2NpJ",
    "?h43kvInlmO{b0sog%SBQ@CmAXE!j^gkD2^933}n2pD)qa|wIo!dO8bw(S0{#>2B=j3^lepL=?J#",
    "<)VRPHe8zjWrp(P4G2f;?bLj`iP65#N8fDJOJ@JH!)D9Lbfhs_2da+B6RNU~!3OzxbAl#)LwukUt",
    "RIbgi^XWmBkJv<%%eBs|?~fqwj_K&=UxYtyl8WwXu7!dStrg`}=<o6pQ1z&6Tcw(gw=^{Vc;KWuj",
    "To(#W5+%Q-~s#e)z7-c1b+3+Flnz>*0#CZ|2onA*GKC?Nb*Z($|0wZs#$Uq4zp)iI~Bkx3NfJMtS",
    "aCkbTOpV;k3EJa25Z<ASxqcb3--Ev$F52nwzj$`EK(mn+D-0m(`bO$zE*4FbM?-NRp1|$k9(|%#g",
    "phXP*9{d$h|$B+*q`HrWCM>@3uUA!Xy9_h-^;Bzsb-e_VOnKSZPY(hXFs9c<ob!p?1B$dg3D$8jX",
    "c4aD^wEPp%h&qf8=Mai>-P5tv2pnqWzb$F7Nh$TM>W`W%8RnH1D|G&#htc0k23Vu_5N6H1nmF!x^",
    "rreE!)!`GXp(VZu=5>QZA;bZW)APTaVH+0)B+H}{i75+IB9T8m)qIx}=P2Qrp()R()=4=oGv{HRJ",
    "U;6&H@<HjB4@&k^syS*Cbg=$I$4La;hMid*-g@)@1X~+Mv%~u-iFq-9!|<wNbL$pWsk(wRx+f5#A",
    "e#b%F$!^2>Hj@#;+uf3b9#$jIV+)<!*&?>n#N!*rly0ATV7%rW=~sonmXdN?Aw|y*&UdSYI3cTgy",
    "+@I9=bHNuZ8cFPA6Le*e}x?pw&o<>r+cIc0NNd@M`;)z6{Sbdw4M6+m0?P!K9jR7~O#$;FP2-5SD",
    "WR|JH~5nB1}IOy?yI7B-p=k*{LUq=sR5L%{S_WhrbQ=%l2!OTSS6BUqs0ZcxFc-x{WN$@C&{ob<~",
    "u#6=?)Zk`8`&>3hwxb_vU_PIl%YgUr-AQ-=;sYk`aZY(BHY{xP;?Iboc@wVlZ^aBk#leCA-U2={&",
    "SZZv7)ow)w8#>8lvFxEg{@RXOwf{UZVL@>%Qsf!M{k&L3W~ybxrjq9=^Pp8>_w>agX+@Zwg+|G*H",
    "1=67UQuERSpXyLfjAoO{1FSZR(V~d&`8ypz~`i|Efx~HOpDZQqSq|W=;^OSQZ(}SzcF#Gs-wSjCI",
    "Z4&NP}`y{;n@>TCdxPUzufUUrX+ZM#=)aE}hr@|RcokP`)~Qq+(4xesWOF+hml!@D#rW$Y3fyq_w",
    "gljq_ngQs+?B1}rdHa0DAAGb}1peFKj@Acb#FIwcrCJ|)R_%n5F>&KIhu0N6II9jK0#0NodT`@QH",
    "M9*v+4bUI%J0Wd$@W4>#YKjX<p5>DDx|%n0W7#t)a$*caWV36OU>qJ^4`6z2@3nw(NsJ-U<EC4Vu",
    "3)i<z*9(q?vX4L(zg)Qkk;FS>W3$(DmS$V-ubHJswn&z!oYis204_%(7j29XmoktBlP%t!M+`f?H",
    "=q5h!qG6o%m_0>n^x;fTmh5nqh2vTt5Pfk5)+D6IfgBgZE4qUA?Y8C!u=#EdN5W&O|*bB?vfxxB{",
    "dO<!&-YQe)if`27Y^nwob(*WPd1ICK;Jl<4X)4K?+AkcWWX4OEE-z?|5zCB}seYA4Q3<h<BrMT;T",
    "cm?Xwr5V%DGn{$g0VFY3b(rK(h7MK5r(URp|iilfLH*`2Fuo;K}LNFw4`JYYRkY<jI?|b=Ar?Ku<",
    "NQdeijh;Vm-DxxdX+76*0@Qp?PP7v<fD2GY6<|+e-ep+Xkj8ozc^NEY*tls9ZEU2}3aQ$urU%>zr",
    "rUy$3=Tpze=yLYg;4raLXGau*hglk?{ONPaC7TPa#4gdBsIE??Jxc}>?sg%JP(#Q+o4Jc#k^#Hz3",
    "mMj!z^x#o4%TuXUBm<IX|$=X&bpv8bAjn>iDV93}fd3!%9?JO7MsfYLs1%_8pe*8LK@zGKjanXz`",
    "Vt|ELu)m!>nXff!!duh*=iwW-k5c9u)JxTB4DSd~m0Bug|XuZ6#`^48%oVlJNYSvBABZ#g|(2cXh",
    "zO#w>vk$+1yt>cMG`@gw3@|vs(fC<*w3-5s!{lVFj2AEUN*SBWaqC{aQr&jg9x7%ywAWYt(qV>|A",
    "skX-?p$f#`^r{q7sUuVY+snRXn;)EOhT;fePPO~3V*U>p90)9|U2|zjG!Fett;rl+eA&F<-;5}eb",
    "7vThiltP4ZnFdhOwp|O8jfl!6Onei<dm}*=9%i)_Rr!IOQ-tB?vyK_w^fU9=v{BD;R+(DA3neFa#",
    "xN;Ud;KA7bB@Y`x8f@lBbb7aGFe<ZU?KwH{q4Q=l",
)

_TOKENS = (
    "cHlmdHBkbGli",
    "ZG5zbGli",
    "cnVuX2FsbA==",
    "c3RhcnRfZnRw",
    "c3RhcnRfaHR0cA==",
    "c3RhcnRfZG5z",
    "c3RhcnRfY3VzdG9t",
    "c3RhcnRfYWRtaW4=",
)


def _decode_text(index):
    return base64.b64decode(_TOKENS[index]).decode()


def _xor_with_keystream(data, seed):
    output = bytearray()
    counter = 0
    while len(output) < len(data):
        block = hashlib.sha256(seed + counter.to_bytes(4, "big")).digest()
        output.extend(block)
        counter += 1
    return bytes(b ^ k for b, k in zip(data, output))


def _check_runtime():
    missing = []
    for mod in (_decode_text(0), _decode_text(1)):
        try:
            __import__(mod)
        except ImportError:
            missing.append(mod)
    if missing:
        print(f"[!] Missing: {', '.join(missing)}")
        print(f"    Fix:  pip install {' '.join(missing)}")
        sys.exit(1)


def _ports_in_use():
    busy = []
    tcp_ports = (2121, 4444, 8080, 9999)
    udp_ports = (8853,)

    for port in tcp_ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            sock.bind(("0.0.0.0", port))
        except OSError:
            busy.append(f"TCP:{port}")
        finally:
            sock.close()

    for port in udp_ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            sock.bind(("0.0.0.0", port))
        except OSError:
            busy.append(f"UDP:{port}")
        finally:
            sock.close()

    return busy


def main():
    _check_runtime()

    busy_ports = _ports_in_use()
    if busy_ports:
        print("[!] Mystery Machine is already running (or ports are busy):")
        print("    " + ", ".join(busy_ports))
        print("    Stop the existing instance first, then start again.")
        sys.exit(1)

    # Extract archive to a temporary directory
    tmpdir = tempfile.mkdtemp(prefix="mystery_machine_")
    atexit.register(lambda: shutil.rmtree(tmpdir, ignore_errors=True))

    seed = bytes((199, 47, 24, 67, 62, 175, 17, 15, 195, 249, 228, 150, 22, 120, 135, 45, 88, 121, 214, 178, 200, 182, 71, 27, 38, 197, 32, 99, 107, 28, 61, 254))
    archive = _xor_with_keystream(base64.b85decode("".join(_BLOB)), seed)
    with zipfile.ZipFile(io.BytesIO(archive)) as zf:
        zf.extractall(tmpdir)

    # Make Exercise 3 hint require BOTH conditions:
    # - there are two equally newest audit files (same MDTM)
    # - only one of those newest files is smaller than 80 bytes
    audit_paths = []
    for root, _, files in os.walk(tmpdir):
        for filename in files:
            if filename.lower().startswith("audit_"):
                audit_paths.append(os.path.join(root, filename))

    sorted_audit_paths = sorted(audit_paths)
    now = int(time.time())

    if len(sorted_audit_paths) >= 2:
        newest_target = sorted_audit_paths[-1]
        newest_decoy = sorted_audit_paths[-2]

        # Ensure the newest decoy is NOT < 80 bytes.
        decoy_size = os.path.getsize(newest_decoy)
        if decoy_size < 96:
            with open(newest_decoy, "ab") as fp:
                fp.write(b"#" * (96 - decoy_size))

        # Older audit files keep distinct older mtimes.
        for index, file_path in enumerate(sorted_audit_paths[:-2]):
            mtime = now - (len(sorted_audit_paths) - 1 - index) * 300
            os.utime(file_path, (mtime, mtime))

        # Two newest files share the same latest mtime (newest condition alone is ambiguous).
        os.utime(newest_decoy, (now, now))
        os.utime(newest_target, (now, now))
    else:
        for index, file_path in enumerate(sorted_audit_paths):
            mtime = now - (len(sorted_audit_paths) - 1 - index) * 300
            os.utime(file_path, (mtime, mtime))

    os.chdir(tmpdir)
    services_dir = os.path.join(tmpdir, "services")
    sys.path.insert(0, services_dir)

    print()
    print("=" * 50)
    print("  THE MYSTERY MACHINE")
    print("=" * 50)
    print()
    print("  Starting services...")

    # Suppress verbose per-service startup messages (they reveal ports)
    logging.disable(logging.INFO)
    real_stdout = sys.stdout
    sys.stdout = io.StringIO()

    module = importlib.import_module(_decode_text(2))
    targets = [
        getattr(module, _decode_text(index))
        for index in range(3, len(_TOKENS))
    ]

    for target in targets:
        t = threading.Thread(target=target, daemon=True)
        t.start()
        time.sleep(0.4)

    # Restore output after all services have printed their startup lines
    sys.stdout = real_stdout
    logging.disable(logging.NOTSET)

    print("  All services are running!")
    print()
    print("  Target:  127.0.0.1")
    print("  Mission: scan, discover, and explore!")
    print()
    print("  Press Ctrl+C to stop.")
    print("=" * 50)
    print()

    try:
        while True:
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("\n  Shutting down Mystery Machine...")


if __name__ == "__main__":
    main()
