%global tl_name collection-langjapanese
%global tl_revision 76651

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Japanese
Group:		Publishing
URL:		https://www.ctan.org/pkg/collection-langjapanese
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-langjapanese.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(ascmac)
Requires:	texlive(asternote)
Requires:	texlive(babel-japanese)
Requires:	texlive(bxbase)
Requires:	texlive(bxcjkjatype)
Requires:	texlive(bxcoloremoji)
Requires:	texlive(bxghost)
Requires:	texlive(bxjaholiday)
Requires:	texlive(bxjalipsum)
Requires:	texlive(bxjaprnind)
Requires:	texlive(bxjatoucs)
Requires:	texlive(bxjscls)
Requires:	texlive(bxorigcapt)
Requires:	texlive(bxwareki)
Requires:	texlive(chuushaku)
Requires:	texlive(collection-langcjk)
Requires:	texlive(convbkmk)
Requires:	texlive(convert-jpfonts)
Requires:	texlive(endnotesj)
Requires:	texlive(gckanbun)
Requires:	texlive(gentombow)
Requires:	texlive(haranoaji)
Requires:	texlive(haranoaji-extra)
Requires:	texlive(ieejtran)
Requires:	texlive(ifptex)
Requires:	texlive(ifxptex)
Requires:	texlive(ipaex)
Requires:	texlive(japanese-mathformulas)
Requires:	texlive(japanese-otf)
Requires:	texlive(jieeetran)
Requires:	texlive(jlreq)
Requires:	texlive(jlreq-deluxe)
Requires:	texlive(jpneduenumerate)
Requires:	texlive(jpnedumathsymbols)
Requires:	texlive(jsclasses)
Requires:	texlive(kanbun)
Requires:	texlive(lshort-japanese)
Requires:	texlive(luatexja)
Requires:	texlive(luwa-ul)
Requires:	texlive(mendex-doc)
Requires:	texlive(morisawa)
Requires:	texlive(outoruby)
Requires:	texlive(pbibtex-base)
Requires:	texlive(pbibtex-manual)
Requires:	texlive(platex)
Requires:	texlive(platex-tools)
Requires:	texlive(platexcheat)
Requires:	texlive(plautopatch)
Requires:	texlive(ptex)
Requires:	texlive(ptex-base)
Requires:	texlive(ptex-fontmaps)
Requires:	texlive(ptex-fonts)
Requires:	texlive(ptex-manual)
Requires:	texlive(ptex2pdf)
Requires:	texlive(pxbase)
Requires:	texlive(pxchfon)
Requires:	texlive(pxcjkcat)
Requires:	texlive(pxjahyper)
Requires:	texlive(pxjodel)
Requires:	texlive(pxrubrica)
Requires:	texlive(pxufont)
Requires:	texlive(texlive-ja)
Requires:	texlive(uplatex)
Requires:	texlive(uptex)
Requires:	texlive(uptex-base)
Requires:	texlive(uptex-fonts)
Requires:	texlive(wadalab)
Requires:	texlive(zxjafbfont)
Requires:	texlive(zxjatype)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Support for Japanese; additional packages are in collection-langcjk.

