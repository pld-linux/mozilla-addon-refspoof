Summary:	A simple toolbar that allow to load a page with a different Referer.
Name:		mozilla-addon-refspoof
%define		_realname	refspoof
Version:	0.4.0
%define fver    %(echo %{version} | tr "." "_")
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://refspoof.mozdev.org/%{_realname}_%{fver}.xpi
Source1:	%{_realname}-installed-chrome.txt
URL:		http://refspoof.mozdev.org/
BuildRequires:	zip
BuildRequires:	unzip
BuildArch:	noarch
Requires:	mozilla >= 1.0-7
BuildRoot:	%{tmpdir}/%{_realname}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/X11R6
%define         _chromedir      %{_libdir}/mozilla/chrome

%description
A simple toolbar that allow to load a page with a different Referer.

%prep
%setup -q -c %{name}-%{version}

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
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt

%postun
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname}-installed-chrome.txt
