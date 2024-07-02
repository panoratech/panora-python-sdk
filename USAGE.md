<!-- Start SDK Example Usage [usage] -->
```python
import panora

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.app_controller_hello()

if res.string is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->