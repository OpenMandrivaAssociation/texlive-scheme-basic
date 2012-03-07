# revision 17228
# category Scheme
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-scheme-basic
Version:	20120307
Release:	1
Summary:	basic scheme (plain and LaTeX)
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/scheme-basic.tar.xz
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
%setup -c -a0

%build

%install
