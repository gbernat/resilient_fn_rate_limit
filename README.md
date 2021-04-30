<!--
  This Install README.md is generated by running:
  "resilient-sdk docgen -p fn_rate_limit --install-guide"

  It is best edited using a Text Editor with a Markdown Previewer. VS Code
  is a good example. Checkout https://guides.github.com/features/mastering-markdown/
  for tips on writing with Markdown

  If you make manual edits and run docgen again, a .bak file will be created

  Store any screenshots in the "doc/screenshots" directory and reference them like:
  ![screenshot: screenshot_1](./doc/screenshots/screenshot_1.png)
-->

# fn-rate-limit Functions for IBM Resilient

- [Release Notes](#release-notes)
- [Overview](#overview)
- [Requirements](#requirements)
- [Installation](#installation)
- [Uninstall](#uninstall)
- [Troubleshooting](#troubleshooting)
- [Support](#support)

---

## Release Notes
<!--
  Specify all changes in this release. Do not remove the release 
  notes of a previous release
-->
### v1.0.0
* Initial Release

---

## Overview
<!--
  Provide a high-level description of the function itself and its remote software or application.
  The text below is parsed from the "description" and "long_description" attributes in the setup.py file
-->
**Resilient Circuits Components for 'fn_rate_limit'**

 ![screenshot: main](./doc/screenshots/main.png)

Resilient Circuits Components for 'fn_rate_limit'

---

## Requirements
<!--
  List any Requirements 
-->
* Resilient platform >= `v40.1.50`
* An Integration Server running `resilient_circuits>=30.0.0`
  * To set up an Integration Server see: [ibm.biz/res-int-server-guide](https://ibm.biz/res-int-server-guide)
  * If using API Keys, minimum required permissions are:
      * Org Data: Read, Edit
      * Function: Read
---

## Installation
* Download the `fn_rate_limit.zip`.
* Copy the `.zip` to your Integration Server and SSH into it.
* **Unzip** the package:
  ```
  $ unzip fn_rate_limit-x.x.x.zip
  ```
* **Change Directory** into the unzipped directory:
  ```
  $ cd fn_rate_limit-x.x.x
  ```
* **Install** the package:
  ```
  $ pip install fn_rate_limit-x.x.x.tar.gz
  ```
* Import the **configurations** into your app.config file:
  ```
  $ resilient-circuits config -u -l fn-rate-limit
  ```
* Import the fn_rate_limit **customizations** into the Resilient platform:
  ```
  $ resilient-circuits customize -y -l fn-rate-limit
  ```
* Open the config file, scroll to the bottom and edit your fn_rate_limit configurations:
  ```
  $ nano ~/.resilient/app.config
  ```
  | Config | Required | Example | Description |
  | ------ | :------: | ------- | ----------- |
  | **db_user** | Yes | `USER` | *Enter a description of the config here* |
  | **db_password** | Yes | `PASSWORD` | *Enter a description of the config here* |
  | **db_host** | Yes | `127.0.0.1` | *Enter a description of the config here* |
  | **db_port** | Yes | `3306` | *Enter a description of the config here* |
  | **database** | Yes | `Rate_limit` | *Enter a description of the config here* |

* **Save** and **Close** the app.config file.
* [Optional]: Run selftest to test the Integration you configured:
  ```
  $ resilient-circuits selftest -l fn-rate-limit
  ```
* **Run** resilient-circuits or restart the Service on Windows/Linux:
  ```
  $ resilient-circuits run
  ```


---

## Uninstall
* SSH into your Integration Server.
* **Uninstall** the package:
  ```
  $ pip uninstall fn-rate-limit
  ```
* Open the config file, scroll to the [fn_rate_limit] section and remove the section or prefix `#` to comment out the section.
* **Save** and **Close** the app.config file.

---

## Troubleshooting
There are several ways to verify the successful operation of a function.

### Resilient Action Status
* When viewing an incident, use the Actions menu to view **Action Status**.
* By default, pending and errors are displayed.
* Modify the filter for actions to also show Completed actions.
* Clicking on an action displays additional information on the progress made or what error occurred.

### Resilient Scripting Log
* A separate log file is available to review scripting errors.
* This is useful when issues occur in the pre-processing or post-processing scripts.
* The default location for this log file is: `/var/log/resilient-scripting/resilient-scripting.log`.

### Resilient Logs
* By default, Resilient logs are retained at `/usr/share/co3/logs`.
* The `client.log` may contain additional information regarding the execution of functions.

### Resilient-Circuits
* The log is controlled in the `.resilient/app.config` file under the section [resilient] and the property `logdir`.
* The default file name is `app.log`.
* Each function will create progress information.
* Failures will show up as errors and may contain python trace statements.

---

<!--
  If necessary, use this section to describe how to configure your security application to work with the integration.
  Delete this section if the user does not need to perform any configuration procedures on your product.

## Configure <Product_Name>

* Step One
* Step Two
* Step Three

---
-->

## Support
| Name | Version | Author | Support URL |
| ---- | ------- | ------ | ----------- |
| fn_rate_limit | 1.0.0 | Guido Bernat | <<your company url>> |