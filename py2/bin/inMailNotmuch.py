#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""\
* TODO *[Summary]* :: An =ICM=: Notmuch based user agent
"""

####+BEGIN: bx:icm:python:top-of-file :partof "bystar" :copyleft "halaal+minimal"
"""
*  This file:/acct/smb/com/dev-py/LUE/Sync/pypi/pkgs/unisos/marme/dev/bin/inMailUserAgent.py :: [[elisp:(org-cycle)][| ]]
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
__icmName__ = "inMailUserAgent"
####+END:

####+BEGIN: bx:global:timestamp:version-py :style "date"
__version__ = "201805293951"
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
import shutil

import collections

from unisos import ucf
from unisos import icm

from blee.icmPlayer import bleep

from bisos.currents import bxCurrentsConfig

from unisos.common import icmsPkgLib
from unisos.marme import marmeAcctsLib


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
** DONE [[elisp:(org-cycle)][| ]]  Current         :: [2018-05-30 Wed] BxoIdSr Updates Completed [[elisp:(org-cycle)][| ]]
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
    
    bleep.commonParamsSpecify(icmParams)    
    
    marmeAcctsLib.commonParamsSpecify(icmParams)
    
    icm.argsparseBasedOnIcmParams(parser, icmParams)

    # So that it can be processed later as well.
    G.icmParamDictSet(icmParams)
    
    return



####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "examples" :cmndType "ICM-Cmnd-FWrk"  :comment "FrameWrk: ICM Examples" :parsMand "" :parsOpt "" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
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
        def menuItem(verbosity): icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity=verbosity)
        def execLineEx(cmndStr): icm.ex_gExecMenuItem(execLine=cmndStr)

        logControler = icm.LOG_Control()
        logControler.loggerSetLevel(20)

        icm.icmExampleMyName(G.icmMyName(), G.icmMyFullName())
        
        icm.G_commonBriefExamples()    

        bleep.examples_icmBasic()

        defaultMailDom = marmeAcctsLib.enabledInMailAcctObtain(
            bxoId=curGet_bxoId(),
            sr=curGet_sr(),
        )
        
