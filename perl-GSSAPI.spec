%define upstream_name	 GSSAPI
%define upstream_version 0.28

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Perl extension providing access to the GSSAPIv2 library
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/G/GA/GAAS/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	krb5-devel
BuildRequires:	perl-devel

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

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
%make OPTIMIZE="$RPM_OPT_FLAGS"

%check
%make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man?/*
