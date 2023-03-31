Name:		texlive-texosquery
Version:	53676
Release:	2
Summary:	Cross-platform Java application to query OS information
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/texosquery
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texosquery.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texosquery.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texosquery.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a cross-platform Java application to
query OS information designed for use in TeX's shell escape
mechanism. The application can query the following: locale and
codeset current working directory user home directory temporary
directory OS name, arch and version Current date and time in
PDF format (for TeX formats that don't provide
\pdfcreationdate) Date-time stamp of a file in PDF format (for
TeX formats that don't provide \pdffilemoddate) Size of a file
in bytes (for TeX formats that don't provide \pdffilesize)
Contents of a directory (captured as a list) Directory contents
filtered by regular expression (captured as a list) URI of a
file Canonical path of a file All paths use a forward slash as
directory divider so results can be used, for example, in
commands like \includegraphics. There are files provided for
easy access in TeX documents: texosquery.tex: generic TeX code
texosquery.sty: LaTeX package This provides commands to run
texosquery using TeX's shell escape mechanism and capture the
result in a control sequence. The category code of most of
TeX's default special characters (and some other potentially
problematic characters) is temporarily changed to 12 while
reading the result.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_datadir}
cp -a texmf-dist %{buildroot}%{_datadir}

%files
%doc %{_texmfdistdir}/texmf-dist/source/support/texosquery
%{_texmfdistdir}/texmf-dist/tex/latex/texosquery
%{_texmfdistdir}/texmf-dist/scripts/texosquery
%doc %{_texmfdistdir}/texmf-dist/doc/support/texosquery

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
