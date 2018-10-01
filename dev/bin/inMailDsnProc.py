#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""\
* TODO *[Summary]* :: An =ICM=: Process Incoming DSN (Delivery Status Notifications)
"""

####+BEGIN: bx:icm:python:top-of-file :partof "bystar" :copyleft "halaal+minimal"
"""
*  This file:/acct/smb/com/dev-py/LUE/Sync/pypi/pkgs/unisos/marme/dev/bin/inMailDsnProc.py :: [[elisp:(org-cycle)][| ]]
 is part of The Libre-Halaal ByStar Digital Ecosystem. http://www.by-star.net
 *CopyLeft*  This Software is a Libre-Halaal Poly-Existential. See http://www.freeprotocols.org
 A Python Interactively Command Module (PyICM). Part Of ByStar.
 Best Developed With COMEEGA-Emacs And Best Used With Blee-ICM-Players.
 Warning: All edits wityhin Dynamic Blocks may be lost.
"""
####+END:

"""
*  [[elisp:(org-cycle)][| *ICM-INFO:* |]] :: Author, Copyleft and Version Information
"""
####+BEGIN: bx:icm:python:name :style "fileName"
__icmName__ = "inMailDsnProc"
####+END:

####+BEGIN: bx:global:timestamp:version-py :style "date"
__version__ = "201805293523"
####+END:

####+BEGIN: bx:global:icm:status-py :status "Production"
__status__ = "Production"
####+END:

__credits__ = [""]

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/libre/ByStar/InitialTemplates/update/sw/icm/py/icmInfo-mbNedaGpl.py"
icmInfo = {
    'authors':         ["[[http://mohsen.1.banan.byname.net][Mohsen Banan]]"],
    'copyright':       "Copyright 2017, [[http://www.neda.com][Neda Communications, Inc.]]",
    'licenses':        ["[[https://www.gnu.org/licenses/agpl-3.0.en.html][Affero GPL]]", "Libre-Halaal Services License", "Neda Commercial License"],
    'maintainers':     ["[[http://mohsen.1.banan.byname.net][Mohsen Banan]]",],
    'contacts':        ["[[http://mohsen.1.banan.byname.net/contact]]",],
    'partOf':          ["[[http://www.by-star.net][Libre-Halaal ByStar Digital Ecosystem]]",]
}
####+END:

####+BEGIN: bx:icm:python:topControls :partof "bystar" :copyleft "halaal+minimal"
"""
*  [[elisp:(org-cycle)][|/Controls/| ]] :: [[elisp:(org-show-subtree)][|=]]  [[elisp:(show-all)][Show-All]]  [[elisp:(org-shifttab)][Overview]]  [[elisp:(progn (org-shifttab) (org-content))][Content]] | [[file:Panel.org][Panel]] | [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] | [[elisp:(bx:org:run-me)][Run]] | [[elisp:(bx:org:run-me-eml)][RunEml]] | [[elisp:(delete-other-windows)][(1)]] | [[elisp:(progn (save-buffer) (kill-buffer))][S&Q]]  [[elisp:(save-buffer)][Save]]  [[elisp:(kill-buffer)][Quit]] [[elisp:(org-cycle)][| ]]
** /Version Control/ ::  [[elisp:(call-interactively (quote cvs-update))][cvs-update]]  [[elisp:(vc-update)][vc-update]] | [[elisp:(bx:org:agenda:this-file-otherWin)][Agenda-List]]  [[elisp:(bx:org:todo:this-file-otherWin)][ToDo-List]]
"""
####+END:

####+BEGIN: bx:icm:python:section :title "ContentsList"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *ContentsList*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:icm:python:icmItem :itemType "=Imports=" :itemTitle "*IMPORTS*"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || =Imports=      :: *IMPORTS*  [[elisp:(org-cycle)][| ]]
"""
####+END:

import sys
import os

import collections

from unisos import ucf
from unisos import icm

from blee.icmPlayer import bleep

from bisos.currents import bxCurrentsConfig

from unisos.x822Msg import msgOut
#from bxMsg import msgIn
#from bxMsg import msgLib

from unisos.marme import marmeAcctsLib
from unisos.marme import marmeSendLib
from unisos.marme import marmeTrackingLib

import re

import email
import mailbox

import flufl.bounce

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.MIMEBase import MIMEBase


g_importedCmnds = {        # Enumerate modules from which CMNDs become invokable
    'bleep': bleep.__file__,
    'marmeAcctsLib': marmeAcctsLib.__file__,    
}


####+BEGIN: bx:icm:python:section :title "= =Framework::= ICM  Description (Overview) ="
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *= =Framework::= ICM  Description (Overview) =*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:


####+BEGIN: bx:icm:python:cmnd:classHead :modPrefix "new" :cmndName "icmOverview" :parsMand "" :parsOpt "" :argsMin "0" :argsMax "3" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || ICM-Cmnd       :: /icmOverview/ parsMand= parsOpt= argsMin=0 argsMax=3 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class icmOverview(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 3,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        argsList=[],         # or Args-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome
            effectiveArgsList = G.icmRunArgsGet().cmndArgs
        else:
            effectiveArgsList = argsList

        callParamsDict = {}
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome

        cmndArgsSpecDict = self.cmndArgsSpec()
        if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
            return cmndOutcome
