#! /usr/bin/python2.7
# -*- coding: utf-8 -*-
"""\
* TODO *[Summary]* :: Needs to be modernized from iim to icm -- A replacement module for qmail-remote with complete SMTP implementation and  a plugins framework.
* Authors: Mohsen Banan --  http://mohsen.1.banan.byname.net/contact\
"""

####+BEGIN: bx:dblock:global:iim:name-py :style "fileName"
__iimName__ = "msgProc"
####+END:

####+BEGIN: bx:dblock:global:timestamp:version-py :style "date"
__version__ = "201704260843"
####+END:

"""
####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/libre/ByStar/InitialTemplates/software/plusOrg/dblock/inserts/topControls.org"
*  /Controls/ ::  [[elisp:(org-cycle)][| ]]  [[elisp:(show-all)][Show-All]]  [[elisp:(org-shifttab)][Overview]]  [[elisp:(progn (org-shifttab) (org-content))][Content]] | [[file:Panel.org][Panel]] | [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] | [[elisp:(bx:org:run-me)][Run]] | [[elisp:(bx:org:run-me-eml)][RunEml]] | [[elisp:(delete-other-windows)][(1)]] | [[elisp:(progn (save-buffer) (kill-buffer))][S&Q]]  [[elisp:(save-buffer)][Save]]  [[elisp:(kill-buffer)][Quit]] [[elisp:(org-cycle)][| ]]
** /Version Control/ ::  [[elisp:(call-interactively (quote cvs-update))][cvs-update]]  [[elisp:(vc-update)][vc-update]] | [[elisp:(bx:org:agenda:this-file-otherWin)][Agenda-List]]  [[elisp:(bx:org:todo:this-file-otherWin)][ToDo-List]] 

####+END:
"""

"""
*      ================
*  #################### CONTENTS-LIST ################
*  [[elisp:(org-cycle)][| ]]  [Info]          :: *[Current-Info:]* Status/Maintenance -- General TODO List [[elisp:(org-cycle)][| ]]
**  [[elisp:(org-cycle)][| ]]  Current      :: Just getting started [[elisp:(org-cycle)][| ]]
*  [[elisp:(org-cycle)][| ]]  [Xref]          :: *[Related/Xrefs:]*  <<Xref-Here->>  -- External Documents  [[elisp:(org-cycle)][| ]]
**  [[elisp:(org-cycle)][| ]]  Current      :: [[file:/libre/ByStar/InitialTemplates/activeDocs/bxServices/versionControl/fullUsagePanel-en.org::Xref-VersionControl][Panel Roadmap Documentation]] [[elisp:(org-cycle)][| ]]
"""

"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(delete-other-windows)][(1)]]      *Imports And Description -- describe()*
"""

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || =Imports=    ::  Imports [[elisp:(org-cycle)][| ]]
"""

####+BEGINNOT: bx:dblock:global:file-insert :file "" Add Path As ParameterNOTYET
"""
*  [[elisp:(org-show-subtree)][|=]]  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  insertPathForImports    [[elisp:(org-cycle)][| ]]
"""
def insertPathForImports(path):
    import os
    import sys
    absolutePath = os.path.abspath(path)    
    if os.path.isdir(absolutePath):
        sys.path.insert(1, absolutePath)

insertPathForImports("../lib/python/")

####+END:


import sys

import os
#import shlex
#import subprocess

#from datetime import datetime

import iim
import empna

import re
#import pprint

import email
import mailbox
import smtplib

import flufl.bounce

from email.mime.text import MIMEText
#from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email import Encoders

#from yapsy.PluginManager import PluginManager
import yapsy.PluginManager

####+BEGIN: bx:dblock:python:import:jediWorkAround :namespace "unisos" :module "ucf" :file "ucf"
# Development Workaround  For JediWorkaround
import ucf
####+END:

####+BEGIN: bx:dblock:python:import:jediWorkAround :namespace "unisos" :module "icm" :file "icm"
# External Usage
from unisos.icm import icm
####+END:


from bxMsg import msgOut
from bxMsg import msgIn
#from bxMsg import msgLib


