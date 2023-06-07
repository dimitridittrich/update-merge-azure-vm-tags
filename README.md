# update-merge-azure-vm-tags

This script is designed to ease the process of changing the business.start, business.stop, and business.environment tags on Azure Virtual Machines.<br>
This was a specific need because these tags were responsible for defining the times when the VMs would turn on and/or turn off automatically (this process is done by another automation that runs in a script in a Rundeck job).<br>
Important: This script does not change the tags that already exist in the VMs, it only edits and/or adds the three tags already mentioned.<br>

To use the script you need:<br>

- Python version 3.11.2 or higher (earlier versions have not been tested)
- Install azure-mgmt-resource, eg:
pip install azure-identity azure-mgmt-resource
- Clone the repository to your machine.
- Open in VSCode and export the environment variables "AZURE_CLIENT_ID", "AZURE_CLIENT_SECRET" and "AZURE_TENANT_ID" referring to the Service Principal (with the appropriate accesses) in your VSCODE terminal, as shown in the example below:
export AZURE_CLIENT_ID="xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
export AZURE_CLIENT_SECRET="xxxxxxxxxxxxxxxxxxxxx"
export AZURE_TENANT_ID="xxxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
- Edit and save the "update_vm_tags.csv" file with the information of the VMs you need, as you can see in the example of this repository.
- Run the python file as shown below:
python3 update_vm_tags.py
- Follow the prints in Terminal to check if the changes were made correctly.
