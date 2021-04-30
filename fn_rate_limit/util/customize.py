# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_rate_limit"""

try:
    from resilient import ImportDefinition
except ImportError:
    # Support Apps running on resilient-circuits < v35.0.195
    from resilient_circuits.util import ImportDefinition


def codegen_reload_data():
    """
    Parameters required reload codegen for the fn_rate_limit package
    """
    return {
        "package": u"fn_rate_limit",
        "message_destinations": [u"fn_rate_limit"],
        "functions": [u"rate_limit_add_resource_request"],
        "workflows": [u"add_resource_request"],
        "actions": [u"Add resource request"],
        "incident_fields": [],
        "incident_artifact_types": [],
        "datatables": [],
        "automatic_tasks": [],
        "scripts": []
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    Contents:
    - Message Destinations:
        - fn_rate_limit
    - Functions:
        - rate_limit_add_resource_request
    - Workflows:
        - add_resource_request
    - Rules:
        - Add resource request
    """

    yield ImportDefinition(u"""
eyJhY3Rpb25fb3JkZXIiOiBbXSwgImFjdGlvbnMiOiBbeyJhdXRvbWF0aW9ucyI6IFtdLCAiY29u
ZGl0aW9ucyI6IFtdLCAiZW5hYmxlZCI6IHRydWUsICJleHBvcnRfa2V5IjogIkFkZCByZXNvdXJj
ZSByZXF1ZXN0IiwgImlkIjogNDI4LCAibG9naWNfdHlwZSI6ICJhbGwiLCAibWVzc2FnZV9kZXN0
aW5hdGlvbnMiOiBbXSwgIm5hbWUiOiAiQWRkIHJlc291cmNlIHJlcXVlc3QiLCAib2JqZWN0X3R5
cGUiOiAiaW5jaWRlbnQiLCAidGFncyI6IFtdLCAidGltZW91dF9zZWNvbmRzIjogODY0MDAsICJ0
eXBlIjogMSwgInV1aWQiOiAiMzNmM2JhYWEtMzE3ZS00ZjAyLWE1ZjctNGIyZTRmNTBiMWQ2Iiwg
InZpZXdfaXRlbXMiOiBbXSwgIndvcmtmbG93cyI6IFsiYWRkX3Jlc291cmNlX3JlcXVlc3QiXX1d
LCAiYXBwcyI6IFtdLCAiYXV0b21hdGljX3Rhc2tzIjogW10sICJleHBvcnRfZGF0ZSI6IDE2MTk2
OTQyMjIzNzYsICJleHBvcnRfZm9ybWF0X3ZlcnNpb24iOiAyLCAiZmllbGRzIjogW3siYWxsb3df
ZGVmYXVsdF92YWx1ZSI6IGZhbHNlLCAiYmxhbmtfb3B0aW9uIjogZmFsc2UsICJjYWxjdWxhdGVk
IjogZmFsc2UsICJjaGFuZ2VhYmxlIjogdHJ1ZSwgImNob3NlbiI6IGZhbHNlLCAiZGVmYXVsdF9j
aG9zZW5fYnlfc2VydmVyIjogZmFsc2UsICJkZXByZWNhdGVkIjogZmFsc2UsICJleHBvcnRfa2V5
IjogIl9fZnVuY3Rpb24vcmF0ZV9saW1pdF9yZXNvdXJjZSIsICJoaWRlX25vdGlmaWNhdGlvbiI6
IGZhbHNlLCAiaWQiOiAxMTExLCAiaW5wdXRfdHlwZSI6ICJ0ZXh0IiwgImludGVybmFsIjogZmFs
c2UsICJpc190cmFja2VkIjogZmFsc2UsICJuYW1lIjogInJhdGVfbGltaXRfcmVzb3VyY2UiLCAi
b3BlcmF0aW9uX3Blcm1zIjoge30sICJvcGVyYXRpb25zIjogW10sICJwbGFjZWhvbGRlciI6ICIi
LCAicHJlZml4IjogbnVsbCwgInJlYWRfb25seSI6IGZhbHNlLCAicmljaF90ZXh0IjogZmFsc2Us
ICJ0YWdzIjogW10sICJ0ZW1wbGF0ZXMiOiBbXSwgInRleHQiOiAicmF0ZV9saW1pdF9yZXNvdXJj
ZSIsICJ0b29sdGlwIjogIiIsICJ0eXBlX2lkIjogMTEsICJ1dWlkIjogImFlOTdiZWY1LTY0YTkt
NDBmNi05NTJlLTA5MGJkMWJiZGY5YyIsICJ2YWx1ZXMiOiBbXX0sIHsiYWxsb3dfZGVmYXVsdF92
YWx1ZSI6IGZhbHNlLCAiYmxhbmtfb3B0aW9uIjogZmFsc2UsICJjYWxjdWxhdGVkIjogZmFsc2Us
ICJjaGFuZ2VhYmxlIjogdHJ1ZSwgImNob3NlbiI6IGZhbHNlLCAiZGVmYXVsdF9jaG9zZW5fYnlf
c2VydmVyIjogZmFsc2UsICJkZXByZWNhdGVkIjogZmFsc2UsICJleHBvcnRfa2V5IjogIl9fZnVu
Y3Rpb24vcmF0ZV9saW1pdF9ldmVudF9kYXRhIiwgImhpZGVfbm90aWZpY2F0aW9uIjogZmFsc2Us
ICJpZCI6IDExMTIsICJpbnB1dF90eXBlIjogInRleHQiLCAiaW50ZXJuYWwiOiBmYWxzZSwgImlz
X3RyYWNrZWQiOiBmYWxzZSwgIm5hbWUiOiAicmF0ZV9saW1pdF9ldmVudF9kYXRhIiwgIm9wZXJh
dGlvbl9wZXJtcyI6IHt9LCAib3BlcmF0aW9ucyI6IFtdLCAicGxhY2Vob2xkZXIiOiAiIiwgInBy
ZWZpeCI6IG51bGwsICJyZWFkX29ubHkiOiBmYWxzZSwgInJpY2hfdGV4dCI6IGZhbHNlLCAidGFn
cyI6IFtdLCAidGVtcGxhdGVzIjogW10sICJ0ZXh0IjogInJhdGVfbGltaXRfZXZlbnRfZGF0YSIs
ICJ0b29sdGlwIjogIkFkZGl0aW9uYWwgaW5mb3JtYXRpb24iLCAidHlwZV9pZCI6IDExLCAidXVp
ZCI6ICIyMDU2NDFhNS00NjA3LTRiNWUtOTkwMi1jNDA5YWJkYzMzMDMiLCAidmFsdWVzIjogW119
LCB7ImV4cG9ydF9rZXkiOiAiaW5jaWRlbnQvaW50ZXJuYWxfY3VzdG9taXphdGlvbnNfZmllbGQi
LCAiaWQiOiAwLCAiaW5wdXRfdHlwZSI6ICJ0ZXh0IiwgImludGVybmFsIjogdHJ1ZSwgIm5hbWUi
OiAiaW50ZXJuYWxfY3VzdG9taXphdGlvbnNfZmllbGQiLCAicmVhZF9vbmx5IjogdHJ1ZSwgInRl
eHQiOiAiQ3VzdG9taXphdGlvbnMgRmllbGQgKGludGVybmFsKSIsICJ0eXBlX2lkIjogMCwgInV1
aWQiOiAiYmZlZWMyZDQtMzc3MC0xMWU4LWFkMzktNGEwMDA0MDQ0YWExIn1dLCAiZnVuY3Rpb25z
IjogW3siYXBwcyI6IFtdLCAiY3JlYXRlZF9kYXRlIjogMTYxOTYyODE2OTMyMCwgImNyZWF0b3Ii
OiB7ImRpc3BsYXlfbmFtZSI6ICJHdWlkbyBCZXJuYXQgKFRFQ08pIiwgImlkIjogNDAsICJuYW1l
IjogImdiZXJuYXRAcHJvdmVlZG9yLnRlY28uY29tLmFyIiwgInR5cGUiOiAidXNlciJ9LCAiZGVz
Y3JpcHRpb24iOiB7ImZvcm1hdCI6ICJ0ZXh0IiwgImNvbnRlbnQiOiAiUmVnaXN0ZXJzIGEgbmV3
IHJlcXVlc3QgZm9yIHRoZSByZXNvdXJjZS4gUmV0dXJucyB3aGV0aGVyIFJhdGUgTGltaXQgaXMg
dHJpZ2dlcmVkLiJ9LCAiZGVzdGluYXRpb25faGFuZGxlIjogImZuX3JhdGVfbGltaXQiLCAiZGlz
cGxheV9uYW1lIjogIlJhdGUgTGltaXQ6IEFkZCByZXNvdXJjZSByZXF1ZXN0IiwgImV4cG9ydF9r
ZXkiOiAicmF0ZV9saW1pdF9hZGRfcmVzb3VyY2VfcmVxdWVzdCIsICJpZCI6IDE1NSwgImxhc3Rf
bW9kaWZpZWRfYnkiOiB7ImRpc3BsYXlfbmFtZSI6ICJHdWlkbyBCZXJuYXQgKFRFQ08pIiwgImlk
IjogNDAsICJuYW1lIjogImdiZXJuYXRAcHJvdmVlZG9yLnRlY28uY29tLmFyIiwgInR5cGUiOiAi
dXNlciJ9LCAibGFzdF9tb2RpZmllZF90aW1lIjogMTYxOTY5Mjg1NDU1MywgIm5hbWUiOiAicmF0
ZV9saW1pdF9hZGRfcmVzb3VyY2VfcmVxdWVzdCIsICJ0YWdzIjogW10sICJ1dWlkIjogIjAyY2Iw
NjMyLWVlNTEtNGQyYi04YTVmLTYzNDY2YjlmMzcxZSIsICJ2ZXJzaW9uIjogMiwgInZpZXdfaXRl
bXMiOiBbeyJjb250ZW50IjogImFlOTdiZWY1LTY0YTktNDBmNi05NTJlLTA5MGJkMWJiZGY5YyIs
ICJlbGVtZW50IjogImZpZWxkX3V1aWQiLCAiZmllbGRfdHlwZSI6ICJfX2Z1bmN0aW9uIiwgInNo
b3dfaWYiOiBudWxsLCAic2hvd19saW5rX2hlYWRlciI6IGZhbHNlLCAic3RlcF9sYWJlbCI6IG51
bGx9LCB7ImNvbnRlbnQiOiAiMjA1NjQxYTUtNDYwNy00YjVlLTk5MDItYzQwOWFiZGMzMzAzIiwg
ImVsZW1lbnQiOiAiZmllbGRfdXVpZCIsICJmaWVsZF90eXBlIjogIl9fZnVuY3Rpb24iLCAic2hv
d19pZiI6IG51bGwsICJzaG93X2xpbmtfaGVhZGVyIjogZmFsc2UsICJzdGVwX2xhYmVsIjogbnVs
bH1dLCAid29ya2Zsb3dzIjogW3siYWN0aW9ucyI6IFtdLCAiZGVzY3JpcHRpb24iOiBudWxsLCAi
bmFtZSI6ICJBZGQgcmVzb3VyY2UgcmVxdWVzdCIsICJvYmplY3RfdHlwZSI6ICJpbmNpZGVudCIs
ICJwcm9ncmFtbWF0aWNfbmFtZSI6ICJhZGRfcmVzb3VyY2VfcmVxdWVzdCIsICJ0YWdzIjogW10s
ICJ1dWlkIjogbnVsbCwgIndvcmtmbG93X2lkIjogMzI4fV19XSwgImdlb3MiOiBudWxsLCAiZ3Jv
dXBzIjogbnVsbCwgImlkIjogNDEsICJpbmJvdW5kX21haWxib3hlcyI6IG51bGwsICJpbmNpZGVu
dF9hcnRpZmFjdF90eXBlcyI6IFtdLCAiaW5jaWRlbnRfdHlwZXMiOiBbeyJ1cGRhdGVfZGF0ZSI6
IDE2MTk2OTQyMjEwNTMsICJjcmVhdGVfZGF0ZSI6IDE2MTk2OTQyMjEwNTMsICJ1dWlkIjogImJm
ZWVjMmQ0LTM3NzAtMTFlOC1hZDM5LTRhMDAwNDA0NGFhMCIsICJkZXNjcmlwdGlvbiI6ICJDdXN0
b21pemF0aW9uIFBhY2thZ2VzIChpbnRlcm5hbCkiLCAiZXhwb3J0X2tleSI6ICJDdXN0b21pemF0
aW9uIFBhY2thZ2VzIChpbnRlcm5hbCkiLCAibmFtZSI6ICJDdXN0b21pemF0aW9uIFBhY2thZ2Vz
IChpbnRlcm5hbCkiLCAiZW5hYmxlZCI6IGZhbHNlLCAic3lzdGVtIjogZmFsc2UsICJwYXJlbnRf
aWQiOiBudWxsLCAiaGlkZGVuIjogZmFsc2UsICJpZCI6IDB9XSwgImluZHVzdHJpZXMiOiBudWxs
LCAibGF5b3V0cyI6IFtdLCAibG9jYWxlIjogbnVsbCwgIm1lc3NhZ2VfZGVzdGluYXRpb25zIjog
W3siYXBpX2tleXMiOiBbIjBiM2I3MDg4LWU5OTktNGQxNi05MGMyLTU3YjQzY2UyMzAzYyJdLCAi
ZGVzdGluYXRpb25fdHlwZSI6IDAsICJleHBlY3RfYWNrIjogdHJ1ZSwgImV4cG9ydF9rZXkiOiAi
Zm5fcmF0ZV9saW1pdCIsICJuYW1lIjogImZuX3JhdGVfbGltaXQiLCAicHJvZ3JhbW1hdGljX25h
bWUiOiAiZm5fcmF0ZV9saW1pdCIsICJ0YWdzIjogW10sICJ1c2VycyI6IFtdLCAidXVpZCI6ICJm
ODNhNzZiNC0zOWRkLTRhMDUtODYxMC01YmYyNjQ2NTljMDQifV0sICJub3RpZmljYXRpb25zIjog
bnVsbCwgIm92ZXJyaWRlcyI6IFtdLCAicGhhc2VzIjogW10sICJyZWd1bGF0b3JzIjogbnVsbCwg
InJvbGVzIjogW10sICJzY3JpcHRzIjogW10sICJzZXJ2ZXJfdmVyc2lvbiI6IHsiYnVpbGRfbnVt
YmVyIjogNTAsICJtYWpvciI6IDQwLCAibWlub3IiOiAxLCAidmVyc2lvbiI6ICI0MC4xLjUwIn0s
ICJ0YWdzIjogW10sICJ0YXNrX29yZGVyIjogW10sICJ0aW1lZnJhbWVzIjogbnVsbCwgInR5cGVz
IjogW10sICJ3b3JrZmxvd3MiOiBbeyJhY3Rpb25zIjogW10sICJjb250ZW50IjogeyJ2ZXJzaW9u
IjogMSwgIndvcmtmbG93X2lkIjogImFkZF9yZXNvdXJjZV9yZXF1ZXN0IiwgInhtbCI6ICI8P3ht
bCB2ZXJzaW9uPVwiMS4wXCIgZW5jb2Rpbmc9XCJVVEYtOFwiPz48ZGVmaW5pdGlvbnMgeG1sbnM9
XCJodHRwOi8vd3d3Lm9tZy5vcmcvc3BlYy9CUE1OLzIwMTAwNTI0L01PREVMXCIgeG1sbnM6YnBt
bmRpPVwiaHR0cDovL3d3dy5vbWcub3JnL3NwZWMvQlBNTi8yMDEwMDUyNC9ESVwiIHhtbG5zOm9t
Z2RjPVwiaHR0cDovL3d3dy5vbWcub3JnL3NwZWMvREQvMjAxMDA1MjQvRENcIiB4bWxuczpvbWdk
aT1cImh0dHA6Ly93d3cub21nLm9yZy9zcGVjL0RELzIwMTAwNTI0L0RJXCIgeG1sbnM6cmVzaWxp
ZW50PVwiaHR0cDovL3Jlc2lsaWVudC5pYm0uY29tL2JwbW5cIiB4bWxuczp4c2Q9XCJodHRwOi8v
d3d3LnczLm9yZy8yMDAxL1hNTFNjaGVtYVwiIHhtbG5zOnhzaT1cImh0dHA6Ly93d3cudzMub3Jn
LzIwMDEvWE1MU2NoZW1hLWluc3RhbmNlXCIgdGFyZ2V0TmFtZXNwYWNlPVwiaHR0cDovL3d3dy5j
YW11bmRhLm9yZy90ZXN0XCI+PHByb2Nlc3MgaWQ9XCJhZGRfcmVzb3VyY2VfcmVxdWVzdFwiIGlz
RXhlY3V0YWJsZT1cInRydWVcIiBuYW1lPVwiQWRkIHJlc291cmNlIHJlcXVlc3RcIj48ZG9jdW1l
bnRhdGlvbi8+PHN0YXJ0RXZlbnQgaWQ9XCJTdGFydEV2ZW50XzE1NWFzeG1cIj48b3V0Z29pbmc+
U2VxdWVuY2VGbG93XzFobnNrdzk8L291dGdvaW5nPjwvc3RhcnRFdmVudD48c2VydmljZVRhc2sg
aWQ9XCJTZXJ2aWNlVGFza18wN29vanlpXCIgbmFtZT1cIlJhdGUgTGltaXQ6IEFkZCByZXNvdXJj
ZSByZXF1ZXN0XCIgcmVzaWxpZW50OnR5cGU9XCJmdW5jdGlvblwiPjxleHRlbnNpb25FbGVtZW50
cz48cmVzaWxpZW50OmZ1bmN0aW9uIHV1aWQ9XCIwMmNiMDYzMi1lZTUxLTRkMmItOGE1Zi02MzQ2
NmI5ZjM3MWVcIj57XCJpbnB1dHNcIjp7fSxcInBvc3RfcHJvY2Vzc2luZ19zY3JpcHRcIjpcImlu
Y2lkZW50LmFkZE5vdGUoc3RyKHJlc3VsdHMpKVwiLFwicG9zdF9wcm9jZXNzaW5nX3NjcmlwdF9s
YW5ndWFnZVwiOlwicHl0aG9uM1wiLFwicHJlX3Byb2Nlc3Npbmdfc2NyaXB0XCI6XCJpbnB1dHMu
cmF0ZV9saW1pdF9yZXNvdXJjZSA9ICdkZXNoYWJpbGl0YXJfdXN1YXJpb19hZCdcXG5pbnB1dHMu
cmF0ZV9saW1pdF9ldmVudF9kYXRhID0gJ1JlZ2lzdHJhZG8gZW4gSW5jaWRlbnRlIFt7fV0nLmZv
cm1hdChpbmNpZGVudC5pZClcIixcInByZV9wcm9jZXNzaW5nX3NjcmlwdF9sYW5ndWFnZVwiOlwi
cHl0aG9uM1wifTwvcmVzaWxpZW50OmZ1bmN0aW9uPjwvZXh0ZW5zaW9uRWxlbWVudHM+PGluY29t
aW5nPlNlcXVlbmNlRmxvd18xaG5za3c5PC9pbmNvbWluZz48b3V0Z29pbmc+U2VxdWVuY2VGbG93
XzBnMHM4N2U8L291dGdvaW5nPjwvc2VydmljZVRhc2s+PHNlcXVlbmNlRmxvdyBpZD1cIlNlcXVl
bmNlRmxvd18xaG5za3c5XCIgc291cmNlUmVmPVwiU3RhcnRFdmVudF8xNTVhc3htXCIgdGFyZ2V0
UmVmPVwiU2VydmljZVRhc2tfMDdvb2p5aVwiLz48ZW5kRXZlbnQgaWQ9XCJFbmRFdmVudF8xeWJl
Z3pvXCI+PGluY29taW5nPlNlcXVlbmNlRmxvd18wZzBzODdlPC9pbmNvbWluZz48L2VuZEV2ZW50
PjxzZXF1ZW5jZUZsb3cgaWQ9XCJTZXF1ZW5jZUZsb3dfMGcwczg3ZVwiIHNvdXJjZVJlZj1cIlNl
cnZpY2VUYXNrXzA3b29qeWlcIiB0YXJnZXRSZWY9XCJFbmRFdmVudF8xeWJlZ3pvXCIvPjx0ZXh0
QW5ub3RhdGlvbiBpZD1cIlRleHRBbm5vdGF0aW9uXzFreHhpeXRcIj48dGV4dD5TdGFydCB5b3Vy
IHdvcmtmbG93IGhlcmU8L3RleHQ+PC90ZXh0QW5ub3RhdGlvbj48YXNzb2NpYXRpb24gaWQ9XCJB
c3NvY2lhdGlvbl8xc2V1ajQ4XCIgc291cmNlUmVmPVwiU3RhcnRFdmVudF8xNTVhc3htXCIgdGFy
Z2V0UmVmPVwiVGV4dEFubm90YXRpb25fMWt4eGl5dFwiLz48L3Byb2Nlc3M+PGJwbW5kaTpCUE1O
RGlhZ3JhbSBpZD1cIkJQTU5EaWFncmFtXzFcIj48YnBtbmRpOkJQTU5QbGFuZSBicG1uRWxlbWVu
dD1cInVuZGVmaW5lZFwiIGlkPVwiQlBNTlBsYW5lXzFcIj48YnBtbmRpOkJQTU5TaGFwZSBicG1u
RWxlbWVudD1cIlN0YXJ0RXZlbnRfMTU1YXN4bVwiIGlkPVwiU3RhcnRFdmVudF8xNTVhc3htX2Rp
XCI+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIzNlwiIHdpZHRoPVwiMzZcIiB4PVwiMTYyXCIgeT1c
IjE4OFwiLz48YnBtbmRpOkJQTU5MYWJlbD48b21nZGM6Qm91bmRzIGhlaWdodD1cIjBcIiB3aWR0
aD1cIjkwXCIgeD1cIjE1N1wiIHk9XCIyMjNcIi8+PC9icG1uZGk6QlBNTkxhYmVsPjwvYnBtbmRp
OkJQTU5TaGFwZT48YnBtbmRpOkJQTU5TaGFwZSBicG1uRWxlbWVudD1cIlRleHRBbm5vdGF0aW9u
XzFreHhpeXRcIiBpZD1cIlRleHRBbm5vdGF0aW9uXzFreHhpeXRfZGlcIj48b21nZGM6Qm91bmRz
IGhlaWdodD1cIjMwXCIgd2lkdGg9XCIxMDBcIiB4PVwiOTlcIiB5PVwiMjU0XCIvPjwvYnBtbmRp
OkJQTU5TaGFwZT48YnBtbmRpOkJQTU5FZGdlIGJwbW5FbGVtZW50PVwiQXNzb2NpYXRpb25fMXNl
dWo0OFwiIGlkPVwiQXNzb2NpYXRpb25fMXNldWo0OF9kaVwiPjxvbWdkaTp3YXlwb2ludCB4PVwi
MTY5XCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIyMjBcIi8+PG9tZ2RpOndheXBvaW50
IHg9XCIxNTNcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjI1NFwiLz48L2JwbW5kaTpC
UE1ORWRnZT48YnBtbmRpOkJQTU5TaGFwZSBicG1uRWxlbWVudD1cIlNlcnZpY2VUYXNrXzA3b29q
eWlcIiBpZD1cIlNlcnZpY2VUYXNrXzA3b29qeWlfZGlcIj48b21nZGM6Qm91bmRzIGhlaWdodD1c
IjgwXCIgd2lkdGg9XCIxMDBcIiB4PVwiMjkwXCIgeT1cIjE2NlwiLz48L2JwbW5kaTpCUE1OU2hh
cGU+PGJwbW5kaTpCUE1ORWRnZSBicG1uRWxlbWVudD1cIlNlcXVlbmNlRmxvd18xaG5za3c5XCIg
aWQ9XCJTZXF1ZW5jZUZsb3dfMWhuc2t3OV9kaVwiPjxvbWdkaTp3YXlwb2ludCB4PVwiMTk4XCIg
eHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIyMDZcIi8+PG9tZ2RpOndheXBvaW50IHg9XCIy
OTBcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjIwNlwiLz48YnBtbmRpOkJQTU5MYWJl
bD48b21nZGM6Qm91bmRzIGhlaWdodD1cIjEzXCIgd2lkdGg9XCIwXCIgeD1cIjI0NFwiIHk9XCIx
ODRcIi8+PC9icG1uZGk6QlBNTkxhYmVsPjwvYnBtbmRpOkJQTU5FZGdlPjxicG1uZGk6QlBNTlNo
YXBlIGJwbW5FbGVtZW50PVwiRW5kRXZlbnRfMXliZWd6b1wiIGlkPVwiRW5kRXZlbnRfMXliZWd6
b19kaVwiPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMzZcIiB3aWR0aD1cIjM2XCIgeD1cIjQ3MFwi
IHk9XCIxODhcIi8+PGJwbW5kaTpCUE1OTGFiZWw+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIxM1wi
IHdpZHRoPVwiMFwiIHg9XCI0ODhcIiB5PVwiMjI3XCIvPjwvYnBtbmRpOkJQTU5MYWJlbD48L2Jw
bW5kaTpCUE1OU2hhcGU+PGJwbW5kaTpCUE1ORWRnZSBicG1uRWxlbWVudD1cIlNlcXVlbmNlRmxv
d18wZzBzODdlXCIgaWQ9XCJTZXF1ZW5jZUZsb3dfMGcwczg3ZV9kaVwiPjxvbWdkaTp3YXlwb2lu
dCB4PVwiMzkwXCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIyMDZcIi8+PG9tZ2RpOndh
eXBvaW50IHg9XCI0NzBcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjIwNlwiLz48YnBt
bmRpOkJQTU5MYWJlbD48b21nZGM6Qm91bmRzIGhlaWdodD1cIjEzXCIgd2lkdGg9XCIwXCIgeD1c
IjQzMFwiIHk9XCIxODRcIi8+PC9icG1uZGk6QlBNTkxhYmVsPjwvYnBtbmRpOkJQTU5FZGdlPjwv
YnBtbmRpOkJQTU5QbGFuZT48L2JwbW5kaTpCUE1ORGlhZ3JhbT48L2RlZmluaXRpb25zPiJ9LCAi
Y29udGVudF92ZXJzaW9uIjogMSwgImNyZWF0b3JfaWQiOiAiZ2Jlcm5hdEBwcm92ZWVkb3IudGVj
by5jb20uYXIiLCAiZGVzY3JpcHRpb24iOiAiIiwgImV4cG9ydF9rZXkiOiAiYWRkX3Jlc291cmNl
X3JlcXVlc3QiLCAibGFzdF9tb2RpZmllZF9ieSI6ICJnYmVybmF0QHByb3ZlZWRvci50ZWNvLmNv
bS5hciIsICJsYXN0X21vZGlmaWVkX3RpbWUiOiAxNjE5NjkzMTQ3OTUyLCAibmFtZSI6ICJBZGQg
cmVzb3VyY2UgcmVxdWVzdCIsICJvYmplY3RfdHlwZSI6ICJpbmNpZGVudCIsICJwcm9ncmFtbWF0
aWNfbmFtZSI6ICJhZGRfcmVzb3VyY2VfcmVxdWVzdCIsICJ0YWdzIjogW10sICJ1dWlkIjogImUw
ZjNkNTQxLWM3N2EtNDFiYS04MmYwLWU0N2UyYzBlNTc3ZSIsICJ3b3JrZmxvd19pZCI6IDMyOH1d
LCAid29ya3NwYWNlcyI6IFtdfQ==
""")