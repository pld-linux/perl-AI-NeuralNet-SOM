#
# Conditional build:
%bcond_without	tests	# don't perform "make test"

%define		pdir	AI
%define		pnam	NeuralNet-SOM
Summary:	AI::NeuralNet::SOM - simple Kohonen Self-Organizing Maps
Summary(pl.UTF-8):	AI::NeuralNet::SOM - proste SOM Kohonena
Name:		perl-AI-NeuralNet-SOM
Version:	0.07
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1bb481059871065d9376109059ce45c2
URL:		http://search.cpan.org/dist/AI-NeuralNet-SOM/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AI::NeuralNet::SOM - simple Kohonen Self-Organizing Maps.

%description -l pl.UTF-8
AI::NeuralNet::SOM - proste SOM (samoorganizujące się odwzorowania)
Kohonena.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{perl_vendorlib}/AI/NeuralNet/
%dir %{perl_vendorlib}/AI/NeuralNet/SOM
%{perl_vendorlib}/AI/NeuralNet/SOM.pm
%{perl_vendorlib}/AI/NeuralNet/SOM/*.pm
%{_mandir}/man3/*
