class JiraCloudRestApiURL:
    _instance_url = "your-instance-url"

    @staticmethod
    def get_issue(issue_key: str):
        return f"{JiraCloudRestApiURL._instance_url}/rest/api/2/issue/{issue_key}"

    @staticmethod
    def edit_issue(issue_key: str):
        return f"{JiraCloudRestApiURL._instance_url}/rest/api/2/issue/{issue_key}"

    @staticmethod
    def get_issue_changelog(issue_key: str):
        return f"{JiraCloudRestApiURL._instance_url}/rest/api/2/issue/{issue_key}/changelog"

    @staticmethod
    def get_issue_fields():
        return f"{JiraCloudRestApiURL._instance_url}/rest/api/2/field"

    @staticmethod
    def get_field_contexts(field_id: str):
        return f"{JiraCloudRestApiURL._instance_url}/rest/api/2/field/{field_id}/context"

    @staticmethod
    def get_field_options(field_id: str, context_id: str):
        return f"{JiraCloudRestApiURL._instance_url}/rest/api/2/field/{field_id}/context/{context_id}/option"

    @staticmethod
    def search_for_issues_with_jql():
        return f"{JiraCloudRestApiURL._instance_url}/rest/api/2/search"

    # Working with a Projects
    @staticmethod
    def get_all_projects():
        return f"{JiraCloudRestApiURL._instance_url}/rest/api/2/project"

    @staticmethod
    def get_project_by_key(project_key: str):
        return f"{JiraCloudRestApiURL._instance_url}/rest/api/2/project/{project_key}"

    @staticmethod
    def get_project_components(project_key: str):
        return f"{JiraCloudRestApiURL._instance_url}/rest/api/2/project/{project_key}/components"

    # Working with a screens
    @staticmethod
    def get_screens():
        return f"{JiraCloudRestApiURL._instance_url}/rest/api/2/screens"

    @staticmethod
    def delete_screen(screen_id: int):
        return f"{JiraCloudRestApiURL._instance_url}/rest/api/2/screens/{str(screen_id)}"

    # Working with a screen schemes
    @staticmethod
    def get_screen_schemes():
        return f"{JiraCloudRestApiURL._instance_url}/rest/api/2/screenscheme"

    @staticmethod
    def delete_screen_scheme(screen_scheme_id: str):
        return f"{JiraCloudRestApiURL._instance_url}/rest/api/2/screenscheme/{screen_scheme_id}"
