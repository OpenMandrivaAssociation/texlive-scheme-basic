%global tl_name scheme-basic
%global tl_revision 54191

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	basic scheme (plain and latex)
Group:		Publishing
URL:		https://www.ctan.org/pkg/scheme-basic
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/scheme-basic.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(collection-basic)
Requires:	texlive(collection-latex)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is the basic TeX Live scheme: it is a small set of files sufficient
to typeset plain TeX or LaTeX documents in PostScript or PDF, using the
Computer Modern fonts. This scheme corresponds to collection-basic and
collection-latex.