####+END:

        moduleDescription="""
*       [[elisp:(org-show-subtree)][|=]]  [[elisp:(org-cycle)][| *Description:* | ]]
**  [[elisp:(org-cycle)][| ]]  [Xref]          :: *[Related/Xrefs:]*  <<Xref-Here->>  -- External Documents  [[elisp:(org-cycle)][| ]]

**  [[elisp:(org-cycle)][| ]]	Model and Terminology 					   :Overview:
*** See BISOS Documentation for ICM's model and terminology
**      [End-Of-Description]
"""
        
        moduleUsage="""
*       [[elisp:(org-show-subtree)][|=]]  [[elisp:(org-cycle)][| *Usage:* | ]]

**      How-Tos:
*** TODO Edit icmInfo to identify author, etc
*** TODO Select ICM type in g_icmChars
*** TODO Enhance g_argsExtraSpecify for your parameters
*** TODO Add your Commands
*** TODO Enhance Examples Cmnd
**      [End-Of-Usage]
"""
        
        moduleStatus="""
*       [[elisp:(org-show-subtree)][|=]]  [[elisp:(org-cycle)][| *Status:* | ]]
**  [[elisp:(org-cycle)][| ]]  [Info]          :: *[Current-Info:]* Status/Maintenance -- General TODO List [[elisp:(org-cycle)][| ]]
** TODO [[elisp:(org-cycle)][| ]]  Current         :: Just getting started [[elisp:(org-cycle)][| ]]
**      [End-Of-Status]
"""

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/libre/ByStar/InitialTemplates/update/sw/icm/py/moduleOverview.py"
        icm.unusedSuppressForEval(moduleUsage, moduleStatus)
        actions = self.cmndArgsGet("0&2", cmndArgsSpecDict, effectiveArgsList)
        if actions[0] == "all":
            cmndArgsSpec = cmndArgsSpecDict.argPositionFind("0&2")
            argChoices = cmndArgsSpec.argChoicesGet()
            argChoices.pop(0)
            actions = argChoices
        for each in actions:
            print each
            if interactive:
                #print( str( __doc__ ) )  # This is the Summary: from the top doc-string
                #version(interactive=True)
                exec("""print({})""".format(each))
                
        return(format(str(__doc__)+moduleDescription))

    """
**  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Method-anyOrNone :: /cmndArgsSpec/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self):
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = icm.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0&2",
            argName="actions",
            argDefault='all',
            argChoices=['all', 'moduleDescription', 'moduleUsage', 'moduleStatus'],
            argDescription="Output relevant information",
        )

        return cmndArgsSpecDict
####+END:

####+BEGIN: bx:icm:python:section :title "Common Module Support Facilities (BxoIdSr)"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Common Module Support Facilities (BxoIdSr)*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:dblock:global:file-insert :file "/libre/ByStar/InitialTemplates/update/sw/icm/py/curGetBxOSr.py"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-BxoIdSr   :: /curGet_{bxoId,sr}/ retType=str argsList=nil  [[elisp:(org-cycle)][| ]]
"""

def curGet_bxoId(): return bxCurrentsConfig.bxoId_fpObtain(configBaseDir=None)
def curGet_sr(): return bxCurrentsConfig.sr_fpObtain(configBaseDir=None)
def cmndParsCurBxoSr(cps): cps['bxoId'] = curGet_bxoId(); cps['sr'] = curGet_sr()

####+END:


####+BEGIN: bx:icm:python:section :title "= =Framework::= ICM Hooks ="
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *= =Framework::= ICM Hooks =*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:icm:python:func :funcName "g_icmChars" :comment "ICM Characteristics Spec" :funcType "FrameWrk" :retType "Void" :deco "" :argsList ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-FrameWrk  :: /g_icmChars/ =ICM Characteristics Spec= retType=Void argsList=nil  [[elisp:(org-cycle)][| ]]
"""
def g_icmChars():
####+END:
    icmInfo['panel'] = "{}-Panel.org".format(__icmName__)
    icmInfo['groupingType'] = "IcmGroupingType-pkged"
    icmInfo['cmndParts'] = "IcmCmndParts[common] IcmCmndParts[param]"
    
g_icmChars()


####+BEGIN: bx:icm:python:func :funcName "g_icmPreCmnds" :funcType "FrameWrk" :retType "Void" :deco "default" :argsList ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-FrameWrk  :: /g_icmPreCmnds/ retType=Void argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
@icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def g_icmPreCmnds():
####+END:
    """ PreHook """
    pass


####+BEGIN: bx:icm:python:func :funcName "g_icmPostCmnds" :funcType "FrameWrk" :retType "Void" :deco "default" :argsList ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-FrameWrk  :: /g_icmPostCmnds/ retType=Void argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
@icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def g_icmPostCmnds():
####+END:
    """ PostHook """
    pass


####+BEGIN: bx:icm:python:section :title "= =Framework::= Options, Arguments and Examples Specifications ="
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *= =Framework::= Options, Arguments and Examples Specifications =*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:


####+BEGIN: bx:icm:python:func :funcName "g_argsExtraSpecify" :comment "FrameWrk: ArgsSpec" :funcType "FrameWrk" :retType "Void" :deco "" :argsList "parser"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-FrameWrk  :: /g_argsExtraSpecify/ =FrameWrk: ArgsSpec= retType=Void argsList=(parser)  [[elisp:(org-cycle)][| ]]
"""
def g_argsExtraSpecify(
    parser,
):
####+END:
    """Module Specific Command Line Parameters.
    g_argsExtraSpecify is passed to G_main and is executed before argsSetup (can not be decorated)
    """
    G = icm.IcmGlobalContext()
    icmParams = icm.ICM_ParamDict()

    icmParams.parDictAdd(
        parName='moduleVersion',
        parDescription="Module Version",
        parDataType=None,
        parDefault=None,
        parChoices=list(),
        parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--version',
    )

    icmParams.parDictAdd(
        parName='inFile',
        parDescription="Input File",
        parDataType=None,
        parDefault=None,
        parChoices=["someFile", "UserInput"],
        parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--inFile',
    )
    
    bleep.commonParamsSpecify(icmParams)
    marmeAcctsLib.commonParamsSpecify(icmParams)        
    
    icm.argsparseBasedOnIcmParams(parser, icmParams)

    # So that it can be processed later as well.
    G.icmParamDictSet(icmParams)
    
    return


