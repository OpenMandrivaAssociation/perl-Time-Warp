%define upstream_name    Time-Warp
%define upstream_version 0.55

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:	1

Summary:    Change the start and speed of Event time
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        https://github.com/manwar/Time-Warp
Source0:    https://cpan.metacpan.org/authors/id/M/MA/MANWAR/Time-Warp-%{upstream_version}.tar.gz


BuildRequires:	make
BuildRequires: perl-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Our external experience unfolds in 3 1/2 dimensions (time has a
dimensionality of 1/2). The Time::Warp module offers developers control
over the measurement of time.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README
%{_mandir}/man3/*
%perl_vendorlib/*




%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.500.0-4
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.500.0-3mdv2011.0
+ Revision: 556185
- rebuild for perl 5.12
- rebuild

* Sun Nov 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.500.0-1mdv2010.1
+ Revision: 471288
- import perl-Time-Warp


* Sun Nov 29 2009 cpan2dist 0.5-1mdv
- initial mdv release, generated with cpan2dist
