#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	Config
%define		pnam	AutoConf
%include	/usr/lib/rpm/macros.perl
Summary:	Config::AutoConf - A module to implement some of AutoConf macros in pure Perl
Summary(pl.UTF-8):	Config::AutoConf - moduł implementujący część makr AutoConfa w czystym Perlu
Name:		perl-Config-AutoConf
Version:	0.317
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Config/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	29f87fc7803f1725f6daafcf416089ce
URL:		https://metacpan.org/release/Config-AutoConf/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Capture-Tiny
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Config::AutoConf is intended to provide the same opportunities to Perl
developers as GNU Autoconf does for Shell developers.

As Perl is the second most deployed language (mind: every Unix comes
with Perl, several mini-computers have Perl and even lot's of Windows
machines run Perl software - which requires deployed Perl there, too),
this gives wider support than Shell based probes.

The API is leaned against GNU Autoconf, but we try to make the API
(especially optional arguments) more Perl'ish than m4 abilities allow
to the original.

%description -l pl.UTF-8
Config::AutoConf ma na celu udostępnienie programistom Perla tych
samych możliwości, jakie GNU Autoconf udostępnia programistom powłoki.

Jako że Perl jest drugim najczęściej wdrażanym językiem (a konkretnie:
każdy Unix jest dostarczany z Perlem, niektóre minikomputery mają
Perla, nawet wiele komputerów z Windows uruchamia oprogramowanie w
Perlu - co oznacza, że też zawiera Perla), co daje szerszą obsługę,
niż ma uniksowa powłoka.

API jest oparte na GNU Autoconfie, ale z próbą uczynienia go
(zwłaszcza argumentów opcjonalnych) bardziej perlowym, niż pozwalają
na to możliwości m4.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes LICENSE
%{perl_vendorlib}/Config/AutoConf.pm
%{_mandir}/man3/Config::AutoConf.3pm*