"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || FrmWrk-IIF   ::  describe    [[elisp:(org-cycle)][| ]]
"""
# Can't be decorated in Native-SON-Modules
#@iim.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def describe(interactive=False):
    moduleDescription="""
*       [[elisp:(org-cycle)][| *Description:* | ]]
**       Functional Specification :Overview:
    Replacement for qmail-remote -- http://www.qmail.org/man/man8/qmail-remote.html
    Adds following features:
*** Complete SMTP Submit Protocol based on the email.smtp python library.
*** X-RemMail headers
*** Plugins for addition of modules to process the msg before submission.
**       Comptibility Requirements -- qmail-remote interface
**       Control and Configuration -- smtproutes
**       Plugins
**       :Contacts:
	[[elisp:(bystar:bbdb:search-here "Mohsen Banan")][Mohsen BANAN]]
**       *[End-Of-Description]*
"""
####+BEGINNOT: bx:dblock:global:file-insert :file "/libre/ByStar/InitialTemplates/software/plusOrg/dblock/inserts/g_describe.py"  
    #try: iim.callableEntryEnhancer(type='iif')
    #except StopIteration:  return

    # Is Broken In Native SON
    # iim.callableEntryEnhancer(type='describe')

####+END:

    if iim.Interactivity().interactiveInvokation(interactive):
        print( str( __doc__ ) )  # This is the Summary: from the top doc-string
        print(moduleDescription)
        return
    else:
        return("Version: " + format(str(__version__)) + format(str(__doc__) + moduleDescription))

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || FrmWrk-IIF   ::  usage    [[elisp:(org-cycle)][| ]]
"""
# Can't be decorated in Native-SON-Modules
#@iim.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def usage(interactive=False):
    moduleDescription="""
*       [[elisp:(org-cycle)][| *Usage:* | ]]

**       See-Also:
***      iim -i describe
***      iim -i version
**      *[End-Of-Usage]*
"""

    if iim.Interactivity().interactiveInvokation(interactive):
        print( str( __doc__ ) )  # This is the Summary: from the top doc-string
        version(interactive=True)
        print(moduleDescription)
        return
    else:
        return(format(str(__doc__)+moduleDescription))

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || FrmWrk-IIF   ::  version    [[elisp:(org-cycle)][| ]]
"""
# Can't be decorated in Native-SON-Modules
#@iim.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def version(interactive=False):
    if iim.Interactivity().interactiveInvokation(interactive):
        print("* IIM-Version: {ver}".format(ver=str( __version__ )))
        return
    else:
        return(format(str(__version__)))

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || FrmWrk-IIF   ::  g_iimPreIifs    [[elisp:(org-cycle)][| ]]
"""

@iim.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def g_iimPreIifs():
    G = iim.IimGlobalContext()

    iimFuncs=G.iimModuleFunctionsList()

    # func_auxInvokable does a setattr for func's auxInvokable attribute
    for func in iimFuncs:
        if iim.str_endsWith(func.name, "_auxInvokable"):
            eval(func.name + '()')

    iifsList=list()
    for func in iimFuncs:
        callable = iim.FUNC_strToFunc(func.name)
        try:    
            if callable.auxInvokable:
                #print "{func} is YES auxInvokable".format(func=func.name)
                G.auxInvokationContextSet(iim.AuxInvokationContext.IimRole)
                eval(func.name + '()')
                auxResults = G.auxInvokationResults()
                if auxResults == "iif":
                    iifsList.append(func.name)
                    
        except AttributeError:
            pass
            #print "{func} is NOT auxInvokable".format(func=func.name)
            
    G.iifNamesSet(iifsList)
    #print(iifsList)

    for func in iimFuncs:
        callable = iim.FUNC_strToFunc(func.name)
        try:    
            if callable.auxInvokable:
                #print "{func} is YES auxInvokable".format(func=func.name)
                G.auxInvokationContextSet(iim.AuxInvokationContext.DocString)
                eval(func.name + '()')
                #auxResults = G.auxInvokationResults()
                #if auxResults == "iif":
                    #iifsList.append(func.name)
                    
        except AttributeError:
            pass
            #print "{func} is NOT auxInvokable".format(func=func.name)
    

    iim.iimParamsToFileParamsUpdate(
        parRoot="./var/{myName}/iimIn/paramsFp".format(myName=G.iimMyName()),
        iimParams=G.iimParamDictGet(),
    )
    
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || FrmWrk-IIF   ::  g_iimPostIifs    [[elisp:(org-cycle)][| ]]
"""

@iim.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def g_iimPostIifs():
    pass



"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(delete-other-windows)][(1)]]      *Options, Arguments and Examples Specifications*
"""

