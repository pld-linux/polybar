Summary:	Fast and easy-to-use status bar
Name:		polybar
Version:	3.7.2
Release:	1
License:	MIT, BSD
Group:		X11/Window Managers
Source0:	https://github.com/polybar/polybar/releases/download/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	1c9273c7eef5b542448d6054d9aa3ac5
Patch0:		includes.patch
URL:		https://polybar.github.io/
BuildRequires:	alsa-lib-devel
BuildRequires:	cairo-devel
BuildRequires:	cmake >= 3.5.0
BuildRequires:	curl-devel
BuildRequires:	i3
BuildRequires:	i3-devel
BuildRequires:	jsoncpp-devel >= 1.7.7
BuildRequires:	libmpdclient-devel
BuildRequires:	libnl-devel
BuildRequires:	libstdc++-devel >= 6:9
BuildRequires:	libuv-devel >= 1.3.0
BuildRequires:	libxcb-devel >= 1.12
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio
BuildRequires:	pulseaudio-devel
BuildRequires:	python3 >= 1:3.5
BuildRequires:	python3-Sphinx
BuildRequires:	python3-xcbgen
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.719
BuildRequires:	sphinx-pdg
BuildRequires:	xcb-proto
BuildRequires:	xcb-util-cursor-devel
BuildRequires:	xcb-util-devel
BuildRequires:	xcb-util-image-devel
BuildRequires:	xcb-util-wm-devel
BuildRequires:	xcb-util-xrm-devel
Requires:	jsoncpp >= 1.7.7
Requires:	libuv >= 1.3.0
Requires:	libxcb >= 1.12
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Polybar aims to help users build beautiful and highly customizable
status bars for their desktop environment, without the need of having
a black belt in shell scripting.

%package -n bash-completion-polybar
Summary:	bash-completion for polybar
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	bash-completion >= 1:2.0
BuildArch:	noarch

%description -n bash-completion-polybar
bash-completion for polybar.

%package -n zsh-completion-polybar
Summary:	zsh-completion for polybar
Summary(pl.UTF-8):	Uzupełnianie nazw w zsh dla polybar
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	zsh
BuildArch:	noarch

%description -n zsh-completion-polybar
zsh-completion for polybar.

%prep
%setup -q
%patch -P0 -p1

%build
install -d build
cd build
%cmake ..

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md SUPPORT.md
%dir %{_sysconfdir}/polybar
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/polybar/config.ini
%attr(755,root,root) %{_bindir}/polybar
%attr(755,root,root) %{_bindir}/polybar-msg
%{_mandir}/man1/polybar.1*
%{_mandir}/man1/polybar-msg.1*
%{_mandir}/man5/polybar.5*

%files -n bash-completion-polybar
%defattr(644,root,root,755)
%{bash_compdir}/polybar

%files -n zsh-completion-polybar
%defattr(644,root,root,755)
%{zsh_compdir}/_polybar
%{zsh_compdir}/_polybar_msg
