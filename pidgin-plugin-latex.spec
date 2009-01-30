%define pidgin_ver %(pkg-config --modversion pidgin 2>/dev/null || echo ERROR)
Summary:	A plugin for Pidgin which translates LaTeX code into images in your IM and Chat conversations
Summary(hu.UTF-8):	Egy Pidgin plugin, amely LaTeX-kódot képekre alakít az IM és Chat beszélgetéseidben
Name:		pidgin-plugin-latex
Version:	1.3
Release:	0.1
License:	GPL
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/pidgin-latex/pidgin-latex-%{version}.tar.bz2
# Source0-md5:	33aa374092e9a83f82b49602fb9296a6
URL:		http://sourceforge.net/projects/pidgin-latex/
BuildRequires:	pidgin-devel >= 2.2
BuildRequires:	pkgconfig
Requires:	/usr/bin/latex
Requires:	ImageMagick
Requires:	pidgin >= %{pidgin_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A plugin for Pidgin which translates LaTeX code into images in your IM
and Chat conversations.

%description -l hu.UTF-8
Egy Pidgin plugin, amely LaTeX-kódot képekre alakít az IM és Chat
beszélgetéseidben.

%prep
%setup -q -n pidgin-latex

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}

%{__make} install \
PREFIX=$RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
%attr(755,root,root) %{_libdir}/pidgin/*.so