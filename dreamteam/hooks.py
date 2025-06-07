app_name = "dreamteam"
app_title = "dreamteam"
app_publisher = "Ravi Kumar"
app_description = "my custom app for FrappeHRM"
app_email = "ravikumar.me14@gmail.com"
app_license = "apache-2.0"
app_logo_url = "/assets/dreamteam/images/dreamteam-logo.svg"
# brand_html = '<div><img src="/assets/dreamteam/images/dreamteam-logo.svg"/> TennisMart</div>'




# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = "/assets/dreamteam/css/dreamteam.css"
app_include_scss = "/assets/dreamteam/scss/dreamteam.scss"
#app_include_scss = "/assets/dreamteam/scss/dreamteam.scss"
app_include_js = "/assets/dreamteam/js/dreamteam.js"


# include js, css files in header of web template
#web_include_css = "/assets/dreamteam/css/dreamteam.css" 
web_include_css = "/assets/dreamteam/css/dreamteam.css"
#web_include_css = "/assets/css/dreamteam.css"
# app_include_css = "/assets/dreamteam/css/dreamteam.css"
web_include_js = "/assets/dreamteam/js/dreamteam.js"

#include custom scss in every website theme (without file extension ".scss")
website_theme_scss = "/assets/dreamteam/scss/website" # 
#website_theme_scss = "/dreamteam/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "dreamteam/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

website_context = {
	"favicon": "/assets/dreamteam/images/dreamteam-favicon.svg",
	"splash_image": "/assets/frappe/images/frappe-framework-logo.svg",      
}

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "dreamteam.utils.jinja_methods",
#	"filters": "dreamteam.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "dreamteam.install.before_install"
after_install = "dreamteam.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "dreamteam.uninstall.before_uninstall"
# after_uninstall = "dreamteam.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "dreamteam.utils.before_app_install"
after_app_install = "dreamteam.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "dreamteam.utils.before_app_uninstall"
# after_app_uninstall = "dreamteam.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "dreamteam.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"dreamteam.tasks.all"
#	],
#	"daily": [
#		"dreamteam.tasks.daily"
#	],
#	"hourly": [
#		"dreamteam.tasks.hourly"
#	],
#	"weekly": [
#		"dreamteam.tasks.weekly"
#	],
#	"monthly": [
#		"dreamteam.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "dreamteam.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "dreamteam.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "dreamteam.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["dreamteam.utils.before_request"]
# after_request = ["dreamteam.utils.after_request"]

# Job Events
# ----------
# before_job = ["dreamteam.utils.before_job"]
# after_job = ["dreamteam.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"dreamteam.auth.validate"
# ]

standard_help_items = [
	{
		"item_label": "About",
		"item_type": "Action",
		"action": "frappe.ui.toolbar.show_about()",
		"is_standard": 1,
	},
	{
		"item_label": "Keyboard Shortcuts",
		"item_type": "Action",
		"action": "frappe.ui.toolbar.show_shortcuts(event)",
		"is_standard": 1,
	},
	{
		"item_label": "Frappe Support",
		"item_type": "Route",
		"route": "https://learn.microsoft.com/en-us/docs/",
		"is_standard": 1,
	},
]