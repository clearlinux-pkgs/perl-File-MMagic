#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-File-MMagic
Version  : 1.30
Release  : 3
URL      : http://search.cpan.org/CPAN/authors/id/K/KN/KNOK/File-MMagic-1.30.tar.gz
Source0  : http://search.cpan.org/CPAN/authors/id/K/KN/KNOK/File-MMagic-1.30.tar.gz
Summary  : Guess file type from contents
Group    : Development/Tools
License  : BSD-3-Clause-Attribution
Requires: perl-File-MMagic-man
BuildRequires : file-dev

%description
File::MMagic
NOKUBI Takatsugu <knok@daionet.gr.jp>
Yukio USUDA  <usu@namazu.org>

%package man
Summary: man components for the perl-File-MMagic package.
Group: Default

%description man
man components for the perl-File-MMagic package.


%prep
%setup -q -n File-MMagic-1.30

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test || :

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/File/MMagic.pm

%files man
%defattr(-,root,root,-)
/usr/share/man/man3/File::MMagic.3
