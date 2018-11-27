# These and other macros are documented in dhd/droid-hal-device.inc
# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device latte
%define vendor xiaomi

%define vendor_pretty Mi Pad 2
%define device_pretty Xiaomi

%define device_target_cpu i486

%define installable_zip 1

%define enable_kernel_update 1
%define straggler_files \
/fstab \
/intel_prop.cfg \
/rfkill_bt.sh
%{nil}


%include rpm/dhd/droid-hal-device.inc

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"

