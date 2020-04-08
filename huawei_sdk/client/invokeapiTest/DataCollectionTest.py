import json

from huawei_sdk.client.invokeapi.Authentication import Authentication
from huawei_sdk.client.invokeapi.DataCollection import DataCollection

from huawei_sdk.client.dto.AuthOutDTO import AuthOutDTO
from huawei_sdk.client.dto.QueryBatchDevicesInfoInDTO import QueryBatchDevicesInfoInDTO
from huawei_sdk.client.dto.QueryDeviceCapabilitiesInDTO import QueryDeviceCapabilitiesInDTO
from huawei_sdk.client.dto.QueryDeviceDataHistoryInDTO import QueryDeviceDataHistoryInDTO
from huawei_sdk.client.dto.QueryDeviceDesiredHistoryInDTO import QueryDeviceDesiredHistoryInDTO
from huawei_sdk.constant.Constant import Constant


class DataCollectionTest(object):
    def queryBatchDevicesInfo(self):
        qbdiInDTO = QueryBatchDevicesInfoInDTO()
        qbdiInDTO.gatewayId = "ce598cf9-942e-4fd2-814e-f4ca3659632a"
        qbdiInDTO.appId = "wk14orhpOumkAouraCpOsoQ3iO4a"
        return qbdiInDTO

    def queryDeviceDataHistory(self):
        qddhInDTO = QueryDeviceDataHistoryInDTO()
        qddhInDTO.deviceId = "ce598cf9-942e-4fd2-814e-f4ca3659632a"
        qddhInDTO.gatewayId = "ce598cf9-942e-4fd2-814e-f4ca3659632a"
        qddhInDTO.appId = "WHkdwPLjoWB7iFCOX_X_c65AUtka"
        return qddhInDTO

    def queryDeviceDesiredHistory(self):
        qddhInDTO = QueryDeviceDesiredHistoryInDTO()
        qddhInDTO.deviceId = "ce598cf9-942e-4fd2-814e-f4ca3659632a"
        qddhInDTO.gatewayId = "ce598cf9-942e-4fd2-814e-f4ca3659632a"
        qddhInDTO.appId = "WHkdwPLjoWB7iFCOX_X_c65AUtka"
        return qddhInDTO

    def queryDeviceCapabilities(self):
        qdcInDTO = QueryDeviceCapabilitiesInDTO()
        qdcInDTO.deviceId = "ce598cf9-942e-4fd2-814e-f4ca3659632a"
        qdcInDTO.gatewayId = "ce598cf9-942e-4fd2-814e-f4ca3659632a"
        qdcInDTO.appId = "WHkdwPLjoWB7iFCOX_X_c65AUtka"
        return qdcInDTO


if __name__ == "__main__":
    dcTest = DataCollectionTest()
    authentication = Authentication()
    dataCollection = DataCollection()

    # get accessToken at first
    result = authentication.getAuthToken(Constant().clientInfo())
    authOutDTO = AuthOutDTO()
    authOutDTO.setAccessToken(json.loads(result)['accessToken'])
    accessToken = authOutDTO.getAccessToken()

    # query device info
    deviceId = "ce598cf9-942e-4fd2-814e-f4ca3659632a"
    dq = dataCollection.querySingleDeviceInfo(deviceId, None, None, accessToken)
    print("====== query device info ======")
    print("result:", dq + "\n")

    # query batch device info
    dataCollection.queryBatchDevicesInfo(dcTest.queryBatchDevicesInfo(), accessToken)
    print("====== query batch device info ======")
    print("result:", dq + "\n")

    # query device data history
    dq = dataCollection.queryDeviceDataHistory(dcTest.queryDeviceDataHistory(), accessToken)
    print("====== query device data history ======")
    print("result:", dq + "\n")

    # query device desired history
    dq = dataCollection.queryDeviceDesiredHistory(dcTest.queryDeviceDesiredHistory(), accessToken)
    print("====== query device desired history ======")
    print("result:", dq + "\n")

    # query device desired capabilities
    dq = dataCollection.queryDeviceCapabilities(dcTest.queryDeviceCapabilities(), accessToken)
    print("====== query device desired capabilities ======")
    print("result:", dq + "\n")
