#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""\
* *[Summary]* :: An =ICM=: Install dependencies of ICMs-Pkgs.
"""

####+BEGIN: bx:icm:python:top-of-file :partof "bystar" :copyleft "halaal+minimal"
"""
*  This file:/de/bx/nne/dev-py/pypi/pkgs/unisos/marme/dev/bin/pkgMarmeManage.py :: [[elisp:(org-cycle)][| ]]
** is part of The Libre-Halaal ByStar Digital Ecosystem. http://www.by-star.net
** *CopyLeft*  This Software is a Libre-Halaal Poly-Existential. See http://www.freeprotocols.org
** A Python Interactively Command Module (PyICM). Part Of ByStar.
** Best Developed With COMEEGA-Emacs And Best Used With Blee-ICM-Players.
** Warning: All edits wityhin Dynamic Blocks may be lost.
"""
####+END:

"""
*  [[elisp:(org-cycle)][| *ICM-INFO:* |]] :: Author, Copyleft and Version Information
"""
####+BEGIN: bx:icm:python:name :style "fileName"
__icmName__ = "pkgMarmeManage"
####+END:

####+BEGIN: bx:global:timestamp:version-py :style "date"
__version__ = "201712253350"
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
*  [[elisp:(org-cycle)][|/Controls/| ]] :: [[elisp:(org-show-subtree)][|=]] [[elisp:(show-all)][Show-All]]  [[elisp:(org-shifttab)][Overview]]  [[elisp:(progn (org-shifttab) (org-content))][Content]] | [[file:Panel.org][Panel]] | [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] | [[elisp:(bx:org:run-me)][Run]] | [[elisp:(bx:org:run-me-eml)][RunEml]] | [[elisp:(delete-other-windows)][(1)]] | [[elisp:(progn (save-buffer) (kill-buffer))][S&Q]]  [[elisp:(save-buffer)][Save]]  [[elisp:(kill-buffer)][Quit]] [[elisp:(org-cycle)][| ]]
** /Version Control/ ::  [[elisp:(call-interactively (quote cvs-update))][cvs-update]]  [[elisp:(vc-update)][vc-update]] | [[elisp:(bx:org:agenda:this-file-otherWin)][Agenda-List]]  [[elisp:(bx:org:todo:this-file-otherWin)][ToDo-List]]
"""
####+END:

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/libre/ByStar/InitialTemplates/software/plusOrg/dblock/inserts/pyWorkBench.org"
"""
* 
*  /Python Workbench/ ::  [[elisp:(org-cycle)][| ]]  [[elisp:(python-check (format "pyclbr %s" (bx:buf-fname))))][pyclbr]] || [[elisp:(python-check (format "pyflakes %s" (bx:buf-fname)))][pyflakes]] | [[elisp:(python-check (format "pychecker %s" (bx:buf-fname))))][pychecker (executes)]] | [[elisp:(python-check (format "pep8 %s" (bx:buf-fname))))][pep8]] | [[elisp:(python-check (format "flake8 %s" (bx:buf-fname))))][flake8]] | [[elisp:(python-check (format "pylint %s" (bx:buf-fname))))][pylint]]  [[elisp:(org-cycle)][| ]]
"""
####+END:

####+BEGIN: bx:icm:python:section :title "ContentsList"
"""

*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *ContentsList*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:icm:python:icmItem :itemType "=Imports=" :itemTitle "*IMPORTS*"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || =Imports=      :: *IMPORTS*  [[elisp:(org-cycle)][| ]]
"""
####+END:

import sys
import os

import platform
import collections

####+BEGIN: bx:dblock:global:file-insert :file "/libre/ByStar/InitialTemplates/update/sw/icm/py/importUcfIcmG.py"
from unisos import ucf
from unisos import icm

icm.unusedSuppressForEval(ucf.__file__)  # in case icm and ucf are not used

G = icm.IcmGlobalContext()
G.icmLibsAppend = __file__
G.icmCmndsLibsAppend = __file__

from blee.icmPlayer import bleep

####+END:

from  bisos.platform import bxPlatformThis
from  bisos.platform import bxPlatformConfig

