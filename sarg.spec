#
Summary:	Squid log analyzer
Summary(es):	generador de informes del squid por utilizador/ip/nombre
Summary(pl):	Analizator logów Squida
Summary(pt_BR):	Gerador de relatórios por usuário/ip/nome do squid
Name:		sarg
Version:	2.0.1
Release:	0.2
License:	GPL v2
Group:		Networking
Source0:	http://dl.sourceforge.net/sarg/%{name}-%{version}.tar.gz
# Source0-md5:	a2f025eb47c2569dc1e39f383c989c78
Source1:	%{name}.crontab
Patch0:		%{name}-font.patch
Patch1:		%{name}-config.patch
Patch2:		%{name}-paths.patch
Patch3:		%{name}-quiet.patch
URL:		http://sarg.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
Requires:	XFree86-fonts
Requires:	squid
Obsoletes:	sqmgrlog
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sarg - Squid Analysis Report Generator is a tool that allow you to
view "where" your users are going to on the Internet. Sarg generate
reports in html, with many fields, like: users, IP Addresses, bytes,
sites and times.

%description -l es
Sarg (era Sqmgrlog) genera informes por utilizador/ip/nombre hacia el
fichero de log del SQUID. Los informes serán generados en HTML o
correo.

%description -l pl
Sarg jest narzêdziem dziêki któremu mo¿esz sprawdzaæ jakie adresy w
Internecie odwiedzaj± twoi u¿ytkownicy. Sarg generuje raporty w
HTML-u.

%description -l pt_BR
O Sarg (antigo Sqmgrlog) gera relatórios por usuário/ip/nome
baseando-se no arquivo de log do SQUID. Os relatórios são gerados em
HTML ou por email.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__aclocal}
%{__autoconf}
cp -f %{_datadir}/automake/config.* cfgaux
%configure \
	 --enable-sysconfdir=%{_sysconfdir}/%{name}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir}/%{name},/etc/cron.d}
install -d $RPM_BUILD_ROOT{/var/lib/%{name}/{images,tmp},%{_datadir}/%{name},%{_mandir}/man1}

%{__make} install \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	SYSCONFDIR=$RPM_BUILD_ROOT%{_sysconfdir}/%{name} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1/

install sarg.conf $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/sarg.conf
install %{SOURCE1} $RPM_BUILD_ROOT/etc/cron.d/%{name}
mv $RPM_BUILD_ROOT{%{_sysconfdir}/%{name}/images,%{_datadir}/%{name}}
mv $RPM_BUILD_ROOT{%{_sysconfdir}/%{name}/languages,%{_datadir}/%{name}}
rm -r $RPM_BUILD_ROOT{/etc/sarg/sarg-php,/etc/sarg/fonts}
rm $RPM_BUILD_ROOT/etc/sarg/css.tpl

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sarg
%doc ChangeLog README CONTRIBUTORS DONATIONS BETA-TESTERS sarg-php
%attr(771,root,stats) %dir /var/lib/%{name}
%attr(771,root,stats) %dir /var/lib/%{name}/images
%attr(770,root,stats) %dir /var/lib/%{name}/tmp
%dir %{_sysconfdir}/%{name}
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/%{name}/sarg.conf
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/%{name}/exclude_codes
%config(noreplace) %verify(not size mtime md5) /etc/cron.d/%{name}
%{_datadir}/%{name}
%{_mandir}/man?/*
