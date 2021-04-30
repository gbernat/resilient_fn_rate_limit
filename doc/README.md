<!--
  This User README.md is generated by running:
  "resilient-sdk docgen -p fn_rate_limit --user-guide"

  It is best edited using a Text Editor with a Markdown Previewer. VS Code
  is a good example. Checkout https://guides.github.com/features/mastering-markdown/
  for tips on writing with Markdown

  If you make manual edits and run docgen again, a .bak file will be created

  Store any screenshots in the "doc/screenshots" directory and reference them like:
  ![screenshot: screenshot_1](./screenshots/screenshot_1.png)
-->

# **User Guide:** fn_rate_limit_v1.0.0

## Table of Contents
- [Key Features](#key-features)
- [Function - Rate Limit: Add resource request](#function---rate-limit-add-resource-request)
- [Rules](#rules)

---

## Key Features
<!--
  List the Key Features of the Integration
-->
* Key Feature 1
* Key Feature 2
* Key Feature 3

---

## Function - Rate Limit: Add resource request
Registers a new request for the resource. Returns whether Rate Limit is triggered.

 ![screenshot: fn-rate-limit-add-resource-request ](./screenshots/fn-rate-limit-add-resource-request.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `rate_limit_event_data` | `text` | No | `-` | Additional information |
| `rate_limit_resource` | `text` | No | `-` | - |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

```python
results = {
    # TODO: Copy and paste an example of the Function Output within this code block.
    # To view the output of a Function, run resilient-circuits in DEBUG mode and invoke the Function. 
    # The Function results will be printed in the logs: "resilient-circuits run --loglevel=DEBUG"
}
```

</p>
</details>

<details><summary>Workflows</summary>

  <details><summary>Example Pre-Process Script:</summary>
  <p>

  ```python
  inputs.rate_limit_resource = 'deshabilitar_usuario_ad'
inputs.rate_limit_event_data = 'Registrado en Incidente [{}]'.format(incident.id)
  ```

  </p>
  </details>

  <details><summary>Example Post-Process Script:</summary>
  <p>

  ```python
  incident.addNote(str(results))
  ```

  </p>
  </details>

</details>

---




## Rules
| Rule Name | Object | Workflow Triggered |
| --------- | ------ | ------------------ |
| Add resource request | incident | `add_resource_request` |

---

<!--
## Inform Resilient Users
  Use this section to optionally provide additional information so that Resilient playbook 
  designer can get the maximum benefit of your integration.
-->