from unisos.common import icmsPkgLib
from unisos.marme import marmePkgThis


g_importedCmnds = {        # Enumerate modules from which CMNDs become invokable
    'bleep': bleep.__file__,
    'bxPlatformConfig': bxPlatformConfig.__file__,    
    'icmsPkgLib': icmsPkgLib.__file__,
}


####+BEGIN: bx:icm:python:section :title "= =Framework::= ICM  Description (Overview) ="
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *= =Framework::= ICM  Description (Overview) =*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:


####+BEGIN: bx:icm:python:cmnd:classHead :modPrefix "new" :cmndName "icmOverview" :parsMand "" :parsOpt "" :argsMin "0" :argsMax "3" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || ICM-Cmnd       :: /icmOverview/ parsMand= parsOpt= argsMin=0 argsMax=3 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class icmOverview(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 3,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        argsList=None,         # or Args-Input
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
        cmndArgsSpec = {"0&-1": ['moduleDescription', 'moduleUsage', 'moduleStatus']}
        cmndArgsValid = cmndArgsSpec["0&-1"]
        icm.unusedSuppressForEval(moduleDescription, moduleUsage, moduleStatus)
        for each in effectiveArgsList:
            if each in cmndArgsValid:
                if interactive:
                    exec("""print({})""".format(each))
                
        return(format(str(__doc__)+moduleDescription))
####+END:


        
####+BEGIN: bx:icm:python:func :funcName "canon_pythonPkgsSpec" :funcType "anyOrNone" :retType "bool" :deco "" :argsList ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /canon_pythonPkgsSpec/ retType=bool argsList=nil  [[elisp:(org-cycle)][| ]]
"""
def canon_pythonPkgsSpec(
):
####+END:
    pkgs = collections.OrderedDict()
    pkgs["notmuch"] = None
    pkgs["flufl.bounce"] = "2.3"
    return pkgs

####+BEGIN: bx:icm:python:func :funcName "canon_linuxPkgsSpec" :funcType "anyOrNone" :retType "bool" :deco "" :argsList ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-anyOrNone :: /canon_linuxPkgsSpec/ retType=bool argsList=nil  [[elisp:(org-cycle)][| ]]
"""
def canon_linuxPkgsSpec(
):
####+END:
    pkgs = collections.OrderedDict()
    pkgs["offlineimap"] = None
    return pkgs


####+BEGIN: bx:icm:python:section :title "= =Framework::= ICM Hooks ="
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *= =Framework::= ICM Hooks =*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:icm:python:func :funcName "g_icmChars" :comment "ICM Characteristics Spec" :funcType "FrameWrk" :retType "Void" :deco "" :argsList ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-FrameWrk  :: /g_icmChars/ =ICM Characteristics Spec= retType=Void argsList=nil  [[elisp:(org-cycle)][| ]]
"""
def g_icmChars(
):
####+END:
    icmInfo['panel'] = "{}-Panel.org".format(__icmName__)
    icmInfo['groupingType'] = "IcmGroupingType-pkged"
    icmInfo['cmndParts'] = "IcmCmndParts[common] IcmCmndParts[param]"
    
g_icmChars()


####+BEGIN: bx:icm:python:func :funcName "g_icmPreCmnds" :funcType "FrameWrk" :retType "Void" :deco "default" :argsList ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-FrameWrk  :: /g_icmPreCmnds/ retType=Void argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
@icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def g_icmPreCmnds(
):
####+END:
    """ PreHook """
    pass


####+BEGIN: bx:icm:python:func :funcName "g_icmPostCmnds" :funcType "FrameWrk" :retType "Void" :deco "default" :argsList ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-FrameWrk  :: /g_icmPostCmnds/ retType=Void argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
@icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def g_icmPostCmnds(
):
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
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-FrameWrk  :: /g_argsExtraSpecify/ =FrameWrk: ArgsSpec= retType=Void argsList=(parser)  [[elisp:(org-cycle)][| ]]
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
   
    icmsPkgLib.commonParamsSpecify(icmParams)
       
    icm.argsparseBasedOnIcmParams(parser, icmParams)

    # So that it can be processed later as well.
    G.icmParamDictSet(icmParams)
    
    return


####+BEGIN: bx:icm:python:cmnd:classHead :modPrefix "new" :cmndName "examples" :cmndType "ICM-Cmnd-FWrk"  :comment "FrameWrk: ICM Examples" :parsMand "" :parsOpt "" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || ICM-Cmnd-FWrk  :: /examples/ =FrameWrk: ICM Examples= parsMand= parsOpt= argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
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
        def menuItem(): icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little')
        def execLineEx(cmndStr): icm.ex_gExecMenuItem(execLine=cmndStr)

        logControler = icm.LOG_Control()
        logControler.loggerSetLevel(20)

        icm.icmExampleMyName(G.icmMyName(), G.icmMyFullName())
        
        icm.G_commonBriefExamples()    

        bleep.examples_icmBasic()

        
####+BEGIN: bx:icm:python:cmnd:subSection :title "Dev And Testing"
        """
