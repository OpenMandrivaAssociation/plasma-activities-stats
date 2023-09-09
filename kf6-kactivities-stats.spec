%define libname %mklibname KF6ActivitiesStats
%define devname %mklibname KF6ActivitiesStats -d
%define git 20230909

Name: kf6-kactivities-stats
Version: 5.240.0
Release: %{?git:0.%{git}.}1
Source0: https://invent.kde.org/frameworks/kactivities-stats/-/archive/master/kactivities-stats-master.tar.bz2#/kactivities-stats-%{git}.tar.bz2
Summary: Library for accessing the usage data collected by the activities system
URL: https://invent.kde.org/frameworks/kactivities-stats
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Sql)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6QuickWidgets)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6Activities)
BuildRequires: boost-devel
Requires: %{libname} = %{EVRD}

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

%prep
%autosetup -p1 -n kactivities-stats-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_datadir}/qlogging-categories6/kactivities-stats.*

%files -n %{devname}
%{_includedir}/KF6/KActivitiesStats
%{_libdir}/cmake/KF6ActivitiesStats
%{_qtdir}/mkspecs/modules/qt_KActivitiesStats.pri
%{_qtdir}/doc/KF6ActivitiesStats.*
%{_libdir}/pkgconfig/KF6ActivitiesStats.pc

%files -n %{libname}
%{_libdir}/libKF6ActivitiesStats.so*
