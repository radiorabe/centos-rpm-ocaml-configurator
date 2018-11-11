%define debug_package %{nil}

Name:           ocaml-configurator
Version:        0.11.0
Release:        0.1%{?dist}
Summary:        Helper library for gathering system configuration

%global libname %(echo %{name} | sed -e 's/^ocaml-//')

# NOTE: The license changes to MIT at some point after the 0.11.0 tag
License:        Apache-2.0
URL:            https://github.com/janestreet/configurator/
Source0:        https://github.com/janestreet/configurator/archive/v%{version}/%{name}-%{version}.tar.gz

BUildRequires:  jbuilder
BuildRequires:  ocaml
BuildRequires:  ocaml-base-devel
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
%autosetup -n %{libname}-%{version}

# Generate debuginfo, or try to.
sed 's/ocamlc/ocamlc -g/g' -i Makefile
sed 's/ocamlopt/ocamlopt -g/g' -i Makefile

%build
%make_build

%install
# Currently configurator installs itself with ocamlfind.
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
make install PREFIX=$OCAMLFIND_DESTDIR

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
* Sun Nov 11 2018 Lucas Bickel <hairmare@rabe.ch> - 0.11.0-0.1
- Fix Fedora build by disabling debug package

* Sun Nov 11 2018 Lucas Bickel <hairmare@rabe.ch> - 0.11.0-0.0
- Initial build for pcre-ocaml package bump
