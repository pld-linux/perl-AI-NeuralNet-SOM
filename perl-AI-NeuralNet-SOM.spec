#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	AI
%define		pnam	NeuralNet-SOM
Summary:	AI::NeuralNet::SOM - A simple Kohonen Self-Organizing Maps
Summary(pl):	AI::NeuralNet::SOM - proste SOM Kohonena
Name:		perl-AI-NeuralNet-SOM
Version:	0.02
Release:	5
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AI::NeuralNet::SOM - A simple Kohonen Self-Organizing Maps.

%description -l pl
AI::NeuralNet::SOM - proste SOM (Samo-Organizuj±ce siê Odwzorowania)
Kohonena.

%prep
%setup -q -n %{name}-%{version} -c

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/AI/NeuralNet/*.pm
%dir %{perl_vendorlib}/auto/AI/NeuralNet
%dir %{perl_vendorlib}/auto/AI/NeuralNet/SOM
%{perl_vendorlib}/auto/AI/NeuralNet/SOM/autosplit.ix
%{_mandir}/man3/*