**  [[elisp:(beginning-of-buffer)][Top]] ================ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]          *Dev And Testing*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

        icm.cmndExampleMenuChapter('*General Dev and Testing IIFs*')

        cmndName = "unitTest"

        cmndArgs = "" 
        cps = cpsInit() ; # cps['icmsPkgName'] = icmsPkgName 
        icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little')
        icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='full')        
        
        icm.cmndExampleMenuChapter('*BinsPreps*')

        cmndAction = " -i binsPreps" ; cmndArgs = ""
        menuLine = """{cmndAction} {cmndArgs}""".format(cmndAction=cmndAction, cmndArgs=cmndArgs)
        icm.cmndExampleMenuItem(menuLine, verbosity='none')

        cmndAction = " -i binsPrepsCurInfo" ; cmndArgs = ""
        menuLine = """{cmndAction} {cmndArgs}""".format(cmndAction=cmndAction, cmndArgs=cmndArgs)
        icm.cmndExampleMenuItem(menuLine, verbosity='none')

        icm.cmndExampleMenuSection('*Install ICMs Needed Linux Packages*')
        
        cmndAction = " -i canon_linuxPkgInstall" ; cmndArgs = ""
        menuLine = """{cmndAction} {cmndArgs}""".format(cmndAction=cmndAction, cmndArgs=cmndArgs)
        icm.cmndExampleMenuItem(menuLine, verbosity='none')

        icm.cmndExampleMenuSection('*Install ICMs Needed Python Packages*')
        
        cmndAction = " -i canon_pythonPkgInstall" ; cmndArgs = ""
        menuLine = """{cmndAction} {cmndArgs}""".format(cmndAction=cmndAction, cmndArgs=cmndArgs)
        icm.cmndExampleMenuItem(menuLine, verbosity='none')
        
        #
        # ICMs PKG Information
        #

        icmsPkgInfoBaseDir = marmePkgThis.icmsPkgBase_dir()

        print icmsPkgInfoBaseDir

        icmsPkgLib.examples_pkgInfoParsFull(
            icmsPkgNameSpecification(),
            icmsPkgInfoBaseDir=icmsPkgInfoBaseDir,
            icmsPkgControlBaseDir=icmsPkgControlBaseDirDefault(),
            icmsPkgRunBaseDir=icmsPkgRunBaseDirDefault(),
        )


        #def execLineEx(cmndStr): icm.ex_gExecMenuItem(execLine=cmndStr)
        #execLineEx("""ls""")

####+BEGIN: bx:icm:python:section :title "ICM Commands"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *ICM Commands*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:


####+BEGIN: bx:icm:python:section :title "Platform FPs"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Platform FPs*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

    
configBaseDir = bxPlatformThis.pkgBase_configDir()

#platformConfigFpBase = bxPlatformConfig.configPkgInfoFpBaseDir_obtain(configBaseDir)
bisosUserName = bxPlatformConfig.bisosUserName_fpObtain(configBaseDir)
bisosGroupName = bxPlatformConfig.bisosGroupName_fpObtain(configBaseDir)
#platformControlBaseDir = bxPlatformConfig.platformControlBaseDir_fpObtain(configBaseDir)

