%define modname	GSSAPI
%define modver	0.28

Summary:	Perl extension providing access to the GSSAPIv2 library
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	21
License:	GPLv2
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://search.cpan.org/CPAN/authors/id/G/GA/GAAS/%{modname}-%{modver}.tar.gz
BuildRequires:	krb5-devel
BuildRequires:	perl-devel
BuildRequires:	pkgconfig(com_err)

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
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="%{optflags}"

%check
# Looks like latest krb5 is not fully supported :-/
#make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

