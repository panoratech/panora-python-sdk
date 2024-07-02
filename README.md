# panora-python

<div align="left">
    <a href="https://speakeasyapi.dev/"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" style="width: 100px; height: 28px;" />
    </a>
</div>


## 🏗 **Welcome to your new SDK!** 🏗

It has been generated successfully based on your OpenAPI spec. However, it is not yet ready for production use. Here are some next steps:
- [ ] 🛠 Make your SDK feel handcrafted by [customizing it](https://www.speakeasyapi.dev/docs/customize-sdks)
- [ ] ♻️ Refine your SDK quickly by iterating locally with the [Speakeasy CLI](https://github.com/speakeasy-api/speakeasy)
- [ ] 🎁 Publish your SDK to package managers by [configuring automatic publishing](https://www.speakeasyapi.dev/docs/advanced-setup/publish-sdks)
- [ ] ✨ When ready to productionize, delete this section from the README

<!-- Start SDK Installation [installation] -->
## SDK Installation

```bash
pip install git+https://github.com/panoratech/panora-python-sdk.git
```
<!-- End SDK Installation [installation] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

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

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

### [Panora SDK](docs/sdks/panora/README.md)

* [app_controller_hello](docs/sdks/panora/README.md#app_controller_hello)
* [get_health](docs/sdks/panora/README.md#get_health)
* [get_hello_protected](docs/sdks/panora/README.md#get_hello_protected)

### [auth](docs/sdks/auth/README.md)

* [sign_up](docs/sdks/auth/README.md#sign_up) - Register
* [sign_in](docs/sdks/auth/README.md#sign_in) - Log In
* [get_panora_core_users](docs/sdks/auth/README.md#get_panora_core_users) - Get users
* [auth_controller_get_profile](docs/sdks/auth/README.md#auth_controller_get_profile)
* [get_api_keys](docs/sdks/auth/README.md#get_api_keys) - Retrieve API Keys
* [delete_api_key](docs/sdks/auth/README.md#delete_api_key) - Delete API Keys
* [generate_api_key](docs/sdks/auth/README.md#generate_api_key) - Create API Key
* [refresh_access_token](docs/sdks/auth/README.md#refresh_access_token) - Refresh Access Token

### [connections](docs/sdks/connections/README.md)

* [handle_o_auth_callback](docs/sdks/connections/README.md#handle_o_auth_callback) - Capture oAuth callback
* [handle_api_key_callback](docs/sdks/connections/README.md#handle_api_key_callback) - Capture api key callback
* [get_connections](docs/sdks/connections/README.md#get_connections) - List Connections

### [webhook](docs/sdks/webhook/README.md)

* [get_webhooks_metadata](docs/sdks/webhook/README.md#get_webhooks_metadata) - Retrieve webhooks metadata 
* [create_webhook_metadata](docs/sdks/webhook/README.md#create_webhook_metadata) - Add webhook metadata
* [delete_webhook](docs/sdks/webhook/README.md#delete_webhook) - Delete Webhook
* [update_webhook_status](docs/sdks/webhook/README.md#update_webhook_status) - Update webhook status
* [verify_event](docs/sdks/webhook/README.md#verify_event) - Verify payload sgnature of the webhook

### [managed_webhooks](docs/sdks/managedwebhooks/README.md)

* [get_managed_webhooks](docs/sdks/managedwebhooks/README.md#get_managed_webhooks) - Retrieve managed webhooks
* [update_managed_webhooks_status](docs/sdks/managedwebhooks/README.md#update_managed_webhooks_status) - Update managed webhook status
* [create_managed_webhook](docs/sdks/managedwebhooks/README.md#create_managed_webhook) - Create managed webhook
* [create_remote_third_party_webhook](docs/sdks/managedwebhooks/README.md#create_remote_third_party_webhook) - Create Remote Third Party Webhook

### [mw](docs/sdks/mw/README.md)

* [handle_third_party_webhook](docs/sdks/mw/README.md#handle_third_party_webhook) - Handle Third Party Webhook

### [ticketing_tickets](docs/sdks/ticketingtickets/README.md)

* [get_tickets](docs/sdks/ticketingtickets/README.md#get_tickets) - List a batch of Tickets
* [add_ticket](docs/sdks/ticketingtickets/README.md#add_ticket) - Create a Ticket
* [get_ticket](docs/sdks/ticketingtickets/README.md#get_ticket) - Retrieve a Ticket

### [ticketing_users](docs/sdks/ticketingusers/README.md)

* [get_ticketing_users](docs/sdks/ticketingusers/README.md#get_ticketing_users) - List a batch of Users
* [get_ticketing_user](docs/sdks/ticketingusers/README.md#get_ticketing_user) - Retrieve a User

### [ticketing_accounts](docs/sdks/ticketingaccounts/README.md)

* [get_ticketing_accounts](docs/sdks/ticketingaccounts/README.md#get_ticketing_accounts) - List a batch of Accounts
* [get_ticketing_account](docs/sdks/ticketingaccounts/README.md#get_ticketing_account) - Retrieve an Account

### [ticketing_contacts](docs/sdks/ticketingcontacts/README.md)

* [get_ticketing_contacts](docs/sdks/ticketingcontacts/README.md#get_ticketing_contacts) - List all Contacts
* [get_ticketing_contact](docs/sdks/ticketingcontacts/README.md#get_ticketing_contact) - Retrieve a Contact

### [crm_companies](docs/sdks/crmcompanies/README.md)

* [get_companies](docs/sdks/crmcompanies/README.md#get_companies) - List a batch of Companies
* [add_crm_company](docs/sdks/crmcompanies/README.md#add_crm_company) - Create a Company
* [update_company](docs/sdks/crmcompanies/README.md#update_company) - Update a Company
* [get_crm_company](docs/sdks/crmcompanies/README.md#get_crm_company) - Retrieve a Company

### [crm_contacts](docs/sdks/crmcontacts/README.md)

* [list_crm_contacts](docs/sdks/crmcontacts/README.md#list_crm_contacts) - List CRM Contacts
* [add_crm_contact](docs/sdks/crmcontacts/README.md#add_crm_contact) - Create CRM Contact
* [get_crm_contact](docs/sdks/crmcontacts/README.md#get_crm_contact) - Retrieve a CRM Contact

### [crm_deals](docs/sdks/crmdeals/README.md)

* [get_deals](docs/sdks/crmdeals/README.md#get_deals) - List a batch of Deals
* [add_deal](docs/sdks/crmdeals/README.md#add_deal) - Create a Deal
* [get_deal](docs/sdks/crmdeals/README.md#get_deal) - Retrieve a Deal

### [crm_engagements](docs/sdks/crmengagements/README.md)

* [get_engagements](docs/sdks/crmengagements/README.md#get_engagements) - List a batch of Engagements
* [add_engagement](docs/sdks/crmengagements/README.md#add_engagement) - Create a Engagement
* [get_engagement](docs/sdks/crmengagements/README.md#get_engagement) - Retrieve a Engagement

### [crm_notes](docs/sdks/crmnotes/README.md)

* [get_notes](docs/sdks/crmnotes/README.md#get_notes) - List a batch of Notes
* [add_note](docs/sdks/crmnotes/README.md#add_note) - Create a Note
* [get_note](docs/sdks/crmnotes/README.md#get_note) - Retrieve a Note

### [crm_stages](docs/sdks/crmstages/README.md)

* [get_stages](docs/sdks/crmstages/README.md#get_stages) - List a batch of Stages
* [get_stage](docs/sdks/crmstages/README.md#get_stage) - Retrieve a Stage

### [crm_tasks](docs/sdks/crmtasks/README.md)

* [get_tasks](docs/sdks/crmtasks/README.md#get_tasks) - List a batch of Tasks
* [add_task](docs/sdks/crmtasks/README.md#add_task) - Create a Task
* [get_task](docs/sdks/crmtasks/README.md#get_task) - Retrieve a Task

### [crm_users](docs/sdks/crmusers/README.md)

* [get_crm_users](docs/sdks/crmusers/README.md#get_crm_users) - List a batch of Users
* [get_crm_user](docs/sdks/crmusers/README.md#get_crm_user) - Retrieve a User

### [ticketing_collections](docs/sdks/ticketingcollections/README.md)

* [get_collections](docs/sdks/ticketingcollections/README.md#get_collections) - List a batch of Collections
* [get_collection](docs/sdks/ticketingcollections/README.md#get_collection) - Retrieve a Collection

### [ticketing_comments](docs/sdks/ticketingcomments/README.md)

* [get_comments](docs/sdks/ticketingcomments/README.md#get_comments) - List a batch of Comments
* [add_comment](docs/sdks/ticketingcomments/README.md#add_comment) - Create a Comment
* [get_comment](docs/sdks/ticketingcomments/README.md#get_comment) - Retrieve a Comment

### [ticketing_tags](docs/sdks/ticketingtags/README.md)

* [get_ticketing_tags](docs/sdks/ticketingtags/README.md#get_ticketing_tags) - List a batch of Tags
* [get_ticketing_tag](docs/sdks/ticketingtags/README.md#get_ticketing_tag) - Retrieve a Tag

### [ticketing_teams](docs/sdks/ticketingteams/README.md)

* [get_teams](docs/sdks/ticketingteams/README.md#get_teams) - List a batch of Teams
* [get_team](docs/sdks/ticketingteams/README.md#get_team) - Retrieve a Team

### [linked_users](docs/sdks/linkedusers/README.md)

* [add_linked_user](docs/sdks/linkedusers/README.md#add_linked_user) - Add Linked User
* [fetch_linked_users](docs/sdks/linkedusers/README.md#fetch_linked_users) - Retrieve Linked Users
* [add_batch_linked_users](docs/sdks/linkedusers/README.md#add_batch_linked_users) - Add Batch Linked Users
* [get_linked_user](docs/sdks/linkedusers/README.md#get_linked_user) - Retrieve a Linked User
* [linked_user_from_remote_id](docs/sdks/linkedusers/README.md#linked_user_from_remote_id) - Retrieve a Linked User From A Remote Id

### [organisations](docs/sdks/organisations/README.md)

* [get_organisations](docs/sdks/organisations/README.md#get_organisations) - Retrieve Organisations
* [create_organisation](docs/sdks/organisations/README.md#create_organisation) - Create an Organisation

### [projects](docs/sdks/projects/README.md)

* [get_projects](docs/sdks/projects/README.md#get_projects) - Retrieve projects
* [create_project](docs/sdks/projects/README.md#create_project) - Create a project

### [field_mappings](docs/sdks/fieldmappings/README.md)

* [get_field_mappings_entities](docs/sdks/fieldmappings/README.md#get_field_mappings_entities) - Retrieve field mapping entities
* [get_field_mappings](docs/sdks/fieldmappings/README.md#get_field_mappings) - Retrieve field mappings
* [get_field_mapping_values](docs/sdks/fieldmappings/README.md#get_field_mapping_values) - Retrieve field mappings values
* [define_target_field](docs/sdks/fieldmappings/README.md#define_target_field) - Define target Field
* [create_custom_field](docs/sdks/fieldmappings/README.md#create_custom_field) - Create Custom Field
* [map_field](docs/sdks/fieldmappings/README.md#map_field) - Map Custom Field
* [get_custom_provider_properties](docs/sdks/fieldmappings/README.md#get_custom_provider_properties) - Retrieve Custom Properties

### [events](docs/sdks/events/README.md)

* [get_panora_core_events](docs/sdks/events/README.md#get_panora_core_events) - Retrieve Events
* [get_events_count](docs/sdks/events/README.md#get_events_count) - Retrieve Events Count

### [magic_links](docs/sdks/magiclinks/README.md)

* [create_magic_link](docs/sdks/magiclinks/README.md#create_magic_link) - Create a Magic Link
* [get_magic_links](docs/sdks/magiclinks/README.md#get_magic_links) - Retrieve Magic Links
* [get_magic_link](docs/sdks/magiclinks/README.md#get_magic_link) - Retrieve a Magic Link

### [passthrough](docs/sdks/passthrough/README.md)

* [passthrough_request](docs/sdks/passthrough/README.md#passthrough_request) - Make a passthrough request

### [connections_strategies](docs/sdks/connectionsstrategies/README.md)

* [create_connection_strategy](docs/sdks/connectionsstrategies/README.md#create_connection_strategy) - Create Connection Strategy
* [toggle_connection_strategy](docs/sdks/connectionsstrategies/README.md#toggle_connection_strategy) - Activate/Deactivate Connection Strategy
* [delete_connection_strategy](docs/sdks/connectionsstrategies/README.md#delete_connection_strategy) - Delete Connection Strategy
* [update_connection_strategy](docs/sdks/connectionsstrategies/README.md#update_connection_strategy) - Update Connection Strategy
* [get_connection_strategy_credentials](docs/sdks/connectionsstrategies/README.md#get_connection_strategy_credentials) - Get Connection Strategy Credential
* [get_credentials](docs/sdks/connectionsstrategies/README.md#get_credentials) - Fetch credentials info needed for connections
* [get_connection_strategies_for_project](docs/sdks/connectionsstrategies/README.md#get_connection_strategies_for_project) - Fetch All Connection Strategies for Project

### [syncs](docs/sdks/syncs/README.md)

* [get_sync_status](docs/sdks/syncs/README.md#get_sync_status) - Retrieve sync status of a certain vertical
* [resync](docs/sdks/syncs/README.md#resync) - Resync common objects across a vertical

### [project_connectors](docs/sdks/projectconnectors/README.md)

* [update_connectors_to_project](docs/sdks/projectconnectors/README.md#update_connectors_to_project) - Update Connectors for a project
* [get_connectors_from_project](docs/sdks/projectconnectors/README.md#get_connectors_from_project) - Retrieve connectors by Project Id

### [hris_bankinfo](docs/sdks/hrisbankinfo/README.md)

* [get_bankinfos](docs/sdks/hrisbankinfo/README.md#get_bankinfos) - List a batch of Bankinfos
* [add_bankinfo](docs/sdks/hrisbankinfo/README.md#add_bankinfo) - Create a Bankinfo
* [get_bankinfo](docs/sdks/hrisbankinfo/README.md#get_bankinfo) - Retrieve a Bankinfo

### [hris_benefit](docs/sdks/hrisbenefit/README.md)

* [get_benefits](docs/sdks/hrisbenefit/README.md#get_benefits) - List a batch of Benefits
* [add_benefit](docs/sdks/hrisbenefit/README.md#add_benefit) - Create a Benefit
* [get_benefit](docs/sdks/hrisbenefit/README.md#get_benefit) - Retrieve a Benefit

### [hris_company](docs/sdks/hriscompany/README.md)

* [get_companys](docs/sdks/hriscompany/README.md#get_companys) - List a batch of Companys
* [add_hris_company](docs/sdks/hriscompany/README.md#add_hris_company) - Create a Company
* [get_hris_company](docs/sdks/hriscompany/README.md#get_hris_company) - Retrieve a Company

### [hris_dependent](docs/sdks/hrisdependent/README.md)

* [get_dependents](docs/sdks/hrisdependent/README.md#get_dependents) - List a batch of Dependents
* [add_dependent](docs/sdks/hrisdependent/README.md#add_dependent) - Create a Dependent
* [get_dependent](docs/sdks/hrisdependent/README.md#get_dependent) - Retrieve a Dependent

### [hris_employeepayrollrun](docs/sdks/hrisemployeepayrollrun/README.md)

* [get_employee_payroll_runs](docs/sdks/hrisemployeepayrollrun/README.md#get_employee_payroll_runs) - List a batch of EmployeePayrollRuns
* [add_employee_payroll_run](docs/sdks/hrisemployeepayrollrun/README.md#add_employee_payroll_run) - Create a EmployeePayrollRun
* [get_employee_payroll_run](docs/sdks/hrisemployeepayrollrun/README.md#get_employee_payroll_run) - Retrieve a EmployeePayrollRun

### [hris_employee](docs/sdks/hrisemployee/README.md)

* [get_employees](docs/sdks/hrisemployee/README.md#get_employees) - List a batch of Employees
* [add_employee](docs/sdks/hrisemployee/README.md#add_employee) - Create a Employee
* [get_employee](docs/sdks/hrisemployee/README.md#get_employee) - Retrieve a Employee

### [hris_employerbenefit](docs/sdks/hrisemployerbenefit/README.md)

* [get_employer_benefits](docs/sdks/hrisemployerbenefit/README.md#get_employer_benefits) - List a batch of EmployerBenefits
* [add_employer_benefit](docs/sdks/hrisemployerbenefit/README.md#add_employer_benefit) - Create a EmployerBenefit
* [get_employer_benefit](docs/sdks/hrisemployerbenefit/README.md#get_employer_benefit) - Retrieve a EmployerBenefit

### [hris_employment](docs/sdks/hrisemployment/README.md)

* [get_employments](docs/sdks/hrisemployment/README.md#get_employments) - List a batch of Employments
* [add_employment](docs/sdks/hrisemployment/README.md#add_employment) - Create a Employment
* [get_employment](docs/sdks/hrisemployment/README.md#get_employment) - Retrieve a Employment

### [hris_group](docs/sdks/hrisgroup/README.md)

* [get_groups](docs/sdks/hrisgroup/README.md#get_groups) - List a batch of Groups
* [add_group](docs/sdks/hrisgroup/README.md#add_group) - Create a Group
* [get_group](docs/sdks/hrisgroup/README.md#get_group) - Retrieve a Group

### [hris_location](docs/sdks/hrislocation/README.md)

* [get_locations](docs/sdks/hrislocation/README.md#get_locations) - List a batch of Locations
* [add_location](docs/sdks/hrislocation/README.md#add_location) - Create a Location
* [get_location](docs/sdks/hrislocation/README.md#get_location) - Retrieve a Location

### [hris_paygroup](docs/sdks/hrispaygroup/README.md)

* [get_pay_groups](docs/sdks/hrispaygroup/README.md#get_pay_groups) - List a batch of PayGroups
* [add_pay_group](docs/sdks/hrispaygroup/README.md#add_pay_group) - Create a PayGroup
* [get_pay_group](docs/sdks/hrispaygroup/README.md#get_pay_group) - Retrieve a PayGroup

### [hris_payrollrun](docs/sdks/hrispayrollrun/README.md)

* [get_payroll_runs](docs/sdks/hrispayrollrun/README.md#get_payroll_runs) - List a batch of PayrollRuns
* [add_payroll_run](docs/sdks/hrispayrollrun/README.md#add_payroll_run) - Create a PayrollRun
* [get_payroll_run](docs/sdks/hrispayrollrun/README.md#get_payroll_run) - Retrieve a PayrollRun

### [hris_timeoff](docs/sdks/hristimeoff/README.md)

* [get_timeoffs](docs/sdks/hristimeoff/README.md#get_timeoffs) - List a batch of Timeoffs
* [add_timeoff](docs/sdks/hristimeoff/README.md#add_timeoff) - Create a Timeoff
* [get_timeoff](docs/sdks/hristimeoff/README.md#get_timeoff) - Retrieve a Timeoff

### [hris_timeoffbalance](docs/sdks/hristimeoffbalance/README.md)

* [get_timeoff_balances](docs/sdks/hristimeoffbalance/README.md#get_timeoff_balances) - List a batch of TimeoffBalances
* [add_timeoff_balance](docs/sdks/hristimeoffbalance/README.md#add_timeoff_balance) - Create a TimeoffBalance
* [get_timeoff_balance](docs/sdks/hristimeoffbalance/README.md#get_timeoff_balance) - Retrieve a TimeoffBalance

### [marketingautomation_action](docs/sdks/marketingautomationaction/README.md)

* [get_actions](docs/sdks/marketingautomationaction/README.md#get_actions) - List a batch of Actions
* [add_action](docs/sdks/marketingautomationaction/README.md#add_action) - Create a Action
* [get_action](docs/sdks/marketingautomationaction/README.md#get_action) - Retrieve a Action

### [marketingautomation_automation](docs/sdks/marketingautomationautomation/README.md)

* [get_automations](docs/sdks/marketingautomationautomation/README.md#get_automations) - List a batch of Automations
* [add_automation](docs/sdks/marketingautomationautomation/README.md#add_automation) - Create a Automation
* [get_automation](docs/sdks/marketingautomationautomation/README.md#get_automation) - Retrieve a Automation

### [marketingautomation_campaign](docs/sdks/marketingautomationcampaign/README.md)

* [get_campaigns](docs/sdks/marketingautomationcampaign/README.md#get_campaigns) - List a batch of Campaigns
* [add_campaign](docs/sdks/marketingautomationcampaign/README.md#add_campaign) - Create a Campaign
* [get_campaign](docs/sdks/marketingautomationcampaign/README.md#get_campaign) - Retrieve a Campaign

### [marketingautomation_contact](docs/sdks/marketingautomationcontact/README.md)

* [get_marketing_automation_contacts](docs/sdks/marketingautomationcontact/README.md#get_marketing_automation_contacts) - List a batch of Contacts
* [add_marketing_automation_contact](docs/sdks/marketingautomationcontact/README.md#add_marketing_automation_contact) - Create a Contact
* [get_marketing_automation_contact](docs/sdks/marketingautomationcontact/README.md#get_marketing_automation_contact) - Retrieve a Contact

### [marketingautomation_email](docs/sdks/marketingautomationemail/README.md)

* [get_emails](docs/sdks/marketingautomationemail/README.md#get_emails) - List a batch of Emails
* [add_email](docs/sdks/marketingautomationemail/README.md#add_email) - Create a Email
* [get_email](docs/sdks/marketingautomationemail/README.md#get_email) - Retrieve a Email

### [marketingautomation_event](docs/sdks/marketingautomationevent/README.md)

* [get_marketing_automation_events](docs/sdks/marketingautomationevent/README.md#get_marketing_automation_events) - List a batch of Events
* [add_event](docs/sdks/marketingautomationevent/README.md#add_event) - Create a Event
* [get_event](docs/sdks/marketingautomationevent/README.md#get_event) - Retrieve a Event

### [marketingautomation_list](docs/sdks/marketingautomationlist/README.md)

* [get_lists](docs/sdks/marketingautomationlist/README.md#get_lists) - List a batch of Lists
* [add_list](docs/sdks/marketingautomationlist/README.md#add_list) - Create a List
* [get_list](docs/sdks/marketingautomationlist/README.md#get_list) - Retrieve a List

### [marketingautomation_message](docs/sdks/marketingautomationmessage/README.md)

* [get_messages](docs/sdks/marketingautomationmessage/README.md#get_messages) - List a batch of Messages
* [add_message](docs/sdks/marketingautomationmessage/README.md#add_message) - Create a Message
* [get_message](docs/sdks/marketingautomationmessage/README.md#get_message) - Retrieve a Message

### [marketingautomation_template](docs/sdks/marketingautomationtemplate/README.md)

* [get_templates](docs/sdks/marketingautomationtemplate/README.md#get_templates) - List a batch of Templates
* [add_template](docs/sdks/marketingautomationtemplate/README.md#add_template) - Create a Template
* [get_template](docs/sdks/marketingautomationtemplate/README.md#get_template) - Retrieve a Template

### [marketingautomation_user](docs/sdks/marketingautomationuser/README.md)

* [get_marketing_automation_users](docs/sdks/marketingautomationuser/README.md#get_marketing_automation_users) - List a batch of Users
* [add_marketing_automation_user](docs/sdks/marketingautomationuser/README.md#add_marketing_automation_user) - Create a User
* [get_marketing_automation_user](docs/sdks/marketingautomationuser/README.md#get_marketing_automation_user) - Retrieve a User

### [ats_activity](docs/sdks/atsactivity/README.md)

* [get_activitys](docs/sdks/atsactivity/README.md#get_activitys) - List a batch of Activitys
* [add_activity](docs/sdks/atsactivity/README.md#add_activity) - Create a Activity
* [get_activity](docs/sdks/atsactivity/README.md#get_activity) - Retrieve a Activity

### [ats_application](docs/sdks/atsapplication/README.md)

* [get_applications](docs/sdks/atsapplication/README.md#get_applications) - List a batch of Applications
* [add_application](docs/sdks/atsapplication/README.md#add_application) - Create a Application
* [get_application](docs/sdks/atsapplication/README.md#get_application) - Retrieve a Application

### [ats_attachment](docs/sdks/atsattachment/README.md)

* [get_ats_attachments](docs/sdks/atsattachment/README.md#get_ats_attachments) - List a batch of Attachments
* [add_ats_attachment](docs/sdks/atsattachment/README.md#add_ats_attachment) - Create a Attachment
* [get_ats_attachment](docs/sdks/atsattachment/README.md#get_ats_attachment) - Retrieve a Attachment

### [ats_candidate](docs/sdks/atscandidate/README.md)

* [get_candidates](docs/sdks/atscandidate/README.md#get_candidates) - List a batch of Candidates
* [add_candidate](docs/sdks/atscandidate/README.md#add_candidate) - Create a Candidate
* [get_candidate](docs/sdks/atscandidate/README.md#get_candidate) - Retrieve a Candidate

### [ats_department](docs/sdks/atsdepartment/README.md)

* [get_departments](docs/sdks/atsdepartment/README.md#get_departments) - List a batch of Departments
* [add_department](docs/sdks/atsdepartment/README.md#add_department) - Create a Department
* [get_department](docs/sdks/atsdepartment/README.md#get_department) - Retrieve a Department

### [ats_interview](docs/sdks/atsinterview/README.md)

* [get_interviews](docs/sdks/atsinterview/README.md#get_interviews) - List a batch of Interviews
* [add_interview](docs/sdks/atsinterview/README.md#add_interview) - Create a Interview
* [get_interview](docs/sdks/atsinterview/README.md#get_interview) - Retrieve a Interview

### [ats_jobinterviewstage](docs/sdks/atsjobinterviewstage/README.md)

* [get_job_interview_stages](docs/sdks/atsjobinterviewstage/README.md#get_job_interview_stages) - List a batch of JobInterviewStages
* [add_job_interview_stage](docs/sdks/atsjobinterviewstage/README.md#add_job_interview_stage) - Create a JobInterviewStage
* [get_job_interview_stage](docs/sdks/atsjobinterviewstage/README.md#get_job_interview_stage) - Retrieve a JobInterviewStage

### [ats_job](docs/sdks/atsjob/README.md)

* [get_jobs](docs/sdks/atsjob/README.md#get_jobs) - List a batch of Jobs
* [add_job](docs/sdks/atsjob/README.md#add_job) - Create a Job
* [get_job](docs/sdks/atsjob/README.md#get_job) - Retrieve a Job

### [ats_offer](docs/sdks/atsoffer/README.md)

* [get_offers](docs/sdks/atsoffer/README.md#get_offers) - List a batch of Offers
* [add_offer](docs/sdks/atsoffer/README.md#add_offer) - Create a Offer
* [get_offer](docs/sdks/atsoffer/README.md#get_offer) - Retrieve a Offer

### [ats_office](docs/sdks/atsoffice/README.md)

* [get_offices](docs/sdks/atsoffice/README.md#get_offices) - List a batch of Offices
* [add_office](docs/sdks/atsoffice/README.md#add_office) - Create a Office
* [get_office](docs/sdks/atsoffice/README.md#get_office) - Retrieve a Office

### [ats_rejectreason](docs/sdks/atsrejectreason/README.md)

* [get_reject_reasons](docs/sdks/atsrejectreason/README.md#get_reject_reasons) - List a batch of RejectReasons
* [add_reject_reason](docs/sdks/atsrejectreason/README.md#add_reject_reason) - Create a RejectReason
* [get_reject_reason](docs/sdks/atsrejectreason/README.md#get_reject_reason) - Retrieve a RejectReason

### [ats_scorecard](docs/sdks/atsscorecard/README.md)

* [get_score_cards](docs/sdks/atsscorecard/README.md#get_score_cards) - List a batch of ScoreCards
* [add_score_card](docs/sdks/atsscorecard/README.md#add_score_card) - Create a ScoreCard
* [get_score_card](docs/sdks/atsscorecard/README.md#get_score_card) - Retrieve a ScoreCard

### [ats_screeningquestion](docs/sdks/atsscreeningquestion/README.md)

* [get_screening_questions](docs/sdks/atsscreeningquestion/README.md#get_screening_questions) - List a batch of ScreeningQuestions
* [add_screening_question](docs/sdks/atsscreeningquestion/README.md#add_screening_question) - Create a ScreeningQuestion
* [get_screening_question](docs/sdks/atsscreeningquestion/README.md#get_screening_question) - Retrieve a ScreeningQuestion

### [ats_tag](docs/sdks/atstag/README.md)

* [get_ats_tags](docs/sdks/atstag/README.md#get_ats_tags) - List a batch of Tags
* [add_tag](docs/sdks/atstag/README.md#add_tag) - Create a Tag
* [get_ats_tag](docs/sdks/atstag/README.md#get_ats_tag) - Retrieve a Tag

### [ats_user](docs/sdks/atsuser/README.md)

* [get_ats_users](docs/sdks/atsuser/README.md#get_ats_users) - List a batch of Users
* [add_ats_user](docs/sdks/atsuser/README.md#add_ats_user) - Create a User
* [get_ats_user](docs/sdks/atsuser/README.md#get_ats_user) - Retrieve a User

### [ats_eeocs](docs/sdks/atseeocs/README.md)

* [get_eeocss](docs/sdks/atseeocs/README.md#get_eeocss) - List a batch of Eeocss
* [add_eeocs](docs/sdks/atseeocs/README.md#add_eeocs) - Create a Eeocs
* [get_eeocs](docs/sdks/atseeocs/README.md#get_eeocs) - Retrieve a Eeocs

### [accounting_account](docs/sdks/accountingaccount/README.md)

* [get_accounting_accounts](docs/sdks/accountingaccount/README.md#get_accounting_accounts) - List a batch of Accounts
* [add_account](docs/sdks/accountingaccount/README.md#add_account) - Create a Account
* [get_accounting_account](docs/sdks/accountingaccount/README.md#get_accounting_account) - Retrieve a Account

### [accounting_address](docs/sdks/accountingaddress/README.md)

* [get_addresss](docs/sdks/accountingaddress/README.md#get_addresss) - List a batch of Addresss
* [add_address](docs/sdks/accountingaddress/README.md#add_address) - Create a Address
* [get_address](docs/sdks/accountingaddress/README.md#get_address) - Retrieve a Address

### [accounting_attachment](docs/sdks/accountingattachment/README.md)

* [get_accounting_attachments](docs/sdks/accountingattachment/README.md#get_accounting_attachments) - List a batch of Attachments
* [add_accounting_attachment](docs/sdks/accountingattachment/README.md#add_accounting_attachment) - Create a Attachment
* [get_accounting_attachment](docs/sdks/accountingattachment/README.md#get_accounting_attachment) - Retrieve a Attachment

### [accounting_balancesheet](docs/sdks/accountingbalancesheet/README.md)

* [get_balance_sheets](docs/sdks/accountingbalancesheet/README.md#get_balance_sheets) - List a batch of BalanceSheets
* [add_balance_sheet](docs/sdks/accountingbalancesheet/README.md#add_balance_sheet) - Create a BalanceSheet
* [get_balance_sheet](docs/sdks/accountingbalancesheet/README.md#get_balance_sheet) - Retrieve a BalanceSheet

### [accounting_cashflowstatement](docs/sdks/accountingcashflowstatement/README.md)

* [get_cashflow_statements](docs/sdks/accountingcashflowstatement/README.md#get_cashflow_statements) - List a batch of CashflowStatements
* [add_cashflow_statement](docs/sdks/accountingcashflowstatement/README.md#add_cashflow_statement) - Create a CashflowStatement
* [get_cashflow_statement](docs/sdks/accountingcashflowstatement/README.md#get_cashflow_statement) - Retrieve a CashflowStatement

### [accounting_companyinfo](docs/sdks/accountingcompanyinfo/README.md)

* [get_company_infos](docs/sdks/accountingcompanyinfo/README.md#get_company_infos) - List a batch of CompanyInfos
* [add_company_info](docs/sdks/accountingcompanyinfo/README.md#add_company_info) - Create a CompanyInfo
* [get_company_info](docs/sdks/accountingcompanyinfo/README.md#get_company_info) - Retrieve a CompanyInfo

### [accounting_contact](docs/sdks/accountingcontact/README.md)

* [get_accounting_contacts](docs/sdks/accountingcontact/README.md#get_accounting_contacts) - List a batch of Contacts
* [add_accounting_contact](docs/sdks/accountingcontact/README.md#add_accounting_contact) - Create a Contact
* [get_accounting_contact](docs/sdks/accountingcontact/README.md#get_accounting_contact) - Retrieve a Contact

### [accounting_creditnote](docs/sdks/accountingcreditnote/README.md)

* [get_credit_notes](docs/sdks/accountingcreditnote/README.md#get_credit_notes) - List a batch of CreditNotes
* [add_credit_note](docs/sdks/accountingcreditnote/README.md#add_credit_note) - Create a CreditNote
* [get_credit_note](docs/sdks/accountingcreditnote/README.md#get_credit_note) - Retrieve a CreditNote

### [accounting_expense](docs/sdks/accountingexpense/README.md)

* [get_expenses](docs/sdks/accountingexpense/README.md#get_expenses) - List a batch of Expenses
* [add_expense](docs/sdks/accountingexpense/README.md#add_expense) - Create a Expense
* [get_expense](docs/sdks/accountingexpense/README.md#get_expense) - Retrieve a Expense

### [accounting_incomestatement](docs/sdks/accountingincomestatement/README.md)

* [get_income_statements](docs/sdks/accountingincomestatement/README.md#get_income_statements) - List a batch of IncomeStatements
* [add_income_statement](docs/sdks/accountingincomestatement/README.md#add_income_statement) - Create a IncomeStatement
* [get_income_statement](docs/sdks/accountingincomestatement/README.md#get_income_statement) - Retrieve a IncomeStatement

### [accounting_invoice](docs/sdks/accountinginvoice/README.md)

* [get_invoices](docs/sdks/accountinginvoice/README.md#get_invoices) - List a batch of Invoices
* [add_invoice](docs/sdks/accountinginvoice/README.md#add_invoice) - Create a Invoice
* [get_invoice](docs/sdks/accountinginvoice/README.md#get_invoice) - Retrieve a Invoice

### [accounting_item](docs/sdks/accountingitem/README.md)

* [get_items](docs/sdks/accountingitem/README.md#get_items) - List a batch of Items
* [add_item](docs/sdks/accountingitem/README.md#add_item) - Create a Item
* [get_item](docs/sdks/accountingitem/README.md#get_item) - Retrieve a Item

### [accounting_journalentry](docs/sdks/accountingjournalentry/README.md)

* [get_journal_entrys](docs/sdks/accountingjournalentry/README.md#get_journal_entrys) - List a batch of JournalEntrys
* [add_journal_entry](docs/sdks/accountingjournalentry/README.md#add_journal_entry) - Create a JournalEntry
* [get_journal_entry](docs/sdks/accountingjournalentry/README.md#get_journal_entry) - Retrieve a JournalEntry

### [accounting_payment](docs/sdks/accountingpayment/README.md)

* [get_payments](docs/sdks/accountingpayment/README.md#get_payments) - List a batch of Payments
* [add_payment](docs/sdks/accountingpayment/README.md#add_payment) - Create a Payment
* [get_payment](docs/sdks/accountingpayment/README.md#get_payment) - Retrieve a Payment

### [accounting_phonenumber](docs/sdks/accountingphonenumber/README.md)

* [get_phone_numbers](docs/sdks/accountingphonenumber/README.md#get_phone_numbers) - List a batch of PhoneNumbers
* [add_phone_number](docs/sdks/accountingphonenumber/README.md#add_phone_number) - Create a PhoneNumber
* [get_phone_number](docs/sdks/accountingphonenumber/README.md#get_phone_number) - Retrieve a PhoneNumber

### [accounting_purchaseorder](docs/sdks/accountingpurchaseorder/README.md)

* [get_purchase_orders](docs/sdks/accountingpurchaseorder/README.md#get_purchase_orders) - List a batch of PurchaseOrders
* [add_purchase_order](docs/sdks/accountingpurchaseorder/README.md#add_purchase_order) - Create a PurchaseOrder
* [get_purchase_order](docs/sdks/accountingpurchaseorder/README.md#get_purchase_order) - Retrieve a PurchaseOrder

### [accounting_taxrate](docs/sdks/accountingtaxrate/README.md)

* [get_tax_rates](docs/sdks/accountingtaxrate/README.md#get_tax_rates) - List a batch of TaxRates
* [add_tax_rate](docs/sdks/accountingtaxrate/README.md#add_tax_rate) - Create a TaxRate
* [get_tax_rate](docs/sdks/accountingtaxrate/README.md#get_tax_rate) - Retrieve a TaxRate

### [accounting_trackingcategory](docs/sdks/accountingtrackingcategory/README.md)

* [get_tracking_categorys](docs/sdks/accountingtrackingcategory/README.md#get_tracking_categorys) - List a batch of TrackingCategorys
* [add_tracking_category](docs/sdks/accountingtrackingcategory/README.md#add_tracking_category) - Create a TrackingCategory
* [get_tracking_category](docs/sdks/accountingtrackingcategory/README.md#get_tracking_category) - Retrieve a TrackingCategory

### [accounting_transaction](docs/sdks/accountingtransaction/README.md)

* [get_transactions](docs/sdks/accountingtransaction/README.md#get_transactions) - List a batch of Transactions
* [add_transaction](docs/sdks/accountingtransaction/README.md#add_transaction) - Create a Transaction
* [get_transaction](docs/sdks/accountingtransaction/README.md#get_transaction) - Retrieve a Transaction

### [accounting_vendorcredit](docs/sdks/accountingvendorcredit/README.md)

* [get_vendor_credits](docs/sdks/accountingvendorcredit/README.md#get_vendor_credits) - List a batch of VendorCredits
* [add_vendor_credit](docs/sdks/accountingvendorcredit/README.md#add_vendor_credit) - Create a VendorCredit
* [get_vendor_credit](docs/sdks/accountingvendorcredit/README.md#get_vendor_credit) - Retrieve a VendorCredit

### [filestorage_drive](docs/sdks/filestoragedrive/README.md)

* [get_drives](docs/sdks/filestoragedrive/README.md#get_drives) - List a batch of Drives
* [add_drive](docs/sdks/filestoragedrive/README.md#add_drive) - Create a Drive
* [get_drive](docs/sdks/filestoragedrive/README.md#get_drive) - Retrieve a Drive

### [filestorage_file](docs/sdks/filestoragefile/README.md)

* [get_files](docs/sdks/filestoragefile/README.md#get_files) - List a batch of Files
* [add_file](docs/sdks/filestoragefile/README.md#add_file) - Create a File
* [get_file](docs/sdks/filestoragefile/README.md#get_file) - Retrieve a File

### [filestorage_folder](docs/sdks/filestoragefolder/README.md)

* [get_folders](docs/sdks/filestoragefolder/README.md#get_folders) - List a batch of Folders
* [add_folder](docs/sdks/filestoragefolder/README.md#add_folder) - Create a Folder
* [get_folder](docs/sdks/filestoragefolder/README.md#get_folder) - Retrieve a Folder

### [filestorage_sharedlink](docs/sdks/filestoragesharedlink/README.md)

* [get_sharedlinks](docs/sdks/filestoragesharedlink/README.md#get_sharedlinks) - List a batch of Sharedlinks
* [add_sharedlink](docs/sdks/filestoragesharedlink/README.md#add_sharedlink) - Create a Sharedlink
* [get_sharedlink](docs/sdks/filestoragesharedlink/README.md#get_sharedlink) - Retrieve a Sharedlink

### [filestorage_permission](docs/sdks/filestoragepermission/README.md)

* [get_permissions](docs/sdks/filestoragepermission/README.md#get_permissions) - List a batch of Permissions
* [add_permission](docs/sdks/filestoragepermission/README.md#add_permission) - Create a Permission
* [get_permission](docs/sdks/filestoragepermission/README.md#get_permission) - Retrieve a Permission

### [ticketing_attachments](docs/sdks/ticketingattachments/README.md)

* [get_ticketing_attachments](docs/sdks/ticketingattachments/README.md#get_ticketing_attachments) - List a batch of Attachments
* [add_ticketing_attachment](docs/sdks/ticketingattachments/README.md#add_ticketing_attachment) - Create a Attachment
* [get_ticketing_attachment](docs/sdks/ticketingattachments/README.md#get_ticketing_attachment) - Retrieve a Attachment
* [download_attachment](docs/sdks/ticketingattachments/README.md#download_attachment) - Download a Attachment
<!-- End Available Resources and Operations [operations] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

### Example

```python
import panora
from panora.models import errors

s = panora.Panora(
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)

res = None
try:
    res = s.app_controller_hello()

except errors.SDKError as e:
    # handle exception
    raise(e)

if res.string is not None:
    # handle response
    pass

```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://api.panora.dev` | None |
| 1 | `https://api-sandbox.panora.dev` | None |

#### Example

```python
import panora

s = panora.Panora(
    server_idx=1,
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.app_controller_hello()

if res.string is not None:
    # handle response
    pass

```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import panora

s = panora.Panora(
    server_url="https://api.panora.dev",
    jwt="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.app_controller_hello()

if res.string is not None:
    # handle response
    pass

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [requests](https://pypi.org/project/requests/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.

For example, you could specify a header for every request that this sdk makes as follows:
```python
import panora
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = panora.Panora(client=http_client)
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name        | Type        | Scheme      |
| ----------- | ----------- | ----------- |
| `jwt`       | http        | HTTP Bearer |

To authenticate with the API the `jwt` parameter must be set when initializing the SDK client instance. For example:
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
<!-- End Authentication [security] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release!

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