####+BEGIN: bx:icm:python:cmnd:subSection :title "Dev And Testing"
        """
**  [[elisp:(beginning-of-buffer)][Top]] ================ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]          *Dev And Testing*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:
        #icm.cmndExampleMenuChapter('*General Dev and Testing IIFs*')   

        icm.cmndExampleMenuChapter('*Config File Creation Facilities*')

        icm.cmndExampleMenuSection('*Automated Config File Creation Facilities*')           

        cmndName = "notmuchConfigUpdate" ; cmndArgs = ""
        cps=cpsInit(); cmndParsCurBxoSr(cps);
        menuItem(verbosity='none'); menuItem(verbosity='full')

        cmndName = "notmuchConfigStdout" ; cmndArgs = ""
        cps=cpsInit(); cmndParsCurBxoSr(cps);
        menuItem(verbosity='none'); menuItem(verbosity='full')

        configFile = withInMailDomGetNotmuchConfigPath(
            defaultMailDom,
            bxoId=curGet_bxoId(),
            sr=curGet_sr(),
        )
        
        icm.ANN_write(
            """ls -l {}""".format(configFile)
        )
        icm.ANN_write(
            """cat  {} """.format(configFile)
        )

        icm.cmndExampleMenuSection('*Interactive Config File Creation Facilities*')           

        cmndName = "runNotmuch" ; cmndArgs = "setup" ;
        cps=cpsInit() ;  cmndParsCurBxoSr(cps);
        icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='basic',
                             comment='# Creates/Edits notmuch-config', icmWrapper=None, icmName=None)
        
        icm.cmndExampleMenuSection('*Show/List Config Parameter Settings*')   

        cmndName = "runNotmuch" ; cmndArgs = "config list" ;
        cps=cpsInit() ;  cmndParsCurBxoSr(cps);
        icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='basic',
                             comment='# Shows Key aspects of notmuch-config', icmWrapper=None, icmName=None)
        

        icm.cmndExampleMenuChapter('*Run notmuch -- new, Search*')

        cmndName = "runNotmuch" ; cmndArgs = "new" ;
        cps=cpsInit() ;  cmndParsCurBxoSr(cps);
        icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='basic',
                             comment='# Refresh the index', icmWrapper=None, icmName=None)


        cmndName = "runNotmuch" ; cmndArgs = '''-- search --format=text --output=files "from:"''' ;
        cps=cpsInit() ;  cmndParsCurBxoSr(cps);
        icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='basic',
                             comment='# Search Based on from', icmWrapper=None, icmName=None)

        cmndName = "runNotmuch" ; cmndArgs = '''-- search --format=text --output=files "from:"''' ;
        cps=cpsInit() ;  cmndParsCurBxoSr(cps);
        icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='none',
                             comment='# Search Based on from', icmWrapper='echo', icmName=None)

        cmndName = "runNotmuch" ; cmndArgs = '''-- search "from:"''' ;
        cps=cpsInit() ;  cmndParsCurBxoSr(cps);
        icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='basic',
                             comment='# Search Based on from', icmWrapper=None, icmName=None)

        cmndName = "runNotmuch" ; cmndArgs = '''-- search "from:"''' ;
        cps=cpsInit() ;  cmndParsCurBxoSr(cps);
        icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='none',
                             comment='# Search Based on from', icmWrapper='echo', icmName=None)

        cmndName = "runNotmuch" ; cmndArgs = '''-- search --format=text --output=files "from:" | grep Inbox | xargs egrep "^Subject:"''' ;
        cps=cpsInit() ;  cmndParsCurBxoSr(cps);
        icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='basic',
                             comment='# Search Based on from', icmWrapper=None, icmName=None)

        cmndName = "runNotmuch" ; cmndArgs = '''-- search --format=text --output=files "from:" | grep Inbox | xargs egrep "^Subject:"''' ;
        cps=cpsInit() ;  cmndParsCurBxoSr(cps);
        icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='none',
                             comment='# Search Based on from', icmWrapper="echo", icmName=None)

        cmndName = "runNotmuch" ; cmndArgs = '''-- search --output=files "to: example.com"''' ;
        cps=cpsInit() ;  cmndParsCurBxoSr(cps);
        icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='none',
                             comment='# Search Based on from', icmWrapper="echo", icmName=None)

        marmeAcctsLib.examples_controlProfileManage()

        marmeAcctsLib.examples_enabledInMailAcctConfig()        

        marmeAcctsLib.examples_inMailAcctAccessPars()


####+BEGIN: bx:icm:python:section :title "ICM Commands"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *ICM Commands*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:icm:python:cmnd:classHead :modPrefix "new" :cmndName "unitTest" :parsMand "" :parsOpt "" :argsMin "0" :argsMax "1" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || ICM-Cmnd       :: /unitTest/ parsMand= parsOpt= argsMin=0 argsMax=1 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class unitTest(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 1,}

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

        myName=self.myName()
        thisOutcome = icm.OpOutcome(invokerName=myName)

        print G.icmInfo

        for eachArg in effectiveArgsList:
            icm.ANN_here("{}".format(eachArg))

        print (icm.__file__)
        print sys.path

        import imp
        print(imp.find_module('unisos/icm'))

        @ucf.runOnceOnly
        def echo(str):
            print str
            
        echo("first")
        echo("second")  # Should not run
    
        return thisOutcome
    
    def cmndDocStr(self): return """