#icm.unusedSuppressForEval(moduleDescription, moduleUsage, moduleStatus)

#icm.ANN_write(configBaseDir)
#icm.ANN_here(platformConfigFpBase)
#icm.ANN_here(bisosUserName)
#icm.ANN_here(bisosGroupName)
#icm.ANN_here(platformControlBaseDir)

    

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || IIF       ::  icmsPkgNameSpecification    [[elisp:(org-cycle)][| ]]
"""
def icmsPkgNameSpecification():    return "marme.dev"

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || IIF       ::  icmsPkgControlBaseDirDefault    [[elisp:(org-cycle)][| ]]
"""
#def icmsPkgControlBaseDirDefault():    return os.path.abspath("../../marme.control")
#def icmsPkgControlBaseDirDefault():    return os.path.abspath("/de/bx/nne/mcm0/Sync/marme.control")
#def icmsPkgControlBaseDirDefault():    return os.path.abspath(os.path.join(platformControlBaseDir, "pkgs", "marme"))
def icmsPkgControlBaseDirDefault():    return os.path.abspath(os.path.join("NOTYET", "pkgs", "marme"))

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || IIF       ::  icmsPkgRunBaseDirDefault    [[elisp:(org-cycle)][| ]]
"""
def icmsPkgRunBaseDirDefault():    return os.path.expanduser("~/byStarRunEnv")

####+BEGIN: bx:icm:python:cmnd:classHead :modPrefix "new" :cmndName "binsPreps" :comment "" :parsMand "" :parsOpt "" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || ICM-Cmnd       :: /binsPreps/ parsMand= parsOpt= argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class binsPreps(icm.Cmnd):
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
        pkgsList = canon_pythonPkgsSpec()
        for pkgName in pkgsList:
            pkgVersion = pkgsList[pkgName]
            canon_pythonPkgInstall(pkgName, pkgVersion)

        pkgsList = canon_linuxPkgsSpec()
        for pkgName in pkgsList:
            pkgVersion = pkgsList[pkgName]
            canon_linuxPkgInstall(pkgName, pkgVersion)
            
        
        return cmndOutcome.set(
            opError=icm.OpError.Success,
            opResults=None,
        )

####+BEGIN: bx:icm:python:cmnd:classHead :modPrefix "new" :cmndName "binsPrepsCurInfo" :comment "" :parsMand "" :parsOpt "" :argsMin "0" :argsMax "0" :asFunc "" :interactiveP ""
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || ICM-Cmnd       :: /binsPrepsCurInfo/ parsMand= parsOpt= argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class binsPrepsCurInfo(icm.Cmnd):
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
        #G = icm.IcmGlobalContext()
        #g_runArgs = G.icmRunArgsGet()

        #
        # Python Packages
        #
        pkgsList = canon_pythonPkgsSpec()
        for pkgName in pkgsList:
            # Not all packages ahve __version__ so this is not reliable
            #exec("import {pyModule}".format(pyModule=each))
            #exec("print {pyModule}.__version__".format(pyModule=each))

            installedVer = pythonPkg_versionGet(pkgName)

            installedLoc = pythonPkg_locationGet(pkgName)
            
            icm.ANN_write(
                "Python:: pkgName={pkgName} -- expectedVer={expectedVer} -- installedVer={installedVer} -- installedLoc={installedLoc}"
                .format(pkgName=pkgName,
                        expectedVer=pkgsList[pkgName],
                        installedVer=installedVer,
                        installedLoc=installedLoc,
                ))
            
        #
        # Linux Packages
        #
        pkgsList = canon_linuxPkgsSpec()
        for pkgName in pkgsList:

            installedVer = linuxPkg_versionGet(pkgName)
            
            icm.ANN_write(
                "Linux::  pkgName={pkgName} -- expectedVer={expectedVer} -- installedVer={installedVer}"
                .format(pkgName=pkgName,
                        expectedVer=pkgsList[pkgName],
                        installedVer=installedVer,
                ))
            
        return cmndOutcome.set(
            opError=icm.OpError.Success,
            opResults=None,
        )
    

####+BEGIN: bx:icm:python:section :title "Supporting Classes And Functions"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Supporting Classes And Functions*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:
"""
*       /Empty/  [[elisp:(org-cycle)][| ]]
"""


"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || IIF       ::  canon_linuxPkgInstall    [[elisp:(org-cycle)][| ]]
"""
def canon_linuxPkgInstall(
        pkgName,
        pkgVersion,
):
    """
** Install a given Linux pkg based on its canonical name and version.
"""
    distroName = platform.linux_distribution()[0]
    
    if  distroName == "Ubuntu":
        return linuxPkgInstall_aptGet(pkgName, pkgVersion)
    elif distroName == "Redhat":
        return linuxPkgInstall_yum(pkgName, pkgVersion)
    else:
        icm.EH_problem_info("Unsupported Distribution == {}".format(distroName))
        return

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || IIF       ::  linuxPkgInstall_ubuntu    [[elisp:(org-cycle)][| ]]
"""
def linuxPkgInstall_aptGet(
        pkgName,
        pkgVersion,
):
    """
