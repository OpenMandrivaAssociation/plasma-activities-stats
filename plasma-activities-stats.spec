%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

%define libname %mklibname PlasmaActivitiesStats
%define devname %mklibname PlasmaActivitiesStats -d
#define git 20240222
%define gitbranch Plasma/6.0
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

Name: plasma-activities-stats
Version: 6.5.5
Release: %{?git:0.%{git}.}1
%if 0%{?git:1}
Source0: https://invent.kde.org/plasma/plasma-activities-stats/-/archive/%{gitbranch}/plasma-activities-stats-%{gitbranchd}.tar.bz2#/plasma-activities-stats-%{git}.tar.bz2
%else
Source0: http://download.kde.org/%{stable}/plasma/%{version}/plasma-activities-stats-%{version}.tar.xz
%endif
Summary: Library for accessing the usage data collected by the activities system
URL: https://invent.kde.org/frameworks/plasma-activities-stats
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Sql)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6QuickWidgets)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(PlasmaActivities)
BuildRequires: boost-devel
BuildRequires: python
BuildRequires: doxygen
BuildSystem: cmake
BuildOption: -DBUILD_QCH:BOOL=ON
BuildOption: -DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
Requires: %{libname} = %{EVRD}
# Renamed after 6.0 2025-04-27
%rename kf6-plasma-activities-stats

%description
Library for accessing the usage data collected by the activities system

%package -n %{libname}
Summary: Library for accessing the usage data collected by the activities system
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
Library for accessing the usage data collected by the activities system

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Library for accessing the usage data collected by the activities system

%package doc
Summary: Developer documentation for %{name} in Qt Assistant format
Group: Development/C

%description doc
Developer documentation for %{name} in Qt Assistant format

%files doc
%{_qtdir}/doc/PlasmaActivitiesStats.*

%files
%{_datadir}/qlogging-categories6/plasma-activities-stats.*

%files -n %{devname}
%{_includedir}/PlasmaActivitiesStats
%{_libdir}/cmake/PlasmaActivitiesStats
%{_libdir}/pkgconfig/PlasmaActivitiesStats.pc

%files -n %{libname}
%{_libdir}/libPlasmaActivitiesStats.so*
