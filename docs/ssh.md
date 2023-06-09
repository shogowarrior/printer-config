# SSH Documentation

This document will guide you through passwordless SSH to printer. Replace the following as per your need:
* `username`
* `printer`


```bash
ssh printer
```

## SSH Alias Setup

1. Open the SSH configuration file on your local machine with the command:
   ```bash
   vim ~/.ssh/config
   ```
   If the file doesn't exist, create it.

2. Add the following lines to the SSH configuration file:
   ```bash
   Host printer
     HostName printer.local
     HostName 192.168.0.130
     User username
     IdentityFile ~/.ssh/id_rsa_printer
     IdentitiesOnly yes
   ```

## SSH passwordless Setup

1. Generate an SSH key pair for the specific printer using the command:
   ```bash
   ssh-keygen -t rsa -b 4096 -f ~/.ssh/id_rsa_printer
   ```

2. You will be prompted to provide a passphrase for the key. You can either enter a passphrase or leave it empty for a passphrase-less key.

3. The key pair will be generated with the private key saved as `~/.ssh/id_rsa_printer` and the public key saved as `~/.ssh/id_rsa_printer.pub`.

4. Copy the public key (`id_rsa_printer.pub`) to the remote server's `authorized_keys` file using the command:
   ```
   ssh-copy-id -i ~/.ssh/id_rsa_printer.pub username@printer
   ```