** Install a given linux pkg with apt-get based on its canonical name and version.
"""
    installedVersion = linuxPkg_versionGet(pkgName)
    if pkgVersion:
        if installedVersion == pkgVersion:
            icm.ANN_write("Linux::  {pkgName} ver={ver} (as expected) is already installed -- skipped".format(
                pkgName=pkgName, ver=installedVersion))
            return
        else:
            outcome = icm.subProc_bash(
                """echo NOTYET pip install {pkgName}=={pkgVersion}"""
                .format(pkgName=pkgName, pkgVersion=pkgVersion)
            ).log()
            if outcome.isProblematic(): return icm.EH_badOutcome(outcome)
            resultStr = outcome.stdout.strip()
            icm.ANN_write(resultStr)
            return

    installedVersion = linuxPkg_versionGet(pkgName)
    if installedVersion:
        icm.ANN_write("Linux::  {pkgName} ver={ver} (as any) is already installed -- skipped".format(
            pkgName=pkgName, ver=installedVersion))
        return
    else:
        outcome = icm.subProc_bash(
            """sudo apt-get install {pkgName}"""
            .format(pkgName=pkgName)
        ).log()
        if outcome.isProblematic(): return icm.EH_badOutcome(outcome)
        resultStr = outcome.stdout.strip()
        icm.ANN_write(resultStr)
        return


"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || IIF       ::  linuxPkgInstall_redhat    [[elisp:(org-cycle)][| ]]
"""
def linuxPkgInstall_yum(
        pkgName,
        pkgVersion,
):
    """
** Install a given linux pkg with yum based on its canonical name and version.
"""

    outcome = icm.subProc_bash(
        """sudo yum install {pkgName}"""
        .format(pkgName=pkgName)
    ).log()
    if outcome.isProblematic(): return icm.EH_badOutcome(outcome)
    resultStr = outcome.stdout.strip()
    icm.ANN_write(resultStr)
    return


"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || IIF       ::  linuxPkg_versionGet    [[elisp:(org-cycle)][| ]]
"""
def linuxPkg_versionGet(
        pkgName,
):
    """
** Return version as string if Python pkgName is installed
** Return None if Python pkgName is not installed
"""
    dpkgQueryOpts = """dpkg-query --show --showformat='${db:Status-Status}\n'"""
    outcome = icm.subProc_bash(
        """{dpkgQueryOpts} {pkgName}"""
        .format(dpkgQueryOpts=dpkgQueryOpts, pkgName=pkgName)
    ).log()
    if outcome.isProblematic():
        icm.EH_badOutcome(outcome)
        return None

    resultStr = outcome.stdout.strip()
    if resultStr == "":
        return None
    
    dpkgQueryOpts = """dpkg-query --show --showformat='${Version}\n'"""
    outcome = icm.subProc_bash(
        """{dpkgQueryOpts} {pkgName}"""
        .format(dpkgQueryOpts=dpkgQueryOpts, pkgName=pkgName)
    ).log()
    if outcome.isProblematic():
        icm.EH_badOutcome(outcome)
        return None
    
    resultStr = outcome.stdout.strip()
    if resultStr == "":
        return None
    else:
        return resultStr



"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || IIF       ::  canon_pythonPkgInstall    [[elisp:(org-cycle)][| ]]
"""
def canon_pythonPkgInstall(
        pkgName,
        pkgVersion,
):
    """
** Install a given Python pkg based on its canonical name and version.
"""
    return pythonPkg_install_pip(pkgName, pkgVersion)    

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || IIF       ::  pythonPkg_install_ubuntu    [[elisp:(org-cycle)][| ]]
"""
def pythonPkg_install_pip(
        pkgName,
        pkgVersion,
):
    """
