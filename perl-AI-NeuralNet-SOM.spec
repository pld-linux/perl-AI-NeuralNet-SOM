#
# Conditional build:
%bcond_without	tests	# don't perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	AI
%define		pnam	NeuralNet-SOM
Summary:	AI::NeuralNet::SOM - simple Kohonen Self-Organizing Maps
Summary(pl.UTF-8):   AI::NeuralNet::SOM - proste SOM Kohonena
Name:		perl-AI-NeuralNet-SOM
Version:	0.02
Release:	6
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	dc75102fb80be96677461d3838847805
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
%setup -q -c

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
%{perl_vendorlib}/AI/NeuralNet/*.pm
%dir %{perl_vendorlib}/auto/AI/NeuralNet
%dir %{perl_vendorlib}/auto/AI/NeuralNet/SOM
%{perl_vendorlib}/auto/AI/NeuralNet/SOM/autosplit.ix
%{_mandir}/man3/*
