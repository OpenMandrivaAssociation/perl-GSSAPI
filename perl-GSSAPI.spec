%define modname GSSAPI

Summary:	Perl extension providing access to the GSSAPIv2 library
Name:		perl-%{modname}
Version:	0.28
Release:	5
License:	GPLv2
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{modname}
Source0:	http://search.cpan.org/CPAN/authors/id/G/GA/GAAS/%{modname}-%{version}.tar.gz
BuildRequires:	pkgconfig(krb5)
BuildRequires:	perl-devel
BuildRequires:	pkgconfig(com_err)
# (tpg) fix upgrade
Provides:	perl-GSSAPI = 0.280.0-26
Obsoletes:	perl-GSSAPI < 0.280.0-26

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
%autosetup -p1 -n %{modname}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make_build OPTIMIZE="%{optflags}"

#check
# Looks like latest krb5 is not fully supported :-/
#make test

%install
%make_install

%files
%doc Changes README
# Looks weird with new perl?
%{_libdir}/perl5/vendor_perl/*
#{perl_vendorlib}/*
%doc %{_mandir}/man3/*
