# Integração com Salesforce (Apex)

Use Callouts para conectar ao Gateway APIBrasil.

## Código Apex (`APIBrasilService.cls`)

```apex
public class APIBrasilService {
    @AuraEnabled
    public static Map<String, Object> consultarCEP(String cep) {
        Http http = new Http();
        HttpRequest request = new HttpRequest();
        request.setEndpoint('https://gateway.apibrasil.io/api/v2/cep/cep');
        request.setMethod('POST');
        request.setHeader('Content-Type', 'application/json');
        request.setHeader('Authorization', 'Bearer ' + 'SEU_TOKEN');
        request.setHeader('DeviceToken', 'SEU_DEVICE_TOKEN');
        
        // Body
        request.setBody('{"cep": "' + cep + '"}');
        
        HttpResponse response = http.send(request);
        
        if (response.getStatusCode() == 200) {
            return (Map<String, Object>) JSON.deserializeUntyped(response.getBody());
        }
        return null;
    }
}
```

*Nota: Lembre-se de adicionar `https://gateway.apibrasil.io` nas **Remote Site Settings** do Salesforce.*
