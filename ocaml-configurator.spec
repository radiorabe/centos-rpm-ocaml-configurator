%define debug_package %{nil}

Name:           ocaml-configurator
Version:        0.11.0
Release:        0.3%{?dist}
Summary:        Helper library for gathering system configuration

%global libname %(echo %{name} | sed -e 's/^ocaml-//')

# NOTE: The license changes to MIT at some point after the 0.11.0 tag
License:        Apache-2.0
URL:            https://github.com/janestreet/configurator/
Source0:        https://github.com/janestreet/configurator/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         ocaml-configurator-0.11.0-pervasives-from-stdlib.patch

BuildRequires:  ocaml
BuildRequires:  ocaml-base-devel
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-stdio-devel

%description
Configurator is a small library that helps writing OCaml scripts
that test features available on the system, in order to generate
config.h files for instance.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
%setup -q -n %{libname}-%{version}
%patch -P 0 -p 1

%build
%make_build

%install
# Currently configurator installs itself with ocamlfind.
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
# use dune install instead of make install to allow using --libdir
dune install --prefix=$OCAMLFIND_DESTDIR --libdir=$OCAMLFIND_PREFIX

%files
%doc README.org
%doc %{_libdir}/ocaml/doc/%{libname}
%license LICENSE.txt
%{_libdir}/ocaml/%{libname}
%ifarch %{ocaml_native_compiler}
%exclude %{_libdir}/ocaml/%{libname}/*.a
%exclude %{_libdir}/ocaml/%{libname}/*.cmxa
%exclude %{_libdir}/ocaml/%{libname}/*.cmx
%exclude %{_libdir}/ocaml/%{libname}/*.ml
%exclude %{_libdir}/ocaml/%{libname}/*.mli
%endif

%files devel
%license LICENSE.txt
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{libname}/*.a
%{_libdir}/ocaml/%{libname}/*.cmxa
%{_libdir}/ocaml/%{libname}/*.cmx
%{_libdir}/ocaml/%{libname}/*.mli
%endif

%changelog
* Sat May  2 2020 Lucas Bickel <hairmare@rabe.ch> - 0.11.0-0.3
- Fix lib paths
- use dune bin instead of jbuilder bin
- Replace Pervasives with Stdlib to support newer ocaml versions

* Sat Aug  3 2019 Lucas Bickel <hairmare@rabe.ch> - 0.11.0-0.2
- Fix building with dune instead of jbuilder

* Sun Nov 11 2018 Lucas Bickel <hairmare@rabe.ch> - 0.11.0-0.1
- Fix Fedora build by disabling debug package

* Sun Nov 11 2018 Lucas Bickel <hairmare@rabe.ch> - 0.11.0-0.0
- Initial build for pcre-ocaml package bump
