#!/usr/bin/env python
# -*- coding: UTF-8 -*-
##############################################################################
#
# PDFgui            by DANSE Diffraction group
#                   Simon J. L. Billinge
#                   (c) 2007 trustees of the Michigan State University.
#                   All rights reserved.
#
# File coded by:    Chris Farrow
#
# See AUTHORS.txt for a list of people who contributed.
# See LICENSE.txt for license information.
#
##############################################################################

# generated by wxGlade 0.4.1 on Thu Apr  5 14:04:33 2007

import wx
import wx.lib.filebrowsebutton
from diffpy.pdfgui.gui import pdfguiglobals
from diffpy.pdfgui.gui.pdfpanel import PDFPanel
from diffpy.pdfgui.gui.tooltips import preferencespanel as toolTips
from diffpy.pdfgui.control.controlerrors import ControlFileError
from diffpy.pdfgui.control import structureviewer

class PreferencesPanel(wx.Panel, PDFPanel):
    def __init__(self, *args, **kwds):
        PDFPanel.__init__(self)
        # begin wxGlade: PreferencesPanel.__init__
        kwds["style"] = wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)
        self.sizerPanelName_staticbox = wx.StaticBox(self, -1, "")
        self.labelPanelName = wx.StaticText(self, -1, "Preferences")
        self.labelViewer = wx.StaticText(self, -1, "Structure viewer executable")
        self.textCtrlViewer = wx.TextCtrl(self, -1, "")
        self.buttonViewerBrowse = wx.Button(self, -1, "Browse")
        self.labelArgStr = wx.StaticText(self, -1, "Argument string")
        self.textCtrlArgument = wx.TextCtrl(self, -1, "")
        self.labelFormat = wx.StaticText(self, -1, "Structure format")
        self.choiceFormat = wx.Choice(self, -1, choices=[])
        self.structureDirCheckBox = wx.CheckBox(self, -1, "Remember path to structure files")
        self.dataDirCheckBox = wx.CheckBox(self, -1, "Remember path to data sets")
        self.static_line_1 = wx.StaticLine(self, -1)
        self.okButton = wx.Button(self, wx.ID_OK, "OK")
        self.cancelButton = wx.Button(self, wx.ID_CANCEL, "Cancel")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.onBrowse, self.buttonViewerBrowse)
        self.Bind(wx.EVT_BUTTON, self.onOK, id=wx.ID_OK)
        self.Bind(wx.EVT_BUTTON, self.onCancel, id=wx.ID_CANCEL)
        # end wxGlade
        self.__customProperties()

    def __set_properties(self):
        # begin wxGlade: PreferencesPanel.__set_properties
        self.labelPanelName.SetFont(wx.Font(18, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, "Bitstream Vera Sans"))
        self.structureDirCheckBox.SetToolTipString("Remember the structures directory across sessions. If unchecked, the initial structures directory will default to the current path.")
        self.dataDirCheckBox.SetToolTipString("Remember the data set directory across sessions. If unchecked, the initial data set directory will default to the current path.")
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: PreferencesPanel.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        grid_sizer_1 = wx.GridSizer(3, 3, 10, 10)
        sizerPanelName = wx.StaticBoxSizer(self.sizerPanelName_staticbox, wx.HORIZONTAL)
        sizerPanelName.Add(self.labelPanelName, 1, wx.LEFT|wx.RIGHT|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5)
        sizer_1.Add(sizerPanelName, 0, wx.LEFT|wx.RIGHT|wx.EXPAND, 5)
        grid_sizer_1.Add(self.labelViewer, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.textCtrlViewer, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.buttonViewerBrowse, 0, 0, 0)
        grid_sizer_1.Add(self.labelArgStr, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.textCtrlArgument, 0, wx.EXPAND, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.labelFormat, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.choiceFormat, 0, wx.EXPAND, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        sizer_1.Add(grid_sizer_1, 0, wx.ALL, 5)
        sizer_1.Add(self.structureDirCheckBox, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)
        sizer_1.Add(self.dataDirCheckBox, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)
        sizer_1.Add((0, 0), 1, wx.EXPAND, 0)
        sizer_1.Add(self.static_line_1, 0, wx.LEFT|wx.RIGHT|wx.EXPAND|wx.ALIGN_BOTTOM, 5)
        sizer_3.Add((0, 0), 1, 0, 0)
        sizer_3.Add(self.okButton, 0, wx.ALL|wx.ALIGN_RIGHT, 5)
        sizer_3.Add(self.cancelButton, 0, wx.ALL|wx.ALIGN_RIGHT, 5)
        sizer_1.Add(sizer_3, 0, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        # end wxGlade

    def __customProperties(self):
        """Set the custom properties."""

        # Fill the options in the format choice
        viewer = structureviewer.getStructureViewer()
        formats = viewer.getFileFormats()
        formats.sort()
        for fmt in formats:
            self.choiceFormat.Append(fmt)

        self.setToolTips(toolTips)
        return


    def onCancel(self, event): # wxGlade: PreferencesPanel.<event_handler>
        """Cancel the changes. Go back to the last panel."""
        selections = self.treeCtrlMain.GetSelections()
        if selections:
            node = selections[0]
            entrytype = self.treeCtrlMain.GetNodeType(node)
        else:
            entrytype = None
        self.mainFrame.setMode("fitting")
        self.mainFrame.switchRightPanel(entrytype)
        return 

    def onOK(self, event): # wxGlade: PreferencesPanel.<event_handler>
        """Record all of the preferences and return to fitting mode."""

        # Record structure viewer stuff
        executable = str(self.textCtrlViewer.GetValue()).strip()
        argstr = str(self.textCtrlArgument.GetValue()).strip()
        fileformat = str(self.choiceFormat.GetStringSelection())
        config = {
                "executable" : executable,
                "argstr"     : argstr,
                "fileformat" : fileformat,
                }

        viewer = structureviewer.getStructureViewer()
        viewer.setConfig(config)

        # Structures path
        remember = bool(self.structureDirCheckBox.GetValue())
        if not self.cP.has_section("PHASE"):
            self.cP.add_section("PHASE")
        self.cP.set("PHASE", "remember", str(remember))

        # Data set path
        remember = bool(self.dataDirCheckBox.GetValue())
        if not self.cP.has_section("DATASET"):
            self.cP.add_section("DATASET")
        self.cP.set("DATASET", "remember", str(remember))

        # Get out of here
        self.onCancel(event)
        return

    def refresh(self):
        """Refresh the panel."""

        # Structure viewer stuff
        viewer = structureviewer.getStructureViewer()
        config = viewer.getConfig()
        self.textCtrlViewer.SetValue(config["executable"])
        self.textCtrlArgument.SetValue(config["argstr"])
        self.choiceFormat.SetStringSelection(config["fileformat"])

        remember = False
        if self.cP.has_option("DATASET", "remember"):
            remember = self.cP.getboolean("DATASET", "remember")
        self.dataDirCheckBox.SetValue(remember)

        remember = False
        if self.cP.has_option("PHASE", "remember"):
            remember = self.cP.getboolean("PHASE", "remember")
        self.structureDirCheckBox.SetValue(remember)
        return

    def onBrowse(self, event): # wxGlade: PreferencesPanel.<event_handler>
        d = wx.FileDialog(None, "Choose structure viewer", ".", 
                "", "All Files|*", wx.OPEN|wx.FD_FILE_MUST_EXIST)
        if d.ShowModal() == wx.ID_OK:
            fullpath = d.GetPath()
            self.textCtrlViewer.SetValue(fullpath)
        return

# end of class PreferencesPanel


