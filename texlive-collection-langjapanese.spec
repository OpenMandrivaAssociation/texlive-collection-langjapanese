# revision 33790
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-langjapanese
Version:	20180514
Release:	1
Summary:	Japanese
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-langjapanese.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-collection-langcjk
Requires:	texlive-bxbase
Requires:	texlive-bxcjkjatype
Requires:	texlive-bxjscls
Requires:	texlive-convbkmk
Requires:	texlive-ipaex
Requires:	texlive-japanese
Requires:	texlive-japanese-otf
Requires:	texlive-japanese-otf-uptex
Requires:	texlive-jfontmaps
Requires:	texlive-jsclasses
Requires:	texlive-lshort-japanese
Requires:	texlive-luatexja
Requires:	texlive-ptex
Requires:	texlive-ptex2pdf
Requires:	texlive-pxbase
Requires:	texlive-pxchfon
Requires:	texlive-pxcjkcat
Requires:	texlive-pxjahyper
Requires:	texlive-pxrubrica
Requires:	texlive-uptex
Requires:	texlive-wadalab
Requires:	texlive-zxjafbfont
Requires:	texlive-zxjatype

%description
Support for Japanese; additional packages in collection-
langcjk.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
