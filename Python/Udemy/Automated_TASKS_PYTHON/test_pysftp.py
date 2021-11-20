import pysftp

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None
myHostname = "10.22.51.161"
myUserName = "promptpay"
myPassword = "promptpay"

with pysftp.Connection(host=myHostname, username=myUserName, password=myPassword, cnopts=cnopts) as sftp:
    directory_structure = sftp.listdir_attr()
    for attr in directory_structure:
        print(attr, attr.filename)
