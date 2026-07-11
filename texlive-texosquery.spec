%global tl_name texosquery
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.7
Release:	%{tl_revision}.1
Summary:	Cross-platform Java application to query OS information
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/texosquery
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/texosquery.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/texosquery.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/texosquery.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(texosquery.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a cross-platform Java application to query OS
information designed for use in TeX's shell escape mechanism. The
application can query the following: locale and codeset current working
directory user home directory temporary directory OS name, arch and
version Current date and time in PDF format (for TeX formats that don't
provide \pdfcreationdate) Date-time stamp of a file in PDF format (for
TeX formats that don't provide \pdffilemoddate) Size of a file in bytes
(for TeX formats that don't provide \pdffilesize) Contents of a
directory (captured as a list) Directory contents filtered by regular
expression (captured as a list) URI of a file Canonical path of a file
All paths use a forward slash as directory divider so results can be
used, for example, in commands like \includegraphics. There are files
provided for easy access in TeX documents: texosquery.tex: generic TeX
code texosquery.sty: LaTeX package This provides commands to run
texosquery using TeX's shell escape mechanism and capture the result in
a control sequence. The category code of most of TeX's default special
characters (and some other potentially problematic characters) is
temporarily changed to 12 while reading the result.

