#!/usr/bin/env python
# -*- coding: UTF-8 -*-
##############################################################################
#
# PDFgui            by DANSE Diffraction group
#                   Simon J. L. Billinge
#                   (c) 2006 trustees of the Michigan State University.
#                   All rights reserved.
#
# File coded by:    Chris Farrow, Dmitriy Bryndin
#
# See AUTHORS.txt for a list of people who contributed.
# See LICENSE.txt for license information.
#
##############################################################################

# generated by wxGlade 0.4.1 on Thu Nov  2 11:50:45 2006

__id__ = "$Id$"

import wx
import wx.grid
from diffpy.pdfgui.gui.pdfpanel import PDFPanel
from diffpy.pdfgui.gui.tooltips import phasepanel as toolTips
from diffpy.pdfgui.gui import phasepanelutils
from diffpy.pdfgui.gui.wxExtensions.autowidthlabelsgrid import \
        AutoWidthLabelsGrid

class PhaseResultsPanel(wx.Panel, PDFPanel):
    """GUI Panel, holds phase (structure) related constraints."""
    def __init__(self, *args, **kwds):
        PDFPanel.__init__(self)
        # begin wxGlade: PhaseResultsPanel.__init__
        kwds["style"] = wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)
        self.sizerLatticeParameters_staticbox = wx.StaticBox(self, -1, "")
        self.sizerAdditionalParameters_staticbox = wx.StaticBox(self, -1, "")
        self.sizerAtoms_staticbox = wx.StaticBox(self, -1, "")
        self.sizerPanelName_staticbox = wx.StaticBox(self, -1, "")
        self.labelPanelName = wx.StaticText(self, -1, "Phase Results")
        self.labelA = wx.StaticText(self, -1, "a")
        self.textCtrlA = wx.TextCtrl(self, -1, "", style=wx.TE_READONLY)
        self.labelB = wx.StaticText(self, -1, "b")
        self.textCtrlB = wx.TextCtrl(self, -1, "", style=wx.TE_READONLY)
        self.labelC = wx.StaticText(self, -1, "c")
        self.textCtrlC = wx.TextCtrl(self, -1, "", style=wx.TE_READONLY)
        self.labelAlpha = wx.StaticText(self, -1, "alpha")
        self.textCtrlAlpha = wx.TextCtrl(self, -1, "", style=wx.TE_READONLY)
        self.labelBeta = wx.StaticText(self, -1, "beta")
        self.textCtrlBeta = wx.TextCtrl(self, -1, "", style=wx.TE_READONLY)
        self.labelGamma = wx.StaticText(self, -1, "gamma")
        self.textCtrlGamma = wx.TextCtrl(self, -1, "", style=wx.TE_READONLY)
        self.labelScaleFactor = wx.StaticText(self, -1, "Scale Factor")
        self.textCtrlScaleFactor = wx.TextCtrl(self, -1, "", style=wx.TE_READONLY)
        self.labelDelta1 = wx.StaticText(self, -1, "delta1")
        self.textCtrlDelta1 = wx.TextCtrl(self, -1, "", style=wx.TE_READONLY)
        self.labelDelta2 = wx.StaticText(self, -1, "delta2")
        self.textCtrlDelta2 = wx.TextCtrl(self, -1, "", style=wx.TE_READONLY)
        self.labelSpdiameter = wx.StaticText(self, -1, "spdiameter")
        self.textCtrlSpdiameter = wx.TextCtrl(self, -1, "", style=wx.TE_READONLY)
        self.labelSratio = wx.StaticText(self, -1, "sratio")
        self.textCtrlSratio = wx.TextCtrl(self, -1, "", style=wx.TE_READONLY)
        self.labelRcut = wx.StaticText(self, -1, "rcut")
        self.textCtrlRcut = wx.TextCtrl(self, -1, "", style=wx.TE_READONLY)
        self.labelStepcut = wx.StaticText(self, -1, "stepcut")
        self.textCtrlStepcut = wx.TextCtrl(self, -1, "", style=wx.TE_READONLY)
        self.labelIncludedPairs = wx.StaticText(self, -1, "Included Pairs")
        self.textCtrlIncludedPairs = wx.TextCtrl(self, -1, "all-all", style=wx.TE_READONLY)
        self.gridAtoms = AutoWidthLabelsGrid(self, -1, size=(1, 1))

        self.__set_properties()
        self.__do_layout()
        # end wxGlade
        self.__customProperties()
        return

    def __set_properties(self):
        # begin wxGlade: PhaseResultsPanel.__set_properties
        self.labelPanelName.SetFont(wx.Font(18, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.labelA.SetToolTipString("lat(1)")
        self.textCtrlA.SetToolTipString("lat(1)")
        self.labelB.SetToolTipString("lat(2)")
        self.textCtrlB.SetToolTipString("lat(2)")
        self.labelC.SetToolTipString("lat(3)")
        self.textCtrlC.SetToolTipString("lat(3)")
        self.labelAlpha.SetToolTipString("lat(4)")
        self.textCtrlAlpha.SetToolTipString("lat(4)")
        self.labelBeta.SetToolTipString("lat(5)")
        self.textCtrlBeta.SetToolTipString("lat(5)")
        self.labelGamma.SetToolTipString("lat(6)")
        self.textCtrlGamma.SetToolTipString("lat(6)")
        self.labelScaleFactor.SetToolTipString("phase scale factor")
        self.textCtrlScaleFactor.SetToolTipString("phase scale")
        self.labelDelta1.SetToolTipString("linear atomic correlation factor")
        self.textCtrlDelta1.SetToolTipString("linear atomic correlation factor")
        self.labelDelta2.SetToolTipString("quadratic atomic correlation factor")
        self.textCtrlDelta2.SetToolTipString("quadratic atomic correlation factor")
        self.labelSpdiameter.SetToolTipString("spherical nanoparticle amplitude correction")
        self.textCtrlSpdiameter.SetToolTipString("spherical nanoparticle amplitude correction")
        self.labelSratio.SetToolTipString("low r peak sharpening")
        self.textCtrlSratio.SetToolTipString("low r peak sharpening")
        self.labelRcut.SetToolTipString("peak sharpening cutoff")
        self.textCtrlRcut.SetToolTipString("peak sharpening cutoff")
        self.labelStepcut.SetToolTipString("cutoff for profile step-function")
        self.textCtrlStepcut.SetToolTipString("cutoff for profile step-function")
        self.textCtrlIncludedPairs.SetMinSize((240, 25))
        self.gridAtoms.CreateGrid(0, 11)
        self.gridAtoms.EnableEditing(0)
        self.gridAtoms.EnableDragRowSize(0)
        self.gridAtoms.SetColLabelValue(0, "elem")
        self.gridAtoms.SetColLabelValue(1, "x")
        self.gridAtoms.SetColLabelValue(2, "y")
        self.gridAtoms.SetColLabelValue(3, "z")
        self.gridAtoms.SetColLabelValue(4, "u11")
        self.gridAtoms.SetColLabelValue(5, "u22")
        self.gridAtoms.SetColLabelValue(6, "u33")
        self.gridAtoms.SetColLabelValue(7, "u12")
        self.gridAtoms.SetColLabelValue(8, "u13")
        self.gridAtoms.SetColLabelValue(9, "u23")
        self.gridAtoms.SetColLabelValue(10, "occ")
        # end wxGlade
        self.setToolTips(toolTips)
        

    def __do_layout(self):
        # begin wxGlade: PhaseResultsPanel.__do_layout
        sizerMain = wx.BoxSizer(wx.VERTICAL)
        sizerAtoms = wx.StaticBoxSizer(self.sizerAtoms_staticbox, wx.VERTICAL)
        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizerAdditionalParameters = wx.StaticBoxSizer(self.sizerAdditionalParameters_staticbox, wx.HORIZONTAL)
        grid_sizer_4 = wx.FlexGridSizer(3, 6, 0, 0)
        sizerLatticeParameters = wx.StaticBoxSizer(self.sizerLatticeParameters_staticbox, wx.HORIZONTAL)
        grid_sizer_3 = wx.FlexGridSizer(2, 6, 0, 0)
        sizerPanelName = wx.StaticBoxSizer(self.sizerPanelName_staticbox, wx.HORIZONTAL)
        sizerPanelName.Add(self.labelPanelName, 0, wx.LEFT|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5)
        sizerMain.Add(sizerPanelName, 0, wx.LEFT|wx.RIGHT|wx.EXPAND, 5)
        grid_sizer_3.Add(self.labelA, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5)
        grid_sizer_3.Add(self.textCtrlA, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_3.Add(self.labelB, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5)
        grid_sizer_3.Add(self.textCtrlB, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_3.Add(self.labelC, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5)
        grid_sizer_3.Add(self.textCtrlC, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_3.Add(self.labelAlpha, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5)
        grid_sizer_3.Add(self.textCtrlAlpha, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_3.Add(self.labelBeta, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5)
        grid_sizer_3.Add(self.textCtrlBeta, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_3.Add(self.labelGamma, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5)
        grid_sizer_3.Add(self.textCtrlGamma, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 0)
        sizerLatticeParameters.Add(grid_sizer_3, 1, wx.EXPAND, 0)
        sizerMain.Add(sizerLatticeParameters, 0, wx.LEFT|wx.RIGHT|wx.EXPAND, 5)
        grid_sizer_4.Add(self.labelScaleFactor, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5)
        grid_sizer_4.Add(self.textCtrlScaleFactor, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_4.Add((20, 10), 0, 0, 0)
        grid_sizer_4.Add((20, 10), 0, 0, 0)
        grid_sizer_4.Add((20, 10), 0, 0, 0)
        grid_sizer_4.Add((20, 10), 0, 0, 0)
        grid_sizer_4.Add(self.labelDelta1, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5)
        grid_sizer_4.Add(self.textCtrlDelta1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_4.Add(self.labelDelta2, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5)
        grid_sizer_4.Add(self.textCtrlDelta2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_4.Add(self.labelSpdiameter, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5)
        grid_sizer_4.Add(self.textCtrlSpdiameter, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_4.Add(self.labelSratio, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5)
        grid_sizer_4.Add(self.textCtrlSratio, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_4.Add(self.labelRcut, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5)
        grid_sizer_4.Add(self.textCtrlRcut, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_4.Add(self.labelStepcut, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5)
        grid_sizer_4.Add(self.textCtrlStepcut, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 0)
        sizerAdditionalParameters.Add(grid_sizer_4, 1, wx.EXPAND, 0)
        sizerMain.Add(sizerAdditionalParameters, 0, wx.LEFT|wx.RIGHT|wx.EXPAND, 5)
        sizer_1.Add(self.labelIncludedPairs, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5)
        sizer_1.Add(self.textCtrlIncludedPairs, 0, wx.ALL, 5)
        sizerAtoms.Add(sizer_1, 0, wx.EXPAND, 0)
        sizerAtoms.Add(self.gridAtoms, 1, wx.EXPAND, 0)
        sizerMain.Add(sizerAtoms, 1, wx.LEFT|wx.RIGHT|wx.EXPAND, 5)
        self.SetSizer(sizerMain)
        sizerMain.Fit(self)
        # end wxGlade

    ##########################################################################
    # Misc Methods

    def __customProperties(self):
        """Custom properties for the panel."""
        # The resulting structure
        self.structure = None
        self.constraints = {}
        self.results = None
        return

    def _cache(self):
        """Cache the current structure and constraints for future comparison."""
        pass

    def refresh(self):
        """Refreshes wigets on the panel."""
        # This makes the right thing happen in phasepanelutils. It saves a lot
        # of coding.
        pairs = self.structure.getSelectedPairs()
        self.textCtrlIncludedPairs.SetValue(pairs)
        self.structure = self.results
        phasepanelutils.refreshTextCtrls(self)
        phasepanelutils.refreshGrid(self)
        return

# end of class PhaseResultsPanel
