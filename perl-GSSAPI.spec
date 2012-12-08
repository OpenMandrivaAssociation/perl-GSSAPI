%define upstream_name	 GSSAPI
%define upstream_version 0.28

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    8

Summary:	Perl extension providing access to the GSSAPIv2 library
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/G/GA/GAAS/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	krb5-devel
BuildRequires:	perl-devel

%description
This module gives access to the routines of the GSSAPI library, as described
in rfc2743 and rfc2744 and implemented by the Kerberos-1.2 distribution from
MIT.

Since 0.14 it also compiles and works with Heimdal. Lacks of Heimdal support
are gss_release_oid(), gss_str_to_oid() and fail of some tests. Have a look
at the tests in t/ directory too see what tests fail on Heimdal ( the *.t tests
are just skipping them at the moment)

The API presented by this module is a mildly object oriented reinterpretation
of the C API, where opaque C structures are Perl objects, but the style of
function call has been left mostly untouched. As a result, most routines modify
one or more of the parameters passed to them, reflecting the C call-by-
reference (or call-by-value-return) semantics.

All users of this module are therefore strongly advised to localize all usage
of these routines to minimize pain if and when the API changes.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="%{optflags}"

%check
# Looks like latest krb5 is not fully supported :-/
#make test

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man?/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.280.0-7mdv2012.0
+ Revision: 765291
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.280.0-6
+ Revision: 763830
- rebuilt for perl-5.14.x

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.280.0-5
+ Revision: 763371
- rebuild

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.280.0-4
+ Revision: 667174
- mass rebuild

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 0.280.0-3mdv2011.0
+ Revision: 564440
- rebuild for perl 5.12.1

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.280.0-2mdv2011.0
+ Revision: 555879
- rebuild for perl 5.12

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.280.0-1mdv2011.0
+ Revision: 552306
- update to 0.28

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.26-2mdv2010.1
+ Revision: 426446
- rebuild

* Sun Jul 06 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.26-1mdv2009.0
+ Revision: 232124
- new version

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.24-3mdv2009.0
+ Revision: 223778
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 0.24-2mdv2008.1
+ Revision: 180650
- fix deps

  + Thierry Vignaud <tv@mandriva.org>
    - fix description-line-too-long
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sat May 05 2007 Olivier Thauvin <nanardon@mandriva.org> 0.24-1mdv2008.0
+ Revision: 23368
- 0.24
- Create perl-GSSAPI

