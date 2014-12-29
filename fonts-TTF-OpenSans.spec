%define	fontname open-sans
%define	fontconf 60-%{fontname}.conf
Summary:	Open Sans is a humanist sans-serif typeface designed by Steve Matteson
Name:		fonts-TTF-OpenSans
Version:	1.10
Release:	1
License:	Apache v2.0
Group:		Fonts
URL:		http://www.google.com/fonts/specimen/Open+Sans
# Since the font doesn't have clear upstream, the source zip package is
# downloaded from Google Fonts. It is then converted to tar.gz. All by get-source.sh.
Source0:	http://pkgs.fedoraproject.org/repo/pkgs/open-sans-fonts/open-sans-fonts-%{version}.tar.xz/5fa43b45f45c7ef4b589b3bdf4052d77/open-sans-fonts-%{version}.tar.xz
# Source0-md5:	5fa43b45f45c7ef4b589b3bdf4052d77
Source1:	fontconfig.conf
Source2:	get-source.sh
BuildRequires:	tar >= 1:1.22
BuildRequires:	ttembed
BuildRequires:	xz
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_ttffontsdir	%{_fontsdir}/TTF

%description
Open Sans is a humanist sans serif typeface designed by Steve
Matteson, Type Director of Ascender Corp. This version contains the
complete 897 character set, which includes the standard ISO Latin 1,
Latin CE, Greek and Cyrillic character sets. Open Sans was designed
with an upright stress, open forms and a neutral, yet friendly
appearance. It was optimized for print, web, and mobile interfaces,
and has excellent legibility characteristics in its letter forms.

%prep
%setup -q -n open-sans-fonts-%{version}

%build
# set Embedding permission to 'Installable'
ls *.ttf | xargs ttembed

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_ttffontsdir},%{_sysconfdir}/fonts/conf.d,%{_datadir}/fontconfig/conf.avail}

cp -p *.ttf $RPM_BUILD_ROOT%{_ttffontsdir}
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/fontconfig/conf.avail/%{fontconf}
ln -s %{_datadir}/fontconfig/conf.avail/%{fontconf} $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.d/%{fontconf}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.txt
%{_sysconfdir}/fonts/conf.d/60-open-sans.conf
%{_datadir}/fontconfig/conf.avail/60-open-sans.conf
%{_datadir}/fonts/TTF/OpenSans-Bold.ttf
%{_datadir}/fonts/TTF/OpenSans-BoldItalic.ttf
%{_datadir}/fonts/TTF/OpenSans-ExtraBold.ttf
%{_datadir}/fonts/TTF/OpenSans-ExtraBoldItalic.ttf
%{_datadir}/fonts/TTF/OpenSans-Italic.ttf
%{_datadir}/fonts/TTF/OpenSans-Light.ttf
%{_datadir}/fonts/TTF/OpenSans-LightItalic.ttf
%{_datadir}/fonts/TTF/OpenSans-Regular.ttf
%{_datadir}/fonts/TTF/OpenSans-Semibold.ttf
%{_datadir}/fonts/TTF/OpenSans-SemiboldItalic.ttf
