#! /bin/bash

enabledControlProfile="example.com"

enabledInMailAcct="example.com"
enabledOutMailAcct="example.com"

enabledMailBox=Inbox

bisosVenvName=py2-bisos-3


#########  End-Of-Params-Specification ###########

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

function echoErr { echo "E: $@" 1>&2; }
function echoAnn { echo "A: $@" 1>&2; }
function echoOut { echo "$@"; }


PATH="$PATH:."


here=$(pwd)

foreignBxoBase=$(echo ~/foreignBxo)

hereSansBxoBase=${here##${foreignBxoBase}}

fbxoId=$(echo ${hereSansBxoBase} | cut -c 2- | cut -d / -f 1)


bxoId="mcm"

serviceName="marme"
serviceAdaptation="dsnProc"

serviceRealization=${serviceName}/${serviceAdaptation}

function platformInfoParsSet {
    local here=$(pwd)
    local foreignBxoBase=$(dirname ${here})

    local currentUser=$(id -un)
    local currentUserGroup=$(id -g -n ${currentUser})

    if [ "$( type -t deactivate )" == "function" ] ; then
	deactivate
    fi

    #
    # System-wide bx-platformInfoManage.py is assumed to have been installed
    #
    if ! which bx-platformInfoManage.py > /dev/null ; then
	echoErr "Missing bx-platformInfoManage.py"
	return 1
    fi
    
    local bisosUserName=$( bx-platformInfoManage.py  -i pkgInfoParsGet | grep bisosUserName | cut -d '=' -f 2 )
    local bisosGroupName=$( bx-platformInfoManage.py  -i pkgInfoParsGet | grep bisosGroupName | cut -d '=' -f 2 )
    
    local rootDir_bisos=$( bx-platformInfoManage.py  -i pkgInfoParsGet | grep rootDir_bisos | cut -d '=' -f 2 )
    local rootDir_bxo=$( bx-platformInfoManage.py  -i pkgInfoParsGet | grep rootDir_bxo | cut -d '=' -f 2 )
    local rootDir_deRun=$( bx-platformInfoManage.py  -i pkgInfoParsGet | grep rootDir_deRun | cut -d '=' -f 2 )        

    if [ "${currentUser}" != "${bisosUserName}" ] ; then
	echoErr "currentUser=${currentUser} is not same as bisosUserName=${bisosUserName}"
	return 1
    fi

    local bisosVirtEnvBase="${rootDir_bisos}/venv/${bisosVenvName}"


    source ${bisosVirtEnvBase}/bin/activate    

    #
    # We set the virtenv's params to be same as system's
    #
 
    bx-platformInfoManage.py --bisosUserName="${bisosUserName}"  -i pkgInfoParsSet
    bx-platformInfoManage.py --bisosGroupName="${bisosGroupName}"  -i pkgInfoParsSet     

    bx-platformInfoManage.py --rootDir_bisos="${rootDir_bisos}"  -i pkgInfoParsSet
    bx-platformInfoManage.py --rootDir_bxo="${rootDir_bxo}"  -i pkgInfoParsSet
    bx-platformInfoManage.py --rootDir_deRun="${rootDir_deRun}"  -i pkgInfoParsSet    

    #
    # $(pwd) is used to set --rootDir_foreignBxo
    #
    
    bx-platformInfoManage.py --rootDir_foreignBxo="${foreignBxoBase}"  -i pkgInfoParsSet

    echo "========= bx-platformInfoManage.py -i pkgInfoParsGet ========="
    bx-platformInfoManage.py -i pkgInfoParsGet
}


function bxoSrCurrentsSet {
    bx-currentsManage.py --bxoId="${bxoId}"  -i pkgInfoParsSet
    bx-currentsManage.py --sr="${serviceRealization}"  -i pkgInfoParsSet

    echo "========= bx-currentsManage.py -i pkgInfoParsGet ========="
    bx-currentsManage.py -i pkgInfoParsGet
}

function marmeAcctsParsSet {
    marmeAcctsManage.py --bxoId="${bxoId}" --sr="${serviceRealization}" \
			 -i enabledControlProfileSet  mckenziechase

    marmeAcctsManage.py --bxoId="${bxoId}" --sr="${serviceRealization}" \
			--inMailAcctMboxesPath="/de/run/bisos/r3/bxo/mcm/var/marme/inMail/mckenziechase/fastrackhr/maildir" \
			-i inMailAcctRetrievalParsSet

    echo "========= marmeAcctsManage.py  --bxoId="${bxoId}" --sr="${serviceRealization}" -i inMailAcctParsGet ========="
    marmeAcctsManage.py  --bxoId="${bxoId}" --sr="${serviceRealization}" -i inMailAcctParsGet

    echo "========= marmeAcctsManage.py  --bxoId="${bxoId}" --sr="${serviceRealization}" -i outMailAcctParsGet ========="
    marmeAcctsManage.py  --bxoId="${bxoId}" --sr="${serviceRealization}" -i outMailAcctParsGet
}

platformInfoParsSet

bxoSrCurrentsSet

marmeAcctsParsSet