####+BEGIN: bx:icm:python:cmnd:classHead :modPrefix "new" :cmndName "examples" :cmndType "ICM-Cmnd-FWrk"  :comment "FrameWrk: ICM Examples" :parsMand "" :parsOpt "" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || ICM-Cmnd-FWrk  :: /examples/ =FrameWrk: ICM Examples= parsMand= parsOpt= argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class examples(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome

        callParamsDict = {}
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome

####+END:
        def cpsInit(): return collections.OrderedDict()
        def menuItem(verbosity): icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity=verbosity) # 'little' or 'none'        
        def execLineEx(cmndStr): icm.ex_gExecMenuItem(execLine=cmndStr)

        logControler = icm.LOG_Control()
        logControler.loggerSetLevel(20)

        icm.icmExampleMyName(G.icmMyName(), G.icmMyFullName())
        
        icm.G_commonBriefExamples()    

        bleep.examples_icmBasic()

####+BEGIN: bx:icm:python:cmnd:subSection :title "Real Invokations"
        """
**  [[elisp:(beginning-of-buffer)][Top]] ================ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]          *Real Invokations*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

        icm.cmndExampleMenuChapter('*Real Invokations*')

        cmndName = "maildirApplyToMsg"        
        cmndArgs = "dsnProcessAndRefile"
        cps = collections.OrderedDict(); cmndParsCurBxoSr(cps) # ; cps['runMode'] = 'dryRun' COMMENTED-OUT
        icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, icmWrapper=None, verbosity='little')

        icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, icmWrapper="echo", verbosity='full')        

####+BEGIN: bx:icm:python:cmnd:subSection :title "Examples   ::  Testing -- /DryRun/ -- devTest -- Maildir Apply To Message Processor"
        """
**  [[elisp:(beginning-of-buffer)][Top]] ================ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]          *Examples   ::  Testing -- /DryRun/ -- devTest -- Maildir Apply To Message Processor*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:
        
        icm.cmndExampleMenuChapter('*Testing -- /DryRun/ -- devTest -- Maildir Apply To Message Processor*')

        # menuLine = """--runMode dryRun --inMailAcct={inMailAcct} --inMbox={inMbox} {cmndAction} {cmndArgs}""".format(
        #    inMailAcct=inMailAcct, inMbox=inMbox, cmndAction=cmndAction, cmndArgs=cmndArgs)

        cmndName = "maildirApplyToMsg"        
        cmndArgs = "msgDisect"
        cps = collections.OrderedDict(); cmndParsCurBxoSr(cps) ; #cps['controlProfile'] = enabledControlProfile ; cps['inMailAcct'] = enabledMailAcct
        icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, icmWrapper=None, verbosity='little')

        cmndName = "maildirApplyToMsg"        
        cmndArgs = "dsnReportLong"
        cps = collections.OrderedDict(); cmndParsCurBxoSr(cps) ; #cps['controlProfile'] = enabledControlProfile ; cps['inMailAcct'] = enabledMailAcct
        icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, icmWrapper=None, verbosity='little')

        cmndName = "maildirApplyToMsg"        
        cmndArgs = "dsnProcessAndRefile"
        cps = collections.OrderedDict(); cmndParsCurBxoSr(cps) ; cps['runMode'] = 'dryRun'
        icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, icmWrapper=None, verbosity='little')
        
        cmndName = "maildirApplyToMsg"        
        cmndArgs = "dsnTestSendToCoRecipients"
        cps = collections.OrderedDict(); cmndParsCurBxoSr(cps) ; cps['runMode'] = 'dryRun'
        icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, icmWrapper=None, verbosity='little')

        cmndName = "maildirApplyToMsg"        
        cmndArgs = "dsnTestSendToCoRecipients"
        cps = collections.OrderedDict(); cmndParsCurBxoSr(cps) ; cps['runMode'] = 'runDebug'
        icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, icmWrapper=None, verbosity='little')

        cmndName = "maildirApplyToMsg"        
        cmndArgs = "dsnTestSendToCoRecipients"
        cps = collections.OrderedDict(); cmndParsCurBxoSr(cps) ; cps['runMode'] = 'fullRun'
        icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, icmWrapper=None, verbosity='little')
        
