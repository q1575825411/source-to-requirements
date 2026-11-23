# Android Framework specialization

Use only when target is Android/AOSP/vendor source.

## Trace boundaries
- App/API -> framework facade -> Binder interface/AIDL -> system_server service -> native/HAL/vendor implementation, as applicable.
- For AMS/ATMS: lifecycle, process/user boundaries, background restrictions, locks and callbacks.
- For PMS/PermissionManager: install/update path, permission flags, signature/privileged checks, allowlists, users, roles and persistence.
- For WMS/Input: InputReader/InputDispatcher -> policy interception -> WindowManager/ATMS -> focus, keyguard, HOME/RECENTS and display/user context.
- For USB: UsbService/UsbDeviceManager/UsbHostManager, sysfs/kernel events, properties and role negotiation.
- For Camera: framework -> CameraService -> provider/HAL; startup ordering, binder death, permissions, timeout and vendor loading.

## Device/vendor qualifiers
Record Android release, SoC/vendor branch, product makefiles, overlays, `ro.*`/`persist.*` properties, device config, permissions XML, SELinux policy, init rc and VINTF where relevant. AOSP upstream behavior and vendor changes must be analyzed separately when source is available. Never label a path vendor-specific merely because it resides in a vendor tree without inspecting integration.

## Evidence cautions
- Public API does not guarantee every device's behavior.
- Feature may be gated by resource overlays or system properties.
- Java and native paths may differ; Binder identity and permission enforcement may occur downstream.
- Cross-user and multi-display behavior must not be generalized from single-user paths.
- AOSP 10 and 14 may have renamed or split services; follow actual checkout, not remembered filenames.