** Install a given Python pkg based on its canonical name and version.
If version is specified,  the package is installed or updated to that version.
If version is None, 
    if package is already installed no action is taken
    if package is not installed, the latest is installed
"""
    installedVersion = pythonPkg_versionGet(pkgName)
    if pkgVersion:
        if installedVersion == pkgVersion:
            icm.ANN_write("Python:: {pkgName} ver={ver} (as expected) is already installed -- skipped".format(
                pkgName=pkgName, ver=installedVersion))
            return
        else:
            outcome = icm.subProc_bash(
                """echo pip install {pkgName}=={pkgVersion}"""
                .format(pkgName=pkgName, pkgVersion=pkgVersion)
            ).log()
            if outcome.isProblematic(): return icm.EH_badOutcome(outcome)
            resultStr = outcome.stdout.strip()
            icm.ANN_write(resultStr)
            return

    installedVersion = pythonPkg_versionGet(pkgName)
    if installedVersion:
        icm.ANN_write("Python:: {pkgName} ver={ver} (as any) is already installed -- skipped".format(
            pkgName=pkgName, ver=installedVersion))
        return
    else:
        outcome = icm.subProc_bash(
            """echo pip install {pkgName}"""
            .format(pkgName=pkgName)
        ).log()
        if outcome.isProblematic(): return icm.EH_badOutcome(outcome)
        resultStr = outcome.stdout.strip()
        icm.ANN_write(resultStr)
        return


"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || IIF       ::  pythonPkg_versionGet    [[elisp:(org-cycle)][| ]]
"""
def pythonPkg_versionGet(
        pkgName,
):
    """
** Return version as string if Python pkgName is installed
** Return None if Python pkgName is not installed
"""
    outcome = icm.subProc_bash(
        """pip show {pkg} | egrep '^Version' | cut -d ':' -f 2"""
        .format(pkg=pkgName)
    ).log()
    if outcome.isProblematic():
        icm.EH_badOutcome(outcome)
        return None
    
    resultStr = outcome.stdout.strip()
    if resultStr == "":
        return None
    else:
        return resultStr

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || IIF       ::  pythonPkg_locationGet    [[elisp:(org-cycle)][| ]]
"""    
def pythonPkg_locationGet(
        pkgName,
):
    """
** Return location as string if Python pkgName is installed
** Return None if Python pkgName is not installed
"""
    outcome = icm.subProc_bash(
        """pip show {pkg} | egrep '^Location' | cut -d ':' -f 2"""
        .format(pkg=pkgName)
    ).log()
    if outcome.isProblematic():
        icm.EH_badOutcome(outcome)
        return None
    
    resultStr = outcome.stdout.strip()
    if resultStr == "":
        return None
    else:
        return resultStr
    

    
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
*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func-FrameWrk  :: /G_main/ retType=Void argsList=nil  [[elisp:(org-cycle)][| ]]
"""
def G_main():
####+END:
    """ 
** Replaces ICM dispatcher for other command line args parsings.
"""
    pass

####+BEGIN: bx:icm:python:subSection :title "= =Framework::= g_ Settings -- ICMs Imports ="
"""
*  [[elisp:(beginning-of-buffer)][Top]] ================ [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]          *= =Framework::= g_ Settings -- ICMs Imports =*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

g_examples = examples  # or None 
g_mainEntry = None # of G_main

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