####+BEGIN: bx:icm:python:cmnd:subSection :title "From  marmeAcctsLib.py"
        """
**  [[elisp:(beginning-of-buffer)][Top]] ================ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]          *From  marmeAcctsLib.py*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

        marmeAcctsLib.examples_controlProfileManage()

        #marmeAcctsLib.examples_marmeAcctsLibControls()

        marmeAcctsLib.examples_select_mailBox()        

        marmeAcctsLib.examples_inMailAcctAccessPars()

        marmeAcctsLib.examples_outMailAcctAccessPars()        
        


####+BEGIN: bx:icm:python:section :title "ICM Commands"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *ICM Commands*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "maildirApplyToMsg" :comment "" :parsMand "" :parsOpt "bxoId sr controlProfile inMailAcct inMbox" :argsMin "1" :argsMax "1000" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || ICM-Cmnd       :: /maildirApplyToMsg/ parsMand= parsOpt=bxoId sr controlProfile inMailAcct inMbox argsMin=1 argsMax=1000 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class maildirApplyToMsg(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'bxoId', 'sr', 'controlProfile', 'inMailAcct', 'inMbox', ]
    cmndArgsLen = {'Min': 1, 'Max': 1000,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        bxoId=None,         # or Cmnd-Input
        sr=None,         # or Cmnd-Input
        controlProfile=None,         # or Cmnd-Input
        inMailAcct=None,         # or Cmnd-Input
        inMbox=None,         # or Cmnd-Input
        argsList=[],         # or Args-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome
            effectiveArgsList = G.icmRunArgsGet().cmndArgs
        else:
            effectiveArgsList = argsList

        callParamsDict = {'bxoId': bxoId, 'sr': sr, 'controlProfile': controlProfile, 'inMailAcct': inMailAcct, 'inMbox': inMbox, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        bxoId = callParamsDict['bxoId']
        sr = callParamsDict['sr']
        controlProfile = callParamsDict['controlProfile']
        inMailAcct = callParamsDict['inMailAcct']
        inMbox = callParamsDict['inMbox']

        cmndArgsSpecDict = self.cmndArgsSpec()
        if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
            return cmndOutcome
####+END:
        #cmndArgsSpec = {0: ['msgDisect', 'coRecepientNdr']}
        
        cmndArgs = self.cmndArgsGet("0&-1", cmndArgsSpecDict, effectiveArgsList)
        
        inMailDir = marmeAcctsLib.getPathForAcctMbox(
            controlProfile,
            inMailAcct,
            inMbox,
            bxoId=bxoId,
            sr=sr,
        )

        icm.LOG_here(inMailDir)

        mbox = mailbox.Maildir(
            inMailDir,
            factory=None,  # important!! default does not work
        )

        for msgProc in cmndArgs:            
            
            #icm.ANN_here("thisArg={thisArg}".format(thisArg=msgProc))

            #for msg in mbox:
            for key in mbox.iterkeys():
                try:
                    msg = mbox[key]
                except email.errors.MessageParseError:
                    icm.EH_problem_info(msg)
                    continue                # The message is malformed. Just leave it.
            
                try:
                    eval(msgProc + '(inMailDir, mbox, key, msg)')
                except Exception as e:
                    icm.EH_critical_exception(e)
                    icm.EH_problem_info("Invalid Action: {msgProc}"
                                        .format(msgProc=msgProc))            
                    raise   # NOTYET, in production, the raise should be commented out
        
        return cmndOutcome.set(
            opError=icm.OpError.Success,
            opResults=None,
        )

####+BEGIN: bx:icm:python:method :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Method-anyOrNone :: /cmndArgsSpec/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self):
####+END:        
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = icm.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0&-1",
            argName="cmndArgs",
            argDefault=None,
            argChoices=['msgDisect', 'coRecepientNdr'],
            argDescription="Rest of args for use by action"
        )

        return cmndArgsSpecDict
    

####+BEGIN: bx:icm:python:method :methodName "cmndDocStr" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Method-anyOrNone :: /cmndDocStr/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndDocStr(self):
####+END:        
        return """
