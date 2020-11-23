# -*- coding: utf-8 -*-
#===============================================================================
# NetworkBrowser and MountManager Plugin by acid-burn
# for further License informations see the corresponding License files
# or SourceCodes
#
#===============================================================================

from Components.Language import language
from Tools.Directories import resolveFilename, SCOPE_PLUGINS, SCOPE_LANGUAGE
from boxbranding import getMachineBuild
import os, gettext
from collections import defaultdict

PluginLanguageDomain = "NetworkBrowser"
PluginLanguagePath = "SystemPlugins/NetworkBrowser/locale"

def localeInit():
	gettext.bindtextdomain(PluginLanguageDomain, resolveFilename(SCOPE_PLUGINS, PluginLanguagePath))

def _(txt):
	if gettext.dgettext(PluginLanguageDomain, txt):
		return gettext.dgettext(PluginLanguageDomain, txt)
	else:
		print "[" + PluginLanguageDomain + "] fallback to default translation for " + txt
		return gettext.gettext(txt)

language.addCallback(localeInit())

default_mount_options = defaultdict(str)
default_mount_options["nfs"] = "rw,nolock,tcp"
if getMachineBuild() == "inihdx":
	default_mount_options["cifs"] = "rw,utf8"
else:
	default_mount_options["cifs"] = "rw,utf8,vers=2.1"
