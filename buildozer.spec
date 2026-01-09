[app]
title = BioMech App
package.name = biomech
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy

orientation = portrait
fullscreen = 0
android.permissions = INTERNET

# 关键配置：跳过SDK许可确认，防止卡死
android.accept_sdk_license = True
# 架构支持
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1