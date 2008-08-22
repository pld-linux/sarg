Summary:	Squid log analyzer
Summary(es.UTF-8):	generador de informes del squid por utilizador/ip/nombre
Summary(pl.UTF-8):	Analizator logów Squida
Summary(pt_BR.UTF-8):	Gerador de relatórios por usuário/ip/nome do squid
Name:		sarg
Version:	2.2.5
Release:	1
License:	GPL v2
Group:		Networking
Source0:	http://dl.sourceforge.net/sarg/%{name}-%{version}.tar.gz
# Source0-md5:	0f4481e375dedf9ab8c682c9407162ff
Source1:	%{name}.crontab
Source2:	%{name}-user_limit_block
Patch0:		%{name}-font.patch
Patch1:		%{name}-config.patch
Patch2:		%{name}-paths.patch
Patch3:		%{name}-quiet.patch
Patch4:		%{name}-fix_pathes.patch
URL:		http://sarg.sourceforge.net/sarg.php
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gd-devel
Requires:	squid
Requires:	xorg-font-font-bh-ttf
Obsoletes:	sqmgrlog
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sarg - Squid Analysis Report Generator is a tool that allow you to
view "where" your users are going to on the Internet. Sarg generate
reports in html, with many fields, like: users, IP Addresses, bytes,
sites and times.

%description -l es.UTF-8
Sarg (era Sqmgrlog) genera informes por utilizador/ip/nombre hacia el
fichero de log del SQUID. Los informes serán generados en HTML o
correo.

%description -l pl.UTF-8
Sarg jest narzędziem dzięki któremu możesz sprawdzać jakie adresy w
Internecie odwiedzają twoi użytkownicy. Sarg generuje raporty w
HTML-u.

%description -l pt_BR.UTF-8
O Sarg (antigo Sqmgrlog) gera relatórios por usuário/ip/nome
baseando-se no arquivo de log do SQUID. Os relatórios são gerados em
HTML ou por email.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%{__aclocal}
%{__autoconf}
cp -f /usr/share/automake/config.* cfgaux
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
install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}

mv $RPM_BUILD_ROOT{%{_sysconfdir}/%{name}/images,%{_datadir}/%{name}}
mv $RPM_BUILD_ROOT{%{_sysconfdir}/%{name}/languages,%{_datadir}/%{name}}
rm -r $RPM_BUILD_ROOT{%{_sysconfdir}/sarg/sarg-php,%{_sysconfdir}/sarg/fonts}
rm $RPM_BUILD_ROOT%{_sysconfdir}/sarg/css.tpl

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
%attr(755,root,root) %{_sysconfdir}/%{name}/user_limit_block
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/sarg.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/exclude_codes
%config(noreplace) %verify(not md5 mtime size) /etc/cron.d/%{name}
%{_datadir}/%{name}
%{_mandir}/man?/*
