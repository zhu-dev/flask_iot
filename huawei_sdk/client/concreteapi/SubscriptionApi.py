# coding:utf-8
import json

from huawei_sdk.client.invokeapi.Authentication import Authentication
from huawei_sdk.client.invokeapi.SubscriptionManagement import \
    SubscriptionManagement

from huawei_sdk.client.dto.AuthOutDTO import AuthOutDTO
from huawei_sdk.client.dto.SubDeviceBusinessDataInDTO import SubDeviceBusinessDataInDTO
from huawei_sdk.client.dto.SubDeviceManagementDataInDTO import SubDeviceManagementDataInDTO
from huawei_sdk.client.dto.SubscriptionDTO import SubscriptionDTO
from huawei_sdk.constant.Constant import Constant
from huawei_sdk.client.concreteapi.Subscription import Subscription


def subscribe(notifyType, callbackUrl):
    sb = Subscription(notifyType, callbackUrl)
    authentication = Authentication()
    subscriptionManagement = SubscriptionManagement()

    # get accessToken at first
    result = authentication.getAuthToken(Constant().clientInfo())
    authOutDTO = AuthOutDTO()
    authOutDTO.setAccessToken(json.loads(result)['accessToken'])
    accessToken = authOutDTO.getAccessToken()

    # sub deviceDataChanged notification
    ss = subscriptionManagement.subDeviceBusinessData(sb.subDeviceBusinessData(), accessToken)
    print("====== subscribe to device business data notification ======")
    print("result:", ss + "\n")
    return ss

    # get subscriptionId
    # rddod = SubscriptionDTO()
    # rddod.setSubscriptionId(json.loads(ss)['subscriptionId'])
    # subscriptionId = rddod.getSubscriptionId()
    # print("subscriptionId==", subscriptionId + "\n")
