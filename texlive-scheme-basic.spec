Name:		texlive-scheme-basic
Version:	54191
Release:	2
Summary:	basic scheme (plain and latex)
Group:		Publishing
URL:		https://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/scheme-basic.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-collection-basic
Requires:	texlive-collection-latex

%description
This is the basic TeX Live scheme: it is a small set of files
sufficient to typeset plain TeX or LaTeX documents in
PostScript or PDF, using the Computer Modern fonts.  This
scheme corresponds to collection-basic and collection-latex.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c

%build

%install
