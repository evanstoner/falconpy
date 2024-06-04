"""Internal API endpoint constant library.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <https://unlicense.org>
"""

_threatgraph_endpoints = [
  [
    "combined_edges_get",
    "GET",
    "/threatgraph/combined/edges/v1",
    "Retrieve edges for a given vertex id.  One edge type must be specified",
    "threatgraph",
    [
      {
        "type": "string",
        "description": "Vertex ID to get details for.  Only one value is supported",
        "name": "ids",
        "in": "query",
        "required": True
      },
      {
        "maximum": 100,
        "type": "integer",
        "default": 100,
        "description": "How many edges to return in a single request [1-100]",
        "name": "limit",
        "in": "query"
      },
      {
        "type": "string",
        "description": "The offset to use to retrieve the next page of results",
        "name": "offset",
        "in": "query"
      },
      {
        "enum": [
          "accessed_ad_computer",
          "accessed_adfs_application",
          "accessed_azure_application",
          "accessed_by_kerberos_ticket",
          "accessed_by_session",
          "accessed_okta_application",
          "accessed_ping_fed_application",
          "accessed_service_account",
          "agent_to_self_diagnostic",
          "allowed_by_process",
          "allowed_firewall_rule",
          "app_uninstalled_from_host",
          "asep_file_change",
          "asep_key_update",
          "asep_value_update",
          "assigned_ipv4_address",
          "assigned_ipv6_address",
          "assigned_to_sensor",
          "associated_by_ad_computer",
          "associated_by_ad_group",
          "associated_by_ad_user",
          "associated_by_aggregate_indicator",
          "associated_by_app",
          "associated_by_azure_ad_user",
          "associated_by_azure_app",
          "associated_by_certificate",
          "associated_by_control_graph",
          "associated_by_domain",
          "associated_by_host",
          "associated_by_host_name",
          "associated_by_idp_session",
          "associated_by_incident",
          "associated_by_indicator",
          "associated_by_ip",
          "associated_by_ip4",
          "associated_by_ip6",
          "associated_by_okta_user",
          "associated_by_service_ticket",
          "associated_control_graph",
          "associated_firewall_rule",
          "associated_idp_indicator",
          "associated_incident",
          "associated_indicator",
          "associated_k8s_cluster",
          "associated_k8s_sensor",
          "associated_mobile_forensics_report",
          "associated_mobile_indicator",
          "associated_module",
          "associated_primary_module",
          "associated_quarantined_file",
          "associated_quarantined_module",
          "associated_root_process",
          "associated_to_ad_computer",
          "associated_to_sensor",
          "associated_user_session",
          "associated_with_process",
          "associated_with_sensor",
          "attributed_by_process",
          "attributed_from_domain",
          "attributed_from_module",
          "attributed_on",
          "attributed_on_domain",
          "attributed_on_module",
          "attributed_to",
          "attributed_to_actor",
          "authenticated_from_incident",
          "authenticated_host",
          "blocked_by_app",
          "blocked_by_process",
          "blocked_by_sensor",
          "blocked_dns",
          "blocked_ip4",
          "blocked_ip6",
          "blocked_module",
          "bundled_in_app",
          "bundles_module",
          "cert_is_presented_by",
          "cert_presented",
          "child_process",
          "closed_ip4_socket",
          "closed_ip6_socket",
          "command_history",
          "command_line_parent_process",
          "connected_from_app",
          "connected_from_host",
          "connected_from_process",
          "connected_ip4",
          "connected_ip6",
          "connected_on_customer",
          "connected_on_sensor",
          "connected_to_accessory",
          "connected_to_wifi_ap",
          "connection_killed_by_app",
          "connection_killed_by_process",
          "containerized_app",
          "containerized_by_sensor",
          "control_graph",
          "created_by_incident",
          "created_by_process",
          "created_by_user",
          "created_quarantined_file",
          "created_service",
          "critical_file_accessed",
          "critical_file_modified",
          "customer_agent_has_user",
          "customer_has_sensor",
          "customer_ioc",
          "customer_sensor_to_sensor",
          "customer_user_to_sensor_user",
          "deleted_by_process",
          "deleted_rule",
          "denied_by_firewall_rule",
          "denied_by_process",
          "denied_firewall_rule",
          "detected_module",
          "detection",
          "device",
          "disconnect_from_wifi_ap",
          "disconnected_from_accessory",
          "disconnected_from_host",
          "dns",
          "dns_request",
          "duplicated_by_app",
          "duplicates_app",
          "elf_file_written",
          "established_on_ad_computer",
          "established_on_host_name",
          "established_on_ip4",
          "established_on_ip6",
          "established_on_sensor",
          "established_session",
          "established_user_session",
          "executed_app",
          "executed_by_process",
          "executed_macro_script",
          "executed_script",
          "extracted_file",
          "failed_to_authenticate_ad_user",
          "failed_to_authenticate_to_ad_computer",
          "failed_to_authenticate_to_adfs_app",
          "failed_to_authenticate_to_azure_app",
          "failed_to_authenticate_to_okta_app",
          "failed_to_authenticate_to_ping_app",
          "failed_to_authenticate_to_service_account",
          "file_create_info",
          "file_open_info",
          "fs_post_create",
          "fs_post_open",
          "generated_by_renewing",
          "generated_by_session",
          "generated_dce_rpc_epm_request_against_dc",
          "generated_dce_rpc_request_against_dc",
          "generated_failed_authentication_to_ad_computer",
          "generated_failed_authentication_to_adfs_app",
          "generated_failed_authentication_to_azure_app",
          "generated_failed_authentication_to_okta_app",
          "generated_failed_authentication_to_ping_app",
          "generated_failed_authentication_to_service_account",
          "generated_ldap_search_against_dc",
          "generated_service_ticket",
          "had_code_injected_by_process",
          "has_app_installed",
          "has_attributed_process",
          "has_attribution",
          "has_firmware",
          "hunting_lead",
          "implicated_by_incident",
          "implicated_sensor",
          "included_by_hunting_lead",
          "includes_process",
          "indexed",
          "initiated_by_ad_computer",
          "initiated_by_azure_ad_user",
          "initiated_by_okta_user",
          "initiated_by_user",
          "initiated_session",
          "injected_code_into_process",
          "injected_thread",
          "injected_thread_from_process",
          "installed_app",
          "installed_by_app",
          "installed_on_host",
          "invalid_firewall_rule",
          "invalid_from_process",
          "invalidated_by_process",
          "invalidated_firewall_rule",
          "involved_ad_computer",
          "involved_service_account",
          "ip4_socket_closed_by_app",
          "ip4_socket_closed_by_process",
          "ip4_socket_opened_by_process",
          "ip6_socket_closed_by_app",
          "ip6_socket_closed_by_process",
          "ip6_socket_opened_by_process",
          "ipv4",
          "ipv4_close",
          "ipv4_listen",
          "ipv6",
          "ipv6_close",
          "ipv6_listen",
          "jar_file_written",
          "killed_ip4_connection",
          "killed_ip6_connection",
          "known_by_md5",
          "known_by_sha256",
          "linking_event",
          "loaded_by_process",
          "loaded_module",
          "macho_file_written",
          "macro_executed_by_process",
          "member_of_full_command_line",
          "module",
          "module_written",
          "mounted_on_host",
          "mounted_to_host",
          "network_close_ip4",
          "network_close_ip6",
          "network_connect_ip4",
          "network_connect_ip6",
          "network_listen_ip4",
          "network_listen_ip6",
          "new_executable_written",
          "new_script_written",
          "opened_ip4_socket",
          "opened_ip6_socket",
          "parent_of_command_line",
          "parent_process",
          "parented_by_process",
          "participating_process",
          "pe_file_written",
          "performed_psexec_against_dc",
          "presented_by_cloud",
          "primary_module",
          "primary_module_of_process",
          "quarantined_file",
          "queried_by_process",
          "queried_by_sensor",
          "queried_dns",
          "queried_on_customer",
          "queried_on_sensor",
          "received_from_cloud",
          "registered_by_incident",
          "registered_scheduledtask",
          "renewed_to_generate",
          "reports_aggregate_indicator",
          "resolved_from_domain",
          "resolved_to_ip4",
          "resolved_to_ip6",
          "rooted_control_graph",
          "rule_set_by_process",
          "script",
          "self_diagnostic_to_agent",
          "set_by_process",
          "set_firewall_rule",
          "set_rule",
          "shell_io_redirect",
          "suspicious_dns_request",
          "trigger_process",
          "triggered_by_control_graph",
          "triggered_by_process",
          "triggered_control_graph",
          "triggered_detection",
          "triggered_indicator",
          "triggered_mobile_indicator",
          "triggered_xdr",
          "triggering_domain",
          "triggering_network",
          "uncontainerized_app",
          "uncontainerized_by_sensor",
          "uninstalled_app",
          "unmounted_from_host",
          "unmounted_on_host",
          "user",
          "user_session",
          "witnessed_by_sensor",
          "witnessed_process",
          "wmicreated_by_incident",
          "wmicreated_process",
          "written_by_process",
          "wrote_module"
        ],
        "type": "string",
        "description": "The type of edges that you would like to retrieve",
        "name": "edge_type",
        "in": "query",
        "required": True
      },
      {
        "type": "string",
        "description": "The direction of edges that you would like to retrieve.",
        "name": "direction",
        "in": "query"
      },
      {
        "enum": [
          "cspm",
          "customer",
          "cwpp",
          "device",
          "global"
        ],
        "type": "string",
        "default": "device",
        "description": "Scope of the request",
        "name": "scope",
        "in": "query"
      },
      {
        "type": "boolean",
        "default": False,
        "description": "Return nano-precision entity timestamps",
        "name": "nano",
        "in": "query"
      }
    ]
  ],
  [
    "combined_ran_on_get",
    "GET",
    "/threatgraph/combined/ran-on/v1",
    "Look up instances of indicators such as hashes, domain names, and ip addresses that have been seen on "
    "devices in your environment.",
    "threatgraph",
    [
      {
        "type": "string",
        "description": "The value of the indicator to search by.",
        "name": "value",
        "in": "query",
        "required": True
      },
      {
        "enum": [
          "domain",
          "ipv4",
          "ipv6",
          "md5",
          "sha1",
          "sha256"
        ],
        "type": "string",
        "description": "The type of indicator that you would like to retrieve",
        "name": "type",
        "in": "query",
        "required": True
      },
      {
        "maximum": 100,
        "type": "integer",
        "default": 100,
        "description": "How many edges to return in a single request [1-100]",
        "name": "limit",
        "in": "query"
      },
      {
        "type": "string",
        "description": "The offset to use to retrieve the next page of results",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "boolean",
        "default": False,
        "description": "Return nano-precision entity timestamps",
        "name": "nano",
        "in": "query"
      }
    ]
  ],
  [
    "combined_summary_get",
    "GET",
    "/threatgraph/combined/{}/summary/v1",
    "Retrieve summary for a given vertex ID",
    "threatgraph",
    [
      {
        "enum": [
          "accessories",
          "accessory",
          "actor",
          "ad-computers",
          "ad-groups",
          "ad_computer",
          "ad_group",
          "adfs-applications",
          "adfs_application",
          "aggregate-indicators",
          "aggregate_indicator",
          "any-vertex",
          "azure-ad-users",
          "azure-applications",
          "azure_ad_user",
          "azure_application",
          "certificate",
          "certificates",
          "command-lines",
          "command_line",
          "containerized-apps",
          "containerized_app",
          "control-graphs",
          "control_graph",
          "customer",
          "customers",
          "detection",
          "detection-indices",
          "detection_index",
          "detections",
          "devices",
          "direct",
          "directs",
          "domain",
          "domains",
          "extracted-files",
          "extracted_file",
          "firewall",
          "firewall_rule_match",
          "firewall_rule_matches",
          "firewalls",
          "firmware",
          "firmwares",
          "host-names",
          "host_name",
          "hunting-leads",
          "hunting_lead",
          "idp-indicators",
          "idp-sessions",
          "idp_indicator",
          "idp_session",
          "incident",
          "incidents",
          "indicator",
          "indicators",
          "ipv4",
          "ipv6",
          "k8s_cluster",
          "k8s_clusters",
          "kerberos-tickets",
          "kerberos_ticket",
          "legacy-detections",
          "legacy_detection",
          "macro_script",
          "macro_scripts",
          "mobile-apps",
          "mobile-fs-volumes",
          "mobile-indicators",
          "mobile_app",
          "mobile_fs_volume",
          "mobile_indicator",
          "mobile_os_forensics_report",
          "mobile_os_forensics_reports",
          "module",
          "modules",
          "okta-applications",
          "okta-users",
          "okta_application",
          "okta_user",
          "ping-fed-applications",
          "ping_fed_application",
          "process",
          "processes",
          "quarantined-files",
          "quarantined_file",
          "script",
          "scripts",
          "sensor",
          "sensor-self-diagnostics",
          "sensor_self_diagnostic",
          "tag",
          "tags",
          "user-sessions",
          "user_id",
          "user_session",
          "users",
          "wifi-access-points",
          "wifi_access_point",
          "xdr"
        ],
        "type": "string",
        "description": "Type of vertex to get properties for",
        "name": "vertex-type",
        "in": "path",
        "required": True
      },
      {
        "maxItems": 100,
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "Vertex ID to get details for",
        "name": "ids",
        "in": "query",
        "required": True
      },
      {
        "enum": [
          "cspm",
          "customer",
          "cwpp",
          "device",
          "global"
        ],
        "type": "string",
        "default": "device",
        "description": "Scope of the request",
        "name": "scope",
        "in": "query"
      },
      {
        "type": "boolean",
        "default": False,
        "description": "Return nano-precision entity timestamps",
        "name": "nano",
        "in": "query"
      }
    ]
  ],
  [
    "entities_vertices_get",
    "GET",
    "/threatgraph/entities/{}/v1",
    "Retrieve metadata for a given vertex ID",
    "threatgraph",
    [
      {
        "enum": [
          "accessories",
          "accessory",
          "actor",
          "ad-computers",
          "ad-groups",
          "ad_computer",
          "ad_group",
          "adfs-applications",
          "adfs_application",
          "aggregate-indicators",
          "aggregate_indicator",
          "any-vertex",
          "azure-ad-users",
          "azure-applications",
          "azure_ad_user",
          "azure_application",
          "certificate",
          "certificates",
          "command-lines",
          "command_line",
          "containerized-apps",
          "containerized_app",
          "control-graphs",
          "control_graph",
          "customer",
          "customers",
          "detection",
          "detection-indices",
          "detection_index",
          "detections",
          "devices",
          "direct",
          "directs",
          "domain",
          "domains",
          "extracted-files",
          "extracted_file",
          "firewall",
          "firewall_rule_match",
          "firewall_rule_matches",
          "firewalls",
          "firmware",
          "firmwares",
          "host-names",
          "host_name",
          "hunting-leads",
          "hunting_lead",
          "idp-indicators",
          "idp-sessions",
          "idp_indicator",
          "idp_session",
          "incident",
          "incidents",
          "indicator",
          "indicators",
          "ipv4",
          "ipv6",
          "k8s_cluster",
          "k8s_clusters",
          "kerberos-tickets",
          "kerberos_ticket",
          "legacy-detections",
          "legacy_detection",
          "macro_script",
          "macro_scripts",
          "mobile-apps",
          "mobile-fs-volumes",
          "mobile-indicators",
          "mobile_app",
          "mobile_fs_volume",
          "mobile_indicator",
          "mobile_os_forensics_report",
          "mobile_os_forensics_reports",
          "module",
          "modules",
          "okta-applications",
          "okta-users",
          "okta_application",
          "okta_user",
          "ping-fed-applications",
          "ping_fed_application",
          "process",
          "processes",
          "quarantined-files",
          "quarantined_file",
          "script",
          "scripts",
          "sensor",
          "sensor-self-diagnostics",
          "sensor_self_diagnostic",
          "tag",
          "tags",
          "user-sessions",
          "user_id",
          "user_session",
          "users",
          "wifi-access-points",
          "wifi_access_point",
          "xdr"
        ],
        "type": "string",
        "description": "Type of vertex to get properties for",
        "name": "vertex-type",
        "in": "path",
        "required": True
      },
      {
        "maxItems": 100,
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "Vertex ID to get details for",
        "name": "ids",
        "in": "query",
        "required": True
      },
      {
        "enum": [
          "cspm",
          "customer",
          "cwpp",
          "device",
          "global"
        ],
        "type": "string",
        "default": "device",
        "description": "Scope of the request",
        "name": "scope",
        "in": "query"
      },
      {
        "type": "boolean",
        "default": False,
        "description": "Return nano-precision entity timestamps",
        "name": "nano",
        "in": "query"
      }
    ]
  ],
  [
    "entities_vertices_getv2",
    "GET",
    "/threatgraph/entities/{}/v2",
    "Retrieve metadata for a given vertex ID",
    "threatgraph",
    [
      {
        "enum": [
          "accessories",
          "accessory",
          "actor",
          "ad-computers",
          "ad-groups",
          "ad_computer",
          "ad_group",
          "adfs-applications",
          "adfs_application",
          "aggregate-indicators",
          "aggregate_indicator",
          "any-vertex",
          "azure-ad-users",
          "azure-applications",
          "azure_ad_user",
          "azure_application",
          "certificate",
          "certificates",
          "command-lines",
          "command_line",
          "containerized-apps",
          "containerized_app",
          "control-graphs",
          "control_graph",
          "customer",
          "customers",
          "detection",
          "detection-indices",
          "detection_index",
          "detections",
          "devices",
          "direct",
          "directs",
          "domain",
          "domains",
          "extracted-files",
          "extracted_file",
          "firewall",
          "firewall_rule_match",
          "firewall_rule_matches",
          "firewalls",
          "firmware",
          "firmwares",
          "host-names",
          "host_name",
          "hunting-leads",
          "hunting_lead",
          "idp-indicators",
          "idp-sessions",
          "idp_indicator",
          "idp_session",
          "incident",
          "incidents",
          "indicator",
          "indicators",
          "ipv4",
          "ipv6",
          "k8s_cluster",
          "k8s_clusters",
          "kerberos-tickets",
          "kerberos_ticket",
          "legacy-detections",
          "legacy_detection",
          "macro_script",
          "macro_scripts",
          "mobile-apps",
          "mobile-fs-volumes",
          "mobile-indicators",
          "mobile_app",
          "mobile_fs_volume",
          "mobile_indicator",
          "mobile_os_forensics_report",
          "mobile_os_forensics_reports",
          "module",
          "modules",
          "okta-applications",
          "okta-users",
          "okta_application",
          "okta_user",
          "ping-fed-applications",
          "ping_fed_application",
          "process",
          "processes",
          "quarantined-files",
          "quarantined_file",
          "script",
          "scripts",
          "sensor",
          "sensor-self-diagnostics",
          "sensor_self_diagnostic",
          "tag",
          "tags",
          "user-sessions",
          "user_id",
          "user_session",
          "users",
          "wifi-access-points",
          "wifi_access_point",
          "xdr"
        ],
        "type": "string",
        "description": "Type of vertex to get properties for",
        "name": "vertex-type",
        "in": "path",
        "required": True
      },
      {
        "maxItems": 100,
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "Vertex ID to get details for",
        "name": "ids",
        "in": "query",
        "required": True
      },
      {
        "enum": [
          "cspm",
          "customer",
          "cwpp",
          "device",
          "global"
        ],
        "type": "string",
        "default": "device",
        "description": "Scope of the request",
        "name": "scope",
        "in": "query"
      },
      {
        "type": "boolean",
        "default": False,
        "description": "Return nano-precision entity timestamps",
        "name": "nano",
        "in": "query"
      }
    ]
  ],
  [
    "queries_edgetypes_get",
    "GET",
    "/threatgraph/queries/edge-types/v1",
    "Show all available edge types",
    "threatgraph",
    []
  ]
]
