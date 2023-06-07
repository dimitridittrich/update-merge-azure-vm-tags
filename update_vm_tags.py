import csv
from azure.identity import EnvironmentCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.resource.resources.models import TagsPatchResource

vm_tag_mapping = {}

# CSV
with open('update_vm_tags.csv', 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    for row in csv_reader:
        print(row)
        subscription_id = row['subscription_id']
        resource_group = row['resource_group']
        vm_name = row['vm']
        environment = row['business.environment']
        start_time = row['business.start']
        stop_time = row['business.stop']
        vm_tag_mapping = {'business.environment': environment, 'business.start': start_time, 'business.stop': stop_time}

        # Auth Azure Resource Management
        credentials = EnvironmentCredential()
        resource_client = ResourceManagementClient(credentials, subscription_id)

        # Update VM tags
        print(resource_group)
        vm_id = f"/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.Compute/virtualMachines/{vm_name}"
        print(vm_id)

        tag_patch_resource = TagsPatchResource(
            operation="Merge",
            properties={'tags': vm_tag_mapping}
        )

        resource_client.tags.begin_update_at_scope(vm_id, tag_patch_resource)
        print(f"Tags updated in the VM '{vm_name}'")