Summary:	Fast and easy-to-use status bar
Name:		polybar
Version:	3.5.3
Release:	1
License:	MIT, BSD
Group:		X11/Window Managers
Source0:	https://github.com/polybar/polybar/releases/download/%{version}/%{name}-%{version}.tar.gz 
# Source0-md5:	188c46519c214b3272c99f1d8bb898bf
URL:		https://polybar.github.io/
BuildRequires:	alsa-lib-devel
BuildRequires:	cairo-devel
BuildRequires:	cmake >= 3.1
BuildRequires:	curl-devel
BuildRequires:	i3
BuildRequires:	i3-devel
BuildRequires:	jsoncpp-devel >= 1.7.7
BuildRequires:	libmpdclient-devel
BuildRequires:	libnl-devel
BuildRequires:	libstdc++-devel >= 6:5.1
BuildRequires:	libxcb-devel >= 1.12
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio
BuildRequires:	pulseaudio-devel
BuildRequires:	python3 >= 3.5
BuildRequires:	python3-Sphinx
BuildRequires:	python3-xcbgen
BuildRequires:	rpmbuild(macros) >= 1.719
BuildRequires:	sphinx-pdg
BuildRequires:	xcb-proto
BuildRequires:	xcb-util-cursor-devel
BuildRequires:	xcb-util-devel
BuildRequires:	xcb-util-image-devel
BuildRequires:	xcb-util-wm-devel
BuildRequires:	xcb-util-xrm-devel
Requires:	jsoncpp >= 1.7.7
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
Requires:	bash-completion >= 2.0
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description -n bash-completion-polybar
bash-completion for polybar.

%package -n zsh-completion-polybar
Summary:	zsh-completion for polybar
Summary(pl.UTF-8):	Uzupełnianie nazw w zsh dla polybar
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	zsh
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description -n zsh-completion-polybar
zsh-completion for polybar.

%prep
%setup -q

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
%doc README.md SUPPORT.md config
%attr(755,root,root) %{_bindir}/polybar
%attr(755,root,root) %{_bindir}/polybar-msg
%{_mandir}/man1/polybar.1*
%{_mandir}/man5/polybar.5*

%files -n bash-completion-polybar
%defattr(644,root,root,755)
%{bash_compdir}/polybar

%files -n zsh-completion-polybar
%defattr(644,root,root,755)
%{zsh_compdir}/_polybar
%{zsh_compdir}/_polybar_msg