***** TODO [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Place holder for this commands doc string.
"""


"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Msg-Apply    ::  msgDisect    [[elisp:(org-cycle)][| ]]
"""

@icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def msgDisect(
        maildir,
        mbox,
        key,
        inMsg,
):
    """ """
    for part in inMsg.walk():
        print part.get_content_type()

    return


"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Msg-Apply    ::  dsnReportLong    [[elisp:(org-cycle)][| ]]
"""
@icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def dsnReportLong(
        maildir,        
        mbox,
        key,
        inMsg,
):
    """ """
    tempFailedRecipients, permFailedRecipients = flufl.bounce.all_failures(inMsg)

    failedMsg = fromNonDeliveryReportGetFailedMsg(
        inMsg,
        tempFailedRecipients,
        permFailedRecipients,
    )

    coRecipients = fromFailedMsgGetCoRecipients(
        failedMsg,
        tempFailedRecipients,
        permFailedRecipients,
    )

    dsnType = msgDsnTypeDetect(
        inMsg,
        failedMsg,
        tempFailedRecipients,
        permFailedRecipients,
        coRecipients,
    )

    dsnTypeReports(inMsg, dsnType, "long")

    
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Msg-Apply    ::  dsnTestSendToCoRecipients    [[elisp:(org-cycle)][| ]]
"""
@icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def dsnTestSendToCoRecipients(
        maildir,        
        mbox,
        key,
        inMsg,
):
    """ 
** inMsg is analyzed to see if it contains a bounce. based on that it is catgorized as one of the following:
"""
    dsnProcessAndRefileWithGivenActions(
        maildir,        
        mbox,
        key,
        inMsg,
        action_deliveryReport=None,
        action_receiptNotification=None,
        action_ndrNoCoRecipients=None,
        action_ndrWithCoRecipients=msgSend_test_permanentNdrToCoRecipients,
        action_tmpNonDeliveryReport=None,
        action_notADsn=None,
    )
      


"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Msg-Apply    ::  dsnProcessAndRefile    [[elisp:(org-cycle)][| ]]
"""
@icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def dsnProcessAndRefile(
    maildir,        
    mbox,
    key,
    inMsg,
):
    """ 
** inMsg is analyzed to see if it contains a bounce. based on that it is catgorized as one of the following:
"""
    dsnProcessAndRefileWithGivenActions(
        maildir,        
        mbox,
        key,
        inMsg,
        action_deliveryReport=None,
        action_receiptNotification=None,
        action_ndrNoCoRecipients=None,
        action_ndrWithCoRecipients=msgSend_test_permanentNdrToCoRecipients,
        action_tmpNonDeliveryReport=None,
        action_notADsn=None,
    )

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  dsnProcessAndRefileWithGivenActions    [[elisp:(org-cycle)][| ]]
"""
@icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def dsnProcessAndRefileWithGivenActions(
        maildir,        
        mbox,
        key,
        inMsg,
        action_deliveryReport=None,
        action_receiptNotification=None,
        action_ndrNoCoRecipients=None,
        action_ndrWithCoRecipients=None,
        action_tmpNonDeliveryReport=None,
        action_notADsn=None,
):
    """ 
** inMsg is analyzed to see if it contains a bounce. based on that it is catgorized as one of the following:
*** envNotADsn: If it is not a Delivery Status Notification (DSN) it is filed 
*** envTmpNdr:  A temporary Non-Delivery Report (NDR)
*** envNdrNoCoRecip:  A permanent Non-Delivery Report without any co-recipients
*** envNdrWithCoRecipNotified: A permanent NDR with co-recipients that were notified
*** envNdrWithCoRecip: A permanent NDR with co-recipients that were not notified
*** envDr:  A Delivery Report
*** envRn: A Recipt Notification
"""
    G = icm.IcmGlobalContext()
    runMode = G.icmRunArgsGet().runMode
    
    tempFailedRecipients, permFailedRecipients = flufl.bounce.all_failures(inMsg)

    failedMsg = fromNonDeliveryReportGetFailedMsg(
        inMsg,
        tempFailedRecipients,
        permFailedRecipients,
    )

    coRecipients = fromFailedMsgGetCoRecipients(
        failedMsg,
        tempFailedRecipients,
        permFailedRecipients,
    )

    dsnType = msgDsnTypeDetect(
        inMsg,
        failedMsg,
        tempFailedRecipients,
        permFailedRecipients,
        coRecipients,
    )

    dsnTypeReports(inMsg, dsnType, "short")

    
    if dsnType == DsnType.deliveryReport:
        if action_deliveryReport:
            action_deliveryReport(
                inMsg,
                failedMsg,
                tempFailedRecipients,
                permFailedRecipients,
                coRecipients,
                dsnType,
            )
      
    elif dsnType == DsnType.receiptNotification:
        if action_receiptNotification:
            action_receiptNotification(
                inMsg,
                failedMsg,
                tempFailedRecipients,
                permFailedRecipients,
                coRecipients,
                dsnType,
            )
    
    elif dsnType == DsnType.ndrNoCoRecipients:
        if runMode == 'dryRun':
            pass
        elif runMode == 'runDebug':
            pass
        elif  runMode == 'fullRun':
            if action_ndrNoCoRecipients:
                action_ndrNoCoRecipients(
                    inMsg,
                    failedMsg,
                    tempFailedRecipients,
                    permFailedRecipients,
                    coRecipients,
                    dsnType,
                )

            msgMoveToFolder("envNdrNoCoRecip", maildir, mbox, key, inMsg,)
            marmeTrackingLib.trackEnvPermNdr(inMsg)
        else:
            icm.EH_critical_oops()

        
    elif dsnType == DsnType.ndrWithCoRecipients:
        if runMode == 'dryRun':
            pass
        elif runMode == 'runDebug':
            if action_ndrWithCoRecipients:
                action_ndrWithCoRecipients(
                    inMsg,
                    failedMsg,
                    tempFailedRecipients,
                    permFailedRecipients,
                    coRecipients,
                    dsnType,
                )
        elif  runMode == 'fullRun':
            if action_ndrWithCoRecipients:
                action_ndrWithCoRecipients(
                    inMsg,
                    failedMsg,
                    tempFailedRecipients,
                    permFailedRecipients,
                    coRecipients,
                    dsnType,
                )
            msgMoveToFolder("envNdrWithCoRecipNotified", maildir, mbox, key, inMsg,)            
            marmeTrackingLib.trackSentCoRecipient(inMsg)

        else:
            icm.EH_critical_oops()

    elif dsnType == DsnType.tmpNonDeliveryReport:
        if runMode == 'dryRun':
            pass
        elif runMode == 'runDebug':
            if action_tmpNonDeliveryReport:
                action_tmpNonDeliveryReport(
                    inMsg,
                    failedMsg,
                    tempFailedRecipients,
                    permFailedRecipients,
                    coRecipients,
                    dsnType,
                )
        elif  runMode == 'fullRun':
            if action_tmpNonDeliveryReport:
                action_tmpNonDeliveryReport(
                    inMsg,
                    failedMsg,
                    tempFailedRecipients,
                    permFailedRecipients,
                    coRecipients,
                    dsnType,
                )
            msgMoveToFolder("envTmpNdr", maildir, mbox, key, inMsg,)
            marmeTrackingLib.trackEnvTmpNdr(inMsg)

        else:
            icm.EH_critical_oops()
            
        
    elif dsnType == DsnType.notADsn:
        if runMode == 'dryRun':
            pass
        elif runMode == 'runDebug':
            if action_notADsn:
                action_notADsn(
                    inMsg,
                    failedMsg,
                    tempFailedRecipients,
                    permFailedRecipients,
                    coRecipients,
                    dsnType,
                )
        elif  runMode == 'fullRun':
            if action_notADsn:
                action_notADsn(
                    inMsg,
                    failedMsg,
                    tempFailedRecipients,
                    permFailedRecipients,
                    coRecipients,
                    dsnType,
                )
            msgMoveToFolder("envNotADsn", maildir, mbox, key, inMsg,)

    else:
        icm.EH_critical_oops()
        


"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(delete-other-windows)][(1)]]      *DSN (Delivery Status Notification) Type Processors*
"""
        

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Enum         ::  DsnType    [[elisp:(org-cycle)][| ]]
"""
DsnType = ucf.Enum(
    deliveryReport='deliveryReport',
    receiptNotification='receiptNotification',
    ndrNoCoRecipients='ndrNoCoRecipients',
    ndrWithCoRecipients='ndrWithCoRecipients',
    tmpNonDeliveryReport='tmpNonDeliveryReport',
    notADsn='notADsn',
)


"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  msgDsnTypeDetect    [[elisp:(org-cycle)][| ]]
"""
@icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def msgDsnTypeDetect(
    inMsg,
    failedMsg,
    tempFailedRecipients,
    permFailedRecipients,
    coRecipients,        
):        
    """ 
** Returns a DsnType.
"""
    if tempFailedRecipients:
        return DsnType.tmpNonDeliveryReport
 
    elif permFailedRecipients:
        if coRecipients:
            return DsnType.ndrWithCoRecipients
        else:
            return DsnType.ndrNoCoRecipients

    # Delivery Report Needs To Be Detected

    # Receipt Notification Needs To Be Detected
    
    elif inMsg['subject'] == "Delivery delay notification":
        return DsnType.tmpNonDeliveryReport
        
    else:
        return DsnType.notADsn

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  dsnTypeShortReport    [[elisp:(org-cycle)][| ]]
"""
@icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def dsnTypeShortReport(
        inMsg,
        typeStr,
):
    icm.ANN_note("""{typeStr:15}:: {msgId}""".format(
        typeStr=typeStr, msgId=str(inMsg['message-id']),))

    
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  dsnTypeLongReport    [[elisp:(org-cycle)][| ]]
"""    
@icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def dsnTypeLongReport(
        inMsg,
        typeStr,
):
    icm.ANN_note("""{typeStr:20}:: {msgId} -- {date} -- {subject}""".format(
        typeStr=typeStr, msgId=str(inMsg['message-id']),
        date=str(inMsg['date']), subject=str(inMsg['subject']),
        ))
    

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  dsnTypeReports    [[elisp:(org-cycle)][| ]]
"""
@icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def dsnTypeReports(
    inMsg,
    dsnType,
    reportType,
):

    def dsnTypeStrReport(
            inMsg,
            typeStr,
            reportType,
    ):
        if reportType == "short":
            dsnTypeShortReport(inMsg, typeStr,)
        elif reportType == "long":
            dsnTypeLongReport(inMsg, typeStr,)
        else:
            icm.EH_critical_oops()

    if dsnType == DsnType.deliveryReport:
        dsnTypeStrReport(inMsg, "Delivery Report", reportType,)
        
    elif dsnType == DsnType.receiptNotification:
        dsnTypeStrReport(inMsg, "Receipt Notification", reportType,)
    
    elif dsnType == DsnType.ndrNoCoRecipients:
        dsnTypeStrReport(inMsg, "ndrNoCoRecipients", reportType,)

    elif dsnType == DsnType.ndrWithCoRecipients:
        dsnTypeStrReport(inMsg, "ndrWithCoRecipients", reportType,)
 
    elif dsnType == DsnType.tmpNonDeliveryReport:
        dsnTypeStrReport(inMsg, "tmpNonDeliveryReport", reportType,)        

    elif dsnType == DsnType.notADsn:
        dsnTypeStrReport(inMsg, "Not A DSN", reportType,)        

    else:
        icm.EH_critical_oops()



"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(delete-other-windows)][(1)]]      *Support Functions For MsgProcs*
"""

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  fromNonDeliveryReportGetFailedMsg    [[elisp:(org-cycle)][| ]]
"""
@icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def fromNonDeliveryReportGetFailedMsg(
    nonDeliveryReportMsg,        
    tempFailedRecipients,
    permFailedRecipients,
):
    """ 
** returns the extracted failed message from the non-delivery-report. Or None.
"""

    if not (tempFailedRecipients or permFailedRecipients):
        # This is NOT a nonDeliveryReport
        return None

    #
    # Get the failed message as an attachement
    # 
    for part in nonDeliveryReportMsg.walk():
        if part.get_content_type() == 'message/rfc822':
            failedMsgList = part.get_payload()
            if failedMsgList:
                #for failedMsg in failedMsgList:
                nuOfFailedMsgs = len(failedMsgList)
                if nuOfFailedMsgs != 1:
                    icm.EH_problem_info("More Then One -- Expected One")
                    return None
                else:
                    return failedMsgList[0]

    #
    # So,the failed message was not included and is part of the body.
    #
    
    #scre = re.compile(b'mail to the following recipients could not be delivered')
    scre = re.compile(b'-- The header and top 20 lines of the message follows --')

    msg = nonDeliveryReportMsg
    failedMsgStr = ""
    found = False
    for line in msg.get_payload(decode=True).splitlines():
        if scre.search(line):
            found = "gotIt"
            continue
        if found == "gotIt":  # This consumes an empty line
            found = True
            continue
        if found == True:
            failedMsgStr = failedMsgStr + line + '\n'

    if found:
        return email.message_from_string(failedMsgStr)
    else:
        return None

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  fromFailedMsgGetCoRecipients    [[elisp:(org-cycle)][| ]]
"""
@icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def fromFailedMsgGetCoRecipients(
    failedMsg,
    tempFailedRecipients,
    permFailedRecipients,
):
    """ 
** Return list of CoRecipients or None
"""
    if not (tempFailedRecipients or permFailedRecipients):
        # This is NOT a nonDeliveryReport
        return None

    if not failedMsg:
        icm.EH_critical_unassigedError("UnFound FailedMsg")
        return None
   
    allRecipients= None

    tos = failedMsg.get_all('to', [])
    ccs = failedMsg.get_all('cc', [])
    resent_tos = failedMsg.get_all('resent-to', [])
    resent_ccs = failedMsg.get_all('resent-cc', [])
    allRecipients = email.utils.getaddresses(tos + ccs + resent_tos + resent_ccs)
                
    if not allRecipients:
        icm.EH_problem_unassignedError("allRecipients is None")
        return None

    allRecipientsSet = set()
    for thisRecipient in allRecipients:
        allRecipientsSet.add(thisRecipient[1])

    failedRecipients = tempFailedRecipients | permFailedRecipients
        
    coRecipientsSet = allRecipientsSet - failedRecipients

    if coRecipientsSet:
        return coRecipientsSet
    else:
        return None


"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(delete-other-windows)][(1)]]      *Msg ReFiling*
"""
    

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  msgMoveToFolder    [[elisp:(org-cycle)][| ]]
"""
@icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def msgMoveToFolder(
        destFolder,
        srcMaildir,        
        srcMbox,
        srcKey,
        srcMsg,
):
    """ 
** Given a srcMbox and a srcMsg, move it to the specified  destination.
"""
    srcMailBase = os.path.dirname(srcMaildir)

    destMbox = mailbox.Maildir(
            os.path.join(srcMailBase, destFolder),
            factory=None,  # important!! default does not work
    )

    # Write copy to disk before removing original.
    # If there's a crash, you might duplicate a message, but
    # that's better than losing a message completely.
    destMbox.lock()
    destMbox.add(srcMsg)
    destMbox.flush()
    destMbox.unlock()

    # Remove original message
    srcMbox.lock()
    srcMbox.discard(srcKey)
    srcMbox.flush()
    srcMbox.unlock()

    destMbox.close()

    

"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(delete-other-windows)][(1)]]      *Msg Sending*
"""

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Msg-Send     ::  msgSend_test_permanentNdrToCoRecepiets    [[elisp:(org-cycle)][| ]]
"""
@icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def msgSend_test_permanentNdrToCoRecipients(
    inMsg,
    failedMsg,
    tempFailedRecipients,
    permFailedRecipients,
    coRecipients,
    dsnType,
):
    """ Given a nonDeliveryReportMsg, We focus on the failedMsg
    """

    testToLine = "test@mohsen.banan.1.byname.net"


    failedRecipients = tempFailedRecipients | permFailedRecipients

    failedFromLine = failedMsg['From']
    failedSubjectLine = failedMsg['Subject']
    failedDateLine = failedMsg['date']                                              

    msg = MIMEMultipart()    

    msg['Date'] = email.utils.formatdate(localtime = 1)
    msg['Message-ID'] = email.utils.make_msgid()
    
    msg['Subject'] = """Co-Recipient Non-Delivery-Report  -- Was: {failedSubjectLine}""".format(
        failedSubjectLine=failedSubjectLine)

    msg['From'] = failedFromLine

    toLine = ""
    
    for thisRecipient in coRecipients:
        if toLine:
            toLine = toLine + ', ' + thisRecipient
        else:
            toLine = thisRecipient            

    msg['To'] = testToLine
        
    
    msg.preamble = 'Multipart massage.\n'

    #pp = pprint.PrettyPrinter(indent=4)

    mailBodyStr = """\

Real To Line: {toLine}

A previous message 
    Dated: {failedDateLine}
    To: {failedRecipients} 
for which you were also a recipient, failed. 

This is to let you know that we have received a non-delivery-report (bounce message)
for that email and since you were also a recepient of that email, we are letting you 
know that {failedRecipients} did not recieve that email.

A full copy of the non-delivery-report that we received is attached.

This is a machine generated email and is purely informational.


    """.format(
        failedDateLine=failedDateLine,
        toLine=toLine,
        failedRecipients=" ".join(failedRecipients),
    )

    part = MIMEText(mailBodyStr)
    msg.attach(part)

    part = MIMEBase('message', "rfc822")
    part.set_payload(inMsg.as_string())
    #Encoders.encode_base64(part)

    msg.attach(part)

    sendingMethod = msgOut.SendingMethod.submit
        
    if msgOut.sendingMethodSet(msg, sendingMethod).isProblematic():
        return icm.EH_badLastOutcome()

    if not marmeSendLib.bx822Set_sendWithEnabledAcct(msg, sendingMethod):
        return icm.EH_problem_info("")

    cmndOutcome = marmeSendLib.sendCompleteMessage().cmnd(
        interactive=False,
        msg=msg,
    )

    return cmndOutcome




"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Msg-Send     ::  msgSend_permanentNdrToCoRecepiets    [[elisp:(org-cycle)][| ]]
"""
@icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def msgSend_permanentNdrToCoRecepietsObsoleted(
        failedRecipients,
        nonDeliveryReportMsg,
):
    """ Given a nonDeliveryReportMsg, We focus on the failedMsg
    """

 

    allRecipients= None

    failedMsgWasFound = False

    for part in nonDeliveryReportMsg.walk():
        if part.get_content_type() == 'message/rfc822':
            failedMsgList = part.get_payload()
            failedMsgWasFound = True
            for failedMsg in failedMsgList:
                tos = failedMsg.get_all('to', [])
                ccs = failedMsg.get_all('cc', [])
                resent_tos = failedMsg.get_all('resent-to', [])
                resent_ccs = failedMsg.get_all('resent-cc', [])
                allRecipients = email.utils.getaddresses(tos + ccs + resent_tos + resent_ccs)
                failedFromLine = failedMsg['From']
                failedSubjectLine = failedMsg['Subject']
                failedDateLine = failedMsg['date']                                              
                
            break

    if failedMsgWasFound is False:
        #icm.EH_problem_unassignedError("Failed Message Was UnFound")
        return

    if not allRecipients:
        icm.EH_problem_unassignedError("Failed Message Is Missing All Recipients")
        return

    allRecipientsSet = set()
    for thisRecipient in allRecipients:
        allRecipientsSet.add(thisRecipient[1])
 
    coRecipientsSet = allRecipientsSet - failedRecipients

    msg = MIMEMultipart()    

    msg['Date'] = email.utils.formatdate(localtime = 1)
    msg['Message-ID'] = email.utils.make_msgid()
    
    msg['Subject'] = """Co-Recipient Non-Delivery-Report  -- Was: {failedSubjectLine}""".format(
        failedSubjectLine=failedSubjectLine)

    msg['From'] = failedFromLine

    toLine = ""
    
    for thisRecipient in coRecipientsSet:
        if toLine:
            toLine = toLine + ', ' + thisRecipient
        else:
            toLine = thisRecipient            

    msg['To'] = "test@mohsen.banan.1.byname.net"
        
    
    msg.preamble = 'Multipart massage.\n'

    #pp = pprint.PrettyPrinter(indent=4)

    mailBodyStr = """\

Real To Line: {toLine}

A previous message 
    Dated: {failedDateLine}
    To: {failedRecipients} 
for which you were also a recipient, failed. 

This is to let you know that we have received a non-delivery-report (bounce message)
for that email and since you were also a recepient of that email, we are letting you 
know that {failedRecipients} did not recieve that email.

A full copy of the non-delivery-report that we received is attached.

This is a machine generated email and is purely informational.


    """.format(
        failedDateLine=failedDateLine,
        toLine=toLine,
        failedRecipients=" ".join(failedRecipients),
    )

    part = MIMEText(mailBodyStr)
    msg.attach(part)

    part = MIMEBase('message', "rfc822")
    part.set_payload(failedMsg.as_string())
    #Encoders.encode_base64(part)

    #part.add_header('Content-Disposition', 'attachment; filename="/etc/resolv.conf"')

    msg.attach(part)

    # msgSend_submitWith_byName_sa20000(
    #     msg=msg,
    #     envelopeAddr="test@mohsen.banan.1.byname.net",
    #     recipients=["test@mohsen.banan.1.byname.net"],
    # )

    return



    

####+BEGIN: bx:icm:python:section :title "Supporting Classes And Functions"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Supporting Classes And Functions*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:
"""
*       /Empty/  [[elisp:(org-cycle)][| ]]
"""
    
####+BEGIN: bx:icm:python:section :title "Common/Generic Facilities -- Library Candidates"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Common/Generic Facilities -- Library Candidates*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:
"""
*       /Empty/  [[elisp:(org-cycle)][| ]]
"""

    
####+BEGIN: bx:icm:python:section :title "= =Framework::=   G_main -- Instead Of ICM Dispatcher ="
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *= =Framework::=   G_main -- Instead Of ICM Dispatcher =*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:icm:python:func :funcName "G_main" :funcType "FrameWrk" :retType "Void" :deco "" :argsList ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-FrameWrk  :: /G_main/ retType=Void argsList=nil  [[elisp:(org-cycle)][| ]]
"""
def G_main():
####+END:
    """ 
** Replaces ICM dispatcher for other command line args parsings.
"""
    pass

####+BEGIN: bx:icm:python:icmItem :itemType "Configuration" :itemTitle "= =Framework::= g_ Settings -- ICMs Imports ="
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Configuration  :: = =Framework::= g_ Settings -- ICMs Imports =  [[elisp:(org-cycle)][| ]]
"""
####+END:


g_examples = examples  # or None 
g_mainEntry = None  # or G_main

####+BEGIN: bx:dblock:global:file-insert :file "/libre/ByStar/InitialTemplates/update/sw/icm/py/icm2.G_main.py"
"""
*  [[elisp:(beginning-of-buffer)][Top]] # /Dblk-Begin/ # [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *= =Framework::= ICM main() =*
"""

def classedCmndsDict():
    """
** Should be done here, can not be done in icm library because of the evals.
"""
    callDict = dict()
    for eachCmnd in icm.cmndList_mainsMethods().cmnd(
            interactive=False,
            importedCmnds=g_importedCmnds,
            mainFileName=__file__,
    ):
        try:
            callDict[eachCmnd] = eval("{}".format(eachCmnd))
            continue
        except NameError:
            pass

        for mod in g_importedCmnds:
            try:
                eval("{mod}.{cmnd}".format(mod=mod, cmnd=eachCmnd))
            except AttributeError:
                continue
            try:                
                callDict[eachCmnd] = eval("{mod}.{cmnd}".format(mod=mod, cmnd=eachCmnd))
                break
            except NameError:
                pass
    return callDict

icmInfo['icmName'] = __icmName__
icmInfo['version'] = __version__
icmInfo['status'] = __status__
icmInfo['credits'] = __credits__

G = icm.IcmGlobalContext()
G.icmInfo = icmInfo

def g_icmMain():
    """This ICM's specific information is passed to G_mainWithClass"""
    sys.exit(
        icm.G_mainWithClass(
            inArgv=sys.argv[1:],                 # Mandatory
            extraArgs=g_argsExtraSpecify,        # Mandatory
            G_examples=g_examples,               # Mandatory            
            classedCmndsDict=classedCmndsDict(),   # Mandatory
            mainEntry=g_mainEntry,
            g_icmPreCmnds=g_icmPreCmnds,
            g_icmPostCmnds=g_icmPostCmnds,
        )
    )

g_icmMain()

"""
*  [[elisp:(beginning-of-buffer)][Top]] ## /Dblk-End/ ## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *= =Framework::= ICM main() =*
"""

####+END:

####+BEGIN: bx:icm:python:section :title "Unused Facilities -- Temporary Junk Yard"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Unused Facilities -- Temporary Junk Yard*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:
"""
*       /Empty/  [[elisp:(org-cycle)][| ]]
"""

####+BEGIN: bx:icm:python:section :title "End Of Editable Text"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *End Of Editable Text*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/libre/ByStar/InitialTemplates/software/plusOrg/dblock/inserts/endOfFileControls.org"
#+STARTUP: showall
####+END:
