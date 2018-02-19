# Tools for VM migration

## Prerequisite
- Python 3.6.3 

## Installation
Under the root directory of the repository,
```
pip install -r requirements.txt
```

## Usage
First of all, you need to provide the remote host and password.
```
export VM_HOST=<user@ip_address>
export VM_PASSWORD=<secret>
```
- see a list of Fabric commands
```
fab -l
```
- check host name of remote server
```
fab hostname_check
```
- send file to 
```
fab send_file:<local_file_path>,<remote_file_path>
```
- migrate database
```
fab migrate_db:<db_name>
```
