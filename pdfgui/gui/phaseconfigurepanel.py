#!/usr/bin/env python
########################################################################
#
# PDFgui            by DANSE Diffraction group
#                   Simon J. L. Billinge
#                   (c) 2006 trustees of the Michigan State University.
#                   All rights reserved.
#
# File coded by:    Chris Farrow
#
# See AUTHORS.txt for a list of people who contributed.
# See LICENSE.txt for license information.
#
########################################################################

# -*- coding: UTF-8 -*-
# generated by wxGlade 0.4.1 on Thu Nov  2 11:27:42 2006
__id__ = "$Id$"

import wx
import wx.grid
from diffpy.Structure import Atom
from diffpy.Structure.PeriodicTable import is_element
from diffpy.pdfgui.control.constraint import Constraint
from diffpy.pdfgui.control.controlerrors import *
from insertrowsdialog import InsertRowsDialog
from pdfpanel import PDFPanel
from phasepanelutils import *
from wxExtensions.autowidthlabelsgrid import AutoWidthLabelsGrid
from wxExtensions.validators import TextValidator, FLOAT_ONLY
from supercelldialog import SupercellDialog
from sgstructuredialog import SGStructureDialog


class PhaseConfigurePanel(wx.Panel, PDFPanel):
    """Panel for configuring a phase.
    
    Data members:
        structure       -- reference to PDFStructure, the panel works with
        _focusedText    -- value of a cell ot textctrl before it changes
        lConstraintsMap -- map of TextCtrl name to parameter name
        _row            -- row,    where rightclick occured 
        _col            -- column, where rightclick occured 
    """
    def __init__(self, *args, **kwds):
        PDFPanel.__init__(self)
        # begin wxGlade: PhaseConfigurePanel.__init__
        kwds["style"] = wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)
        self.sizerLatticeParameters_staticbox = wx.StaticBox(self, -1, "")
        self.sizerAdditionalParameters_staticbox = wx.StaticBox(self, -1, "")
        self.sizerAtoms_staticbox = wx.StaticBox(self, -1, "")
        self.sizerPanelName_staticbox = wx.StaticBox(self, -1, "")
        self.labelPanelName = wx.StaticText(self, -1, "Phase Configuration")
        self.labelA = wx.StaticText(self, -1, "a")
        self.textCtrlA = wx.TextCtrl(self, -1, "", style=wx.TE_PROCESS_ENTER)
        self.labelB = wx.StaticText(self, -1, "b")
        self.textCtrlB = wx.TextCtrl(self, -1, "", style=wx.TE_PROCESS_ENTER)
        self.labelC = wx.StaticText(self, -1, "c")
        self.textCtrlC = wx.TextCtrl(self, -1, "", style=wx.TE_PROCESS_ENTER)
        self.labelAlpha = wx.StaticText(self, -1, "alpha")
        self.textCtrlAlpha = wx.TextCtrl(self, -1, "", style=wx.TE_PROCESS_ENTER)
        self.labelBeta = wx.StaticText(self, -1, "beta")
        self.textCtrlBeta = wx.TextCtrl(self, -1, "", style=wx.TE_PROCESS_ENTER)
        self.labelGamma = wx.StaticText(self, -1, "gamma")
        self.textCtrlGamma = wx.TextCtrl(self, -1, "", style=wx.TE_PROCESS_ENTER)
        self.labelScaleFactor = wx.StaticText(self, -1, "Scale Factor")
        self.textCtrlScaleFactor = wx.TextCtrl(self, -1, "", style=wx.TE_PROCESS_ENTER)
        self.labelCorrelationLimit = wx.StaticText(self, -1, "Correlation limit")
        self.textCtrlCorrelationLimit = wx.TextCtrl(self, -1, "", style=wx.TE_PROCESS_ENTER)
        self.labelDelta1 = wx.StaticText(self, -1, "delta1")
        self.textCtrlDelta1 = wx.TextCtrl(self, -1, "", style=wx.TE_PROCESS_ENTER)
        self.labelDelta2 = wx.StaticText(self, -1, "delta2")
        self.textCtrlDelta2 = wx.TextCtrl(self, -1, "", style=wx.TE_PROCESS_ENTER)
        self.labelSrat = wx.StaticText(self, -1, "srat")
        self.textCtrlSrat = wx.TextCtrl(self, -1, "", style=wx.TE_PROCESS_ENTER)
        self.labelRcut = wx.StaticText(self, -1, "rcut")
        self.textCtrlRcut = wx.TextCtrl(self, -1, "", style=wx.TE_PROCESS_ENTER)
        self.gridAtoms = AutoWidthLabelsGrid(self, -1, size=(1, 1))

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.grid.EVT_GRID_CMD_CELL_RIGHT_CLICK, self.onCellRightClick, self.gridAtoms)
        self.Bind(wx.grid.EVT_GRID_CMD_EDITOR_SHOWN, self.onEditorShown, self.gridAtoms)
        self.Bind(wx.grid.EVT_GRID_CMD_LABEL_RIGHT_CLICK, self.onLabelRightClick, self.gridAtoms)
        self.Bind(wx.grid.EVT_GRID_CMD_CELL_CHANGE, self.onCellChange, self.gridAtoms)
        # end wxGlade
        self.__customProperties()

    def __set_properties(self):
        # begin wxGlade: PhaseConfigurePanel.__set_properties
        self.SetFocus()
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
        self.labelCorrelationLimit.Hide()
        self.textCtrlCorrelationLimit.Hide()
        self.labelDelta1.SetToolTipString("linear atomic correlation factor")
        self.textCtrlDelta1.SetToolTipString("linear atomic correlation factor")
        self.labelDelta2.SetToolTipString("quadratic atomic correlation factor")
        self.textCtrlDelta2.SetToolTipString("quadratic atomic correlation factor")
        self.labelSrat.SetToolTipString("low r peak sharpening")
        self.textCtrlSrat.SetToolTipString("low r peak sharpening")
        self.labelRcut.SetToolTipString("peak sharpening cutoff")
        self.textCtrlRcut.SetToolTipString("peak sharpening cutoff")
        self.gridAtoms.CreateGrid(0, 11)
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

    def __do_layout(self):
        # begin wxGlade: PhaseConfigurePanel.__do_layout
        sizerMain = wx.BoxSizer(wx.VERTICAL)
        sizerAtoms = wx.StaticBoxSizer(self.sizerAtoms_staticbox, wx.VERTICAL)
        sizerAdditionalParameters = wx.StaticBoxSizer(self.sizerAdditionalParameters_staticbox, wx.HORIZONTAL)
        grid_sizer_4 = wx.FlexGridSizer(3, 4, 0, 0)
        sizerLatticeParameters = wx.StaticBoxSizer(self.sizerLatticeParameters_staticbox, wx.HORIZONTAL)
        grid_sizer_3 = wx.FlexGridSizer(2, 6, 0, 0)
        sizerPanelName = wx.StaticBoxSizer(self.sizerPanelName_staticbox, wx.HORIZONTAL)
        sizerPanelName.Add(self.labelPanelName, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 5)
        sizerMain.Add(sizerPanelName, 0, wx.ALL|wx.EXPAND, 5)
        grid_sizer_3.Add(self.labelA, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 5)
        grid_sizer_3.Add(self.textCtrlA, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 0)
        grid_sizer_3.Add(self.labelB, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 5)
        grid_sizer_3.Add(self.textCtrlB, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 0)
        grid_sizer_3.Add(self.labelC, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 5)
        grid_sizer_3.Add(self.textCtrlC, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 0)
        grid_sizer_3.Add(self.labelAlpha, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 5)
        grid_sizer_3.Add(self.textCtrlAlpha, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 0)
        grid_sizer_3.Add(self.labelBeta, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 5)
        grid_sizer_3.Add(self.textCtrlBeta, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 0)
        grid_sizer_3.Add(self.labelGamma, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 5)
        grid_sizer_3.Add(self.textCtrlGamma, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 0)
        sizerLatticeParameters.Add(grid_sizer_3, 1, wx.EXPAND, 0)
        sizerMain.Add(sizerLatticeParameters, 0, wx.ALL|wx.EXPAND, 5)
        grid_sizer_4.Add(self.labelScaleFactor, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 5)
        grid_sizer_4.Add(self.textCtrlScaleFactor, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 0)
        grid_sizer_4.Add(self.labelCorrelationLimit, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 5)
        grid_sizer_4.Add(self.textCtrlCorrelationLimit, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 0)
        grid_sizer_4.Add(self.labelDelta1, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 5)
        grid_sizer_4.Add(self.textCtrlDelta1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 0)
        grid_sizer_4.Add(self.labelDelta2, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 5)
        grid_sizer_4.Add(self.textCtrlDelta2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 0)
        grid_sizer_4.Add(self.labelSrat, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 5)
        grid_sizer_4.Add(self.textCtrlSrat, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 0)
        grid_sizer_4.Add(self.labelRcut, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 5)
        grid_sizer_4.Add(self.textCtrlRcut, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 0)
        sizerAdditionalParameters.Add(grid_sizer_4, 1, wx.EXPAND, 0)
        sizerMain.Add(sizerAdditionalParameters, 0, wx.ALL|wx.EXPAND, 5)
        sizerAtoms.Add(self.gridAtoms, 1, wx.EXPAND, 0)
        sizerMain.Add(sizerAtoms, 1, wx.ALL|wx.EXPAND, 5)
        self.SetAutoLayout(True)
        self.SetSizer(sizerMain)
        sizerMain.Fit(self)
        sizerMain.SetSizeHints(self)
        # end wxGlade

    ##########################################################################
    # Misc Methods


    def __customProperties(self):
        """Custom properties for the panel."""
        self.structure = None
        self.constraints = {}
        self.results = None
        self._isotropic = False
        self._row = 0
        self._col = 0
        self._focusedText = None
        self._selectedCells = []

        self.lAtomConstraints = ['x','y','z',
                                 'u11','u22','u33','u12','u13','u23','occ']
        # pdffit internal naming
        self.lConstraintsMap = {
                'textCtrlA'             : 'lat(1)',
                'textCtrlB'             : 'lat(2)',
                'textCtrlC'             : 'lat(3)',
                'textCtrlAlpha'         : 'lat(4)',
                'textCtrlBeta'          : 'lat(5)',
                'textCtrlGamma'         : 'lat(6)',
                'textCtrlScaleFactor'   : 'pscale',
                'textCtrlDelta1'          : 'delta1',
                'textCtrlDelta2'         : 'delta2',
                'textCtrlSrat'          : 'srat',
                'textCtrlRcut'          : 'rcut',
                }

        self.toolTips = {
                'textCtrlA'             : "lat(1)",
                'textCtrlB'             : "lat(2)",
                'textCtrlC'             : "lat(3)",
                'textCtrlAlpha'         : "lat(4)",
                'textCtrlBeta'          : "lat(5)",
                'textCtrlGamma'         : "lat(6)",
                'textCtrlScaleFactor'   : "phase scale factor",
                'textCtrlDelta1'        : "linear atomic correlation factor",
                'textCtrlDelta2'        : "quadratic atomic correlation factor",
                'textCtrlSrat'          : "low r peak sharpening",
                'textCtrlRcut'          : "peak sharpening cutoff",
                }

        # bind onSetFocus onKillFocus events to text controls
        for tname in self.lConstraintsMap:
            self.__dict__[tname].Bind(wx.EVT_SET_FOCUS, self.onSetFocus)
            self.__dict__[tname].Bind(wx.EVT_KILL_FOCUS, self.onKillFocus)
            self.__dict__[tname].SetValidator(TextValidator(FLOAT_ONLY))

        # set cells as float type
        attr = wx.grid.GridCellAttr()
        attr.SetEditor(wx.grid.GridCellFloatEditor())
        attr.SetRenderer(wx.grid.GridCellFloatRenderer())

        # catch key events and apply them to the grid
        self.Bind(wx.EVT_KEY_DOWN, self.onKey)
        return

    def refresh(self):
        """Refreshes wigets on the panel."""
        refreshTextCtrls(self)
        refreshGrid(self)
        self.restrictConstrainedParameters()
        return

    def restrictConstrainedParameters(self):
        """Set 'read-only' boxes that correspond to constrained parameters."""

        # First the TextCtrls
        for key, var in self.lConstraintsMap.iteritems():
            textCtrl = getattr(self, key)
            if var in self.constraints:
                textCtrl.SetEditable(False)
                textCtrl.SetBackgroundColour(
                        wx.SystemSettings_GetColour(wx.SYS_COLOUR_GRAYTEXT))
                textCtrl.SetToolTipString(self.constraints[var].formula)
            else:
                textCtrl.SetEditable(True)
                textCtrl.SetBackgroundColour(wx.NullColour)
                textCtrl.SetToolTipString(self.toolTips[key])

        # Now the grid
        rows = self.gridAtoms.GetNumberRows()
        cols = self.gridAtoms.GetNumberCols()
        selection = []
        
        for i in xrange(rows):
            for j in xrange(1, cols):
                var = self.lAtomConstraints[j-1]
                var += '(%i)'%(i+1)
                if var in self.constraints:
                    self.gridAtoms.SetReadOnly(i, j, True)
                    self.gridAtoms.SetCellBackgroundColour(i, j, 
                        wx.SystemSettings_GetColour(wx.SYS_COLOUR_GRAYTEXT))
                else:
                    self.gridAtoms.SetReadOnly(i, j, False)
                    self.gridAtoms.SetCellBackgroundColour(i, j, wx.NullColour)

        return
    
    def applyTextCtrlChange(self, id, value):
        """Update a structure according to a change in a TextCtrl.
        
        id      --  textctrl id
        value   --  new value  
        """
        if self.structure == None: return
            #raise ControlValueError, "structure is not defined."
        
        try:
            if   id == self.textCtrlA.GetId():
                self.structure.lattice.setLatPar(a = float(value))
            elif id == self.textCtrlB.GetId():
                self.structure.lattice.setLatPar(b = float(value))
            elif id == self.textCtrlC.GetId():
                self.structure.lattice.setLatPar(c = float(value))
            elif id == self.textCtrlAlpha.GetId():
                self.structure.lattice.setLatPar(alpha = float(value))
            elif id == self.textCtrlBeta.GetId():
                self.structure.lattice.setLatPar(beta = float(value))
            elif id == self.textCtrlGamma.GetId():
                self.structure.lattice.setLatPar(gamma = float(value))
            elif id == self.textCtrlScaleFactor.GetId():
                self.structure.pdffit['scale'] = float( value )
            elif id == self.textCtrlDelta1.GetId():
                self.structure.pdffit['delta1'] = float( value )
            elif id == self.textCtrlDelta2.GetId():
                self.structure.pdffit['delta2']  = float( value )
            elif id == self.textCtrlSrat.GetId():
                self.structure.pdffit['srat'] = float( value )
            elif id == self.textCtrlRcut.GetId():
                self.structure.pdffit['rcut']  = float( value )
        except ValueError:
            pass
        return

    def applyCellChange(self, i, j, value):
        """Update an atom according to a change in a cell.
        
        i       --  cell position
        j       --  cell position
        value   --  new value  
        """
        if not self.mainFrame or self.structure == None: return
            #raise ControlValueError, "structure is not defined."

        # The element name
        if j == 0:
            value = value.title()
            if not is_element(value): return
            self.structure[i].element   =       value  # element
            return

        # Other entries
        # ignore the change if the value is not valid
        try:
            value = float(value)
        except ValueError:
            return

        if value == "": value = 0.0
        if j == 1:
            self.structure[i].xyz[0]    = value # x
        elif j == 2:
            self.structure[i].xyz[1]    = value # y
        elif j == 3:
            self.structure[i].xyz[2]    = value # z
        elif j == 4:
            self.structure[i].U[0,0]    = value # U(1,1)
        elif j == 5:
            self.structure[i].U[1,1]    = value # U(2,2)
        elif j == 6:
            self.structure[i].U[2,2]    = value # U(3,3)
        elif j == 7:
            self.structure[i].U[0,1]    = value # U(1,2)
        elif j == 8:
            self.structure[i].U[0,2]    = value # U(1,3)
        elif j == 9:
            self.structure[i].U[1,2]    = value # U(2,3)
        elif j == 10:
            self.structure[i].occupancy = value # occupancy

        self.mainFrame.needsSave()        
        return

    ##########################################################################
    # Event Handlers

    # TextCtrl Events
    def onSetFocus(self, event):
        """Saves a TextCtrl value, to be compared in onKillFocuse later."""
        self._focusedText = event.GetEventObject().GetValue()
        event.Skip()
        return
        
    def onKillFocus(self, event):
        """Check value of TextCtrl and update structure if necessary."""
        if not self.mainFrame: return
        textctrl = event.GetEventObject()
        value = textctrl.GetValue()

        if self._focusedText != value:
            self.applyTextCtrlChange(textctrl.GetId(), value)
            self.refresh()
            self.mainFrame.needsSave()        
                
        self._focusedText = ""
        event.Skip()
        return

    # Grid Events
    def onLabelRightClick(self, event): # wxGlade: PhaseConfigurePanel.<event_handler>
        """Bring up right-click menu."""
        if self.structure != None:
            dx = dy = 0
            if event.GetRow() == -1:
                dy = self.gridAtoms.GetGridCornerLabelWindow().GetSize().y
            if event.GetCol() == -1:
                dx = self.gridAtoms.GetGridCornerLabelWindow().GetSize().x
    
            # do not popup menu if the whole grid is set to read only
            if len(self.structure) == 0:
                self.popupMenu(self.gridAtoms, event.GetPosition().x-dx, 
                        event.GetPosition().y-dy)
        event.Skip()
        return

    def onCellRightClick(self, event): # wxGlade: PhaseConfigurePanel.<event_handler>
        """Bring up right-click menu."""
        self._row = event.GetRow()
        self._col = event.GetCol()
        # If the right-clicked node is not part of a group, then make sure that
        # it is the only selected cell.
        append = False
        r = self._row
        c = self._col
        if self.gridAtoms.IsInSelection(r,c):
            append = True
        self.gridAtoms.SelectBlock(r,c,r,c,append)

        self.popupMenu(self.gridAtoms, event.GetPosition().x, event.GetPosition().y)
        event.Skip()
        return

    def onEditorShown(self, event): # wxGlade: PhaseConfigurePanel.<event_handler>
        """Capture the focused text when the grid editor is shown."""
        i = event.GetRow()
        j = event.GetCol()
        self._focusedText = self.gridAtoms.GetCellValue(i,j)
        self._selectedCells = getSelectedCells(self)
        event.Skip()
        return

    def onCellChange(self, event): # wxGlade: PhaseConfigurePanel.<event_handler>
        """Update focused and selected text when a cell changes."""
        # NOTE: be careful with refresh() => recursion! operations on grid will
        # call onCellChange.
        i = event.GetRow()
        j = event.GetCol()

        # This keeps us out of recursion
        if self._focusedText is None: return
        self._focusedText = None

        value = self.gridAtoms.GetCellValue(i,j)
        self._selectedCells.append((i,j))
        fillCells(self, self._selectedCells, value)
        self.refresh()

        event.Skip()
        return

    def onKey(self, event):
        """Catch key events in the panel."""
        key = event.GetKeyCode()

        # Select All
        # Ctrl A
        if event.ControlDown() and key == 65:
            rows = self.gridAtoms.GetNumberRows()
            cols = self.gridAtoms.GetNumberCols()
            self.gridAtoms.SelectBlock(0,0,rows,cols)

        # Delete an atom
        # Delete
        elif key == 127:
            indices = getSelectedAtoms(self)
            selected = [i for i in indices if isWholeRowSelected(self, i)]
            if selected:
                self.structure.deleteAtoms(indices)
                self.refresh()
                self.mainFrame.needsSave()

        # Ctrl -
        elif event.ControlDown() and key == 45:
            indices = getSelectedAtoms(self)
            self.structure.deleteAtoms(indices)
            self.refresh()
            self.mainFrame.needsSave()

        # Append an atom
        # Ctrl +
        elif event.ControlDown() and event.ShiftDown() and key == 61:
            indices = getSelectedAtoms(self)
            pos = 0
            if indices:
                pos = 1+indices[-1]
            elif self.structure:
                pos = len(self.structure)
            # insert "rows" atoms into the structure
            atoms = [Atom("",[0.0,0.0,0.0])]
            self.structure.insertAtoms(pos, atoms)
            self.refresh()
            self.mainFrame.needsSave()

        else:
            event.Skip()

        return

    ##########################################################################
    # Grid popup menu and handlers

    def popupMenu(self, window, x, y):
        """Creates the popup menu
        
        window  --  window, where to popup a menu
        x       --  x coordinate
        y       --  y coordinate
        """
        # only do this part the first time so the events are only bound once
        if not hasattr(self, "insertID"):
            self.insertID = wx.NewId()
            self.deleteID = wx.NewId()
            self.copyID = wx.NewId()
            self.pasteID = wx.NewId()
            self.supercellID = wx.NewId()
            self.spaceGroupID = wx.NewId()

            self.Bind(wx.EVT_MENU, self.onPopupInsert, id=self.insertID)
            self.Bind(wx.EVT_MENU, self.onPopupDelete, id=self.deleteID)
            self.Bind(wx.EVT_MENU, self.onPopupCopy, id=self.copyID)
            self.Bind(wx.EVT_MENU, self.onPopupPaste, id=self.pasteID)
            self.Bind(wx.EVT_MENU, self.onPopupSupercell, id=self.supercellID)
            self.Bind(wx.EVT_MENU, self.onPopupSpaceGroup, id=self.spaceGroupID)

        # make a menu
        menu = wx.Menu()

        # add some other items
        menu.Append(self.insertID, "Insert atoms...")
        menu.Append(self.deleteID, "Delete atoms")
        menu.AppendSeparator()
        menu.Append(self.copyID, "Copy")
        menu.Append(self.pasteID, "Paste")
        menu.AppendSeparator()
        menu.Append(self.supercellID, "Create supercell...")
        menu.Append(self.spaceGroupID, "Expand space group...")

        # Disable some items if there are no atoms selected
        indices = getSelectedAtoms(self)
        if not indices:
            menu.Enable(self.deleteID, False);
            menu.Enable(self.spaceGroupID, False);

        # Disable some items if there is no structure
        if self.structure is None or len(self.structure) == 0:
            menu.Enable(self.deleteID, False);
            menu.Enable(self.supercellID, False);
            menu.Enable(self.spaceGroupID, False);

        # Check for copy/paste
        if not canCopySelectedCells(self):
            menu.Enable(self.copyID, False)
        if not canPasteIntoCells(self):
            menu.Enable(self.pasteID, False)

        # Popup the menu.  If an item is selected then its handler
        # will be called before PopupMenu returns.
        window.PopupMenu(menu, wx.Point(x,y))
        menu.Destroy()        
        return

    def onPopupInsert(self, event):
        """Adds rows to the grid."""
        if self.structure != None:
            dlg = InsertRowsDialog(self)
            if dlg.ShowModal() == wx.ID_OK:
                rows = dlg.spin_ctrl_Rows.GetValue()
                
                if len(self.structure) == 0:
                    self._row = 0
                elif (dlg.radio_box_where.GetSelection() == 1): # if selected "below"
                    self._row += 1
    
                # insert "rows" atoms into the structure
                atoms = []
                for i in xrange(rows):
                    atoms.append(Atom("",[0.0,0.0,0.0]))
                self.structure.insertAtoms(self._row, atoms)
                self.refresh()
                self.mainFrame.needsSave()
    
            dlg.Destroy()        
        return

    def onPopupDelete(self, event):
        """Deletes the row under mouse pointer from the grid."""
        if self.structure != None:
            indices = getSelectedAtoms(self)
            self.structure.deleteAtoms(indices)
            self.refresh()
            self.mainFrame.needsSave()
        return

    def onPopupCopy(self, event):
        """Copy selected cells."""
        copySelectedCells(self)
        return

    def onPopupPaste(self, event):
        """Paste previously copied cells."""
        pasteIntoCells(self)
        return

    def onPopupSupercell(self, event):
        """Create a supercell with the supercell dialog."""
        if self.structure != None:
            dlg = SupercellDialog(self)
            if dlg.ShowModal() == wx.ID_OK:
                mno = dlg.getMNO()
                self.structure.expandSuperCell(mno)
                self.refresh()
                self.mainFrame.needsSave()
            dlg.Destroy()
        return

    def onPopupSpaceGroup(self, event):
        """Create a supercell with the supercell dialog."""
        if self.structure != None:

            indices = getSelectedAtoms(self)
            dlg = SGStructureDialog(self)
            dlg.mainFrame = self.mainFrame
            dlg.indices = indices
            dlg.setStructure(self.structure)
            if dlg.ShowModal() == wx.ID_OK:
                spcgrp = dlg.getSpaceGroup()
                offset = dlg.getOffset()
                self.structure.expandAsymmetricUnit(spcgrp, indices, offset)
                self.refresh()
                self.mainFrame.needsSave()
            dlg.Destroy()
        return

# end of class PhaseConfigurePanel
