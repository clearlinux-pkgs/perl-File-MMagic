#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-File-MMagic
Version  : 1.30
Release  : 18
URL      : http://search.cpan.org/CPAN/authors/id/K/KN/KNOK/File-MMagic-1.30.tar.gz
Source0  : http://search.cpan.org/CPAN/authors/id/K/KN/KNOK/File-MMagic-1.30.tar.gz
Summary  : Guess file type from contents
Group    : Development/Tools
License  : BSD-3-Clause-Attribution
Requires: perl-File-MMagic-license = %{version}-%{release}
Requires: perl-File-MMagic-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : file-dev

%description
File::MMagic
NOKUBI Takatsugu <knok@daionet.gr.jp>
Yukio USUDA  <usu@namazu.org>

%package dev
Summary: dev components for the perl-File-MMagic package.
Group: Development
Provides: perl-File-MMagic-devel = %{version}-%{release}
Requires: perl-File-MMagic = %{version}-%{release}

%description dev
dev components for the perl-File-MMagic package.


%package license
Summary: license components for the perl-File-MMagic package.
Group: Default

%description license
license components for the perl-File-MMagic package.


%package perl
Summary: perl components for the perl-File-MMagic package.
Group: Default
Requires: perl-File-MMagic = %{version}-%{release}

%description perl
perl components for the perl-File-MMagic package.


%prep
%setup -q -n File-MMagic-1.30
cd %{_builddir}/File-MMagic-1.30

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test || :

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-File-MMagic
cp %{_builddir}/File-MMagic-1.30/COPYING %{buildroot}/usr/share/package-licenses/perl-File-MMagic/2a0a9966f12639766c3eba19fbab0ae4cc88d684
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/File::MMagic.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-File-MMagic/2a0a9966f12639766c3eba19fbab0ae4cc88d684

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/File/MMagic.pm