** Place holder for ICM's experimental or test code.  [[elisp:(org-cycle)][| ]]
*** You can use this Cmnd for rapid prototyping and testing of newly developed functions.
"""


####+BEGIN: bx:icm:python:cmnd:classHead :modPrefix "new" :cmndName "notmuchConfigUpdate" :comment "" :parsMand "" :parsOpt "bxoId sr controlProfile inMailAcct" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || ICM-Cmnd       :: /notmuchConfigUpdate/ parsMand= parsOpt=bxoId sr controlProfile inMailAcct argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class notmuchConfigUpdate(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'bxoId', 'sr', 'controlProfile', 'inMailAcct', ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        bxoId=None,         # or Cmnd-Input
        sr=None,         # or Cmnd-Input
        controlProfile=None,         # or Cmnd-Input
        inMailAcct=None,         # or Cmnd-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome

        callParamsDict = {'bxoId': bxoId, 'sr': sr, 'controlProfile': controlProfile, 'inMailAcct': inMailAcct, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        bxoId = callParamsDict['bxoId']
        sr = callParamsDict['sr']
        controlProfile = callParamsDict['controlProfile']
        inMailAcct = callParamsDict['inMailAcct']

####+END:
        outcome = notmuchConfigStdout().cmnd(
            interactive=False,
            controlProfile=controlProfile,
            inMailAcct=inMailAcct,
            bxoId=bxoId,
            sr=sr,
        )
        if outcome.isProblematic(): return(icm.EH_badOutcome(outcome))

        configFileStr = outcome.stdout

        configFilePath = withInMailDomGetNotmuchConfigPath(
            inMailAcct,
            bxoId=bxoId,
            sr=sr,
        )

        rcFileFromControl = "{controlProfileBaseDir}/inMail/{inMailAcct}/conf/_notmuch-config".format(
            # ../control/inMail/example.com/conf/_notmuch-config
            controlProfileBaseDir=marmeAcctsLib.controlProfileBaseDirGet(
                controlProfile,
                bxoId=bxoId,
                sr=sr,
            ),
            inMailAcct=inMailAcct,
        )
        
        if os.path.isfile(rcFileFromControl):
            shutil.copyfile(rcFileFromControl, configFilePath)
        else:
            with open(configFilePath, "w") as thisFile:
                thisFile.write(configFileStr + '\n')

        if interactive:
            icm.ANN_here("configFilePath={val}".format(val=configFilePath))
        
        return cmndOutcome.set(
            opError=icm.OpError.Success,
            opResults=None,
        )

####+BEGIN: bx:icm:python:func :funcName "withInMailDomGetNotmuchConfigPath" :funcType "anyOrNone" :retType "bool" :deco "default" :argsList "inMailAcct bxoId=None sr=None"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /withInMailDomGetNotmuchConfigPath/ retType=bool argsList=(inMailAcct bxoId=None sr=None) deco=default  [[elisp:(org-cycle)][| ]]
"""
@icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def withInMailDomGetNotmuchConfigPath(
    inMailAcct,
    bxoId=None,
    sr=None,
):
####+END:
    inMailAcctConfBase = os.path.abspath(
        "{configBaseDir}/{inMailAcct}"
        .format(
            configBaseDir=marmeAcctsLib.configBaseDirGet(
                bxoId=bxoId,
                sr=sr,
            ),
            inMailAcct=inMailAcct,
        )
    )

    try: 
        os.makedirs(inMailAcctConfBase)
    except OSError:
        if not os.path.isdir(inMailAcctConfBase):
            raise

    filePath = os.path.join(
        inMailAcctConfBase,
        "_notmuch-config"
    )
    return filePath


