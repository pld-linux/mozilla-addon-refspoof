Summary:	A simple toolbar that allow to load a page with a different Referer
Summary(pl.UTF-8):   Pasek pozwalający wczytywać stronę z innym nagłówkiem Referer
Name:		mozilla-addon-refspoof
%define		_realname	refspoof
Version:	0.5.0
%define	fver	%(echo %{version} | tr . _)
Release:	3
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://download.mozdev.org/refspoof/%{_realname}_%{fver}.xpi
# Source0-md5:	e503189fc771b2a15fea97378796cbb9
Source1:	%{_realname}-installed-chrome.txt
URL:		http://refspoof.mozdev.org/
BuildRequires:	unzip
BuildRequires:	zip
Requires(post,postun):	mozilla >= 5:1.7.3-3
Requires(post,postun):	textutils
Requires:	mozilla >= 2:1.0-7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_chromedir	%{_datadir}/mozilla/chrome

%description
A simple toolbar that allow to load a page with a different Referer.

%description -l pl.UTF-8
Prosty pasek narzędziowy pozwalający wczytywać stronę z innym
nagłówkiem Referer.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

cd %{_realname}
rm -rf CVS
rm -rf content/CVS
zip -r -9 -m ../%{_realname}.jar ./
cd -
install %{_realname}.jar $RPM_BUILD_ROOT%{_chromedir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_chromedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/mozilla-chrome+xpcom-generate

%postun
%{_sbindir}/mozilla-chrome+xpcom-generate

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname}-installed-chrome.txt