####+BEGINNOT: bx:dblock:global:file-insert :file "/libre/ByStar/InitialTemplates/software/plusOrg/dblock/inserts/g_invokesProcIim.py"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || /Dblk-Begin/ ::  g_invokesProc (g_invokesProc(args))   [[elisp:(org-cycle)][| ]]
"""

def g_invokesProc():
    """Invoke the specified function.

This is here and not in iim.g_invokesProc because of naming scopes.
Can't -- eval(invoke + '()') -- from within iim library.
    """

    G = iim.IimGlobalContext()
    iimRunArgs = G.iimRunArgsGet()

    g_iimPreIifs()
    
    for invoke in iimRunArgs.invokes:

        #func = iim.FUNC_strToFunc(invoke)
        try:
            eval(invoke + '(interactive=True)')
            #func(args)
        except Exception as e:
            iim.EH_critical_exception(e)
            iim.EH_problem_info("Invalid Action: {invoke}"
                                 .format(invoke=invoke))            
            raise

    g_iimPostIifs()
    
    return


"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || /Dblk-End/   ::   [[elisp:(org-cycle)][| ]]
"""
    

####+END:

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || =ArgsSpec=   ::  g_argsExtraSpecify    [[elisp:(org-cycle)][| ]]
"""
#@iim.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def g_argsExtraSpecify(parser):
    """Module Specific Command Line Parameters.
    g_argsExtraSpecify is passed to G_main and is executed before argsSetup (can not be decorated)
    """
    G = iim.IimGlobalContext()
    iimParams = iim.IIM_ParamDict()
    
    empna.targetParamListCommonArgs(parser)    
      
    iim.argsparseBasedOnIimParams(parser, iimParams)

    # So that it can be processed later as well.
    G.iimParamDictSet(iimParams)
    
    return

####+BEGIN: bx:dblock:global:file-insert :file "/libre/ByStar/InitialTemplates/software/plusOrg/dblock/inserts/G_examplesIim.top.py"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || FrmWrk-IIF   ::  examples    [[elisp:(org-cycle)][| ]]
"""

@iim.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def examples(interactive=False):
    G_myFullName = sys.argv[0]
    G_myName = os.path.basename(G_myFullName)
    iim.iimExampleMyName(G_myName, os.path.abspath(G_myFullName))
    iim.G_commonBriefExamples()    
    #iim.G_commonExamples()
    #g_curFuncName = iim.FUNC_currentGet().__name__
    logControler = iim.LOG_Control()
    logControler.loggerSetLevel(20)

####+END:

    #iifThis = iim.FUNC_currentGet().__name__

    logControler = iim.LOG_Control()
    logControler.loggerSetLevel(20)

    #verboseDebug = " -v  1"
    #verboseWarning = " -v 30"        
    #verboseError = " -v 30"
    
    iim.iifExampleMenuChapter('*General IIFs*')   

    thisIifAction= " -i mainIif"
    iim.iifExampleMenuItem(
        format("--inFile" + " fileInput"  + thisIifAction),
        verbosity='none')


    iim.ANN_write("cat /opt/public/osmt/samples/email/plainText.inMail | bx-qmail-remote.py")


    
####+BEGIN: bx:dblock:global:file-insert :file "/libre/ByStar/InitialTemplates/software/plusOrg/dblock/inserts/G_examples.bottom.py"
    # Intentionally Left Blank -- previously: lhip.G_devExamples(G_myName)

####+END:


"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(delete-other-windows)][(1)]]      *General Interactively Invokable Functions (IIF)*
"""

"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(delete-other-windows)][(1)]]      *IIM Specific Interactively Invokable Functions (IIM-IIF)*
"""


"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || IIM-IIF      ::  mainIif    [[elisp:(org-cycle)][| ]]
"""
def mainIif_auxInvokable(): iim.frameNuFuncSetAuxInvokable(2)

@iim.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def mainIif(
        interactive=False,
):
    """ Doc String for mainIif """
    iimRole='iif'
    iifParamsMandatory=['1', '2']
    iifParamsOptional=[1,2]
    iifArgsLen=["1+,1,1-", "2"]
####+BEGINNOT: bx:dblock:global:file-insert :file "/libre/ByStar/InitialTemplates/software/plusOrg/dblock/inserts/iimFuncHead.py"
    try: iim.auxInvoke(
            iimRole=iimRole,
            iifParamsMandatory=iifParamsMandatory,
            iifParamsOptional=iifParamsOptional,
            iifArgsLen=iifArgsLen,            
    )
    except StopIteration:  return

    G = iim.IimGlobalContext()
    G.curFuncNameSet(iim.FUNC_currentGet().__name__)
####+END:

    inMsg = msgIn.getMsgFromStdin()

    msgOut.envelopeInfoHeaders(inMsg)

    print inMsg.as_string()    

    return



"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  out,zero,temp_dns,temp_control    [[elisp:(org-cycle)][| ]]
"""

def out(str): sys.stdout.write(str)
def zero():  sys.stdout.write("\0")
def zerodie(): sys.stdout.write("\0")
def outsafe(str): sys.stdout.write(str)
def temp_nomem(): out("ZOut of memory. (#4.3.0)\n") ; zerodie()

def temp_oserr():
    out("Z\
System resources temporarily unavailable. (#4.3.0)\n")
    zerodie()

def temp_noconn():
    out("Z\
Sorry, I wasn't able to establish an SMTP connection. (#4.4.1)\n")
    zerodie()

def temp_read():
    out("ZUnable to read message. (#4.3.0)\n")
    zerodie()

def temp_dnscanon():
    out("Z\
CNAME lookup failed temporarily. (#4.4.3)\n")
    zerodie()

def temp_dns():
    out("Z\
Sorry, I couldn't find any host by that name. (#4.1.2)\n")
    zerodie()

def temp_chdir():
    out("Z\
Unable to switch to home directory. (#4.3.0)\n")
    zerodie()

def temp_control():
    out("Z\
Unable to read control files. (#4.3.0)\n")
    zerodie()
    
def perm_partialline():
    out("D\
SMTP cannot transfer messages with partial final lines. (#5.6.2)\n")
    zerodie()

def perm_usage():
    out("D\
I (qmail-remote) was invoked improperly. (#5.3.5)\n")
    zerodie()

def perm_dns(host):
    out("D\
Sorry, I couldn't find any host named ")
    outsafe(host);
    out(". (#5.1.2)\n")
    zerodie()

def  perm_nomx():
    out("D\
Sorry, I couldn't find a mail exchanger or IP address. (#5.4.4)\n");
    zerodie()
    
def perm_ambigmx():
    out("D\
Sorry. Although I'm listed as a best-preference MX or A for that host,\n\
it isn't in my control/locals file, so I don't treat it as local. (#5.4.6)\n");
    zerodie()
    

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  getControls    [[elisp:(org-cycle)][| ]]
"""
def getControls():
    """ """
    # read "control/timeoutremote"  # Int
    # read "control/timeoutconnect" # Int
    # read control/helohost # String
    # read control/smtproutes # File as a dictionary
    return


"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  outsmtptext    [[elisp:(org-cycle)][| ]]
"""