####+BEGIN: bx:icm:python:cmnd:classHead :modPrefix "new" :cmndName "notmuchConfigStdout" :comment "" :parsMand "" :parsOpt "bxoId sr controlProfile inMailAcct" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || ICM-Cmnd       :: /notmuchConfigStdout/ parsMand= parsOpt=bxoId sr controlProfile inMailAcct argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class notmuchConfigStdout(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'bxoId', 'sr', 'controlProfile', 'inMailAcct', ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        bxoId=None,         # or Cmnd-Input
        sr=None,         # or Cmnd-Input
        controlProfile=None,         # or Cmnd-Input
        inMailAcct=None,         # or Cmnd-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome

        callParamsDict = {'bxoId': bxoId, 'sr': sr, 'controlProfile': controlProfile, 'inMailAcct': inMailAcct, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        bxoId = callParamsDict['bxoId']
        sr = callParamsDict['sr']
        controlProfile = callParamsDict['controlProfile']
        inMailAcct = callParamsDict['inMailAcct']

####+END:

        templateFile = os.path.join(
            marmeAcctsLib.inputsBaseDirGet(),
            "inputs",
            "notmuch/_notmuch-config.template",
        )

        outcome = icm.subProc_bash(
            """\
cat {templateFile} | \
	sed \
	    -e "s@%mailDirPath%@{mailDirPath}@g" \
	    -e "s@%firstName%@{firstName}@g" \
	    -e "s@%lastName%@{lastName}@g" 
"""
            .format(
                templateFile=templateFile,
                # ../var/inMail/example/maildir/Inbox
                mailDirPath=marmeAcctsLib.getPathForAcctMaildir(
                   controlProfile,
                    inMailAcct,
                    bxoId=bxoId,
                    sr=sr,
                ),
                firstName="FirstName",
                lastName="LastName",
            )
        ).log()
        if outcome.isProblematic(): return(icm.EH_badOutcome(outcome))

        if interactive:
            icm.ANN_write(outcome.stdout)
        
        return outcome.set(
            opError=icm.OpError.Success,
            #opResults=outcome.stdout
        )

####+BEGIN: bx:icm:python:cmnd:classHead :modPrefix "new" :cmndName "runNotmuch" :comment "" :parsMand "" :parsOpt "bxoId sr inMailAcct" :argsMin "0" :argsMax "1000" :asFunc "" :interactiveP ""    
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || ICM-Cmnd       :: /runNotmuch/ parsMand= parsOpt=bxoId sr inMailAcct argsMin=0 argsMax=1000 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class runNotmuch(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'bxoId', 'sr', 'inMailAcct', ]
    cmndArgsLen = {'Min': 0, 'Max': 1000,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        bxoId=None,         # or Cmnd-Input
        sr=None,         # or Cmnd-Input
        inMailAcct=None,         # or Cmnd-Input
        argsList=[],         # or Args-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome
            effectiveArgsList = G.icmRunArgsGet().cmndArgs
        else:
            effectiveArgsList = argsList

        callParamsDict = {'bxoId': bxoId, 'sr': sr, 'inMailAcct': inMailAcct, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        bxoId = callParamsDict['bxoId']
        sr = callParamsDict['sr']
        inMailAcct = callParamsDict['inMailAcct']

        cmndArgsSpecDict = self.cmndArgsSpec()
        if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
            return cmndOutcome
####+END:
        cmndArgs = self.cmndArgsGet("0&-1", cmndArgsSpecDict, effectiveArgsList)
        joinedArgs = ucf.str_joinedArgs(cmndArgs)        
        
        defaultMailDom = marmeAcctsLib.enabledInMailAcctObtain(
            bxoId=bxoId,
            sr=sr,
        )               
        configFile = withInMailDomGetNotmuchConfigPath(
            defaultMailDom,
            bxoId=bxoId,
            sr=sr,
        )
        
        outcome = icm.subProc_bash(
            """notmuch --config={configFile} {joinedArgs}"""
            .format(
                configFile=configFile,
                joinedArgs=joinedArgs,
            )
        ).out()
        if outcome.isProblematic(): return(icm.EH_badOutcome(outcome))

        if interactive:
            pass
        
        return outcome.set(
            opError=icm.OpError.Success,
            #opResults=outcome.stdout
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
            argChoices='any',
            argDescription="Rest of args for use by action"
        )
    
        return cmndArgsSpecDict
    
    

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
