Attribute VB_Name = "Module1"
Function CallAnimalModel(poilArg As String, _
plumeArg As String, _
oeufsArg As String, _
laitArg As String, _
volArg As String, _
aquatiqueArg As String, _
predateurArg As String, _
dentsArg As String, _
colonneArg As String, _
respireArg As String, _
venimeuxArg As String, _
nageoiresArg As String, _
jambesArg As String, _
queueArg As String, _
domestiqueArg As String, _
grosArg As String _
) As String

Dim jsonBody As String
jsonBody = "{""poil"":" & """" & poilArg & """" & _
",""plumes"":" & """" & plumeArg & """" & _
",""oeufs"":" & """" & oeufsArg & """" & _
",""lait"":" & """" & laitArg & """" & _
",""vol"":" & """" & volArg & """" & _
",""aquatique"":" & """" & aquatiqueArg & """" & _
",""predateur"":" & """" & predateurArg & """" & _
",""dents"":" & """" & dentsArg & """" & _
",""colonne"":" & """" & colonneArg & """" & _
",""respire"":" & """" & respireArg & """" & _
",""venimeux"":" & """" & venimeuxArg & """" & _
",""nageoires"":" & """" & nageoiresArg & """" & _
",""jambes"":" & jambesArg & _
",""queue"":" & """" & queueArg & """" & _
",""domestique"":" & """" & domestiqueArg & """" & _
",""gros"":" & """" & grosArg & """" & "}"

Set objHTTP = CreateObject("WinHttp.WinHttpRequest.5.1")
URL = "http://192.168.1.192:5000/send"
objHTTP.Open "POST", URL, False
objHTTP.SetRequestHeader "Content-type", "application/json"
objHTTP.SetRequestHeader "User-Agent", "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)"



objHTTP.Send jsonBody

Dim strResp As String
strResp = objHTTP.ResponseText

Dim Json As Object
Set Json = JsonConverter.ParseJson(strResp)

CallAnimalModel = Json("message")

End Function