def outsmtptext():
    out("Remote host said: ");
    out("NotYet: Somthing like: 250 ok 1495256578 qp 14280")
    zero()
    

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  G_main    [[elisp:(org-cycle)][| ]]
"""

def G_main():
    #print sys.argv

    argc = len(sys.argv)

    print argc
    print sys.argv

    if argc < 4:
        print "JJ"
        perm_usage()
        return

    getControls()

    host = sys.argv[1]

    # Lookup host in smtproutes to get "relayHost"

    sender = sys.argv[2]

    recipientsList = sys.argv[3:]

    #print host
    #print sender
    #print recipientsList

    #perm_usage()    
    
    #return 

    msg = msgIn.getMsgFromStdin()

    #print msg.as_string()  

    #return
    
    # Load the plugins from the plugin directory.
    #manager = PluginManager()
    manager = yapsy.PluginManager.PluginManager()    
    manager.setPluginPlaces(["qmailPlugins"])
    manager.collectPlugins()

    print "=================="
    
    for plugin in manager.getAllPlugins():
        print plugin.name

    print "=================="    
    
    #for plugin in manager.getAllPlugins():
        #plugin.plugin_object.print_name()

    print "================== Now We invoke Them In A Particular Order ================"

    orderedList = list()
    
    orderedList.append("Other Plugin")
    orderedList.append("Plugin 1")    
        
    for pluginName in orderedList:
        print pluginName
        for plugin in manager.getAllPlugins():
            if pluginName == plugin.name:
                msg = plugin.plugin_object.msgFilter(msg)

    print msg.as_string()  



"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Func         ::  G_mainOld    [[elisp:(org-cycle)][| ]]
"""
    
def G_mainOld():
    print sys.argv
    
    for thisArg in sys.argv:
        print thisArg

    msg = msgIn.getMsgFromStdin()

    #print msg.as_string()  

    #return
    
    # Load the plugins from the plugin directory.
    #manager = PluginManager()
    manager = yapsy.PluginManager.PluginManager()    
    manager.setPluginPlaces(["plugins"])
    manager.collectPlugins()

    print "=================="
    
    for plugin in manager.getAllPlugins():
        print plugin.name

    print "=================="    
    
    #for plugin in manager.getAllPlugins():
        #plugin.plugin_object.print_name()

    print "================== Now We invoke Them In A Particular Order ================"

    orderedList = list()
    
    orderedList.append("Other Plugin")
    orderedList.append("Plugin 1")    
        
    for pluginName in orderedList:
        print pluginName
        for plugin in manager.getAllPlugins():
            if pluginName == plugin.name:
                msg = plugin.plugin_object.msgFilter(msg)

    print msg.as_string()  



"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(delete-other-windows)][(1)]]      *Common/Generic Facilities -- Library Candidates*
"""

"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(delete-other-windows)][(1)]]      *Python Main*
"""

####+BEGINNOT: bx:dblock:global:file-insert :file "/libre/ByStar/InitialTemplates/software/plusOrg/dblock/inserts/iim.G_main.py"
"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || /Dblk-Begin/ ::  g_iimMain    [[elisp:(org-cycle)][| ]]
"""

def iimCmndPartIncludes(interactive=False): return True

def iimLanguage(interactive=False): print "python"

def g_iimMain():
    """ """
    sys.exit(
        iim.G_main(
            inArgv=sys.argv[1:],            # Mandatory
            #G_examples=examples,            # Mandatory
            G_examples=None,            # Mandatory            
            extraArgs=g_argsExtraSpecify,   # Mandatory
            invokesProc=g_invokesProc,      # Mandatory
            mainEntry=G_main,
        )
    )

g_iimMain()    

"""
*  [[elisp:(org-cycle)][| ]]  [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || /Dblk-End/   ::   [[elisp:(org-cycle)][| ]]
"""

####+END:


"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(delete-other-windows)][(1)]]      *Unused Facilities -- Temporary Junk Yard*
"""


"""
*  [[elisp:(beginning-of-buffer)][Top]] ################ [[elisp:(delete-other-windows)][(1)]]      *End Of Editable Text*
"""

"""
*  [[elisp:(org-cycle)][| ]]  [COMMON]      :: /[dblock] -- End-Of-File Controls/ [[elisp:(org-cycle)][| ]]
"""

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/libre/ByStar/InitialTemplates/software/plusOrg/dblock/inserts/endOfFileControls.org"
#+STARTUP: showall

####+END:
