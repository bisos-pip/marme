#! /bin/bash

function echoErr { echo "E: $@" 1>&2; }
function echoAnn { echo "A: $@" 1>&2; }
function echoOut { echo "$@"; }

function usage {
    echoOut "USAGE:"
    echoOut "$0 setup+prep+run"    
    echoOut "$0 setup+prep"
    echoOut "$0 setup"    
}


if [ $# -ne 1 ] ; then
    echoErr "Bad Nu Of Args -- Expected 1 -- Got $#"
    usage    
    exit 1
fi

configFile="$1"

if [ -f "${configFile}" ] ; then
    source "${configFile}"
else
    echoErr "Missing Config File: ${configFile}"
    exit 1
fi


#
# Assumptions:
#   1) initial bx-platformInfoManage.py base parameters has already been setup
#   2) bx-bases has already been setup
#   3) This script is being run by  --bisosUserName of bx-platformInfoManage.py
#   4) unisos.marme has already been installed in py2-bisos-3 and/or perhaps other venv
#   5) --sr=marme/dsnProc parameters for this foreignBxO has been configured.
#
# Actions Taken:
#   A) Above assumptions are verified
#   B) If a virtenv has been activated, it is used. Otherwise py2-bisos-3 is activated.
#   C) System's bx-platformInfoManage.py are copied into the active virtenv
#   D) $(pwd) is used to set --rootDir_foreignBxo
#   E) bx-currentsManage.py --bxoId and --sr are set for this foreignBxo
#   F) marmeAcctsManage.py params are set for this foreignBxo
#


here=$(pwd)

if [ -z "${fbxoId}" ] ; then
    hereSansBxoBase=${here##${foreignBxoBase}}
    fbxoId=$(echo ${hereSansBxoBase} | cut -c 2- | cut -d / -f 1)
fi



function bxoSrCurrentsSet {
    bx-currentsManage.py --bxoId="${fbxoId}"  -i pkgInfoParsSet
    bx-currentsManage.py --sr="${serviceRealization}"  -i pkgInfoParsSet

    echo "========= bx-currentsManage.py -i pkgInfoParsGet ========="
    bx-currentsManage.py -i pkgInfoParsGet
}

function marmeAcctsParsSet {
    marmeAcctsManage.py --bxoId="${fbxoId}" --sr="${serviceRealization}" \
			 -i enabledControlProfileSet  ${enabledControlProfile}

    marmeAcctsManage.py --bxoId="${fbxoId}" --sr="${serviceRealization}" \
			--inMailAcctMboxesPath="/de/run/bisos/r3/bxo/${fbxoId}/var/marme/inMail/${enabledControlProfile}/${enabledInMailAcct}/maildir" \
			-i inMailAcctRetrievalParsSet

    echo "========= marmeAcctsManage.py  --bxoId="${fbxoId}" --sr="${serviceRealization}" -i inMailAcctParsGet ========="
    marmeAcctsManage.py  --bxoId="${fbxoId}" --sr="${serviceRealization}" -i inMailAcctParsGet

    echo "========= marmeAcctsManage.py  --bxoId="${fbxoId}" --sr="${serviceRealization}" -i outMailAcctParsGet ========="
    marmeAcctsManage.py  --bxoId="${fbxoId}" --sr="${serviceRealization}" -i outMailAcctParsGet

    echo "========= marmeAcctsManage.py  --bxoId="${fbxoId}" --sr="${serviceRealization}" -i bxoSrPkgInfoParsGet ========="
    marmeAcctsManage.py  --bxoId="${fbxoId}" --sr="${serviceRealization}" -i bxoSrPkgInfoParsGet

    echo "========= Making sure that all run-time bases are in place ========="
    echo "========= marmeAcctsManage.py  --bxoId="${fbxoId}" --sr="${serviceRealization}" -i bxoSrPkgInfoMkdirs ========="        
    marmeAcctsManage.py  --bxoId="${fbxoId}" --sr="${serviceRealization}" -i bxoSrPkgInfoMkdirs
}

function marmeIcmsPrep {
    set -x
    inMailRetrieve.py --bxoId="${fbxoId}" --sr="${serviceRealization}" -i offlineimaprcUpdate
    inMailNotmuch.py --bxoId="${fbxoId}" --sr="${serviceRealization}" -i notmuchConfigUpdate
}

function marmeIcmsRunOnce {
    set -x
    inMailRetrieve.py -v 1 --bxoId="${fbxoId}" --sr="${serviceRealization}" -i offlineimapRun
    inMailNotmuch.py --bxoId="${fbxoId}" --sr="${serviceRealization}" -i runNotmuch new
    #inMailNotmuch.py --bxoId="${fbxoId}" --sr="${serviceRealization}" -i runNotmuch -- search "from:"
    inMailDsnProc.py -v 20 --bxoId="${fbxoId}" --sr="${serviceRealization}" --runMode="dryRun"  -i maildirApplyToMsg dsnTestSendToCoRecipients    
}

function marmeFullSetup {
    bxoSrCurrentsSet
    marmeAcctsParsSet
}

case ${runScope} in
    setup+prep+run)
	marmeFullSetup
	marmeIcmsPrep
	marmeIcmsRunOnce
	;;
    setup+prep)
	marmeFullSetup
	marmeIcmsPrep	
	;;
    setup)
	marmeFullSetup
	;;
    *)
	echoErr "Unknown runScope -- ${runScope}"
	;;
esac


